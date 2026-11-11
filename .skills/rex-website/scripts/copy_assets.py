#!/usr/bin/env python3
"""Copy the REX icons, manifest, wordmark/lockup SVGs and chosen brand graphics into a site's public folder.

Usage: python copy_assets.py PUBLIC_DIR [--graphics combinations/02-diagonal-cuts-slanted-blocks ...] [--set A-cut-r-mono]
Run from anywhere inside the Branding repo. Never edits the source asset/ tree.
Graphic names are relative to asset/graphics/ without extension; both the dark and -light SVG are copied.
"""
import argparse, json, pathlib, shutil, sys

ICONS = ["favicon.svg", "favicon.ico", "apple-touch-icon.png", "icon-192.png", "icon-512.png", "app-icon-512.png"]
LOGOS = ["icon-color.svg", "icon-small-color.svg", "icon-mono-white.svg", "icon-mono-black.svg",
         "wordmark-color-on-dark.svg", "wordmark-color-on-light.svg",
         "lockups/lockup-horizontal-descriptor-color-on-dark.svg", "lockups/lockup-horizontal-descriptor-color-on-light.svg"]


def repo_root():
    here = pathlib.Path(__file__).resolve()
    for p in here.parents:
        if (p / "BRAND.md").exists() and (p / "asset").is_dir():
            return p
    sys.exit("Could not find the Branding repo root (BRAND.md + asset/)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("public")
    ap.add_argument("--set", default="A-cut-r-mono")
    ap.add_argument("--graphics", nargs="*", default=["combinations/02-diagonal-cuts-slanted-blocks"])
    a = ap.parse_args()
    root, out = repo_root(), pathlib.Path(a.public)
    src = root / "asset" / a.set
    (out / "brand").mkdir(parents=True, exist_ok=True)
    for name in ICONS:
        shutil.copy2(src / "icons" / name, out / name)
    for name in LOGOS:
        if (src / name).exists():
            shutil.copy2(src / name, out / "brand" / pathlib.Path(name).name)
    for g in a.graphics:
        for suffix in ("", "-light"):
            f = root / "asset" / "graphics" / f"{g}{suffix}.svg"
            if f.exists():
                (out / "graphics").mkdir(exist_ok=True)
                shutil.copy2(f, out / "graphics" / f.name)
            else:
                print(f"missing (maybe still being generated): {f.relative_to(root)}")
    manifest = {
        "name": "REX Cybersecurity", "short_name": "REX", "start_url": "/", "display": "standalone",
        "theme_color": "#09090B", "background_color": "#09090B",
        "icons": [
            {"src": "/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": "/app-icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
    }
    (out / "site.webmanifest").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"copied brand assets to {out}")


if __name__ == "__main__":
    main()
