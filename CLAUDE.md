# Comply: notes for the coding agent

Comply is a DPDP (India) assessment web app. This file is the entry point for any model working here (the owner builds with Claude Sonnet and may call a stronger model as a subagent).

## Start of every session

1. Read `docs/300-mem-index.md`, then `docs/302-mem-project-state.md` and `docs/301-mem-owner-and-working-rules.md`. These are the project's memory: where things stand, what the owner has asked for, and what was learned.
2. Read `docs/14-build-plan.md` for the stage in progress and the documents it points to. `docs/README.md` indexes everything; `docs/00-decisions.md` says what is already decided.
3. **Do not start building until the owner has said to.** `docs/302-mem-project-state.md` records whether they have.

## Memory (docs/3XX)

Working memory is kept in `docs/300-mem-*.md` and up, not in chat history or a private memory store, so it survives context compaction and can be read by any model.

- Update `docs/302-mem-project-state.md` before you stop, every time, so it says exactly where you are and what comes next.
- Append to `docs/304-mem-session-log.md` what you did and decided.
- Add to `docs/301-mem-owner-and-working-rules.md` when the owner gives a new instruction, and to `docs/305-mem-lessons.md` when something costs time.
- Write as you go and commit; a session can be cut off without warning.
- A new memory file takes the next free number and is listed in `docs/300-mem-index.md`.
- Never put secrets or real client data in memory files.

## Rules

- Git is local only. Commit as the configured user (`EswaranS-06`). Never add a `Co-Authored-By` line or any tool attribution. The remote `origin` is the public repo `EswaranS-06/Comply` (D-48): push only when told to, never force-push. `docs/` and `.skills/` are public there, so never put secrets, real client names or client data in any file.
- Work on `forge`. Never commit to `main` by hand; release with `scripts/release.sh vX.Y.Z "summary"` after `pnpm verify` passes. `main` must not contain `docs`, `.skills` or this file.
- When the build departs from a document in `docs/`, change the document in the same commit and add a line to `docs/CHANGELOG.md`.
- Visual design comes only from REX: `.skills/rex-brand` and `.skills/rex-website`. Copy token values; do not retype or invent colours or fonts.
- When a skill in `.skills/` is used, add a row to `docs/16-skills-log.md`.
- Rules and result texts come from the workbooks, as written in `docs/06-rules-engine.md`. Nothing that depends on the workbooks is invented; what is still missing is in `docs/15-open-items.md`.
- Never commit anything from `source-workbooks/`, any `.env` file, or real client data.
- No emojis in project files.
- This is an Instabox sandbox. If it stops, wait 5 to 20 minutes and reconnect; then follow `docs/303-mem-environment.md`.

## Using subagents

A subagent starts with no context. Tell it to read this file and `docs/300-mem-index.md`, name the stage, sub-version and defining documents, and ask it to report what it changed and what it could not verify. Check its diff before committing. Use a stronger model for design decisions, the rules engine, security-sensitive code and bugs whose cause is unclear; use the main model for everything else.
