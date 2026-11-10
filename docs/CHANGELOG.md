# Changelog of documents and plan

Newest first. One line per change: what changed, in which document, and why.

## 10 Nov 2026

- Created the `/docs` folder from the Notion page "DPDP Assessment App: Project Documents" and the owner's answers to 16 planning questions (recorded in 00).
- 02: added features A1 to A7 (password reset, invites, administration area, security settings, MFA, theme switch, sign-off) from the owner's answers; mapped every feature to a build stage.
- 02, 01: F22 and processor logins removed from version 1 (D-04, D-05); eight Should features confirmed in (D-03).
- 04: Auth.js replaced by an in-house credentials flow with server-side sessions; reason in 04 and 07; awaiting owner confirmation (O-18).
- 04: added a measured performance budget because the owner requires fast loading (D-21).
- 07: evidence storage changed from a local volume to MinIO with compress-then-encrypt (D-25); Mailpit added for email (D-23).
- 14: first build plan, stages S0 to S10, versions `v0.0.1` to `v1.0.0`.
- 16: seven skill folders installed in `/.skills`; ponytail also installed as a Claude Code plugin.
