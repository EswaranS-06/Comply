#!/usr/bin/env python3
"""Render a 1200x630 Open Graph image from an HTML source with headless Chrome.

Usage: python render_og.py [SOURCE.html] [OUT.png]
Defaults: templates/og/og-image.html -> templates/portfolio/assets/og/og-image.png
Edit the HTML (headline, label) per page; keep it on obsidian with one motif.
"""
import pathlib, subprocess, sys, tempfile, shutil
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from shoot import find_chrome  # noqa: E402

root = pathlib.Path(__file__).resolve().parent.parent
src = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else root / "templates/og/og-image.html"
out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else root / "templates/portfolio/assets/og/og-image.png"
out.parent.mkdir(parents=True, exist_ok=True)
profile = tempfile.mkdtemp(prefix="rex-og-")
try:
    subprocess.run([find_chrome(), "--headless=new", "--hide-scrollbars", "--no-first-run", f"--user-data-dir={profile}",
                    "--allow-file-access-from-files", "--force-device-scale-factor=1", "--window-size=1200,630",
                    "--virtual-time-budget=4000", f"--screenshot={out.resolve()}", src.resolve().as_uri()],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
finally:
    shutil.rmtree(profile, ignore_errors=True)
print(out, out.stat().st_size, "bytes")
