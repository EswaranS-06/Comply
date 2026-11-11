# 10. Excel import and export

The four workbooks were read on 10 Nov 2026. What they contain is summarised in [17-workbook-summary.md](17-workbook-summary.md), with every column header and dropdown list in its Part 2. This document fixes how Comply reads and writes them.

## Workbooks and sheets

| Workbook | Sheet | Header row | Import | Export | Becomes |
| --- | --- | --- | --- | --- | --- |
| 1 Organisation Profile | Organization | 3 (answers in column C, rows 5 to 47) | Yes | Yes | Organisation profile |
| | Department | 3 | Yes | Yes | Departments |
| | Values, Data | -- | Seed | Yes (unchanged) | Reference lists |
| 2 Applicability Checklist | Checklist | 3 | Answers only (columns G, H) | Yes | Checklist answers; questions are seed |
| | Read Me | -- | No | Yes (unchanged) | -- |
| 3 Inventory workbook | Owners | 17 (document control in rows 2 to 7) | Yes | Yes | Owners; assessment document control |
| | System Inventory, Application Inventory, Security Controls, Vendor List, Policy Inventory | 2 | Yes | Yes | Inventory entities |
| | ROPA | 5 | Yes | Yes | Activities and activity links |
| | Activity Data | 5 | Yes | Yes | Activity elements |
| | Data Flow | 5 | Yes | Yes | Data flow steps |
| | Flow Nodes | 4 | Yes | Yes | Flow nodes |
| | Data Classification | 4 | Seed; then client-added rows and Public tiers only | Yes | Catalogue; client elements; tier overrides |
| | ROPA Read Me, ROPA Values, DC Values | -- | Seed | Yes (unchanged) | Enums and definitions |
| 4 Legal Basis Review | Activity Review | 5 | Columns N, O, Q to AJ, AQ to AS | Yes | Activity reviews and test answers |
| | Element Check | 5 | Columns K, L, P | Yes | Element checks |
| | Findings | 5 | Yes | Yes | Findings |
| | Tests, Law Notes, Values | -- | Seed | Yes (unchanged) | Test catalogue, reference lists |

"Seed" means loaded once by an admin into the shared catalogue (stage S2 and S5), not per assessment.

Export is built by filling a copy of the template workbook, so formatting, colours, Read Me sheets, dropdowns and formulas are kept exactly. The four templates, with the client name removed and sample rows deleted, are stored in the repository under `lib/excel/templates/`.

## Import behaviour (F3)

1. **Upload.** `.xlsx` only, 20 MB limit. One, several or all four workbooks can be uploaded together. The file is parsed on the server and not kept; only its name and checksum are recorded.
2. **Recognise.** Each workbook is recognised by its sheet names, not its file name. Sheets are found by name and columns by header text, not position, so a reordered column still imports. This structure check runs before any row is read: a missing sheet or any missing expected header stops the import with a message naming it. The check, its messages, the single sheet map behind it, the Excel page and the per-screen import and export are planned in [19-excel-exchange.md](19-excel-exchange.md).
3. **Read rows.** A row is read when its ID cell (or first mandatory cell) is filled. The workbooks pre-fill hundreds of empty rows with formulas; those are skipped.
4. **Ignore auto columns.** Every column marked `(auto)` or filled by a formula is ignored: Comply computes these itself. After import, Comply's computed value is compared with the value Excel had cached in the cell; any difference is listed as a **parity warning** (it does not block the import). This is a standing check that the rules in 06 match the workbook.
5. **Validate everything first.** Each row is checked with the same Zod schema the screens use: mandatory columns, dropdown values (exact text; a near miss such as different case is accepted and reported), dates, and ID format. Then links are checked across sheets.
6. **Report.** A preview shows rows to create, rows to update, rows unchanged, parity warnings, and a problem list with workbook, sheet, row number and reason.
7. **Nothing is half-imported.** If any row has a problem, nothing is written. The whole write is one database transaction.
8. **Re-import.** Rows are matched by ID (by owner name for Owners, by activity and element for Activity Data and Element Check, by activity and position for Data Flow). If the import would change existing rows, the preview lists the changes field by field and asks before overwriting. Rows in Comply that are absent from the workbook are left alone, never deleted.
9. **IDs.** IDs in the workbook are kept. The counter for each prefix moves past the highest imported number. A row without an ID gets the next one.
10. **Record.** An Import run row and audit entries are written.

## Rules for particular columns

| Case | Rule |
| --- | --- |
| Sample rows | Rows containing `Sample: delete`, or values starting `(sample`, are listed in the preview and skipped unless the user ticks "import sample rows" |
| Owner columns (dropdown from the Owners sheet) | Matched by name to an Owner in the same import or already in the assessment. An unknown name is a problem |
| ROPA `Department*` | Free text in the workbook. Matched by name to a Department; an unknown name creates the department and says so in the preview |
| ROPA `System IDs*`, `App IDs`, `Control IDs`, `8a. External: Processors (Vendor IDs)` | May hold several IDs separated by `;` or `,`. Each must exist |
| ROPA `7. Internal Recipients`, `8b. External: other recipients`, `10. Security Measures` | Kept as text. IDs inside the text (for example `Operations (DEP-001)`) are not parsed |
| Data Flow `Node ID*` | The workbook's dropdown lists only Flow Node IDs, but SYS-, APP- and VEN- IDs are valid and expected. All four kinds are accepted; the kind is read from the prefix |
| Data Flow `Shared with` | IDs separated by `;`. Node IDs and ACT- IDs are accepted; each must exist |
| Data Flow row order | The order of rows within an activity is kept as the step order |
| Application `Vendor (if third-party)`, `Shares data with` | The workbook stores vendor names. Matched by name to a Vendor; an unknown name is a problem |
| Application `Cross-border transfer (Y/N, country)`, Vendor `Contract start and end dates`, System `Backup` | Kept as the workbook has them (free text or a single list value) |
| Security control `Applies to (System or App ID)*` | One SYS- or APP- ID; must exist |
| Policy `Linked control IDs` | One control ID (the workbook allows a single pick); kept as a many-to-many link so more can be added in Comply |
| Data Classification | Rows matching a catalogue element by ID are compared: a tier of Public becomes a tier override; any other difference from the catalogue is a problem (the catalogue is admin-only). Rows with an unknown ID become client elements of the assessment |
| Activity Review "From the ROPA" columns A to M | Used only to find the activity by ID. If the pasted values differ from Comply's activity, a warning lists the differences; the ROPA values in Comply win |
| Element Check columns C to J | Same: used to find the activity element; differences are warnings |
| Findings `Finding ID` | Kept if present; allocated `LB-` if blank |
| Organisation `Select ...` and example placeholders | The template's placeholder texts (`Select ...`, `e.g. ...`, `As per MCA / ROC filing`, `Type here, one entity per line`) are treated as blank |
| Owners document control | `<... Staff Name>`-style placeholders in angle brackets are treated as blank |
| Dates | Excel dates and text dates in `YYYY-MM-DD` or `DD-MM-YYYY` are accepted; anything else is a problem |

## Export behaviour (F4)

- Same workbooks, same sheet names, same column order and header text, same dropdowns and formatting, because the export fills the template.
- Auto columns keep the template's formulas, and Comply also writes its computed value as the cell's cached result, so the file shows the right outcome even in a viewer that does not recalculate. When Excel recalculates, the formulas produce the same values (this is what the parity tests guarantee).
- Workbook 4 is exported with its "From the ROPA" and Element Check columns filled from Comply, removing the manual paste step.
- A group of more than 992 inventory rows, 300 activities, 1,000 activity elements or flow steps, 200 reviews or 300 findings exceeds the template's prepared rows; the export extends formulas and validations to the rows it needs.
- Findings export matches the findings list on screen, including the current filters if the user chooses "export this view".
- A locked assessment exports with a note of who signed it off and when.
- Round trip is tested: export, then import into an empty assessment, must reproduce the same records with no parity warnings.

## Client data safety

Real client workbooks go in `/srv/comply/source-workbooks/`, which is ignored by git. The templates committed under `lib/excel/templates/` are cleaned first: the a real client name document control values and the sample rows are removed, and a test fails if the string of any known client name appears in a committed template.

## Seed data taken from the workbooks

Committed as JSON under `prisma/seed/`, generated by a script from the workbooks so it can be regenerated when a workbook changes:

| Seed | Rows | From |
| --- | --- | --- |
| Element groups | 20 | DC Values, table 1 |
| Data elements | 254 | Data Classification |
| Type, tier and high-risk definitions | 3 + 4 + 6 | DC Values, tables 2 to 4 |
| Test definitions | 23 | Legal Basis Review, Tests (short labels from the Activity Review headers) |
| Checklist questions | 35 | Applicability Checklist, Checklist |
| Law notes | 9 + 5 + 5 | Legal Basis Review, Law Notes; ROPA Values (Sec 7 in plain words) |
| Fourth Schedule classes, notifiable classes, other laws | 6 + 4 + 28 | Organisation Profile, Values |
| Dropdown lists | all | ROPA Values, Values, hidden Data sheet, inline lists |
