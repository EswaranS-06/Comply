# Changelog of documents and plan

Newest first. One line per change: what changed, in which document, and why.

## 10 Nov 2026 (later still): working memory

- 300 to 305 (new): working memory in `/docs`, at the owner's instruction, so that a build driven by Claude Sonnet (with a stronger model as subagent where needed) starts from everything learned so far and nothing is lost to context compaction.
- `CLAUDE.md` rewritten: read the memory first, keep it current, do not build until the owner says so, how to brief subagents.
- Build is on hold until the owner gives the go-ahead (301, I-18).

## 10 Nov 2026 (later): workbooks received

- The four template workbooks were found in `/data/home/REX/DPDP-Workbooks`, copied to `source-workbooks/` (not committed) and read in full.
- 17 (new): summary of the workbooks, with every column header and dropdown list generated from the files.
- 06: rewritten from the actual formulas. Rules renumbered R-0 to R-12; row alerts (R-0), cross-border check (R-5) and element finding (R-8) added; outcome rule corrected (exemption tests also count when an exemption is claimed, children tests when children's data is present, consent status "Not captured" fails, blank Sec 7 clause is open). All "pending workbook" markers removed.
- 05: field lists replaced with the workbook's; added Organisation profile, Department, Client element, Checklist question and Reference list; applications, policies and owners gained fields Notion did not list.
- 10: rewritten for four workbooks; export now fills the template; parity warnings compare computed values with the workbook's cached values.
- 02: A8 (organisation profile and departments) added; F3, F4, F5, F6, F7, F11, F12, F14, F15, F16, F21 reworded to the workbook's logic.
- 09: Organisation screens added; checklist and legal basis screens updated; security review screen marked not designed.
- 14: workbook dependencies removed from S2 to S7; S2 gains `v0.2.3` (organisation profile, seed script) and the catalogue moves to `v0.2.4`; other workbooks join import and export in the stage that builds their screens; S5 exit check split so only the Auklet totals wait for the demo; S8 notes F21 is blocked.
- 15: O-3 to O-7, O-9, O-11 closed; O-1 narrowed to the missing Auklet demo; O-8 raised to blocking; O-22 to O-36 added.
- 00: D-11 updated; D-12 to D-15 added.
- 12: parity test split into three parts; template hygiene test added.

## 10 Nov 2026

- Created the `/docs` folder from the Notion page "DPDP Assessment App: Project Documents" and the owner's answers to 16 planning questions (recorded in 00).
- 02: added features A1 to A7 (password reset, invites, administration area, security settings, MFA, theme switch, sign-off) from the owner's answers; mapped every feature to a build stage.
- 02, 01: F22 and processor logins removed from version 1 (D-04, D-05); eight Should features confirmed in (D-03).
- 04: Auth.js replaced by an in-house credentials flow with server-side sessions; reason in 04 and 07; awaiting owner confirmation (O-18).
- 04: added a measured performance budget because the owner requires fast loading (D-21).
- 07: evidence storage changed from a local volume to MinIO with compress-then-encrypt (D-25); Mailpit added for email (D-23).
- 14: first build plan, stages S0 to S10, versions `v0.0.1` to `v1.0.0`.
- 16: seven skill folders installed in `/.skills`; ponytail also installed as a Claude Code plugin.
