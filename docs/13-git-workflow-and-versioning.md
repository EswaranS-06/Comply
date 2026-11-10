# 13. Git workflow and versioning

## Ground rules (D-40)

- Git is used locally only. Nothing is pushed, and no remote is added, unless the owner says so.
- Every commit is authored by `EswaranS-06 <eswaransk06@gmail.com>` (already set in the global git config). No `Co-Authored-By` line and no tool attribution of any kind.
- One commit per logical change, with a plain message: what changed, and why if it is not obvious.

## Branches (D-41)

| Branch | What it is | Contains `/docs`, `/.skills`, `CLAUDE.md` |
| --- | --- | --- |
| `forge` | The build branch. Always the newest state of everything. All work is committed here. | Yes |
| `main` | The timeline of working versions. One commit per release, each tagged. Never committed to by hand. | No |

`forge` may hold work that is unfinished or not yet verified. `main` never does.

## Version numbers

`vMAJOR.MINOR.PATCH`, used this way before 1.0:

| Part | Meaning | Example |
| --- | --- | --- |
| MINOR | A completed build stage (S0 = 0.1, S1 = 0.2, ... S9 = 0.10) | `v0.2.0` = stage S1 complete |
| PATCH | A working sub-version inside the next stage, numbered from 1 | `v0.1.1`, `v0.1.2` are steps towards S1 |
| MAJOR | `v1.0.0` is version 1: every stage complete and hardened | |

So the timeline on `main` reads: `v0.0.1`, `v0.0.2` ... (sub-versions of S0) then `v0.1.0` (S0 complete), `v0.1.1` ... then `v0.2.0` (S1 complete), and so on to `v1.0.0`. The full list is in the build plan.

After `v1.0.0`: PATCH for fixes, MINOR for features.

## Releasing

When a sub-version or stage is finished on `forge` and the release gate in 12 passes:

```bash
scripts/release.sh v0.1.2 "Password reset and invites"
```

The script:

1. Refuses to run unless on `forge` with a clean tree and an unused version number.
2. Switches to `main` and replaces its content with the `forge` tree **minus** `docs`, `.skills` and `CLAUDE.md`.
3. Commits as `v0.1.2: Password reset and invites`, noting the `forge` commit it was built from.
4. Tags the `main` commit `v0.1.2` and tags the source commit `forge-v0.1.2`.
5. Switches back to `forge`.

`main` is not merged from `forge`; each release is a snapshot. This keeps `main` free of documents and skills without merge conflicts, and makes `git log main` a clean list of versions.

## Useful commands

```bash
git log main --oneline                 # the version timeline
git diff v0.1.0 v0.2.0 --stat          # what a stage changed
git checkout v0.2.0                    # run an old working version
git log forge --oneline                # full working history
git diff forge-v0.2.0 forge -- docs    # how the documents changed since a release
```

## Fixing a released version

Fix on `forge`, verify, release the next PATCH number. `main` is never edited directly and tags are never moved.

## Before the sandbox expires

The repository exists only on this machine and the owner has chosen to handle backup (D-43). `git bundle create comply.bundle --all` produces one file holding both branches and all tags, if the owner wants to copy it off.
