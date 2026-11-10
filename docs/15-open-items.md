# 15. Open items

Things that are missing, unverified or at risk. Each is closed by a decision in 00 or a change to the relevant document.

## Blocking

| # | Item | Blocks | Needed from |
| --- | --- | --- | --- |
| O-1 | **Excel workbooks not uploaded.** Needed in `/srv/comply/source-workbooks/`: (a) Inventory workbook, (b) the workbook with the ROPA, Legal Basis Review and Data Classification sheets, (c) the Applicability and exemptions checklist, (d) the Auklet School demo if it is a separate file. | S2 catalogue seed, S3, S4 rules, S5, S7 checklist, the parity test | Owner |
| O-2 | **Sandbox access ends around 17 Nov 2026**, about halfway through the plan. No backup is made (D-43) and nothing is pushed. | Everything after that date | Owner: extend the sandbox, or move the repository before then |

## To confirm from the workbooks

| # | Item | Document |
| --- | --- | --- |
| O-3 | Exact columns of every Inventory sheet, including the Policy Inventory | 05, 10 |
| O-4 | The exact 14 ROPA template fields and their order | 05 |
| O-5 | Which tests belong to which route; what K1 to K3, E1, E2 and R1 apply to | 06 R-4 |
| O-6 | How zone is derived from system hosting and location and from vendor data location | 06 R-2 |
| O-7 | Tier order and the mapping of claimed-basis wording to routes | 06 R-1, R-5 |
| O-8 | The Rule 6 (a) to (e) result matrix: what "client says" is built from and how it combines with evidence seen | 06 R-7 |
| O-9 | Phase 1 checklist questions and how answers map to duties and exemptions | 06 R-8 |
| O-10 | Whether findings from the security review use the `LB-` prefix or their own | 05 |
| O-11 | Meaning of flags D2, D3, D4, D7 as worded in the workbook, and whether D1, D5, D6 exist elsewhere | 05 |

## To verify outside the project

| # | Item |
| --- | --- |
| O-12 | "Most client duties under the Rules start about 13 May 2027" is a working statement. Verify against the Gazette before it appears in any client-facing text. |
| O-13 | Every law reference in the test catalogue carries a Verify tag until an admin clears it against the Gazette text. |

## Risks accepted for version 1

| # | Risk | Mitigation |
| --- | --- | --- |
| O-14 | Uploaded evidence is not virus-scanned | Type allow-list, files are only ever downloaded as attachments, never rendered by the app. Scanner (ClamAV) can be added as a Compose service later |
| O-15 | Arial is a system font; on a device without it the fallback (Helvetica, then the default sans) is used | Acceptable; widths are tested with the fallback |
| O-16 | Backups in production are scripted but not scheduled | Documented in 11; scheduling is the server owner's task |
| O-17 | Reset links copied by an admin pass through a second person | Links are single-use and short-lived; the copy action is in the audit log |

## Departures from the Notion documents

| # | Departure | Why |
| --- | --- | --- |
| O-18 | Auth.js replaced by an in-house credentials flow with server-side sessions | Admin-adjustable lockout, timeouts and forced sign-out need a session record (04, 07). **Owner to confirm.** |
| O-19 | F22 and processor logins removed from version 1 | D-04, D-05 |
| O-20 | F5, F13, F17, F19, F20, F21, F23, F24 promoted from "if time allows" to planned | D-03 |
| O-21 | Evidence in MinIO from the start, not a local volume | D-25 |
