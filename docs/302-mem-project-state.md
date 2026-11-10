# 302. Memory: project state

**Keep this file true. Update it before stopping, every session.**

Last updated: 10 Nov 2026.

## Where things stand

| | |
| --- | --- |
| Phase of work | Planning finished. **No application code exists.** |
| Build status | **On hold. The owner said to wait until told to start (301, I-18).** |
| Build stage | S0 not started |
| Last release on `main` | None. `main` holds only the initial commit (README, `.gitignore`) |
| Next release | `v0.0.1` (first sub-version of S0) |
| Working branch | `forge` |
| Who builds | Claude Sonnet as the main agent; a stronger model as a subagent where needed (301, I-16) |

## What exists in the repository

- `README.md`, `.gitignore`, `CLAUDE.md`
- `scripts/release.sh`: publishes `forge` to `main` without `docs`, `.skills`, `CLAUDE.md`, and tags. Dry-run tested in a throwaway clone on 10 Nov 2026; never run for real yet.
- `docs/00` to `17`: the full specification and plan.
- `docs/300` to `305`: this memory.
- `.skills/`: `rex-brand`, `rex-website`, `hallmark`, `taste-skill`, `frontend-design`, `awesome-design-md`, `ponytail` (details in 16).
- `source-workbooks/` (ignored by git): the four template workbooks and their README.

Nothing else. No `package.json`, no Compose file, no database.

## The next step, when the owner says go

Start S0, sub-version `v0.0.1`, as written in 14:

1. On `forge`: scaffold Next.js (App Router) + TypeScript strict with pnpm in the repository root; ESLint, Prettier, Vitest, Playwright; `pnpm verify` script.
2. `compose.yaml` with a `dev` profile: PostgreSQL 17, MinIO, Mailpit. `.env.example`.
3. Prisma connected, first migration, `/api/health`.
4. Record the exact versions installed in `docs/CHANGELOG.md` (04 says versions are pinned at this point).
5. Run the release gate (12) and release `v0.0.1` with `scripts/release.sh`.
6. Update this file and 304; tick the table at the bottom of 14.

Before writing any UI (from `v0.0.2`), read 08 and the `rex-website` skill, and log the skill use in 16.

## Waiting on the owner

| Item | Detail | Blocks |
| --- | --- | --- |
| Go-ahead to build | Explicit instruction required | Everything |
| Filled Auklet School demo workbooks | 15, O-1 | Final parity totals in S5; the `v1.0.0` gate |
| Phase 4 security review design | 15, O-8 | `v0.8.1` (F21) |
| Sandbox lifetime | SSH access ends about 17 Nov 2026; the plan runs to 22 Nov; no backup by the owner's choice | Work after 17 Nov |
| Confirmations | 15, "For the owner to confirm": O-18 (Auth.js replaced), O-22 to O-28, O-10. The build proceeds on these unless the owner objects | Nothing, but ask if a quiet moment comes |

## Not blocked

Stages S0 to S4, S6, S7, S9 and most of S5 and S8 can be built with what is in the repository now.

## Changes to this machine made outside the repository

- `/srv/comply` ownership changed from `root` to `user` (10 Nov 2026).
- Claude Code plugin `ponytail@ponytail` 5.3.3 installed for the `user` account, marketplace `DietrichGebert/ponytail` (10 Nov 2026).
- Nothing was changed in `/data/home/REX`.
