# 06. Rules engine

All automatic results come from pure functions in `lib/rules`. A rule takes plain records and returns a result; it never touches the database, the clock or the user. That is what makes workbook parity testable.

**Source:** every rule below was read from the formulas in the workbooks in `source-workbooks/` on 10 Nov 2026 (workbook 3 "Inventory, ROPA, Activity Data, Data Flow and Data Classification" and workbook 4 "Legal Basis Review"). The sheet and column each rule comes from is given so it can be re-checked. Result texts are reproduced exactly, because the export must show the same words as the workbook.

Where the app does something the workbook does not, it is marked **(app addition)**.

## R-0 Row alerts (inventory)

Each inventory row gets a list of alerts. Two kinds: **mandatory** (a field must be filled because of another answer) and **not applicable** (a field should be empty or cannot be relied on because of another answer). In the workbook they are joined with ` | `; the app shows them as separate flags. Columns marked `*` in 10 are always mandatory.

**System** (System Inventory, column O)

| When | Alert |
| --- | --- |
| Stores personal data = No | `Data categories: not applicable - personal data = No`; `Data Principal categories: not applicable - personal data = No` |
| Stores personal data = Yes and Data categories blank | `Data categories: mandatory - personal data = Yes` |
| Stores personal data = Yes and Data Principal categories blank | `Data Principal categories: mandatory - personal data = Yes` |

**Application** (Application Inventory, column T)

| When | Alert |
| --- | --- |
| Type = In-house | `Vendor: not applicable - app type = In-house` |
| Type = Third-party or SaaS, and Vendor blank | `Vendor: mandatory - app type = Third-party/SaaS` |
| Personal data processed = No | `<field>: not applicable - personal data = No` for each of: Data elements, Purpose, Collection point, Consent/notice, Children's data, Shares data with, Cross-border, Retention, Deletion method |
| Personal data processed = Yes and the field is blank | `<field>: mandatory - personal data = Yes` for each of the same nine fields |

**Security control** (Security Controls, column N)

| When | Alert |
| --- | --- |
| Implemented = No or Not applicable | `Description: not applicable - control not implemented`; `Evidence available: not applicable - control not implemented` |
| Implemented = Yes or Partial, Description blank | `Description: mandatory - control is implemented` |
| Implemented = Yes or Partial, Evidence available blank | `Evidence available: mandatory - control is implemented` |
| Implemented = No or Not applicable, or Evidence available = No | `Evidence reference: not applicable - no control or no evidence` |
| Implemented = Yes or Partial, Evidence available = Yes or Partial, Evidence reference blank | `Evidence reference: mandatory - evidence available = Yes/Partial` |
| Implemented = No, Partial or Not applicable, Gap or remarks blank | `Gap/remarks: mandatory - control is not fully implemented` |

**Vendor** (Vendor List, column Q)

| When | Alert |
| --- | --- |
| Handles personal data = No | `Data categories shared: not applicable - personal data = No`; `Sub-processors: not applicable - personal data = No` |
| Handles personal data = Yes, Data categories shared blank | `Data categories shared: mandatory - personal data = Yes` |
| Handles personal data = Yes, Sub-processors blank | `Sub-processors: mandatory - personal data = Yes` |
| Handles personal data = No, or Contract in place = No | `Breach clause: not applicable - no personal data or no contract`; `Deletion clause: not applicable - no personal data or no contract` |
| Handles personal data = Yes, Contract in place is not No, Breach clause blank | `Breach clause: mandatory - personal data = Yes` |
| Same, Deletion clause blank | `Deletion clause: mandatory - personal data = Yes` |
| Contract in place = No | `Security clause: not applicable - no contract in place`; `Contract dates: not applicable - no contract in place` |
| Contract in place = Yes or Expired, Security clause blank | `Security clause: mandatory - contract in place` |
| Contract in place = Yes or Expired, Contract dates blank | `Contract dates: mandatory - contract in place` |

**Policy** (Policy Inventory, columns K and R)

Next review due = Last review date + 12 months (blank if no last review date).

| When | Alert |
| --- | --- |
| Status = Draft, Expired or Not available | `<field>: cannot be relied on - status = Draft/Expired/Not available` for Approved by, Approval date, Evidence reference |
| Status = Approved or Under review, field blank | `<field>: mandatory - policy is Approved/Under review` for Approved by, Approval date, Evidence reference |
| Status = Approved, Last review date blank | `Last review date: mandatory - policy is Approved` |
| Status = Draft or Not available | `Communicated to staff: cannot be communicated - policy is Draft/Not available` |
| Status = Approved, Communicated to staff blank | `Communicated to staff: mandatory - policy is Approved` |
| Next review due is before today | `Next review due: review is overdue` |

The policy overdue alert needs today's date; the rule takes the date as an input so it stays pure.

## R-1 Activity roll-ups

Source: ROPA columns G, AQ, AR, AS. Input: the activity's elements with their catalogue rows.

| Output | Rule | When there are no elements |
| --- | --- | --- |
| Elements | count of the activity's elements | `0` |
| 5. Categories of Personal Data | the distinct groups of its elements, in the order of the 20 groups in DC Values, each followed by `; ` | `No elements listed yet` |
| Highest tier | first that is present, in this order: Confidential, Internal, Standard, Public | `No elements yet` |
| High-risk types present | those present, in this order: Government ID, Financial, Health, Biometric, Location, each followed by `; ` | `None flagged` (also when elements exist but none is high-risk) |

The tier of an element is the client's tier override if one exists (only Public can be set), otherwise the catalogue tier.

## R-2 Node lookup and trust zone

Source: Data Flow columns D to G. The node kind is read from the ID prefix (the text before the first `-`).

| Prefix | Node type | Name comes from | Zone |
| --- | --- | --- | --- |
| `SYS` | System | System Inventory | from that system (below) |
| `APP` | App | Application Inventory | from the system the app is hosted on; `Unknown` if "Hosted on" is blank or not found |
| `VEN` | Vendor | Vendor List | Data location = India: `Cloud or vendor (India)`. Outside India or Both: `Outside India`. Anything else or not found: `Unknown` |
| anything else (`DP`, `DEP`, `EXT`) | the node's own type from Flow Nodes | Flow Nodes | the zone recorded on the flow node; `Unknown` if not found |

Zone of a system, in order:

1. Hosting = On-premises: `Client premises`.
2. Location is blank, or contains "unknown" or "not known" (any case): `Unknown`.
3. Location contains "India" (any case): `Cloud or vendor (India)`.
4. Otherwise: `Outside India`.

Zone values: Data principal, Client premises, Cloud or vendor (India), Other organisation (India), Outside India, Unknown. Flow node types: Data principal, Department, External party.

Note for build: rule 3 is a text search, so a location such as "Indiana, USA" would wrongly count as India. The app keeps a separate country field on the system (filled from the location text on import, editable) and uses it when present; the text rule is the fallback and the parity test still runs on the workbook's rule. **(app addition, to confirm with owner)**

## R-3 Data flow step check

Source: Data Flow column K. First match wins.

| # | When | Result |
| --- | --- | --- |
| 1 | Node ID blank | `Node ID missing` |
| 2 | Node ID not found in the Inventory or Flow Nodes | `ID not found in the Inventory or Flow Nodes` |
| 3 | Activity ID not found | `Activity ID not in ROPA` |
| 4 | Shared further blank | `Ask: shared further?` |
| 5 | Shared further = Not sure | `Evidence needed` |
| 6 | Shared further = Yes and Shared with blank | `Who is it shared with?` |
| 7 | Shared further = No and Shared with filled | `Contradiction: No, but Shared with is filled` |
| 8 | otherwise | `OK` |

In the app, cases 1 to 3 cannot be created on screen (IDs are picked from lists) and can only arise during import, where they are import problems.

Shared with holds node IDs (SYS-, APP-, VEN-, DEP-, EXT-, DP-) and activity IDs (ACT-, meaning the data is reused for another purpose, which needs its own legal basis). The app also checks that each ID in Shared with exists. **(app addition)**

## R-4 Activity path check

Source: ROPA columns AM, AN.

Outside recipients = the number of the activity's data flow steps whose node type is Vendor or External party.

| # | When | Result |
| --- | --- | --- |
| 1 | Shared outside the client blank | `Ask: shared outside the client?` |
| 2 | Shared outside = Yes and outside recipients = 0 | `Yes, but no outside recipient in Data Flow` |
| 3 | Shared outside = No and outside recipients > 0 | `No, but Data Flow has an outside recipient` |
| 4 | the activity has no data flow steps | `No Data Flow rows yet` |
| 5 | Shared outside = Not sure | `Evidence needed` |
| 6 | otherwise | `OK` |

## R-5 Cross-border check

Source: ROPA columns AO, AP.

Leaves India per data = `Yes` if any of the activity's elements has Leaves India (D7) = Yes, or any of its flow steps has zone Outside India; otherwise `No / not flagged`.

| When | Result |
| --- | --- |
| Leaves India per data = Yes and 11a Cross-Border Transfer is not Yes | `Data shows it leaves India: check 11a` |
| Leaves India per data is not Yes and 11a = Yes | `11a says Yes but no flow outside India recorded` |
| otherwise | `OK` |

## R-6 Route mismatch

Source: Activity Review column P. Inputs: the route we conclude, and "3. Legal Basis" claimed in the ROPA.

| # | When | Result |
| --- | --- | --- |
| 1 | Route blank | (nothing) |
| 2 | ROPA legal basis blank | `ROPA basis blank` |
| 3 | Route = Consent (Sec 6) and the ROPA basis contains "Consent" | `Matches ROPA` |
| 4 | Route = Legitimate use (Sec 7) and the ROPA basis starts with "7" | `Matches ROPA` |
| 5 | Route = None identified and the ROPA basis contains "None" | `Matches ROPA` |
| 6 | Route = Exemption only (Sec 17), or Out of scope | `Matches ROPA` |
| 7 | otherwise | `ROPA says: <ROPA legal basis>` |

Case 7 is shown in the danger colour.

## R-7 Legal basis outcome

Source: Activity Review columns AK to AP. Inputs: the route; the Sec 7 clause; the answers to the tests; from the ROPA: Consent status, Exemption claimed, Children's data; from Element Check: the number of elements with E1 = No and with E2 = No.

**Which test groups count**

| Group | Tests | Counts when |
| --- | --- | --- |
| Consent | C1 to C10 | route = Consent (Sec 6) |
| Sec 7 | L1 to L4 | route = Legitimate use (Sec 7) |
| Exemption | X1 to X3 | route = Exemption only (Sec 17), **or** the ROPA's Exemption claimed is filled and is not "Not claimed" |
| Children | K1 to K3 | the ROPA's Children's data = Yes |

Groups combine: a Consent-route activity with children's data counts C1 to C10 and K1 to K3. R1 is not answered as a question; it is the "no basis" result itself. E1 and E2 are answered per element on the Element Check.

**Tests failed**

- Route None identified or Out of scope: 0.
- Otherwise the sum of:
  - each "No" among the counted groups' tests;
  - plus 1 if route = Consent and the ROPA's Consent status is "Not captured";
  - plus 1 (not one per element) if route = Consent and any element has E1 = No or E2 = No.

**Tests open**

- Route None identified or Out of scope: 0.
- Otherwise the sum of each blank or "Not sure" among the counted groups' tests, plus 1 if route = Legitimate use (Sec 7) and the Sec 7 clause is blank.

"Not applicable" is neither failed nor open.

**Outcome** (first match wins)

| # | When | Outcome |
| --- | --- | --- |
| 1 | Route blank | `Decide the route` |
| 2 | Route = None identified | `Gap: no legal basis` |
| 3 | Route = Out of scope | `Out of scope: record reason` |
| 4 | Tests failed > 0 | `Gap` |
| 5 | Tests open > 0 | `Cannot conclude yet` |
| 6 | otherwise | `Supported` |

**Why**

| When | Text |
| --- | --- |
| Route = None identified | `R1: no Sec 4(1) basis identified` |
| Tests failed > 0 | `Failed: ` followed by the ref of each failed test in the order C1 to C10, L1 to L4, X1 to X3, K1 to K3, each followed by `; `, then `ROPA says consent not captured; ` if that applied, then `Element Check (E1/E2); ` if that applied |
| else Tests open > 0 | `Open: <n> test(s) blank or Not sure` |
| otherwise | (empty) |

Open elements (E1 or E2 blank or Not sure) do **not** count as open tests on the activity in the workbook; they show only on the element row (R-8). The app follows the workbook, and the coverage dashboard lists open element checks separately. **(dashboard listing is an app addition)**

## R-8 Element check finding

Source: Element Check column O. First match wins.

| # | When | Result |
| --- | --- | --- |
| 1 | E1 = No | `Not needed for the purpose (E1)` |
| 2 | E2 = No | `Not named in the notice (E2)` |
| 3 | the element's Child's data (D3) = Yes but the activity's Children's data is not Yes | `Child flag differs from Activity Review` |
| 4 | E1 or E2 is blank or Not sure | `Open` |
| 5 | otherwise | `OK` |

## R-9 Finding lookups

Source: Findings columns C, D, F. A finding's activity name and department come from the activity; its law reference is the Legal reference of its test ref in the test catalogue.

## R-10 Coverage **(app addition, from Notion F13)**

Per assessment: activities with no elements, no data flow steps, no owner, or no route; activities whose path ends in a step with Shared further = Yes and nothing after it; rows with mandatory alerts (R-0); steps and activities whose checks are not `OK`; open element checks; counts of activities by outcome.

## R-11 Phase 1 checklist

Source: workbook 2, Checklist sheet. The workbook holds no formulas: each question carries a fixed text, "What the answer decides", that tells the assessor what follows from each answer. The app shows that text beside the answer and builds no computed applicability result beyond these plain summaries:

- Part A: a list of the entity questions answered Yes, No, Not sure or not answered, with their "decides" text.
- Part B, per activity: the same, plus the picked values of P3 (role) and P9 (Sec 7 clause) shown next to the activity's "Our role" and "Legal basis" so a difference is visible.
- Part C is not a separate checklist: D2, D3, D4 and D7 are the per-use flags on activity elements; D1 is the catalogue's "Personal data?"; D5 is the catalogue's high-risk type; D6 is the catalogue's fixed-retention law.

Any automatic conclusion from checklist answers (for example "duty X does not apply") is not in the workbook and is not built in version 1.

## R-12 System security review (F21)

**Not defined in these workbooks.** Workbook 4 says evidence testing of security controls is Phase 4 and outside it. The Security Controls sheet has a "Linked DPDP requirement (Rule 6 item)" list of seven values (Encryption or masking, Access control, Logging and monitoring, Backup and continuity, Log retention (1 year), Processor contract, Other measures), which does not match the "(a) to (e), five rows per system" wording in Notion. The rule is blocked until the owner supplies the Phase 4 design (15, O-8).

## Acceptance case: Auklet School

`fixtures/auklet/` will hold the demo as JSON, produced by importing the filled demo workbooks. The parity test asserts, per activity, the outcome, the why text, the route mismatch, the roll-ups, the zones and every check, and these totals:

| Outcome | Count |
| --- | --- |
| Supported | 1 |
| Gap | 3 |
| Gap: no legal basis | 2 |
| Cannot conclude yet | 2 |

**The filled Auklet School workbooks have not been supplied** (the files received are empty templates with one sample activity). Until they are, each rule above is tested against cases written from the formulas, and against the one sample activity (ACT-001 "Delivery scheduling").
