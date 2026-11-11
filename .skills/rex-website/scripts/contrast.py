#!/usr/bin/env python3
"""WCAG 2.x contrast checks for REX tokens.

  python contrast.py                      # audit templates/tokens.css, dark + light
  python contrast.py path/to/tokens.css   # audit another copy
  python contrast.py "#A855F7" "#FFFFFF"  # one pair

Thresholds: 4.5 body text, 3.0 large text (>=24px or >=18.66px bold) and UI/graphics (focus rings, borders that carry meaning).
Exit code 1 if any required pair fails.
"""
import pathlib, re, sys

PAIRS = [  # (foreground, background, minimum, note)
    ("text", "bg", 4.5, "body"), ("text", "surface", 4.5, "body on cards"),
    ("text-muted", "bg", 4.5, "secondary text"), ("text-muted", "surface", 4.5, "secondary on cards"),
    ("text-muted", "bg-raised", 4.5, "secondary on raised sections"),
    ("heading", "bg", 4.5, "headings"),
    ("accent-text", "bg", 4.5, "links"), ("accent-text", "surface", 4.5, "links on cards"),
    ("accent-text", "bg-raised", 4.5, "labels on raised sections"),
    ("accent-2-text", "bg", 4.5, "purple text"), ("accent-2-text", "surface", 4.5, "purple text on cards"),
    ("on-accent", "accent", 4.5, "primary button label"),
    ("accent", "bg", 3.0, "blue fills / large text / UI"),
    ("focus", "bg", 3.0, "focus ring"), ("focus", "surface", 3.0, "focus ring on cards"),
    ("code-text", "code-bg", 4.5, "code"),
]


def lum(hex_):
    h = hex_.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    def ch(v):
        v = int(v, 16) / 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(h[i:i + 2]) for i in (0, 2, 4))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def block(css, selector_regex):
    m = re.search(selector_regex + r"\s*\{(.*?)\n\}", css, re.S | re.M)
    return dict(re.findall(r"--([\w-]+)\s*:\s*([^;]+);", m.group(1))) if m else {}


def resolve(name, scope, base, depth=0):
    v = scope.get(name, base.get(name, "")).strip()
    m = re.fullmatch(r"var\(--([\w-]+)\)", v)
    if m and depth < 10:
        return resolve(m.group(1), scope, base, depth + 1)
    return v if re.fullmatch(r"#[0-9a-fA-F]{3,6}", v) else None


def audit(path):
    css = pathlib.Path(path).read_text(encoding="utf-8")
    base = block(css, r"^:root")
    light = {**base, **block(css, r'^\[data-theme="light"\]')}
    failed = 0
    for theme, scope in (("dark", base), ("light", light)):
        print(f"\n{theme.upper()}")
        for fg, bg, need, note in PAIRS:
            a, b = resolve(fg, scope, base), resolve(bg, scope, base)
            if not a or not b:
                print(f"  skip  {fg} on {bg} (not a flat hex)")
                continue
            r = ratio(a, b)
            ok = r >= need
            failed += not ok
            print(f"  {'pass' if ok else 'FAIL'}  {r:5.2f} >= {need}  {fg} {a} on {bg} {b}  ({note})")
    return failed


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 2 and all(a.startswith("#") for a in args):
        r = ratio(*args)
        print(f"{r:.2f}:1  body {'pass' if r >= 4.5 else 'fail'}  large/UI {'pass' if r >= 3 else 'fail'}")
        sys.exit(0)
    target = args[0] if args else pathlib.Path(__file__).resolve().parent.parent / "templates" / "tokens.css"
    sys.exit(1 if audit(target) else 0)
