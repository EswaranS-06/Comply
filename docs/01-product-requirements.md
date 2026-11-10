# 01. Product requirements

## What Comply is

A web app that lets an assessor run a DPDP (Digital Personal Data Protection Act, India) compliance assessment for a client Data Fiduciary as one connected flow, instead of separate Excel workbooks. The client's facts are entered once, linked by ID, and checked automatically.

## The problem

The old review used a fixed list of 114 questions, asked department by department, each answer marked Received, Not Received, Gap or Risk. It had four faults:

1. The question list decided coverage, not the client's real work, so scope was missed.
2. The department was treated as the unit of work, but one department runs many processes with different purposes.
3. The same facts were asked again across workbooks, which tires the client.
4. Answers were not linked, so nothing could be checked or automated.

The method was already fixed in Excel (walkthrough interviews feeding linked sheets). Comply makes that method usable, repeatable and checkable.

## Users

| User | What they do |
| --- | --- |
| Assessor (primary) | Runs the assessment: records activities, data and flows, answers tests, logs findings |
| Reviewer | Checks the assessor's work and signs it off |
| Client contributor | Client staff who fill in inventory and walkthrough facts |
| Client viewer | Client lead who reads agreed findings |
| Firm admin | Manages users, clients, client employees, security settings and the shared catalogues |

Details: [03-roles-and-permissions.md](03-roles-and-permissions.md).

## Goals

1. Replace the question list with walkthrough-driven records: processing activities, data elements and data flow.
2. Ask once, store once, link by ID. A fact lives in one place; everywhere else stores only the ID.
3. Check automatically: missing links, contradictions, and the outcome of each legal basis test.
4. Give the assessor one findings log across all phases.
5. Import from and export to the existing Excel workbooks, so work in progress is not lost.
6. Be fast: screens open and tables respond without visible waiting (budget in 04).

## The assessment method and version 1 coverage

| Phase | User does | System does | In version 1 |
| --- | --- | --- | --- |
| 1 Scope and Role | Answers the entity and activity checklist | Shows which duties can apply and which exemptions to test | Yes (F5) |
| 2 Discover Data | Records inventory, activities, data elements, data flow | Rolls up categories, highest tier and high-risk types; derives trust zones; flags gaps | Yes |
| 3 Legal Basis | Picks the basis route, answers the tests | Works out Supported, Gap or Cannot conclude, with the reason | Yes |
| 4 Duties | Tests security per system | Works out a result from the client's answer plus the evidence seen | Security review only (F21). Other duties (F22) dropped, D-04 |
| 5 to 7 Rate, Remediate, Report | Not designed | Not designed | No |

## In scope for version 1

- One sign-in page, five roles, password reset, admin-controlled security settings, optional MFA.
- Administration area: firm users, clients, client employees, assessments and their members, catalogues, security settings.
- Excel import and export of the four assessment workbooks: Organisation Profile, Applicability and Exemptions Checklist, the Inventory workbook (inventory, ROPA, Activity Data, Data Flow, Flow Nodes, Data Classification) and Legal Basis Review.
- Organisation profile and departments (workbook 1).
- Inventory: systems, applications, vendors, security controls, policies, owners.
- Data Classification catalogue (254 elements in 20 groups, four tiers).
- ROPA activities, their data elements, and their data flow with automatic trust zones.
- Phase 1 applicability and exemptions checklist.
- Legal Basis Review with automatic outcomes, and the element check.
- System security review (Rule 6 per system), once its design is supplied (15, O-8).
- One findings log, with evidence attachments.
- Coverage dashboard and checks.
- Audit log of every change to assessment data.
- Sign-off and lock.
- Client contributor entry and client findings view.

## Out of scope for version 1

- Vendor, client and activity duties (F22) and processor logins.
- The interactive data flow diagram.
- Ratings, remediation tracking, report generation (Phases 5 to 7).
- Frameworks other than DPDP (ISO 27001, SOC 2, GDPR).
- Single sign-on, payments, in-app notifications, a mobile app, other languages, AI features, a public API.
- Multi-firm management.

## What success looks like

- An assessor completes Phases 1 to 3 for one client without opening Excel, except to import or export.
- No fact is typed twice: IDs are picked from lists and names are looked up.
- Every activity shows an outcome and the reason for it.
- The Auklet School demo data loads and gives the same outcomes as the workbook demo: **1 Supported, 3 Gap, 2 Gap: no legal basis, 2 Cannot conclude yet.**
- The findings list exported from the app matches what is on screen.
- The performance budget in 04 is met on the target server size.

## Constraints and assumptions

- The legal tests and notes are working summaries of the Act and Rules. The assessor checks the Gazette text before quoting to a client. The app supports judgement; it is not a legal opinion. The app says this on the Legal Basis screens.
- Most client duties under the Rules start about 13 May 2027 (working statement, to verify). Findings before then are written as readiness gaps.
- Client-facing screens stay simple. Heavy process could make a client cancel.
- Demo data uses pseudo names only.
- Real client workbooks are never committed to git (`/source-workbooks/` is ignored).
- Most client duties start about 13 May 2027 and Rule 4 about 13 Nov 2026, per the checklist workbook; both dates are to be verified.
