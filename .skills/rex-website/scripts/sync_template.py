#!/usr/bin/env python3
"""Refresh the portfolio template from the live brand assets after asset/ is regenerated.

- Re-copies icons and the hero graphics into templates/portfolio/assets/.
- Re-inlines the header icon (icon-small-color.svg) and wordmark (wordmark-color-on-dark.svg) into
  templates/portfolio/index.html and templates/og/og-image.html. Wordmark letters become currentColor.
- Re-renders the OG image.

Usage: python sync_template.py [--set A-cut-r-mono]
Also usable on any page that uses <svg class="lockup__icon" ...> / <svg class="lockup__wordmark" ...>:
  python sync_template.py --pages path/to/page.html
"""
import argparse, pathlib, re, shutil, subprocess, sys

SKILL = pathlib.Path(__file__).resolve().parent.parent
ICONS = ["favicon.svg", "favicon.ico", "apple-touch-icon.png", "icon-192.png", "icon-512.png", "app-icon-512.png"]
GRAPHICS = ["combinations/02-diagonal-cuts-slanted-blocks.svg", "combinations/02-diagonal-cuts-slanted-blocks-light.svg"]


def repo_root():
    for p in SKILL.parents:
        if (p / "BRAND.md").exists() and (p / "asset").is_dir():
            return p
    sys.exit("Branding repo root not found")


def clean_paths(svg, text_to_current=False):
    view_box = re.search(r'viewBox="([^"]+)"', svg).group(1)
    paths = []
    for m in re.finditer(r"<path\b([^>]*)/>", svg):
        attrs = m.group(1)
        fill = re.search(r'fill="([^"]+)"', attrs).group(1)
        d = re.search(r'\bd="([^"]+)"', attrs).group(1)
        if text_to_current and ('data-color="text"' in attrs or fill.lower() in ("#f3f3f3", "#1c1c1c", "#ffffff", "#09090b")):
            fill = "currentColor"
        paths.append(f'<path fill="{fill.upper() if fill.startswith("#") else fill}" d="{d}"/>')
    return view_box, "".join(paths)


def inline(cls, view_box, paths):
    return f'<svg class="{cls}" viewBox="{view_box}" aria-hidden="true" focusable="false">{paths}</svg>'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", default="A-cut-r-mono")
    ap.add_argument("--pages", nargs="*")
    a = ap.parse_args()
    root = repo_root()
    src = root / "asset" / a.set
    tpl = SKILL / "templates" / "portfolio"
    if not a.pages:
        for n in ICONS:
            shutil.copy2(src / "icons" / n, tpl / "assets" / "icons" / n)
        for g in GRAPHICS:
            f = root / "asset" / "graphics" / g
            if f.exists():
                shutil.copy2(f, tpl / "assets" / "graphics" / f.name)
    icon = inline("lockup__icon", *clean_paths((src / "icon-small-color.svg").read_text(encoding="utf-8")))
    word = inline("lockup__wordmark", *clean_paths((src / "wordmark-color-on-dark.svg").read_text(encoding="utf-8"), True))
    pages = [pathlib.Path(p) for p in a.pages] if a.pages else [tpl / "index.html", SKILL / "templates" / "og" / "og-image.html"]
    for page in pages:
        html = page.read_text(encoding="utf-8")
        html = re.sub(r'<svg class="lockup__icon".*?</svg>', lambda _: icon, html, flags=re.S)
        html = re.sub(r'<svg class="lockup__wordmark".*?</svg>', lambda _: word, html, flags=re.S)
        page.write_text(html, encoding="utf-8")
        print("updated", page)
    if not a.pages:
        subprocess.run([sys.executable, str(SKILL / "scripts" / "render_og.py")], check=True)


if __name__ == "__main__":
    main()
