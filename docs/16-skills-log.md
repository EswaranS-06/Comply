# 16. Skills log

Agent skills are kept in `/.skills` and committed on `forge` (D-32). Every time a skill is used during the build, a row is added to the usage log below, in the same commit as the work it influenced.

## Installed

| Folder | What it is | Source | Commit | Licence | Notes |
| --- | --- | --- | --- | --- | --- |
| `.skills/rex-brand` | REX brand brief, tokens, fonts note, logo set A, master icon | `/data/home/REX` (owner's own) | `c0d3859` | Owner | Copied so the build does not depend on a folder outside the repository |
| `.skills/rex-website` | REX web tokens, Tailwind preset, component, layout and Next.js notes, contrast script | `/data/home/REX/.claude/skills/rex-website` | `c0d3859` | Owner | The authority on anything visual |
| `.skills/hallmark` | Design skill against generic generated UI | github.com/Nutlope/hallmark, `skills/hallmark` | `407fa68` | MIT | |
| `.skills/taste-skill` | Frontend design judgement skill | github.com/Leonxlnx/taste-skill, `skills/taste-skill` | `f6b7657` | MIT | The `assets/` folder (37 MB of images) was left out |
| `.skills/frontend-design` | Anthropic's frontend design skill | github.com/anthropics/skills, `skills/frontend-design` | `2c5958e` | See `LICENSE.txt` in the folder | |
| `.skills/awesome-design-md` | 84 `DESIGN.md` references from well-known products | github.com/VoltAgent/awesome-design-md, `design-md` | `fcc7028` | MIT | Reference for structure only; REX overrides all colour and type |
| `.skills/ponytail` | Reuse-before-writing skills: ponytail, -audit, -debt, -gain, -help, -review | github.com/DietrichGebert/ponytail, `skills/` | `96608e0` | MIT | Also installed as a Claude Code plugin, see below |

All were downloaded on 10 Nov 2026. Third-party skills are reference text; scripts inside them are read before being run.

## Ponytail plugin

Besides the copy in `.skills/ponytail`, ponytail is installed as a Claude Code plugin for the `user` account on this machine (`ponytail@ponytail` 5.3.3, marketplace `DietrichGebert/ponytail`), which is how its session hooks and `/ponytail` commands become active. It runs three small Node hooks (session start, subagent start, prompt submit). Four optional plugin settings are unset and left at their defaults.

## Rules of use

1. REX (`rex-brand`, `rex-website`) decides every colour, typeface and motif. No other skill may introduce a colour or font.
2. `hallmark`, `taste-skill` and `frontend-design` are used for layout, hierarchy and avoiding generic output.
3. `awesome-design-md` files are read for how dense tools are structured, never copied.
4. `ponytail` applies to all code: reuse what exists (in the repository, the standard library, the platform) before writing new code.

## Usage log

| Date | Version | Skill | Used for | Outcome |
| --- | --- | --- | --- | --- |
| 10 Nov 2026 | planning | `rex-brand`, `rex-website` | Writing 08-design-system: palette, semantic tokens, type roles, contrast rules, theme mechanism | Tokens and rules adopted; app type scale and status colours derived from kit ramps |
