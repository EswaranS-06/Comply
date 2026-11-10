# Brand rules for the web

Source: `BRAND.md` (repo root). Re-read it before large jobs; it wins over this file if they disagree.

## Personality and voice

- Personality: technical, minimal, trustworthy.
- Voice: technical and authoritative. Precise, evidence-led, confident.
- Write like a lab report with a point of view. Name the technique, tool, log source, ATT&CK ID, number.
- No hype, no unsupported claims ("world-class", "military-grade", "unhackable", "100% secure"), no fear marketing,
  no exclamation marks, no emojis, no hooded-hacker or padlock stock imagery.
- Short declarative headings. Pairs work well: "Defence first. Offence to prove it."
- Claims need evidence on the page or a link to it. If a number is not real, do not invent one; leave a clear placeholder.
- British spelling (defence, offence, prioritised, licence as noun). `lang="en-GB"`.

Copy checklist: Would a senior engineer find a sentence vague? Does every claim point at evidence? Is anything decorative?

## The acronym rule

| Context | Expansion |
|---|---|
| Portfolio and main website (default, always) | **R**esilience · **E**ngineering · e**X**clusion |
| Social posts only, per post content | Offence: Reconnaissance · Exploitation · eXecution (proposed); Purple: Research · Engineering · eXploitation (proposed); Educational: Research · Education · eXploration; Professional: Reliability · Expertise · eXcellence |

- On the website only the Defence expansion appears, including on Offence/Education/Professional service sections. Do not re-expand REX per section.
- Separator is a middle dot with spaces: `Resilience · Engineering · eXclusion`.
- "eXclusion" is deliberate. Never uppercase the expansion (`text-transform: none`, class `acr-line`), or the stylised X disappears.
- Highlight the initials (R, E, X) with `--accent-text`; separators in `--accent-2-text`. Mark separators `aria-hidden` when they are separate spans.
- The expansion is not a tagline. Taglines are undecided; do not invent or present one as official.

## Logo usage on the web

- Default set: `asset/A-cut-r-mono` (kit A is built on it). `asset/master/rex-icon-color.svg` is the large gradient master icon: use for big hero/OG marks only, not at small sizes.
- Header: icon (small mark, `icon-small-color.svg` paths) + wordmark. Inline both SVGs; the wordmark letters R and E use `fill="currentColor"` so they follow the theme, the X keeps blue #2563EB and purple #A855F7.
- At 48px and below use the small mark. Minimum header icon 24px, wordmark height 14px or more.
- Clear space around the lockup: at least the icon height x 0.5.
- Never: recolour the X, stretch, add shadows/glows, put the colour logo on busy art without a scrim, use a lock or shield beside it.
- Mono variants (`*-mono-white.svg`, `*-mono-black.svg`) for one-colour contexts and forced-colours.
