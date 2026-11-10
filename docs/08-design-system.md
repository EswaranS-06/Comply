# 08. Design system

Comply uses the REX Cybersecurity identity and nothing else (D-30). The source is `/data/home/REX`; the parts the build needs are copied into `/.skills/rex-brand` (brief, tokens, logo set A, master icon) and `/.skills/rex-website` (web tokens, Tailwind preset, component and layout notes) so the build does not depend on a folder outside the repository.

**Rule: token values are copied from `.skills/rex-website/templates/tokens.css`, never retyped.** If a value is needed that the kit does not have, it is derived from a kit ramp, checked for contrast, and recorded in this document.

## Personality

Technical, minimal, trustworthy. Precision over decoration: every element on a screen serves the assessor's task. Comply is a working tool used for hours, so the brand shows in type, colour discipline and a few cut corners, not in illustration.

## Colour

Brand palette (confirmed, not altered):

| Name | Hex | Role in Comply |
| --- | --- | --- |
| Obsidian | `#09090B` | Dark theme page background |
| Deep Indigo | `#312E81` | Depth and tint only; never text or borders on dark |
| Signal Blue | `#2563EB` | Primary action, selection, focus on light |
| Ultraviolet | `#A855F7` | Sparse secondary accent: index numbers, the active stage marker |
| White | `#FFFFFF` | Light theme background, headings on dark |

Ratio per screen: base 85 to 90 percent, neutrals 5 to 10 percent, blue 3 to 5 percent, purple 1 to 2 percent.

Semantic tokens (from the kit):

| Token | Dark | Light |
| --- | --- | --- |
| `--bg` | `#09090B` | `#FFFFFF` |
| `--bg-raised` | `#0F0F12` | `#F7F7F8` |
| `--surface` / `--surface-2` | `#141418` / `#1A1A1F` | `#FFFFFF` / `#EFEFF3` |
| `--border` / `--border-strong` | `#27272A` / `#3F3F46` | `#E4E4E7` / `#D4D4D8` |
| `--text` / `--text-muted` | `#F4F4F5` / `#A1A1AA` | `#18181B` / `#52525B` |
| `--heading` | `#FFFFFF` | `#09090B` |
| `--accent` | `#2563EB` | `#2563EB` |
| `--accent-text` | `#6D9DFD` | `#1D4ED8` |
| `--accent-2-text` | `#A855F7` | `#902DE0` |
| `--focus` | `#6D9DFD` | `#2563EB` |

Status colours come from the kit ramps (`tokens.css`, success / warning / danger / info) and are the only non-brand hues allowed. They carry meaning, never decoration:

| Meaning | Used for | Light | Dark (text on obsidian) |
| --- | --- | --- | --- |
| Success | Supported, Pass, Closed | success-700 `#08795E` | success-300 `#66E2BC` |
| Warning | Cannot conclude yet, Partial, Not sure, missing field | warning-700 `#8F5A06` | warning-300 `#F3BD7F` |
| Danger | Gap, Gap: no legal basis, route mismatch, contradiction | danger-700 `#B4312B` | danger-300 `#FEB2A8` |
| Info | Out of scope, Not tested, neutral notices | info-700 `#196AAF` | info-300 `#9ECDFE` |

The dark-theme status shades are chosen from the kit ramps for this app and are confirmed with the contrast script in S0 (target 4.5:1 for text). Status is never shown by colour alone: every status has a text label, and flags have an icon.

Contrast rules carried over from the kit: blue `#2563EB` on obsidian is 3.85:1, so it is used for fills and large text only, and small blue text on dark uses `#6D9DFD`. Purple on white fails body text, so light theme uses `#902DE0`.

## Typography

| Role | Family | Weights | Used for |
| --- | --- | --- | --- |
| Display | Space Grotesk | 500, 700 | Page titles, section headings, sign-in headline |
| Text | Arial (system) | 400, 700 | Body, form fields, table cells |
| Mono | IBM Plex Mono | 400, 500 | Human IDs (SYS-001), test refs (C3), law references, labels, counts, dates |

Space Grotesk and IBM Plex Mono are self-hosted through `next/font` (files are downloaded at build time and served by the app; no run-time request to Google, D-28).

App scale (the kit scale is for marketing pages; a data tool needs a tighter one, derived from the same steps):

| Step | Size / line | Use |
| --- | --- | --- |
| Page title | 28 / 1.2, Space Grotesk 500, tracking +0.02em | one per screen |
| Section | 20 / 1.2, Space Grotesk 500 | panels, dialogs |
| Body | 15 / 1.5, Arial | forms, prose |
| Table | 14 / 1.45, Arial | grid cells |
| Label | 12 / 1.3, IBM Plex Mono 500, uppercase, tracking +0.04em | field labels, column heads, tags |

The sign-in page uses the kit's larger display steps.

## Shape and motif

- **Diagonal cut** is the primary motif. In the app it appears as the chamfered corner (`--chamfer`, clip-path, two-layer border technique from `layout-and-motifs.md`) on primary buttons, the active navigation item, cards on the dashboard and dialog frames.
- All other corners are square or 2px. No pill shapes, no soft drop shadows; depth is shown with surface steps and hairline borders.
- Dot grid and angle-grid patterns are allowed as a quiet background on empty states and the sign-in page only.
- The blue-to-violet gradient (`--rex-gradient`) is used once per screen at most: the sign-in panel edge and the progress rail.
- Glitch and blob motifs are not used in the app.
- Logo: set A (IBM Plex Mono wordmark) from `.skills/rex-brand/logo`, unmodified, with the dark or light variant matching the theme. Favicons from `logo/icons`.

## Theme

Dark is the default for every new user (D-31). The toggle in the top bar switches to light; the choice is saved on the user record and mirrored in a cookie so the server renders the right theme on first paint with no flash. The device's own light/dark setting is not followed, because the owner chose a fixed dark default.

## Components

Built in `components/ui`, each in both themes, each keyboard-usable:

| Component | Notes |
| --- | --- |
| Button | primary (blue fill, chamfer), secondary (border), ghost, danger |
| Field | text, textarea, select, combobox with search (ID pickers), date, yes/no/not-sure segmented control |
| Data grid | sticky header and first column, virtual rows, inline edit, row alerts, column resize, keyboard navigation like a spreadsheet |
| ID chip | mono text, hover shows the looked-up name; click opens the record |
| Status tag | outcome and status values with label + colour |
| Flag | check result with icon, text and a link to the row that causes it |
| Dialog, drawer | record edit opens in a right-hand drawer so the grid stays visible |
| Toast | save confirmation and errors |
| Tabs, breadcrumb, stage rail | the stage rail shows the assessment phases and how complete each is |
| Empty state | one sentence and one action, dot-grid background |
| Admin table | users and clients with filters, bulk actions |

## Accessibility

WCAG 2.2 AA: visible focus ring (`--focus`, 2px), full keyboard operation of grids and dialogs, labels on every field, 4.5:1 text contrast in both themes, `prefers-reduced-motion` respected, targets at least 24px.

## Motion

Short and functional: 120 to 180 ms ease-out for drawers, menus and toasts. Nothing animates on page load. No motion in tables.

## How the design skills are used

| Skill | Role |
| --- | --- |
| `rex-brand`, `rex-website` | The law: tokens, type, motifs, contrast script |
| `hallmark` | Used once, at S0, to design the sign-in page and app shell so they look designed rather than generated; its anti-default floor is applied to later screens |
| `taste-skill` | Checklist when composing dense screens (spacing rhythm, hierarchy) |
| `frontend-design` | General guidance on intentional type and layout |
| `awesome-design-md` | Reference only: how Linear, Vercel, Supabase and Sentry structure dense dark tools. Their colours and fonts are never copied; REX overrides everything visual |

Each use is logged in 16.
