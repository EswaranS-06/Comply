# 301. Memory: the owner and how they want the work done

## The owner

- Git identity: `EswaranS-06 <eswaransk06@gmail.com>`. Works in cybersecurity; owns the REX Cybersecurity brand (`/data/home/REX`).
- Runs DPDP (India) compliance assessments for clients using Excel workbooks they designed. Comply turns that method into an app.
- Writes short, fast messages, often with typos. Read for intent; when a message is genuinely ambiguous on something that matters, ask, otherwise pick the sensible reading and say which you picked.
- Likes being asked questions before work starts ("ask me tons of question"), likes clear recommendations with the options, and usually takes the recommended one but adds their own conditions. **Read the additions carefully**: they are where the real requirements are.

## Standing instructions

Each is given as the owner said it (lightly trimmed), then what it means in practice.

| # | Date | Owner said | Means |
| --- | --- | --- | --- |
| I-1 | 10 Nov 2026 | "you are going to only use git in local to commit in git No co-author claude and only my name" | Local git only. Never push or add a remote. No `Co-Authored-By` or any tool attribution in commits. Identity is already configured; do not change git config |
| I-2 | 10 Nov 2026 | "`main` you create a own timeline & plan ... everytime you cover each phase create a version also create sub versions then keep the completely working versions/sub-verisons in the `main` this exculdes the `/docs` & `/.skills`" | `main` = only verified working versions, tagged, without `docs`, `.skills`, `CLAUDE.md`. Use `scripts/release.sh`. See 13 |
| I-3 | 10 Nov 2026 | "another branch which have the upto date branch never checked just build and working this have the `/docs` & `/.skills`" | `forge` = the working branch with everything. Commit there freely |
| I-4 | 10 Nov 2026 | "if anything changes while building no issues just write the `/docs` bcz not every goes as plan" | Deviating from the plan is fine. Not recording the deviation is not. Update the document and the changelog in the same commit |
| I-5 | 10 Nov 2026 | "go to the `/data/home/REX` these are theme, font, colour you are going to use so now you are only using this" | REX is the only visual source. No other colours or fonts. Copies are in `.skills/rex-brand` and `.skills/rex-website`. See 08 |
| I-6 | 10 Nov 2026 | "every skills that should exist in the /.skills folder and write it when you are using it" | Any skill used must be in `.skills` and committed; log each use in 16 |
| I-7 | 10 Nov 2026 | "it should be fast not slow loading" | Speed is a requirement with numbers (04, performance budget). Check it before releases |
| I-8 | 10 Nov 2026 | "keep the logins easy (email,pass->login->reset password with JWT (but secure it in the transit) also the login page is only single page" | One sign-in page for all roles; email and password; reset by signed JWT link over HTTPS. See 07 |
| I-9 | 10 Nov 2026 | "you should create a best administration page for managing client, their employee's and processor's logins(if required)" | The admin area is a first-class feature, not a side screen. (Processor logins were later dropped from version 1, D-05) |
| I-10 | 10 Nov 2026 | "i want these like option to able from the admin page too" (about lockout, password policy, session timeout, MFA) | All four are built and each is switchable and tunable from the admin area. See 07 |
| I-11 | 10 Nov 2026 | "go with the both options and use mailpit" | Reset and invite links go by email (Mailpit in dev) and are also shown to the admin to copy |
| I-12 | 10 Nov 2026 | "use the MinIO and try to compress and encrypted to save storage" | Evidence in MinIO; compress, then encrypt. See 07 |
| I-13 | 10 Nov 2026 | "I go with the Recommended option but i also wants it portable Docker Compose" | Target is the owner's own Linux server in India, but the Compose project must run unchanged anywhere |
| I-14 | 10 Nov 2026 | "if it's stops just wait for 5-20mins and try ssh it will automatically starts and you can continue" | A sandbox stop is normal. Wait, reconnect, restart services, carry on from the last commit. See 303 |
| I-15 | 10 Nov 2026 | "once copied it as excel file also along with summarizes it as a .md file" | Keep source material as its original file and also write a Markdown summary of it in `/docs` (done as 17) |
| I-16 | 10 Nov 2026 | "i'm ofc going to create the project with sonnet if needed you as subagents" | The build will be driven by Claude Sonnet. A stronger model is used as a subagent only where needed (hard design or debugging). Documents must therefore be complete and explicit enough for Sonnet to follow without the original conversation |
| I-17 | 10 Nov 2026 | "from now write you memory in the `/docs` with numbers of `3XX+` like `300-mem` so instead of compact and lose memory write it now" | Working memory lives in `docs/3XX-mem-*.md`, kept current and committed. See 300 |
| I-18 | 10 Nov 2026 | "do that instead of building the project wait i tell you" | **Do not start building until the owner explicitly says so.** Planning, documents and memory only |

## Preferences observed (not stated outright)

- Wants things committed, not left in the working tree.
- Chose "Nothing extra" for backup: do not create bundles, snapshots or remotes unprompted. Mentioning the sandbox expiry risk once is enough; do not nag.
- Accepts recommended defaults quickly when the reasoning is given in one line.
- Wants a "Yes / go" button to mean exactly what was offered, nothing more.
- No emojis in project files (a REX brand rule from the owner's own `memory.md`).
- The owner's REX repository has its own working agreement: do not put brand details into an assistant's private memory; the repository's files are the memory. The same spirit applies here, which is why memory is in `/docs`.

## What to ask before assuming

- Anything that changes scope (adding or dropping a feature).
- Anything touching real client data.
- Anything outside `/srv/comply` (the owner's REX repository, the machine's global config).
- Anything that pushes, publishes or sends data off the machine.

## What not to ask about

- Library choices inside the agreed stack, file layout, naming: decide, and record in the changelog if it differs from 04.
- Whether to update the documents: always yes.
