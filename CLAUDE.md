# Comply: notes for the coding agent

Comply is a DPDP (India) assessment web app. Read `docs/README.md` first; `docs/14-build-plan.md` says what to build next and `docs/00-decisions.md` says what is already decided.

## Rules

- Git is local only. Commit as the configured user (`EswaranS-06`). Never add a `Co-Authored-By` line or any tool attribution. Never push or add a remote unless told to.
- Work on `forge`. Never commit to `main` by hand; release with `scripts/release.sh vX.Y.Z "summary"` after `pnpm verify` passes. `main` must not contain `docs`, `.skills` or this file.
- When the build departs from a document in `docs/`, change the document in the same commit and add a line to `docs/CHANGELOG.md`.
- Visual design comes only from REX: `.skills/rex-brand` and `.skills/rex-website`. Copy token values; do not retype or invent colours or fonts.
- When a skill in `.skills/` is used, add a row to `docs/16-skills-log.md`.
- Nothing that depends on the Excel workbooks is invented. If `source-workbooks/` is empty, the item is blocked (`docs/15-open-items.md`).
- Never commit anything from `source-workbooks/`, any `.env` file, or real client data.
- No emojis in project files.
- This is an Instabox sandbox. If it stops, wait 5 to 20 minutes and reconnect; then `docker compose --profile dev up -d` and continue from the last commit.
