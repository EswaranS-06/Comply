# Design tokens

Canonical file: `templates/tokens.css` (copy it; do not retype values). Tailwind preset: `templates/tailwind.config.js`.
Kit source: `identity/rex/kit/A/tokens/` (`tokens.css` with `--bi-*` ramps, `tokens.dtcg.json`, `fonts.css`). The web tokens reuse its ramps but set a darker, obsidian-first semantic layer.

## Palette (confirmed)

| Token | Hex | Role |
|---|---|---|
| `--rex-obsidian` | #09090B | Dark base (dark theme background) |
| `--rex-indigo` | #312E81 | Depth: surfaces, gradients, glows. Text only on light backgrounds |
| `--rex-blue` | #2563EB | Primary accent: buttons, rules, focus on light, large text |
| `--rex-purple` | #A855F7 | Secondary accent: separators, index numbers, small highlights |
| `--rex-white` | #FFFFFF | Light surface, headings on dark |

Ratio guide per screen: obsidian/white base about 85-90 %, neutrals 5-10 %, blue about 3-5 %, purple 1-2 %, indigo as tint only. Blue and purple mark emphasis, never decoration for its own sake.

## Semantic tokens

| Token | Dark | Light | Use |
|---|---|---|---|
| `--bg` | #09090B | #FFFFFF | page |
| `--bg-raised` | #0F0F12 | #F7F7F8 | cut sections |
| `--surface` / `--surface-2` | #141418 / #1A1A1F | #FFFFFF / #EFEFF3 | cards / chips |
| `--border` / `--border-strong` | #27272A / #3F3F46 | #E4E4E7 / #D4D4D8 | hairlines |
| `--text` / `--text-muted` | #F4F4F5 / #A1A1AA | #18181B / #52525B | copy |
| `--heading` | #FFFFFF | #09090B | headings |
| `--accent` | #2563EB | #2563EB | fills |
| `--accent-text` | #6D9DFD | #1D4ED8 | links, labels |
| `--accent-2-text` | #A855F7 | #902DE0 | purple text |
| `--on-accent` | #FFFFFF | #FFFFFF | label on blue |
| `--focus` | #6D9DFD | #2563EB | focus ring |
| `--code-bg` | #0C0C10 | #09090B | code stays dark in both themes |

## Contrast (measured, run `python scripts/contrast.py`)

- Blue #2563EB on obsidian is 3.85:1: fills, large text (24px+, or 18.66px+ bold) and UI only. For small blue text on dark use `--accent-text` #6D9DFD (7.5:1).
- Purple #A855F7 on white is 3.96:1: fails body text. Use #902DE0 (5.8:1) on light. On obsidian #A855F7 passes (5.0:1); on dark cards 4.6:1, so keep it to labels and numbers.
- Indigo #312E81 on obsidian is 1.7:1: never text or meaningful borders on dark.
- White on blue 5.17:1 (buttons pass in both themes).
- Text over brand art must sit on a scrim (see hero `::after`). Verify with a screenshot, not just tokens.
- All 32 audited pairs pass; extend `PAIRS` in `scripts/contrast.py` when you add tokens.

## Typography

| Role | Family | Weights | Notes |
|---|---|---|---|
| Display / headings | Space Grotesk | 500, 700 | tracking +0.02em; kit uses upper case for display labels, sentence case fine for long headings |
| Text | Arial (system) | 400, 700 | body 18px / 1.5, small 14px / 1.45 |
| Mono | IBM Plex Mono | 400, 500 | code, terminal, tags, dates, labels: 12px uppercase, tracking +0.04em |

Scale (kit A, fluid via clamp): display 40-72px, H1 36-64px / 1.05, H2 28-40px / 1.1, H3 20-28px / 1.2, body 18px, small 14px, label 12px.
Measure: 60-75 characters for body (`max-width: 38rem` for leads).

## Theme mechanism

1. Inline head script applies `localStorage["rex-theme"]` as `data-theme` before paint.
2. No stored choice: CSS follows `prefers-color-scheme`; no preference: dark (the `:root` default).
3. Toggle button (`[data-theme-toggle]`, `templates/portfolio/theme.js`) writes the choice, updates `aria-label` and `meta[name=theme-color]`.
Theme-specific images (hero art) swap through a CSS variable (`--hero-art`). Keep `url()` variables in a stylesheet in the same folder as the images' relative root.

## Tailwind snippet (v3)

```js
// tailwind.config.js
module.exports = {
  presets: [require("./rex.tailwind.js")],   // copy of templates/tailwind.config.js
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
};
```
```html
<a class="bg-accent text-on-accent font-mono text-label uppercase chamfer-sm px-5 py-3 hover:bg-accent-hover">Read the research</a>
<p class="font-mono text-label uppercase text-accent-text">03 / Selected research</p>
```
