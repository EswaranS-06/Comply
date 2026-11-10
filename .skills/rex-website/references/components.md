# Components

Working implementations live in `templates/portfolio/index.html` + `styles.css`. Copy from there; the notes below are the rules.

## Header + lockup
- Sticky, 68px, `--bg` at 88 % with backdrop blur, 1px bottom border.
- Inline SVG icon (30px) + wordmark (17px high), gap 0.7rem, link to home with `aria-label="REX Cybersecurity, home"`; SVGs `aria-hidden`.
- Nav links: IBM Plex Mono, small, uppercase, 2px blue underline on hover. Under 680px the nav drops to its own row and scrolls horizontally.
- Theme toggle: 44x44 square button, sun icon in dark, moon in light, label "Switch to light theme".
- Include a skip link to `#main`.

## Hero
- Mono eyebrow with a 40px gradient rule: `REX Cybersecurity / Defence`.
- H1 = acronym expansion, one word per line, initials in `--accent-text`, separators in `--accent-2-text`, mixed case.
- Lead: one or two sentences, muted, max 38rem. Then primary + ghost buttons, then a `dl` meta row (mono labels).
- Background: one combination SVG via `--hero-art` (dark/light), left scrim in `::after`, bottom diagonal cut.

## Buttons
- Mono, uppercase, 48px min height. Primary: blue fill, white label, chamfered top-right (10px). Ghost: 1px `--border-strong`, no chamfer.
- No gradients on buttons. One primary per view.

## Project / write-up cards
- `article`-like `li.card.card--post`: meta row (type in `--accent-text`, `time` right-aligned), H3 title link that stretches over the card (`.card__link::before`), muted summary, chips at the bottom.
- Chamfer 14px top-right; hover lifts 2px and turns the edge blue (no lift under reduced motion).
- Service cards: 2px blue top edge, purple mono index (01-04), title, summary, chips. Services are Defence, Offence, Education, Professional.

## Code / terminal block
- `figure.terminal` with a bar (three small diamonds: blue, purple, zinc; mono title) and `pre > code` in IBM Plex Mono 13px / 1.7.
- Stays dark in both themes (`--code-bg`). Token colours: prompt purple, ok #6D9DFD, warn #C79BFE, dim #8B8B94 (all at least 5.9:1).
- `pre` gets `tabindex="0"` and an `aria-label` because it scrolls horizontally on mobile.
- For real code highlighting, map tokens to the same five colours; no rainbow themes.

## Tag chips
- Mono 11px uppercase, `--surface-2` fill, 1px border, square corners. Content: ATT&CK IDs, platforms, tools. 2-4 per card.

## Timeline
- `ol.timeline` with a 1px rail and rotated 9px blue squares (diamonds) as nodes. Each item: mono `time`, H3 (18px), one muted line.

## Contact panel
- `.frame` with two chamfered corners (top-right, bottom-left), `dl` of channels (mono `dt`), full-width primary button.
- Placeholder contacts use `rex.example`; replace with real ones. Do not publish personal email addresses without confirmation.

## Footer
- Small icon + expansion line (mixed case), link list, legal line: "(c) YEAR REX Cybersecurity. Defence, offence, education and professional services."

## Section heading pattern
- Mono label `NN / Name` in `--accent-text`, then H2. Numbered sections help scanning; keep numbering in DOM order.
