# 15. Open items

Things that are missing, unverified or at risk. Each is closed by a decision in 00 or a change to the relevant document. Closed items are kept at the bottom so the numbers stay stable.

## Blocking

| # | Item | Blocks | Needed from |
| --- | --- | --- | --- |
| O-1 | **Demo and acceptance data.** Settled on 11 Nov 2026 by the three fictional clients in 18 (D-46). They are written descriptions, not filled workbooks, so the fixtures are keyed in by hand and no Excel-cached values exist to compare against. | Nothing. See O-37 and O-38 for what remains | -- |
| O-2 | **Sandbox access ends around 17 Nov 2026**, about halfway through the plan. No backup is made (D-43) and nothing is pushed. | Everything after that date | Owner: extend the sandbox, or move the repository before then |
| O-8 | **The Phase 4 system security review (F21) is not defined anywhere.** Workbook 4 says it is outside its scope. Notion describes "Rule 6 items (a) to (e), five rows per system", but the Security Controls sheet lists seven Rule 6 items (Encryption or masking, Access control, Logging and monitoring, Backup and continuity, Log retention (1 year), Processor contract, Other measures). Needed: the five items, what "client says" is built from, and the Pass / Partial / Gap / Not tested matrix. **Narrowed on 11 Nov 2026:** section 13 of each demo client file (18) shows five items per system, (a) Encryption, (b) Access control, (c) Access logs, (d) Backup, (e) Log retention of 12 months or more, as "client says / evidence seen / result", with results Pass, Partial, Gap (client confirms), Gap: claim not supported, Not tested. Still needed: the owner's confirmation that this is the design, and the full matrix from the two inputs to the result. | `v0.8.1` in S8 | Owner |

## For the owner to confirm

Choices made from the workbooks where they were silent or differed from Notion. The build proceeds on these unless the owner says otherwise.

| # | Item | Document |
| --- | --- | --- |
| O-18 | Auth.js replaced by an in-house credentials flow with server-side sessions | 04, 07 |
| O-22 | Workbook 1 (organisation profile, departments) added to version 1 (D-12) | 02 A8, 05 |
| O-23 | One client = one legal entity; a group is several clients (D-13) | 05 |
| O-24 | Checklist questions shown as A-E1, B-P3, C-D2 to avoid the clash with element tests E1 and E2 (D-15) | 05 |
| O-25 | A separate country field on systems, used for the zone when filled, because the workbook's zone rule searches the location text for the word "India" and would misread a place such as "Indiana, USA" | 06 R-2 |
| O-26 | New controls and policies get `CTL-` and `POL-` IDs; the workbook gives them no prefix | 05 |
| O-10 | Finding IDs use `LB-` for every phase. The workbook's Finding ID has no format, and Notion names `LB-` only | 05 |
| O-27 | Findings can point to a system or vendor (Notion F18) although the workbook's Findings sheet only has an Activity ID | 05 |
| O-28 | Open element checks (E1 or E2 blank or Not sure) do not make an activity "Cannot conclude yet", because the workbook formula does not count them. They are listed on the coverage dashboard instead | 06 R-7 |
| O-37 | Brannock's expected totals: the file's opening table (4 Supported, 2 Gap, 1, 1, 2 Out of scope) differs from its section 12 (6, 3, 1, 1, 1). The build follows section 12 | 18 |
| O-38 | The optional extra rows ACT-008b and ACT-007b (Halvorn) are not loaded; Brannock's ACT-008b is loaded because its section 12 counts it. The "b" rows get ordinary ACT numbers | 18 |
| O-39 | Excel structure check: every expected header must be present, not only the mandatory ones; a missing one is an error | 19, 10 |
| O-40 | Unknown extra columns and sheets are ignored and reported as notes, not errors | 19 |
| O-41 | A single-sheet export holds that sheet plus the reference sheets its dropdowns need | 19 |
| O-42 | A sheet import may not refer to records that are not yet in Comply; the message names the sheet to import first | 19 |
| O-43 | Which colours, if any, mark statuses under the plain interim theme, and when the REX theme is switched on | 08 |

## To confirm in Excel during the build

| # | Item | Stage |
| --- | --- | --- |
| O-29 | Which dropdown list sits on each question of sections 1 to 6 of the Organisation sheet. These validations use a newer Excel format the reading script could not open; the lists themselves are known (hidden Data sheet) | S2 |

## To verify outside the project

| # | Item |
| --- | --- |
| O-12 | "Most client duties (Rules 3, 5-16, 22, 23) start about 13 May 2027; Rule 4 about 13 Nov 2026." The workbook marks this as to verify, with sources differing by a day. Check the Gazette before it appears in client-facing text |
| O-13 | Every law reference in the test catalogue and checklist carries a Verify tag until an admin clears it against the Gazette text. The workbooks single out Sec 5(2) (older consents), Rule 3, Rule 10 and the Fourth Schedule wording |
| O-30 | The checklist's notification status (no Significant Data Fiduciary list, no Sec 17(3) startup notification) is "as at 9 Oct 2026" and must be re-checked on each assessment's reference date |
| O-31 | Workbook 3's tier definitions are marked "proposals for review" |

## Data handling

| # | Item | Status |
| --- | --- | --- |
| O-32 | **A real client name is in a file described as clean.** Workbook 3, Owners sheet: a real client name, document ID a real document ID. | The Excel files are kept out of git. Templates committed for export are cleaned first and a test guards against the name (10, 12). On 11 Nov 2026, before the repository was made public, the name was also removed from all documents and all history (D-48) |
| O-33 | The same workbooks sit untracked inside the owner's REX brand repository (`/data/home/REX/DPDP-Workbooks`) and in `/data/home/DPDP-Workbooks-Clean.zip`. A `git add .` in the REX repository would commit them there | Owner's call; nothing was changed in that repository |

## Risks accepted for version 1

| # | Risk | Mitigation |
| --- | --- | --- |
| O-14 | Uploaded evidence is not virus-scanned | Type allow-list; files are only ever downloaded as attachments, never rendered by the app. A scanner (ClamAV) can be added as a Compose service later |
| O-15 | Arial is a system font; on a device without it the fallback is used | Acceptable; widths are tested with the fallback |
| O-16 | Backups in production are scripted but not scheduled | Documented in 11; scheduling is the server owner's task |
| O-17 | Reset links copied by an admin pass through a second person | Links are single-use and short-lived; the copy action is in the audit log |

## Departures from the Notion documents

| # | Departure | Why |
| --- | --- | --- |
| O-18 | Auth.js replaced by an in-house credentials flow | See above |
| O-19 | F22 and processor logins removed from version 1 | D-04, D-05 |
| O-20 | F5, F13, F17, F19, F20, F21, F23, F24 promoted from "if time allows" to planned | D-03 |
| O-21 | Evidence in MinIO from the start, not a local volume | D-25 |
| O-34 | Route names follow the workbook: "Legitimate use (Sec 7)", not "Sec 7 use"; "Consent (Sec 6)"; "Exemption only (Sec 17)" | D-14 |
| O-35 | The Phase 1 checklist shows what each answer decides as text and computes no applicability result | The workbook has no such formula (06 R-11) |
| O-36 | Import and export cover four workbooks, not "the Inventory workbook and three sheets" | That is how the files are actually organised |

## Closed

| # | Item | Closed by |
| --- | --- | --- |
| O-3 | Exact columns of every Inventory sheet, including the Policy Inventory | 17 Part 2; 05 |
| O-4 | The exact 14 ROPA template fields and their order | 17; 05 |
| O-5 | Which tests belong to which route; what K, E and R tests apply to | 06 R-7: K tests when children's data = Yes; E1 and E2 per element; R1 is the "no basis" result |
| O-6 | How zone is derived | 06 R-2 |
| O-7 | Tier order and the mapping of claimed basis to routes | 06 R-1, R-6 |
| O-9 | Phase 1 checklist questions and what answers lead to | 17; 06 R-11 |
| O-11 | Meaning of flags D2, D3, D4, D7, and where D1, D5, D6 are | 06 R-11: D1 is "Personal data?", D5 the high-risk type and D6 the fixed-retention law, all on the catalogue |
