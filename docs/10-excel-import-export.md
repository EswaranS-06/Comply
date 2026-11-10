# 10. Excel import and export

**Status:** the workbooks have not been uploaded yet (see 15). This document fixes the behaviour; the sheet-by-sheet column mapping in the last section is filled in from the real files during stage S3. Nothing about sheet names or columns is guessed.

## Workbooks in scope

| Workbook / sheet | Import | Export | Holds |
| --- | --- | --- | --- |
| Inventory workbook | Yes | Yes | Systems, Applications, Vendors, Security controls, Policies, Owners |
| ROPA sheet | Yes | Yes | Activities, activity elements, flow nodes, data flow |
| Legal Basis Review sheet | Yes | Yes | Routes, test answers, element checks, findings |
| Data Classification sheet | Seed only | Yes | The 254-element catalogue (loaded once by an admin; assessments import tier overrides only) |
| Applicability checklist | Seed only | Later | Phase 1 questions |
| Auklet School demo | Fixture | -- | Becomes `fixtures/auklet/` |

## Import behaviour (F3)

1. **Upload.** `.xlsx` only, 20 MB limit. The file is parsed on the server and never stored after the run; only its name and checksum are kept.
2. **Read.** Sheets are found by name; columns are found by header text, not position, so a reordered column still imports. A missing required sheet or header stops the import with a clear message.
3. **Validate everything first.** Each row is checked with the same Zod schema the screens use, then links are checked across sheets (an application's system, a flow step's node). Derived columns in the workbook (zone, roll-ups, outcome, checks) are ignored on import because the app computes them.
4. **Report.** The user sees a preview: rows to create, rows to update, rows unchanged, and a problem list with sheet, row number and reason.
5. **Nothing is half-imported.** If any row has a problem, nothing is written. The user fixes the workbook and uploads again. The whole write happens in one database transaction.
6. **Re-import.** Rows are matched by human ID (SYS-001). If the import would change existing rows, the preview lists the changes field by field and asks before overwriting. Rows in the app that are absent from the workbook are left alone, never deleted.
7. **IDs.** IDs in the workbook are kept. The ID counter moves past the highest imported number. A row with no ID gets the next one.
8. **Record.** An Import run row and audit entries are written.

## Export behaviour (F4)

- Produces the same workbook layout: same sheet names, same column order, same header text.
- Dropdown columns keep their Excel data-validation lists.
- Derived columns are written as values (the app's computed results), so the exported file shows the same outcomes as the screen.
- Findings export matches the findings list on screen, including the current filters if the user chooses "export this view".
- A locked assessment exports with a note of who signed it off and when.
- Round trip is tested: export, then import into an empty assessment, must reproduce the same records.

## Client data safety

Real client workbooks go in `/srv/comply/source-workbooks/`, which is ignored by git. Only the Auklet School demo (pseudo names) is turned into a committed fixture.

## Column mapping

To be written in S3 from the uploaded files, one table per sheet:

| Sheet | Column header | Field | Required | Allowed values | Notes |
| --- | --- | --- | --- | --- | --- |
| (pending workbooks) | | | | | |
