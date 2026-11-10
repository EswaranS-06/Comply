# 06. Rules engine

All automatic results come from pure functions in `lib/rules`. A rule takes plain records and returns a result; it never touches the database, the clock or the user. That is what makes the workbook parity test possible.

**Status of this document:** the rules below are what the Notion documents state. The exact formulas (which tests belong to which route, how zones are derived from Inventory fields, label wording) are copied from the workbooks when they arrive (D-11). Until then anything marked **(workbook)** is not built.

## R-1 Activity roll-ups (F9)

Input: the activity's elements with their catalogue rows and tier overrides.

| Output | Rule |
| --- | --- |
| Number of elements | count of activity elements |
| Categories of data | distinct element groups, in catalogue order |
| Highest tier | the highest of the elements' effective tiers; order Public < Standard < Internal < Confidential (order to confirm **(workbook)**) |
| High-risk types | distinct high-risk types other than None |

Effective tier = the tier override for this assessment if one exists (only Public may be set), otherwise the catalogue tier.

## R-2 Trust zone (F11)

Zone is never typed for inventory nodes. Values: Data principal, Client premises, Cloud or vendor in India, Other organisation in India, Outside India, Unknown.

| Node kind | Zone comes from |
| --- | --- |
| System | hosting and location country **(workbook)** |
| Application | the system it is hosted on |
| Vendor | data location **(workbook)** |
| Flow node (DP-, DEP-, EXT-) | the zone and country recorded on the node |

Unknown is returned when the fields needed are blank or Not sure.

## R-3 Data path checks (F12)

Evaluated per data flow step and per activity. Each returns a flag with the step it concerns.

| Flag | Raised when |
| --- | --- |
| Node not found | the step's node ID does not exist in the Inventory or flow nodes (can only arise from import) |
| Blank or Not sure | shared further is blank or Not sure |
| Contradiction: shared with | shared further is No but shared with is filled |
| No outside recipient | the activity says shared outside the client = Yes, but no step is shared with a node outside the client |
| Cross-border mismatch | the activity's cross-border answer differs from whether any step's zone is Outside India |
| No end | the flow has no final step (the last step says shared further = Yes with nothing after it) |

## R-4 Legal basis outcome (F14)

Input: the route, the test answers for the activity, the element checks.

1. Route **None identified**: outcome **Gap: no legal basis**.
2. Route **Out of scope**: outcome **Out of scope**.
3. Otherwise take the tests that apply to the route **(workbook: the route-to-test table for C1 to C10, L1 to L4, X1 to X3, K1 to K3, E1, E2, R1)**:
   - any answer **No**: **Gap**
   - otherwise any answer blank or **Not sure**: **Cannot conclude yet**
   - otherwise (all Yes or Not applicable): **Supported**
4. For the Consent route, an element check with Needed = No or Named in notice = No counts as a failed consent test (F16).
5. **Why** lists the failed tests by ref, then the unanswered ones, in catalogue order.

## R-5 Route mismatch (F15)

Compare the reviewer's route with the legal basis the client claimed in the ROPA (mapping of claimed-basis wording to routes **(workbook)**). When they differ, return `ROPA says: <claimed basis>`.

## R-6 Coverage (F13)

Per assessment: activities with no elements, no flow steps, no owner, or no route; inventory rows with a missing required field; counts of activities by outcome.

## R-7 System security review result (F21)

Five rows per system, one per Rule 6 item (a) to (e). Inputs: what the client says (from the system's and controls' inventory fields **(workbook)**) and the evidence seen (Yes, Partial, No, blank). Result: Pass, Partial, Gap or Not tested **(workbook: the exact matrix)**.

## R-8 Phase 1 applicability (F5)

Entity answers and activity answers map to which duties can apply and which exemptions to test **(workbook)**.

## Acceptance case: Auklet School

`fixtures/auklet/` holds the demo as JSON, produced by importing the demo workbook once and reviewing the result by hand. The parity test loads it and asserts, per activity, the outcome, the why text, the route mismatch flag, the roll-ups and the path checks. The totals must be:

| Outcome | Count |
| --- | --- |
| Supported | 1 |
| Gap | 3 |
| Gap: no legal basis | 2 |
| Cannot conclude yet | 2 |

A change to `lib/rules` that breaks this test cannot be released.
