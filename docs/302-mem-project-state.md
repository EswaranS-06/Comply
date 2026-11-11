# 302. Memory: project state

**Keep this file true. Update it before stopping, every session.**

Last updated: 11 Nov 2026.

## Where things stand

| | |
| --- | --- |
| Phase of work | Planning finished. **No application code exists.** Only a throwaway outline demo page |
| Build status | **On hold. The owner said to wait until told to start (301, I-18).** |
| Build stage | S0 not started |
| Last release on `main` | None. `main` holds only the initial commit (README, `.gitignore`) |
| Next release | `v0.0.1` (first sub-version of S0) |
| Working branch | `forge` |
| Who builds | Claude Sonnet as the main agent; a stronger model as a subagent where needed (301, I-16) |
| Look of the build | Plain: white background, black lines and text; colour only where needed (D-45, 08). REX theme later |

## What exists in the repository

- `README.md`, `.gitignore`, `CLAUDE.md`
- `scripts/release.sh`: publishes `forge` to `main` without `docs`, `.skills`, `CLAUDE.md`, and tags. Dry-run tested in a throwaway clone on 10 Nov 2026; never run for real yet.
- `docs/00` to `19`: the full specification and plan. Added on 11 Nov: `18` (demo clients) and `19` (Excel exchange plan).
- `docs/demo-clients/`: the owner's three fictional demo client files, unchanged.
- `docs/300` to `305`: this memory.
- `.skills/`: `rex-brand`, `rex-website`, `hallmark`, `taste-skill`, `frontend-design`, `awesome-design-md`, `ponytail` (details in 16).
- `demo/index.html`: the outline demo (below).
- `source-workbooks/` (ignored by git): the four template workbooks and their README.

Nothing else. No `package.json`, no Compose file, no database.

## The outline demo

- One plain HTML page with inline JS and sample data: sign in, clients (the three demo clients), assessment, result. Its result logic is a stand-in, not the rules engine.
- Served by `python3 -m http.server 3000 --directory /srv/comply/demo` as a background process. It does **not** restart after a sandbox stop; run the same command again.
- Published with `instabox-port publish 3000`. The link is public: `https://3000-agq4l32547iaphxs7bq2l5ie6q.instabox.tech`. Close it with `instabox-port unpublish 3000`.
- **`demo/` must be removed, or excluded in `scripts/release.sh`, before the first release**, or it reaches `main`. Port 3000 is also the app's dev port: stop the demo server before `pnpm dev`.

## The next step, when the owner says go

Start S0, sub-version `v0.0.1`, as written in 14:

1. On `forge`: scaffold Next.js (App Router) + TypeScript strict with pnpm in the repository root; ESLint, Prettier, Vitest, Playwright; `pnpm verify` script.
2. `compose.yaml` with a `dev` profile: PostgreSQL 17, MinIO, Mailpit. `.env.example`.
3. Prisma connected, first migration, `/api/health`.
4. Record the exact versions installed in `docs/CHANGELOG.md` (04 says versions are pinned at this point).
5. Run the release gate (12) and release `v0.0.1` with `scripts/release.sh`.
6. Update this file and 304; tick the table at the bottom of 14.

Before writing any UI (from `v0.0.2`), read the "Interim plain theme" section of 08. The REX skills are not used until the owner switches the theme on.

## Waiting on the owner

| Item | Detail | Blocks |
| --- | --- | --- |
| Go-ahead to build | Explicit instruction required | Everything |
| Phase 4 security review design | 15, O-8. Narrowed by section 13 of the demo client files; the result matrix still needs confirming | `v0.8.1` (F21) |
| Sandbox lifetime | SSH access ends about 17 Nov 2026; the plan runs to 22 Nov; no backup by the owner's choice | Work after 17 Nov |
| Confirmations | 15, "For the owner to confirm": O-18 (Auth.js replaced), O-22 to O-28, O-10, and the new O-37 to O-43 (Brannock totals, optional demo rows, Excel check choices, status colours). The build proceeds on these unless the owner objects | Nothing, but ask if a quiet moment comes |

## Not blocked

Stages S0 to S7 and S9, and most of S8, can be built with what is in the repository now. The demo and acceptance data are in hand (18).

## Changes to this machine made outside the repository

- `/srv/comply` ownership changed from `root` to `user` (10 Nov 2026).
- Claude Code plugin `ponytail@ponytail` 5.3.3 installed for the `user` account, marketplace `DietrichGebert/ponytail` (10 Nov 2026).
- Port 3000 published through Instabox, public (10 Nov 2026).
- Nothing was changed in `/data/home/REX`.
