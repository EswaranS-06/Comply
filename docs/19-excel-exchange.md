# 19. Excel exchange: import and export everywhere, and one Excel page

Requested by the owner on 11 Nov 2026 (D-47). This document plans two additions to Excel import (F3) and export (F4):

- **F30. Sheet-level import and export on every screen that holds sheet data.**
- **F31. One Excel page for the whole assessment, with a structure check** that confirms each sheet name and each header before any data is read, and stops with a clear error when something is missing.

[10-excel-import-export.md](10-excel-import-export.md) still defines how rows are read, validated and written. This document adds where the buttons are, the single map of sheets and headers, and the structure check. Nothing here is built yet.

## 1. What the owner asked for

| Asked | Planned as |
| --- | --- |
| "everywhere you can either export or import the excel sheet which has the right data" | Every list screen has **Export sheet** and **Import sheet** for its own sheet (F30) |
| "one page where we can export and import the excel sheet" | The Excel page at `/assessments/[id]/excel`, covering all four workbooks and every sheet (F31) |
| "check the sheet name and map the headers that should exist in the excel" | A sheet map: one definition per sheet of its name, header row and expected headers, used by every import and export |
| "if not you can throw error" | The structure check runs first. A wrong or missing sheet name or header is an error and nothing is imported |

## 2. The sheet map

One registry in code, `lib/excel/sheet-map.ts`, is the only place that knows the layout of the workbooks. The import engine, the export engine, the per-screen buttons, the Excel page and the tests all read it. It is generated from the template workbooks by script (as the tables in 17 were) and then reviewed by hand, never typed from memory.

Each sheet has one entry:

| Field | Meaning | Example |
| --- | --- | --- |
| `key` | Stable name used in code and URLs | `system-inventory` |
| `workbook` | Which of the four workbooks | 3 Inventory workbook |
| `sheetName` | Exact sheet name in the workbook | `System Inventory` |
| `headerRow` | Row that holds the headers | 2 |
| `kind` | `data`, `seed` (admin only) or `reference` (exported unchanged) | `data` |
| `screen` | The screen that shows this data | `/assessments/[id]/inventory/systems` |
| `rowKey` | How a row is matched on re-import | ID column |
| `columns` | Ordered list, one per header | see below |

Each column has:

| Field | Meaning |
| --- | --- |
| `header` | Exact header text in the workbook, including any `*` |
| `field` | The record field it maps to, or none for an auto column |
| `required` | A value is mandatory in every row |
| `auto` | Filled by a formula in the workbook; ignored on import, compared for parity, written on export |
| `type` | text, list (with the list name), date, ID, ID list, yes/no |

The 17 data sheets in the map:

| Workbook | Sheets |
| --- | --- |
| 1 Organisation Profile | Organization, Department |
| 2 Applicability Checklist | Checklist |
| 3 Inventory workbook | Owners, System Inventory, Application Inventory, Security Controls, Vendor List, Policy Inventory, ROPA, Activity Data, Data Flow, Flow Nodes, Data Classification |
| 4 Legal Basis Review | Activity Review, Element Check, Findings |

Header rows and special layouts (the Organization sheet's answers in column C, the Owners sheet's document control block) are as listed in 10.

## 3. The structure check

Runs on every upload, before any row is read. It answers one question: is this the file Comply expects?

### Steps

1. **File.** Must be `.xlsx`, within the size limit, and openable.
2. **Sheets.** List the sheet names in the file. Match each to the sheet map by exact name. Names are compared after trimming spaces and ignoring case; a match made that way is accepted and reported as a note.
3. **Headers.** For each matched sheet, read the header row given by the map and compare with the expected headers. Text is compared after trimming, collapsing repeated spaces and line breaks, and ignoring case. Position does not matter: a moved column is fine.
4. **Verdict per sheet:** OK, OK with notes, or Error.
5. **Stop or continue.** If any sheet being imported has an Error, the import stops there. Nothing is validated further and nothing is written. Otherwise the import continues with row validation as in 10.

### What is an error and what is a note

| Finding | Result | Message shown |
| --- | --- | --- |
| File is not `.xlsx` or cannot be opened | Error | `This file is not an Excel workbook (.xlsx) or is damaged.` |
| No sheet in the file matches the sheet map | Error | `No sheet in this file is one Comply knows. Sheets found: <names>. Expected one of: <names>.` |
| Importing from a screen, and that screen's sheet is not in the file | Error | `Sheet "<expected>" was not found. Sheets found: <names>.` |
| A sheet name is close to an expected one (for example `System Inventry`) | Error | `Sheet "<found>" is not recognised. Did you mean "<expected>"? Rename the sheet and upload again.` |
| An expected header is missing | Error | `Sheet "<sheet>": header "<header>" was not found in row <n>.` One line per missing header |
| A header appears twice | Error | `Sheet "<sheet>": header "<header>" appears more than once (columns <x>, <y>).` |
| The header row is empty (headers are in another row) | Error | `Sheet "<sheet>": no headers found in row <n>. The headers must be in row <n>.` |
| A header is close to an expected one (for example a missing `*`) | Error, with a hint | `Sheet "<sheet>": header "<found>" is not recognised. Did you mean "<expected>"?` |
| A column Comply does not know | Note | `Sheet "<sheet>": column "<header>" is not used and was ignored.` |
| A sheet Comply does not know, alongside known sheets | Note | `Sheet "<name>" is not used and was ignored.` |
| A reference or seed sheet is absent (Read Me, Values) | Note | `Sheet "<name>" is not in the file. It is not needed for import.` |
| A column is in a different position | Nothing | Accepted silently |

All expected headers must be present, including optional and auto columns, because the templates always have them; a missing one means the file is not a Comply workbook or has been edited. This is stricter than 10, which stopped only on mandatory headers; 10 is changed to match (to confirm, 15, O-39).

Errors are collected, not reported one at a time: the user sees every problem in the file at once, grouped by sheet.

### Output of the check

A structure report, shown on screen and kept with the import run:

| Column | Example |
| --- | --- |
| Workbook recognised as | 3 Inventory workbook |
| Sheet | Vendor List |
| Status | Error |
| Headers found / expected | 14 / 15 |
| Problems | header "Deletion clause" not found in row 2 |
| Data rows seen | 15 |

## 4. F31: the Excel page

Route `/assessments/[id]/excel` (already listed in 09 as Import / export). It becomes the one place to move a whole assessment in or out.

### Layout

| Area | Contents |
| --- | --- |
| Top bar | **Export all** (four workbooks in one zip), **Export workbook** (pick one), **Import files** (drop one or several `.xlsx` files) |
| Sheet table | One row per data sheet, grouped by workbook: sheet name, records in Comply, last import (who, when, file name), last export, status of the last check, **Export**, **Import** |
| Check panel | After an upload: the structure report (section 3), then the row problems and the preview of creates, updates and unchanged rows (10), then **Confirm import** or **Cancel** |
| Header map viewer | For any sheet: the expected sheet name, header row and headers, with required and auto marked, and **Download empty template** for that sheet. This is what a user reads to fix a rejected file |
| History | Import and export runs: who, when, file name and checksum, sheets, rows created and updated, result. Opens the stored structure report |

### Import flow

1. **Upload.** One or several files.
2. **Structure check.** Sheet names and headers (section 3). Errors stop here.
3. **Choose sheets.** Every recognised data sheet is ticked by default; the user can untick sheets they do not want to import.
4. **Row validation.** As in 10: mandatory values, dropdown values, dates, IDs, then links across sheets. A link may point to a record in the same upload or one already in the assessment.
5. **Preview.** Creates, updates field by field, unchanged rows, parity warnings, problems.
6. **Confirm.** One transaction. Any problem means nothing is written.
7. **Record.** Import run, structure report and audit entries.

### Export flow

1. Choose all, one workbook, or ticked sheets.
2. The export fills the template (10), so layout, dropdowns and formulas are kept.
3. The file name carries client, workbook and date: `Comply_<client>_<workbook>_<YYYY-MM-DD>.xlsx`.
4. An export run is recorded.

## 5. F30: import and export on every screen

Every screen that shows the data of one sheet gets the same two buttons in its header, built as one shared component driven by the sheet map.

| Screen | Sheet | Export | Import |
| --- | --- | --- | --- |
| Organisation profile | Organization | Yes | Yes |
| Departments | Department | Yes | Yes |
| Phase 1 checklist | Checklist | Yes | Answers only |
| Owners | Owners | Yes | Yes |
| Systems | System Inventory | Yes | Yes |
| Applications | Application Inventory | Yes | Yes |
| Security controls | Security Controls | Yes | Yes |
| Vendors | Vendor List | Yes | Yes |
| Policies | Policy Inventory | Yes | Yes |
| Activities (ROPA) | ROPA | Yes | Yes |
| Activity data | Activity Data | Yes | Yes |
| Data flow | Data Flow | Yes | Yes |
| Flow nodes | Flow Nodes | Yes | Yes |
| Data classification | Data Classification | Yes | Client-added rows and Public tiers only |
| Legal basis review | Activity Review | Yes | Review columns only |
| Element check | Element Check | Yes | Check columns only |
| Findings | Findings | Yes, including "export this view" | Yes |

The limits in the Import column are the ones 10 already sets.

### Export sheet

- Downloads a workbook holding that one sheet with all its rows, plus the reference sheets its dropdowns need, built from the template.
- Formulas that point at sheets not in the file are written as their computed values, so the file opens without broken references.
- If the screen is filtered, the user chooses **all rows** or **this view**.

### Import sheet

- Accepts a file that contains the screen's sheet. The file may be the single-sheet export, or the full workbook; other sheets in it are ignored and listed as notes.
- Runs the same structure check, restricted to that sheet, then the same row validation, preview and confirm, in a dialog on the screen. No different rules.
- Links to other sheets are checked against what is already in the assessment. For example a ROPA row naming `SYS-004` needs that system to exist; if it does not, the row is a problem and the message says to import System Inventory first.
- Suggested order when starting empty, shown on the Excel page: Owners, Department, inventory sheets, Flow Nodes, ROPA, Activity Data, Data Flow, then workbook 4.

## 6. Who can do what

Unchanged from 03: the roles that can import and export workbooks today can use F30 and F31; a role that is export only sees no Import button. Import is also disabled on a locked (signed-off) assessment; export stays available. Seed sheets are imported only from the admin area.

## 7. Server design

| Part | Plan |
| --- | --- |
| `lib/excel/sheet-map.ts` | The registry in section 2 |
| `lib/excel/structure-check.ts` | Pure function: workbook in, structure report out. No database |
| `lib/excel/import.ts`, `export.ts` | The engines in 10, taking a list of sheet keys |
| `POST /api/assessments/[id]/excel/check` | Upload; returns the structure report and, if clean, the row preview. Writes nothing |
| `POST /api/assessments/[id]/excel/import` | Confirms a checked upload by its token; one transaction |
| `GET /api/assessments/[id]/excel/export?sheets=...&view=...` | Streams the file |
| `GET /api/excel/sheet-map` | Feeds the header map viewer |
| Uploaded file | Parsed in memory, held only until confirm or cancel, never stored; name and checksum recorded (as in 10) |

## 8. Tests

| # | Test |
| --- | --- |
| 1 | The sheet map matches the committed templates: every sheet name and header in the map is found in the template, and every template header is in the map |
| 2 | Structure check: one case per row of the table in section 3, asserting the exact message |
| 3 | A file with one wrong header imports nothing, even when every other sheet is valid |
| 4 | Reordered columns import the same records as the original order |
| 5 | Single-sheet round trip for each of the 17 sheets: export sheet, import into an empty assessment (with its prerequisites), same records |
| 6 | Whole-assessment round trip for each demo client (18): export all, import all, no differences and no parity warnings |
| 7 | An export-only role gets no import, by screen and by API |
| 8 | A locked assessment refuses import |

## 9. Where it fits in the build

The stages do not change; the pieces land where their sheets already land (14).

| Stage | Adds |
| --- | --- |
| S3 | Sheet map generator and registry; structure check with all messages; the Excel page with check panel, header map viewer and history; shared Import / Export buttons on the Organisation, Department and inventory screens |
| S4 | Map entries and buttons for ROPA, Activity Data, Data Flow, Flow Nodes, Data Classification |
| S5 | Activity Review, Element Check |
| S6 | Findings |
| S7 | Checklist |
| S10 | Whole-assessment round trip for the three demo clients |

## 10. To confirm with the owner

Listed in 15 as O-39 to O-42. The build proceeds on the plan above unless the owner says otherwise.

| # | Question | Planned answer |
| --- | --- | --- |
| O-39 | Must every expected header be present, or only the mandatory ones? | Every one; a missing header is an error |
| O-40 | Are unknown extra columns and sheets an error? | No; ignored and reported as notes |
| O-41 | What does a single-sheet export contain? | That sheet plus the reference sheets its dropdowns need |
| O-42 | May a sheet import refer to records not yet in Comply? | No; it is a problem that names the sheet to import first |
