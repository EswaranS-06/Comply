# 18. Demo clients

Supplied by the owner on 11 Nov 2026 (D-46). Three fictional clients replace the earlier single demo client as the demo data and the acceptance case. All three are invented; each file opens with a fiction notice.

The full files are kept unchanged in `docs/demo-clients/`:

| Key | Client | File | What it exercises |
| --- | --- | --- | --- |
| A | Quellmark Finance Ltd | [client-a-quellmark-finance.md](demo-clients/client-a-quellmark-finance.md) | Fiduciary; consent-heavy; one joint fiduciary activity; four countries; possible SDF |
| B | Halvorn Systems Pvt Ltd | [client-b-halvorn-systems.md](demo-clients/client-b-halvorn-systems.md) | Mostly Data Processor (Out of scope in Phase 3, work moves to Phase 4); role creep; children's data |
| C | Brannock Auto Components Pvt Ltd | [client-c-brannock-auto-components.md](demo-clients/client-c-brannock-auto-components.md) | Paper records; biometrics; undecided role with contractors; exemption claims; foreign-contract exemption |

Each file has the same sections: snapshot, departments, Part A answers (E1 to E13), inventory (owners, systems, applications, vendors, controls, policies), flow nodes, ROPA, activity data, data flow, hidden processing, expected Phase 3 review, expected Phase 4 checks, what the diagram should show, edge cases.

## How they are used

| Use | How |
| --- | --- |
| Demo data | `pnpm seed:demo` creates the three clients, one assessment each (reference date 2026-11-10), from `fixtures/quellmark/`, `fixtures/halvorn/` and `fixtures/brannock/` |
| Fixtures | JSON keyed in from the files in `docs/demo-clients/`, one file per workbook sheet, so the same data can be loaded by seed or exported to Excel |
| Acceptance case | The parity test (12, test 1 part c) asserts each activity's outcome and the totals below |
| Excel round trip | Each demo assessment is exported to the four workbooks and imported into an empty assessment; the result must be identical (19) |
| Screens and diagram | Section 14 of each file lists what the data flow diagram must show; section 11 lists what the walkthrough should surface |

## Expected Phase 3 outcomes

Taken from section 12 of each file. The files use short names; the result text Comply shows is the workbook's exact text from 06 (for example the Out of scope result).

### A. Quellmark Finance (11 activities)

| Outcome | Count | Activities |
| --- | --- | --- |
| Supported | 4 | ACT-003, 005, 006, 010 |
| Gap | 5 | ACT-001, 002, 004, 007, 009 |
| Gap: no legal basis | 1 | ACT-011 |
| Cannot conclude yet | 1 | ACT-008 |

### B. Halvorn Systems (9 activities)

| Outcome | Count | Activities |
| --- | --- | --- |
| Supported | 1 | ACT-008 |
| Gap | 2 | ACT-006, 007 |
| Gap: no legal basis | 1 | ACT-005 |
| Cannot conclude yet | 1 | ACT-009 |
| Out of scope | 4 | ACT-001 to 004 (processor) |

The file offers two extra rows (ACT-008b, ACT-007b) that bring Supported to 3. They are not loaded unless the owner asks (15, O-38).

### C. Brannock Auto Components (11 activities, 12 with ACT-008b)

| Outcome | Count | Activities |
| --- | --- | --- |
| Supported | 6 | ACT-001, 005, 007, 008b, 010, 011 |
| Gap | 3 | ACT-002, 006, 009 |
| Gap: no legal basis | 1 | ACT-003 |
| Cannot conclude yet | 1 | ACT-004 |
| Out of scope | 1 | ACT-008 |

The file's opening table gives different totals (4 Supported, 2 Gap, 1, 1, 2 Out of scope) from its own section 12. The table above follows section 12, which lists each activity. To confirm (15, O-37).

## Things in the files that need care when keying the fixtures

| # | Point |
| --- | --- |
| 1 | The files are written descriptions, not filled workbooks. Test answers are given "by exception" (only tests that are not Yes); every other test in the active block is Yes |
| 2 | Some rows stand for several records: "VEN-011 to VEN-024" (14 contractors), "DEP-001 to DEP-012" as flow nodes. Each becomes its own record |
| 3 | Nodes are added late in the text (EXT-008, EXT-009 in Brannock; EXT-005 in Halvorn; EXT-008 WhatsApp in Quellmark). They must be created before the flow rows that use them |
| 4 | "ACT-008b" and "ACT-007b" are not IDs the workbook's format allows. If loaded they get the next free ACT number, and the mapping is recorded in the fixture |
| 5 | Values such as "Joint fiduciary (to be decided)", "Paper", "Paper-to-digital", "Expired (12 of 40)" may not be in the workbook dropdowns. Each is checked against 17; a value outside a dropdown is listed in 15 rather than silently changed |
| 6 | Statements marked *(verify)* are working readings of the law. They are shown as notes, never as rules |
| 7 | Section 13 of each file shows Phase 4 as five items per system, (a) Encryption, (b) Access control, (c) Access logs, (d) Backup, (e) Log retention of 12 months or more, each as "client says / evidence seen / result", with results Pass, Partial, Gap (client confirms), Gap: claim not supported, Not tested. This narrows the open Phase 4 design (15, O-8) but does not settle the result matrix |

## What the outline demo shows

`demo/index.html` lists these three clients with a handful of their activities. It is a sketch of the flow only; its result logic is not the rules engine.
