# 300. Memory: index and rules

The 3XX documents are the project's working memory. They exist so that any model or person picking up this project (the owner plans to build with Claude Sonnet, calling a stronger model as a subagent where needed) starts with everything the previous sessions learned, instead of relying on a chat history that gets compacted or lost.

Documents 00 to 17 say **what to build**. Documents 300 and up say **where things stand, how the owner wants the work done, and what was learned along the way**.

## Read at the start of every session

1. This file.
2. [302-mem-project-state.md](302-mem-project-state.md): what is done, what is next, what is blocked.
3. [301-mem-owner-and-working-rules.md](301-mem-owner-and-working-rules.md): how the owner wants you to work.
4. Then [14-build-plan.md](14-build-plan.md) for the stage you are on, and the documents it points to.

Read 303 to 305 when you need them.

## The memory files

| File | Holds | Changes |
| --- | --- | --- |
| [300-mem-index.md](300-mem-index.md) | This index and the rules for writing memory | Rarely |
| [301-mem-owner-and-working-rules.md](301-mem-owner-and-working-rules.md) | Who the owner is, their instructions and preferences, in their own terms | When the owner gives a new instruction or corrects something |
| [302-mem-project-state.md](302-mem-project-state.md) | Current state: branch tips, last release, stage in progress, next step, blockers, things waiting on the owner | **Every session, before stopping** |
| [303-mem-environment.md](303-mem-environment.md) | The sandbox, paths, installed tools, services, how to recover after a stop | When the machine or tooling changes |
| [304-mem-session-log.md](304-mem-session-log.md) | Dated log of what each session did and decided | **Every session, appended** |
| [305-mem-lessons.md](305-mem-lessons.md) | Things that went wrong or were non-obvious, and what to do instead | Whenever something costs time |

New memory files take the next free number (306, 307, ...) and are added to this table.

## Rules for writing memory

1. **Write it when it happens, not at the end.** A session can be cut off at any moment (context limit, sandbox stop). After each sub-version, each owner instruction and each surprise, update the relevant file and commit.
2. **302 is always true.** If you stop mid-task, 302 must say exactly where you stopped and what the next command or file is.
3. **304 is append-only.** Add a dated entry; never rewrite old entries.
4. **Do not duplicate 00 to 17.** Decisions go in 00, open questions in 15, plan changes in 14 and the changelog. Memory points to them.
5. **Record the owner's words when they matter.** Instructions are kept close to how the owner phrased them, with the plain meaning beside them, because paraphrase drifts.
6. **Dates are absolute** (10 Nov 2026, not "today").
7. **No secrets.** Never write passwords, keys, tokens or real client data here. Say where a secret lives, not what it is.
8. Memory files live on `forge` only, like the rest of `/docs`. Commit them as the owner, with no co-author line.

## For a subagent

A subagent starts with no context. When you hand work to one, tell it to read `CLAUDE.md` and this file first, give it the stage and sub-version, and name the documents that define the task. Ask it to report what it changed and what it could not verify; check the diff yourself before committing or releasing.
