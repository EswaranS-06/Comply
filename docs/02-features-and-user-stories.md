# 02. Features and user stories

Priority: **Must** = needed for version 1. **Should** = in version 1 by decision D-03 unless marked dropped. **Later** = after version 1. "Stage" is the build stage in [14-build-plan.md](14-build-plan.md). IDs F1 to F29 come from Notion; A1 to A7 were added on 10 Nov 2026 from the owner's answers, and A8 from the workbooks. Acceptance criteria that quote a rule (R-0 to R-12) refer to [06-rules-engine.md](06-rules-engine.md), which holds the exact workbook logic.

## Access and administration

| ID | Feature | Story | Acceptance criteria | Priority | Stage |
| --- | --- | --- | --- | --- | --- |
| F1 | Sign in and roles | A user signs in with email and password on the single sign-in page; the system shows only what their role allows | Wrong password is refused with a message that does not reveal whether the email exists. A client user cannot open another client's data, by screen or by direct URL or API call. Role rules follow 03. | Must | S1 |
| A1 | Password reset | A user asks for a reset; the system issues a one-time link by email and to the admin | Link is a signed JWT, valid 30 minutes (admin-adjustable), usable once. Using it signs out every other session of that user. | Must | S1 |
| A2 | Invite and first login | An admin creates a user; the user sets their own password from a one-time link | Admin never sees or sets the user's password. Link is emailed and shown to the admin to copy. | Must | S1 |
| A3 | Administration area | An admin manages firm users, clients, each client's employees, and assessment members | Create, edit, deactivate, change role, resend invite, force reset, end sessions. A deactivated user is signed out at once. Lists are searchable and filterable by client, role and status. | Must | S1 |
| A4 | Security settings | An admin switches and tunes lockout, password policy, session timeout and MFA | Each setting has on/off and values (see 07). Changes apply without restart and are written to the audit log. | Must | S1 |
| A5 | Optional TOTP MFA | A user turns on an authenticator app; an admin can require it per role | Setup shows a QR code and recovery codes. Admin can reset a user's MFA. | Should | S1 |
| A6 | Theme switch | A user switches between REX dark and light | Dark by default. Choice is remembered per user and applied before first paint (no flash). | Must | S0 |
| F2 | Clients and assessments | An assessor creates a client and an assessment with a reference date | An assessment holds its own data. Two assessments for one client do not mix data. | Must | S1 |
| F3 | Excel import | An assessor uploads any of the four workbooks; the system reads the sheets into records | Rows import with their IDs. A row problem is listed with workbook, sheet, row and reason. Nothing is half-imported. Re-import asks before overwriting. Auto columns are ignored and compared (parity warnings). Details in 10. | Must | S3 to S7, per workbook |
| F4 | Excel export | An assessor downloads the data as the same four workbooks | Exported sheets open in Excel with the same layout, dropdowns, formulas and column order, because the export fills the template. | Must | S3 to S7, per workbook |
| F30 | Sheet import and export on every screen | On any screen that holds the data of one sheet, an assessor exports that sheet or imports it | Each such screen has Export sheet and Import sheet. The same checks, preview and confirm as F3. Listed per screen in 19. | Must (D-47) | S3 to S7, with each screen |
| F31 | Excel page with structure check | On one page an assessor imports and exports any sheet or all four workbooks, and sees why a file was rejected | Sheet names and headers are checked against the sheet map before any row is read; a missing sheet or header is an error with the exact name, and nothing is imported. The page shows the expected headers per sheet and the history of runs. Details in 19. | Must (D-47) | S3 |
| A8 | Organisation profile and departments | An assessor or client contributor fills the client's profile (37 questions) and lists its departments | Fields and dropdowns match workbook 1. Departments are picked on activities and owners. Section 7 answers are shown beside the matching Part A checklist questions. | Must | S2 |

## Phase 1: Scope and Role

| ID | Feature | Story | Acceptance criteria | Priority | Stage |
| --- | --- | --- | --- | --- | --- |
| F5 | Applicability and exemptions checklist | An assessor answers Part A (E1 to E13) once and Part B (P0 to P14) per activity; the system shows what each answer decides | The 35 questions, answer lists, law references and "What the answer decides" texts match workbook 2. Part C (D1 to D7) is not a separate screen: it is the element flags and catalogue fields. No automatic conclusion is computed, because the workbook has none (R-11). | Should | S7 |

## Phase 2: Discover Data

| ID | Feature | Story | Acceptance criteria | Priority | Stage |
| --- | --- | --- | --- | --- | --- |
| F6 | Inventory records | A user adds systems, applications, vendors, security controls, policies and owners; the system gives each an ID and flags missing answers | IDs are SYS-, APP-, VEN-, unique within the assessment. Row alerts follow R-0 exactly: mandatory fields, and fields that are not applicable given another answer. | Must | S2 |
| F7 | Data Classification catalogue | An assessor browses and searches 254 elements by group; the system shows type, tier and high-risk type | Read-only for assessors. Public tier can be set per client; other tiers are fixed. Only an admin edits the catalogue, with history. An assessor can add client-specific elements, which stay inside that assessment. | Must | S2 |
| F8 | ROPA activities | An assessor adds an activity (one purpose); the system keeps one row per activity following the 14-field ROPA template | All 14 template fields are present, plus role, exemption, children, collection point and walkthrough fields. One purpose is one activity. | Must | S4 |
| F9 | Activity data elements | An assessor picks elements from the catalogue for an activity; the system fills name, group, type, tier and high-risk type and rolls up categories, highest tier and high-risk types onto the activity | The same element can be in many activities. Roll-ups update at once. Flags D2, D3, D4, D7 are saved per use. | Must | S4 |
| F10 | Flow nodes | An assessor adds people, departments and outside organisations that are not in the Inventory | IDs are DP-, DEP-, EXT-. Each has a type, a zone and a country. | Must | S4 |
| F11 | Data flow | An assessor records each place an activity's data passes through, whether it is shared further, and with whom | Each step points to a system, app, vendor or flow node. Shared with accepts node IDs and activity IDs. Zone is worked out from the Inventory (R-2) and never typed for systems, apps and vendors. | Must | S4 |
| F12 | Data path checks | The system flags missing or contradictory flow answers | The step check (R-3), activity path check (R-4) and cross-border check (R-5) give the workbook's results word for word. | Must | S4 |
| F13 | Coverage dashboard | An assessor sees what is still missing | Lists activities with no elements, no flow, no owner, or no basis; counts by outcome. | Should | S7 |

## Phase 3: Legal Basis

| ID | Feature | Story | Acceptance criteria | Priority | Stage |
| --- | --- | --- | --- | --- | --- |
| F14 | Legal basis review | An assessor picks the route (Consent (Sec 6), Legitimate use (Sec 7), Exemption only (Sec 17), Out of scope, None identified) and answers only the tests that apply; the system works out the outcome | The 23 tests as in workbook 4. Consent tests for the Consent route, Sec 7 tests for the Sec 7 route, Exemption tests when the route is Exemption only or an exemption is claimed, Children tests when the activity has children's data. Outcome, tests failed, tests open and Why follow R-7 exactly, including: consent status "Not captured" fails a Consent-route activity, and a blank Sec 7 clause counts as open. | Must | S5 |
| F15 | Route mismatch flag | The system compares our route with the basis the client claimed in the ROPA | Follows R-6. A mismatch shows "ROPA says: ..." in the danger colour. | Must | S5 |
| F16 | Element check | An assessor marks each element Needed and Named in notice; the system feeds a No into the consent result | A No on either counts as one failed consent test for the activity. Each element row shows its own finding (R-8), including a child flag that differs from the activity. | Must | S5 |
| F17 | Test catalogue | An admin maintains the questions, plain reading, law reference and evidence to ask for | Edits keep a version history. Law references show a Verify tag until an admin clears it. | Should | S5 |

## Findings and evidence

| ID | Feature | Story | Acceptance criteria | Priority | Stage |
| --- | --- | --- | --- | --- | --- |
| F18 | Findings log | An assessor logs a gap against an activity, system or vendor; the system fills the department and law reference | Status values: Open, Client to respond, Agreed, Disputed, Closed. Rating stays blank until Phase 5. Findings export matches the screen. | Must | S6 |
| F19 | Evidence attachments | A user attaches a file to a finding, test answer or control | Files open only for allowed roles. File name, uploader and date are kept. Stored compressed and encrypted in MinIO (07). | Should | S6 |
| F20 | Audit log | A reviewer sees who changed which answer and when | Every create, update and delete on assessment data is recorded with before and after values. Recording starts in S2; the viewer screen ships in S6. | Should | S2, S6 |

## Phase 4: Duties

| ID | Feature | Story | Acceptance criteria | Priority | Stage |
| --- | --- | --- | --- | --- | --- |
| F21 | System security review | An assessor records the evidence seen for each Rule 6 item (a) to (e) per system; the system compares it with what the client says and gives Pass, Partial, Gap or Not tested | Rows build from the Inventory, five per system. Highest data tier shows on each row. **Blocked: the workbooks do not define this review (R-12, open item O-8).** | Should | S8 |
| F22 | Vendor, client and activity duties | -- | **Dropped from version 1 (D-04).** | -- | -- |

## Sign-off

| ID | Feature | Story | Acceptance criteria | Priority | Stage |
| --- | --- | --- | --- | --- | --- |
| A7 | Sign-off and lock | A reviewer signs off an assessment; the system locks it | Status moves Draft, In review, Locked. A locked assessment is read-only for everyone except an admin, who must give a reason that is written to the audit log. An assessor cannot sign off (D-08). | Must | S8 |

## Client access

| ID | Feature | Story | Acceptance criteria | Priority | Stage |
| --- | --- | --- | --- | --- | --- |
| F23 | Client contributor entry | A client user fills inventory and walkthrough facts for their own assessment | Cannot see assessor notes, tests, routes, outcomes or other clients (D-09). | Should | S9 |
| F24 | Client findings view | A client lead reads findings the assessor has shared | Only findings marked Shared are visible, and only after sign-off (D-10). | Should | S9 |

## Later (not in version 1)

| ID | Feature |
| --- | --- |
| F22 | Vendor, client and activity duties |
| F25 | Interactive data flow diagram (focus, expand, drag, export PNG, SVG, draw.io) |
| F26 | Ratings using tier and high-risk fields |
| F27 | Remediation tracking with owner and due date |
| F28 | Report generation |
| F29 | In-app and email notifications beyond account emails |
| -- | Processor (vendor) logins, single sign-on, multi-firm management |
