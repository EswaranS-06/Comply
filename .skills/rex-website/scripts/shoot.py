#!/usr/bin/env python3
"""Full-page screenshots of a local HTML page in headless Chrome, dark + light, desktop + mobile.

Stdlib only (talks to Chrome over the DevTools protocol with a tiny WebSocket client).
Also reports horizontal overflow: any element whose box extends past the viewport width.

Usage:
  python shoot.py PAGE.html OUT_DIR [--widths 1440,390] [--themes dark,light] [--prefix portfolio]
  python shoot.py http://localhost:8000/ OUT_DIR

Env: CHROME=path/to/chrome (defaults to the usual Windows/macOS/Linux locations).
Output: OUT_DIR/<prefix>-<width>-<theme>.png and a non-zero exit if overflow is found.
"""
import argparse, base64, json, os, pathlib, random, shutil, socket, struct, subprocess, sys, tempfile, time, urllib.request

CANDIDATES = [
    os.environ.get("CHROME", ""),
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    shutil.which("google-chrome") or "", shutil.which("chromium") or "", shutil.which("chrome") or "",
]


class WS:
    """Minimal client WebSocket (RFC 6455), text frames only. Enough for CDP."""

    def __init__(self, url):
        assert url.startswith("ws://")
        hostport, _, path = url[5:].partition("/")
        host, _, port = hostport.partition(":")
        self.sock = socket.create_connection((host, int(port or 80)), timeout=60)
        key = base64.b64encode(os.urandom(16)).decode()
        req = (f"GET /{path} HTTP/1.1\r\nHost: {hostport}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
               f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n")
        self.sock.sendall(req.encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += self.sock.recv(4096)
        head, _, self.rest = buf.partition(b"\r\n\r\n")
        if b" 101 " not in head.split(b"\r\n")[0]:
            raise RuntimeError(head.decode(errors="replace"))

    def _read(self, n):
        while len(self.rest) < n:
            chunk = self.sock.recv(1 << 20)
            if not chunk:
                raise ConnectionError("socket closed")
            self.rest += chunk
        out, self.rest = self.rest[:n], self.rest[n:]
        return out

    def send(self, text):
        data = text.encode()
        header = bytearray([0x81])
        n = len(data)
        if n < 126:
            header.append(0x80 | n)
        elif n < 65536:
            header += bytes([0x80 | 126]) + struct.pack(">H", n)
        else:
            header += bytes([0x80 | 127]) + struct.pack(">Q", n)
        mask = os.urandom(4)
        header += mask
        self.sock.sendall(bytes(header) + bytes(b ^ mask[i % 4] for i, b in enumerate(data)))

    def recv(self):
        message = b""
        while True:
            b1, b2 = self._read(2)
            n = b2 & 0x7F
            if n == 126:
                n = struct.unpack(">H", self._read(2))[0]
            elif n == 127:
                n = struct.unpack(">Q", self._read(8))[0]
            payload = self._read(n)
            opcode = b1 & 0x0F
            if opcode == 0x8:
                raise ConnectionError("closed by peer")
            if opcode in (0x9, 0xA):
                continue
            message += payload
            if b1 & 0x80:
                return message.decode()


class CDP:
    def __init__(self, ws):
        self.ws, self.next_id, self.events = ws, 0, []

    def call(self, method, **params):
        self.next_id += 1
        my_id = self.next_id
        self.ws.send(json.dumps({"id": my_id, "method": method, "params": params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == my_id:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})
            self.events.append(msg)

    def wait_event(self, name, timeout=30):
        end = time.time() + timeout
        while time.time() < end:
            for i, e in enumerate(self.events):
                if e.get("method") == name:
                    return self.events.pop(i)
            self.events.append(json.loads(self.ws.recv()))
        raise TimeoutError(name)


OVERFLOW_JS = r"""
(() => {
  const vw = document.documentElement.clientWidth, out = [];
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) continue;
    const cs = getComputedStyle(el);
    if (cs.position === 'fixed' || el.closest('[aria-hidden="true"]')) continue;
    let p = el.parentElement, clipped = false;
    while (p && p !== document.body) {
      const ps = getComputedStyle(p);
      if (/(auto|scroll|hidden|clip)/.test(ps.overflowX)) { clipped = true; break; }
      p = p.parentElement;
    }
    if (!clipped && (r.right > vw + 1 || r.left < -1)) {
      out.push(`${el.tagName.toLowerCase()}.${[...el.classList].join('.')} right=${Math.round(r.right)} vw=${vw}`);
    }
  }
  return JSON.stringify({vw, sw: document.documentElement.scrollWidth, items: out.slice(0, 15)});
})()
"""


def find_chrome():
    for c in CANDIDATES:
        if c and pathlib.Path(c).exists():
            return c
    sys.exit("Chrome not found. Set CHROME=/path/to/chrome")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("page")
    ap.add_argument("out")
    ap.add_argument("--widths", default="1440,390")
    ap.add_argument("--themes", default="dark,light")
    ap.add_argument("--prefix", default="page")
    ap.add_argument("--max-height", type=int, default=12000)
    a = ap.parse_args()

    url = a.page if "://" in a.page else pathlib.Path(a.page).resolve().as_uri()
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    port = random.randint(9300, 9900)
    profile = tempfile.mkdtemp(prefix="rex-shoot-")
    proc = subprocess.Popen([find_chrome(), "--headless=new", f"--remote-debugging-port={port}",
                             f"--user-data-dir={profile}", "--hide-scrollbars", "--no-first-run",
                             "--no-default-browser-check", "--allow-file-access-from-files", "about:blank"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    problems = 0
    try:
        for _ in range(100):
            try:
                targets = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=1))
                page = next(t for t in targets if t["type"] == "page")
                break
            except Exception:
                time.sleep(0.15)
        else:
            sys.exit("Chrome DevTools endpoint did not come up")
        cdp = CDP(WS(page["webSocketDebuggerUrl"]))
        cdp.call("Page.enable")
        for width in [int(w) for w in a.widths.split(",")]:
            for theme in a.themes.split(","):
                mobile = width < 700
                cdp.call("Emulation.setDeviceMetricsOverride", width=width, height=900 if not mobile else 844,
                         deviceScaleFactor=1, mobile=mobile)
                cdp.call("Emulation.setEmulatedMedia", features=[{"name": "prefers-color-scheme", "value": theme}])
                cdp.call("Page.navigate", url=url)
                cdp.wait_event("Page.loadEventFired")
                cdp.call("Runtime.evaluate", expression="document.fonts.ready.then(() => true)", awaitPromise=True)
                time.sleep(0.4)
                info = json.loads(cdp.call("Runtime.evaluate", expression=OVERFLOW_JS, returnByValue=True)["result"]["value"])
                height = cdp.call("Runtime.evaluate", expression="document.documentElement.scrollHeight",
                                  returnByValue=True)["result"]["value"]
                height = min(int(height), a.max_height)
                shot = cdp.call("Page.captureScreenshot", format="png", captureBeyondViewport=True,
                                clip={"x": 0, "y": 0, "width": width, "height": height, "scale": 1})
                path = out / f"{a.prefix}-{width}-{theme}.png"
                path.write_bytes(base64.b64decode(shot["data"]))
                flag = ""
                if info["sw"] > info["vw"] or info["items"]:
                    problems += 1
                    flag = f"  OVERFLOW scrollWidth={info['sw']} vw={info['vw']} " + "; ".join(info["items"])
                print(f"{path}  {width}x{height}{flag}")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
        shutil.rmtree(profile, ignore_errors=True)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
