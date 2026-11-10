# Head, SEO, accessibility, performance

## Head
Use `templates/head-snippet.html`. Copy icons + manifest with `python scripts/copy_assets.py <public>`.
- Icons come from `asset/A-cut-r-mono/icons/`: `favicon.ico` (16/32/48), `favicon.svg`, `apple-touch-icon.png` (180), `icon-192/512.png`, `app-icon-512.png` (obsidian tile, manifest `purpose: maskable`).
- `theme-color` per scheme (#09090B / #FFFFFF); the toggle script updates it.
- OG image: 1200x630 PNG from `templates/og/og-image.html` via `python scripts/render_og.py [src] [out]`. Per-article cards: duplicate the HTML, change the headline (max ~6 words per line, 3 lines), keep obsidian + one motif. Always set `og:image:alt`.

## SEO
- One H1 per page; logical H2/H3 order. Title pattern `Page | REX Cybersecurity` (home: `REX Cybersecurity | Resilience · Engineering · eXclusion`).
- Meta description 140-160 chars, factual. Canonical URL on every page.
- JSON-LD: `Organization` on home; `Article`/`TechArticle` (headline, datePublished, author) on write-ups; `Person` if the portfolio is personal.
- Semantic HTML: `header`, `nav[aria-label]`, `main#main`, `section[aria-labelledby]`, `article`, `time[datetime]`, `footer`.
- Real text for headings (no text baked into images). Sitemap + robots.txt on deploy.

## Accessibility (WCAG 2.2 AA)
- Contrast: `python scripts/contrast.py` must pass; check text over art in screenshots.
- Focus: `:focus-visible { outline: 2px solid var(--focus); outline-offset: 3px; }`. Never remove outlines. Primary buttons drop their clip-path on focus so the ring is not clipped.
- Targets at least 44x44 for icon buttons, 48px min height for buttons.
- Reduced motion: disable smooth scroll, transitions, hover lifts under `prefers-reduced-motion: reduce`. No autoplaying animation; no parallax.
- Forced colours: remove clip-paths and decorative art, add `CanvasText` borders.
- Alt text: decorative brand art is CSS background or `alt=""` + `aria-hidden`. Diagrams and screenshots get descriptive alt that states what the reader should learn ("Sysmon event 10 showing PROCESS_VM_READ on lsass.exe"), not "image of".
- Inline logo SVGs: `aria-hidden="true" focusable="false"` with the accessible name on the link.
- Language `en-GB`; skip link; scrollable regions focusable; link text meaningful out of context.

## Performance
- Budget: HTML+CSS+JS under 60 KB gzipped (template is about 15 KB before fonts); LCP under 2.0 s on 4G.
- Backgrounds and art as SVG (2-35 KB). No PNG/JPG art above the fold; never ship the 300-700 KB PNG graphic exports.
- Fonts: two webfonts only (Space Grotesk 500/700, IBM Plex Mono 400/500), `display=swap`, preconnect. For production self-host woff2 subsets with `font-display: swap` and preload the display face. Arial is a system font, never load it.
- No icon fonts, no UI framework for a static site, no carousel libraries, no tracking scripts by default.
- Images that are needed: `width`/`height` attributes, `loading="lazy"` below the fold, AVIF/WebP.
- JS: theme toggle only, `defer`. Everything works without JS (OS theme still applies).
