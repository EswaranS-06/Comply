---
name: rex-website
description: Build on-brand websites, landing pages, the portfolio and web components for REX Cybersecurity. Use whenever the task involves REX web work - a portfolio or main site, a page, section, hero, header, footer, project/write-up card, blog or research page, terminal/code block, theme toggle, favicon/manifest/OG image, Tailwind or CSS tokens, Next.js setup, or reviewing a page for brand, contrast, accessibility or performance. Triggers on REX, REX Cybersecurity, rex site, rex portfolio, brand website, landing page, Resilience Engineering eXclusion, dark theme, diagonal cuts, Space Grotesk, IBM Plex Mono, obsidian #09090B, #2563EB, #A855F7.
---

# REX website skill

Builds REX Cybersecurity web pages that match `BRAND.md`: technical, minimal, trustworthy; dark-first; diagonal-cut geometry; Space Grotesk / Arial / IBM Plex Mono; evidence-led copy.

## Start here

1. Read `BRAND.md` (repo root) if it changed since this skill was written; it overrides these files.
2. Start from the working template: `templates/portfolio/` (index.html, tokens.css, styles.css, theme.js, site.webmanifest, assets/). It is self-contained; copy the folder and edit content. Samples of how it should look: `samples/`.
3. Load only the reference you need:
   - `references/brand.md` - voice, copy rules, the acronym rule, logo usage
   - `references/tokens.md` - palette, semantic tokens, measured contrast, type scale, theme mechanism, Tailwind snippet
   - `references/layout-and-motifs.md` - 12-col grid, spacing, diagonal cuts with clip-path, motif order and restraint, brand graphics paths
   - `references/components.md` - header/lockup, hero, buttons, cards, terminal, chips, timeline, contact, footer
   - `references/head-seo-a11y-perf.md` - head snippet, OG, SEO, accessibility, performance budget
   - `references/nextjs.md` - Next.js + Tailwind (v3 preset and v4 @theme) wiring
4. Verify (always, before reporting done): contrast script, screenshots at 1440 and 390 in dark and light, view them, fix, re-shoot.

## Non-negotiables

- Palette only: #09090B obsidian, #312E81 indigo, #2563EB blue, #A855F7 purple, #FFFFFF, plus the neutral and tint tokens in `templates/tokens.css`. Blue/purple for emphasis, not decoration.
- Small blue text on dark uses #6D9DFD; purple text on light uses #902DE0; indigo is never text on dark. Body text 4.5:1, large text/UI 3:1.
- Dark is the default; light theme is required; `prefers-color-scheme` respected; toggle stores `rex-theme` in localStorage; pre-paint script prevents a flash.
- Acronym on the website is always the Defence expansion: `Resilience · Engineering · eXclusion`, mixed case, never uppercased. Other expansions are for social posts only.
- Header = R icon + REX wordmark (inline SVG from `asset/A-cut-r-mono`, letters `currentColor`, X stays blue/purple).
- Diagonal cuts are the primary motif (same angle everywhere). Max two motifs per viewport, one big brand graphic per page. Shape frequency order: triangles, slanted blocks, dots, angles+grids, angled frames, layered panels, hexagons, 3D, rhombus, glitch, blobs.
- No stock cybersecurity imagery, no padlocks/shields/hoodies, no emojis, no hype words, no invented metrics or tagline.
- Visible focus rings, reduced-motion support, alt text that informs, semantic landmarks, en-GB.
- SVG art (not the PNG exports), two webfonts with `display=swap`, JS limited to the theme toggle.
- Never modify `asset/`, `identity/`, `reference/` or `.skill/`. Copy what a site needs.

## Scripts (Python 3, stdlib + Chrome; PIL not required)

| Command | Does |
|---|---|
| `python .claude/skills/rex-website/scripts/shoot.py PAGE_OR_URL OUT_DIR --prefix NAME [--widths 1440,390] [--themes dark,light]` | Full-page headless Chrome screenshots per width/theme via DevTools; flags horizontal overflow (exit 1). |
| `python .claude/skills/rex-website/scripts/contrast.py [tokens.css]` or `contrast.py "#fg" "#bg"` | WCAG audit of semantic token pairs in both themes. |
| `python .claude/skills/rex-website/scripts/copy_assets.py PUBLIC_DIR [--graphics combinations/02-diagonal-cuts-slanted-blocks]` | Copies favicons, manifest, logos and chosen graphics (dark + light) from `asset/`. |
| `python .claude/skills/rex-website/scripts/render_og.py [SRC.html] [OUT.png]` | Renders the 1200x630 OG card from `templates/og/og-image.html`. |
| `python .claude/skills/rex-website/scripts/sync_template.py [--pages page.html ...]` | After `asset/` is regenerated: re-copies icons/graphics, re-inlines the icon + wordmark SVG paths (letters `currentColor`), re-renders OG. Run it before building if `git status` shows `asset/` changes. |

Chrome path defaults to `C:\Program Files\Google\Chrome\Application\chrome.exe`; override with `CHROME=...`.
View screenshots with the Read tool; tall pages read better cropped into 1100px slices.

## Workflow for a new page or site

1. Copy `templates/portfolio/` (static) or follow `references/nextjs.md` (app).
2. Replace placeholder copy (`rex.example`, sample write-ups, PGP, dates) with real content; keep the voice rules.
3. Pick at most one hero graphic from `asset/graphics/` (dark + `-light`), copy it with `copy_assets.py`, point `--hero-art` at it.
4. Keep the section rhythm: hero (cut bottom) / plain / cut + dots / plain / cut / footer.
5. Run `contrast.py`, `shoot.py`; read each screenshot; fix overflow, wrapping, text-over-art contrast; re-shoot into the project's samples folder.
6. Report: files changed, screenshots, any unverified items (real fonts self-hosted, real links, OG per page).

## Template inventory

- `templates/tokens.css` - canonical CSS variables (also copied into `templates/portfolio/tokens.css`; keep in sync).
- `templates/tailwind.config.js` - Tailwind v3 preset mapped to the variables, plus `cut-*` and `chamfer` utilities.
- `templates/head-snippet.html` - favicon, manifest, theme-color, OG/Twitter, fonts, pre-paint theme script.
- `templates/og/og-image.html` - OG card source.
- `templates/portfolio/` - hero, about (terminal + timeline), services (defence/offence/education/professional), selected research, contact, footer.
