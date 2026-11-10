# 14. Build plan

The build is cut into eleven stages, S0 to S10. Each stage ends in a working, released version on `main`; each stage is split into sub-versions that are also released when they work on their own. Version numbering is explained in 13.

A stage is done only when its **exit checks** pass together with the release gate in 12.

## Order and why

Access and data scoping come first because every later screen depends on them and they are the costliest thing to retrofit. Inventory and the catalogue come before Excel import so there is something to import into. Discovery, then Legal Basis, follow the assessment method. The audit writer is built with the first data screens (S2) so no change is ever unrecorded, though its viewer comes later. Client screens come late because they are reduced views of screens that must exist first.

## Timeline

Target dates assume continuous work from 10 Nov 2026. They are targets, not promises; slips are recorded in the changelog. Stages S3 and S5 cannot finish until the workbooks are uploaded (15).

| Stage | Name | Completes as | Target |
| --- | --- | --- | --- |
| S0 | Foundation | `v0.1.0` | 11 Nov |
| S1 | Access and administration | `v0.2.0` | 12 Nov |
| S2 | Inventory and catalogue | `v0.3.0` | 13 Nov |
| S3 | Excel import and export | `v0.4.0` | 14 Nov |
| S4 | Discovery: activities, elements, data flow | `v0.5.0` | 15 Nov |
| S5 | Legal basis | `v0.6.0` | 16 Nov |
| S6 | Findings, evidence, audit viewer | `v0.7.0` | 17 Nov |
| S7 | Scope checklist and coverage dashboard | `v0.8.0` | 18 Nov |
| S8 | Security review and sign-off | `v0.9.0` | 19 Nov |
| S9 | Client access | `v0.10.0` | 20 Nov |
| S10 | Hardening and version 1 | `v1.0.0` | 22 Nov |

The sandbox's SSH access ends around 17 Nov, in the middle of this plan. Work after that date needs the sandbox extended or the repository moved; see 15.

## S0 Foundation -> v0.1.0

| Version | Delivers |
| --- | --- |
| `v0.0.1` | Next.js + TypeScript project, pnpm, lint, typecheck, Vitest, Playwright, `pnpm verify`. Compose `dev` profile: PostgreSQL, MinIO, Mailpit. Prisma connected, first migration, `/api/health` |
| `v0.0.2` | REX design system: tokens copied from the kit, self-hosted fonts, dark default and light toggle with no flash (A6), base components (button, field, dialog, drawer, toast, status tag) with a component gallery page |
| `v0.0.3` | App shell: top bar, stage rail, empty states, error and not-found pages. Data grid component with virtual rows and inline edit, shown on the gallery with fake data |
| `v0.1.0` | Production `Dockerfile` and `prod` profile with Caddy; contrast script passes for all tokens; performance harness in place |

Exit checks: `docker compose --profile dev up` and `pnpm dev` give a themed shell; production image builds and serves; grid scrolls 2,000 rows smoothly; contrast and axe checks pass in both themes.

## S1 Access and administration -> v0.2.0

| Version | Delivers |
| --- | --- |
| `v0.1.1` | User, Session, SecuritySettings models. Single sign-in page (F1), Argon2id, server-side sessions, sign-out, role-based landing, first-admin bootstrap |
| `v0.1.2` | Invite and reset by JWT link (A1, A2): email through Mailpit and admin copy-link, forgot-password requests, forced change on first login |
| `v0.1.3` | Administration area (A3): overview, firm users, clients, client employees, reset requests; deactivate, force reset, end sessions |
| `v0.1.4` | Security settings screen (A4): lockout, password policy, session timeouts, link lifetimes, all live; IP rate limit; last-admin guard |
| `v0.1.5` | TOTP MFA (A5): setup, recovery codes, Optional / Required per role, admin reset |
| `v0.2.0` | Clients, assessments, members (F2). `lib/authz`, assessment-scoped query helper, audit writer for auth and admin events. Isolation and role-matrix tests |

Exit checks: tests 2, 3, 8 and 9 of 12 pass; an admin can set up a firm, a client, client employees and an assessment end to end; every setting in 07 changes behaviour when switched.

## S2 Inventory and catalogue -> v0.3.0

| Version | Delivers |
| --- | --- |
| `v0.2.1` | The one write path (permission, validation, write, audit in a transaction) and human ID allocation. Owners and Systems grids (F6) with required-field alerts |
| `v0.2.2` | Applications, Vendors, Security controls, Policies (F6); blocked delete with the list of linking records |
| `v0.2.3` | Data Classification catalogue (F7): seed of 20 groups and 254 elements from the workbook, browse and search, per-client Public override |
| `v0.3.0` | Admin catalogue editing with version history; audit entries (F20 recording) for all inventory changes; performance check on the stress fixture |

Exit checks: every inventory entity can be created, edited and deleted with correct IDs; catalogue shows 254 elements in 20 groups; audit rows exist for each change; budget in 04 met.

Depends on: Inventory workbook (exact columns) and Data Classification sheet. Without them, `v0.2.1` and `v0.2.2` are built from the Notion field lists and corrected when the files arrive; `v0.2.3` waits.

## S3 Excel import and export -> v0.4.0

| Version | Delivers |
| --- | --- |
| `v0.3.1` | Column mapping written into 10 from the real workbook. Inventory import (F3): parse, validate all, preview with problem list, all-or-nothing write, import history |
| `v0.3.2` | Re-import with field-by-field change preview and confirm |
| `v0.4.0` | Inventory export (F4) with the same layout and dropdowns; round-trip test |

Exit checks: tests 6 and 7 of 12 pass; the owner's Inventory workbook imports cleanly and the export opens in Excel with working dropdowns.

Depends on: Inventory workbook. **Blocked without it.**

## S4 Discovery -> v0.5.0

| Version | Delivers |
| --- | --- |
| `v0.4.1` | Activities (F8): grid and detail with the 14 ROPA fields, role, exemption, children, collection point and walkthrough tabs; links to systems, apps, vendors, controls |
| `v0.4.2` | Activity elements (F9): catalogue picker, per-use flags, roll-ups (rule R-1) |
| `v0.4.3` | Flow nodes (F10) and data flow steps (F11) with derived trust zone (R-2) |
| `v0.4.4` | Data path checks (F12, R-3) shown beside the flow and on the activity grid |
| `v0.5.0` | ROPA sheet import and export; Auklet School demo loads as a fixture through the importer |

Exit checks: the Auklet demo's activities, elements and flows load; roll-ups, zones and path checks match the workbook; no zone can be typed.

Depends on: ROPA sheet and the Auklet demo workbook for R-2, R-3 and the fixture.

## S5 Legal basis -> v0.6.0

| Version | Delivers |
| --- | --- |
| `v0.5.1` | Test catalogue seeded from the workbook; admin editing with history and the Verify tag (F17) |
| `v0.5.2` | Legal basis review (F14): route picker, tests for the route only, outcome and why (R-4), "not a legal opinion" note |
| `v0.5.3` | Route mismatch flag (F15, R-5) and element check (F16) |
| `v0.6.0` | Legal Basis Review sheet import and export; legal basis overview screen; **Auklet parity test passes** |

Exit checks: test 1 of 12 passes exactly (1 Supported, 3 Gap, 2 Gap: no legal basis, 2 Cannot conclude yet).

Depends on: Legal Basis Review sheet. **Blocked without it.**

## S6 Findings, evidence, audit viewer -> v0.7.0

| Version | Delivers |
| --- | --- |
| `v0.6.1` | Findings log (F18): against activity, system or vendor; auto-filled department and law reference; statuses; share flag; reviewer comments |
| `v0.6.2` | Evidence (F19): compress, encrypt, MinIO; attach to finding, test answer, control; permission-checked download |
| `v0.6.3` | Findings export that matches the screen |
| `v0.7.0` | Audit log viewer (F20) per assessment and in Administration, with before and after values and filters |

Exit checks: tests 10 and 11 of 12 pass; exported findings equal the on-screen list.

## S7 Scope checklist and coverage dashboard -> v0.8.0

| Version | Delivers |
| --- | --- |
| `v0.7.1` | Phase 1 checklist (F5): entity questions, per-activity questions, applicability result (R-8) |
| `v0.8.0` | Coverage dashboard (F13, R-6) as the assessment home: missing items, counts by outcome, links to the rows |

Exit checks: checklist wording and law references match the workbook; every dashboard count links to exactly the rows it counts.

Depends on: Applicability checklist workbook for F5.

## S8 Security review and sign-off -> v0.9.0

| Version | Delivers |
| --- | --- |
| `v0.8.1` | System security review (F21, R-7): five rows per system, evidence seen, result, highest tier |
| `v0.9.0` | Send for review, sign-off and lock, admin unlock with reason (A7); catalogue version pinned at lock |

Exit checks: test 4 of 12 passes; a reviewer can complete sign-off end to end; an assessor cannot.

Depends on: the workbook or a written rule for the R-7 result matrix.

## S9 Client access -> v0.10.0

| Version | Delivers |
| --- | --- |
| `v0.9.1` | Client contributor entry (F23): client home, reduced inventory and activity screens, evidence upload to own items |
| `v0.10.0` | Client findings view (F24) after sign-off, for contributor and viewer |

Exit checks: test 5 of 12 passes; test 2 re-run across every route added since S1.

## S10 Hardening and version 1 -> v1.0.0

| Version | Delivers |
| --- | --- |
| `v0.10.1` | Performance pass against the full budget on the stress fixture; query and bundle review |
| `v0.10.2` | Security pass: review of every server action and download for permission checks, headers, dependency audit, secrets check |
| `v0.10.3` | Accessibility and visual pass on every screen in both themes; tablet check; empty, error and read-only states |
| `v1.0.0` | Production deployment rehearsed from a clean machine using 11; backup and restore rehearsed; `/docs` reviewed line by line against the product; a short user guide per role |

Exit checks: every success measure in 01 is demonstrated; the release gate passes in full; an install from the `v1.0.0` tag on a clean server works by following 11 only.

## After version 1

F22 (other duties), F25 (diagram), F26 to F28 (rate, remediate, report), F29 (notifications), processor logins, single sign-on. None is planned in detail.

## How progress is recorded

| Stage | Status | Released | Notes |
| --- | --- | --- | --- |
| S0 | Not started | -- | |
| S1 | Not started | -- | |
| S2 | Not started | -- | |
| S3 | Not started | -- | Needs workbooks |
| S4 | Not started | -- | Needs workbooks |
| S5 | Not started | -- | Needs workbooks |
| S6 | Not started | -- | |
| S7 | Not started | -- | Needs checklist workbook |
| S8 | Not started | -- | |
| S9 | Not started | -- | |
| S10 | Not started | -- | |

This table is updated in the same commit as each release.
