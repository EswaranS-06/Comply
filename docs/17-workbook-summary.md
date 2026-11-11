# 17. Workbook summary

A summary of the four DPDP assessment workbooks the owner supplied on 10 Nov 2026. The Excel files themselves are kept in `/srv/comply/source-workbooks/` (copied from `/data/home/REX/DPDP-Workbooks`). That folder is ignored by git, because one sheet names a real client (see "Things to know" below); this document is the committed record of what the files contain.

The column tables in Part 2 were generated from the files by script, not typed, so headers and dropdown values are exact. The formulas are written out as rules in [06-rules-engine.md](06-rules-engine.md).

## Part 1. What each workbook is

The workbooks are filled in order 1 to 4, one copy per client.

| # | File | Size | Sheets | Purpose |
| --- | --- | --- | --- | --- |
| 1 | `1 - Organisation Profile.xlsx` | 24 kB | Organization, Department, Values, Data (hidden) | Who the client is, and its departments |
| 2 | `2 - Applicability and Exemptions Checklist.xlsx` | 20 kB | Read Me, Checklist | Phase 1: which duties can apply to the entity, each activity and each data element |
| 3 | `3 - Inventory, ROPA, Activity Data, Data Flow and Data Classification.xlsx` | 562 kB | Owners, System Inventory, Application Inventory, Security Controls, Vendor List, Policy Inventory, ROPA Read Me, ROPA, Activity Data, Data Flow, Flow Nodes, Data Classification, ROPA Values, DC Values | Phase 2: everything discovered about the client's systems, activities, data and flows |
| 4 | `4 - Legal Basis Review.xlsx` | 225 kB | Read Me, Activity Review, Element Check, Findings, Tests, Law Notes, Values | Phase 3: the legal basis tests per activity, the element check and the findings log |

All four are **templates**. Workbook 3 holds one sample activity to show how rows link; workbooks 1, 2 and 4 hold no client answers.

### Workbook 1: Organisation Profile

- **Organization:** a questionnaire of 37 questions in 7 sections, answered in one Response column.

| Section | Questions |
| --- | --- |
| 1 Organisation identity | 1.1 Registered legal name, 1.2 CIN, 1.3 PAN, 1.4 GSTIN, 1.5 Entity type |
| 2 Classification | 2.1 Industry sector, 2.2 Organisation size |
| 3 Primary contact | 3.1 Name, 3.2 Email, 3.3 Designation, 3.4 Phone |
| 4 Organisation detail | 4.1 Registered office address, 4.2 Website, 4.3 Number of locations |
| 5 Personal data scope | 5.1 Approximate number of Data Principals, 5.2 Children's data, 5.3 Health or financial data, 5.4 Data sent outside India, 5.5 Uses third-party vendors |
| 6 Compliance position | 6.1 Privacy notice published, 6.2 Data protection contact, 6.3 Sector regulators, 6.4 Certifications, 6.5 Breach in last 12 months |
| 7 Applicability and exemptions | 7.1 to 7.13: processing in India, offering to people in India, digital form, other group entities (and their list), type of organisation (Fourth Schedule class), Sec 17(3) notification, Significant Data Fiduciary, State body, other exemptions, other laws (and their names), outsourced processing of people outside India |

Dropdown lists (from the hidden Data sheet):

| List | Values |
| --- | --- |
| Entity type | Parent Company, Subsidiary, Private Limited Company, Public Limited Company, LLP, Partnership Firm, One Person Company (OPC), Others |
| Industry sector | BFSI (Banking, Financial Services & Insurance), Healthcare, Manufacturing, IT / ITeS, Retail, Government, Education |
| Organisation size | Micro (< 10 employees), Small (10 - 50 employees), Medium (51 - 200 employees), Large (201 - 1000 employees), Enterprise (1000+ employees) |
| Data Principal count | Under 1,000; 1,000 - 10,000; 10,000 - 1 lakh; 1 lakh - 10 lakh; Above 10 lakh |
| Yes / No | Yes, No |
| Yes / No / Partial | Yes, No, Partial |
| Section 7 answers | 7.2: Yes, No, Not applicable. 7.7, 7.9, 7.10, 7.11, 7.13: Yes, No, Not sure. 7.8: Notified, Not notified, Not sure. 7.6: the classes in Values table 1 |

The dropdowns of sections 1 to 6 and of 7.1, 7.3, 7.4 and 7.6 are stored in a newer Excel validation format that the reading script could not open. Their lists are the ones above; which list sits on which question is obvious for most (entity type, sector, size, count) and is confirmed in Excel during stage S2 for the rest.

- **Department:** one row per department: S.No, Department Name, Name (contact), Process, Phone number, Email-ID, Handles Personal Data?
- **Values:** three reference tables. (1) The five Fourth Schedule Part A classes of Data Fiduciary plus "None of these", with who is in each and what is exempt. (2) Four classes the Government can notify later, with status as at 9 Oct 2026. (3) A starter list of 28 other laws and regulators by area (all sectors, healthcare, education and children, employment, finance), each marked whether it was checked.

Section 7 of this questionnaire asks the client the same things that Part A of workbook 2 asks the assessor (7.1 = E1, 7.2 = E2, 7.3 = E3, 7.4/7.5 = E4, 7.6 = E5, 7.7 = E6, 7.8 = E7, 7.9 = E8, 7.10 = E9, 7.11/7.12 = E10, 7.13 = E12).

### Workbook 2: Applicability and Exemptions Checklist

- **Read Me:** explains why the checklist works at three levels (entity, processing activity, data element) and never at department level, with the sections of the Act that prove it, a worked example, the plan, open points to verify, and the source list (S1 to S5).
- **Checklist:** 35 questions. Columns: Ref, Question, What the answer decides, Legal reference, Evidence to ask for, Source, Answer (mandatory), Client note.

| Part | Refs | Answered | Groups |
| --- | --- | --- | --- |
| A. Entity | E1 to E13 | Once per legal entity | 1 Does the Act reach this entity (E1-E3); 2 What kind of entity (E4-E9); 3 Other laws and data leaving India (E10-E12); 4 Timing (E13) |
| B. Processing activity | P0 to P14 | Per activity | 1 Name the activity (P0); 2 In scope (P1-P2); 3 Our role (P3-P4); 4 Exemptions under Sec 17 (P5-P8); 5 Consent or legitimate use (P9); 6 Children and guardians (P10-P13); 7 Older data (P14) |
| C. Data element | D1 to D7 | Flags on each activity's elements; record only exceptions | D1 personal data?, D2 made public by the person?, D3 child's or guardian-held?, D4 used to decide about the person?, D5 high-risk?, D6 another law fixes retention?, D7 leaves India? |

Answer lists: most questions use Yes, No, Not sure, N/A. E7 uses Notified, Not notified - possible, Not notified - unlikely, Not sure. P3 uses Client decides, Client with others, Acts on instructions of another, Not sure. P9 uses 7(a) Voluntarily given, 7(b)/(c) State function, 7(d) Legal duty, 7(e) Court order, 7(f) Medical emergency, 7(g) Epidemic, 7(h) Disaster, 7(i) Employment, None - consent needed, Not sure.

The sheet has no formulas. What follows from an answer is written as text in "What the answer decides".

### Workbook 3: Inventory, ROPA, Activity Data, Data Flow and Data Classification

Everything is joined by ID; nothing is retyped.

| Sheet | One row per | ID | Rows available | Auto columns |
| --- | --- | --- | --- | --- |
| Owners | Owner (person or department), below a Document Control block | owner name (must be unique) | from row 18 | -- |
| System Inventory | System | SYS- | 992 | Row alerts |
| Application Inventory | Application | APP- | 992 | Row alerts |
| Security Controls | Control | Control ID | 992 | Row alerts |
| Vendor List | Vendor | VEN- | 992 | Row alerts |
| Policy Inventory | Policy | Policy ID | 992 | Next review due, Row alerts |
| ROPA | Processing activity (one purpose) | ACT- | 300 | Categories of personal data, outside recipients, path check, leaves India, cross-border check, elements, highest tier, high-risk types |
| Activity Data | Activity and data element | -- | 1,000 | Activity name, element name, group, type, tier, high-risk type |
| Data Flow | Place an activity's data passes through | -- | 1,000 | Activity name, node name, node type, system used for zone, zone, check |
| Flow Nodes | Person group, department or outside organisation not in the Inventory | DP-, DEP-, EXT- | 496 | -- |
| Data Classification | Data element | DE-<group code>-<number> | 254 preloaded | -- |
| ROPA Values, DC Values | Dropdown lists and definitions | -- | -- | -- |

The Owners sheet's Document Control block holds: document title, document ID, client or entity, prepared by, reviewed by, approved by, classification, version, date, effective date, last change date, last change by.

The ROPA has 45 columns in seven bands: Activity (ID, name, department), the ROPA template fields 2 to 14, "More detail we need" (our role, exemption, children's data, older consent, collection point, system, app and control IDs, retention law, deletion method), Notes (process description), Walkthrough (interview date, staff interviewed, evidence seen, side channels, say versus show, client confirmed, confirmed date), Data path checks, and the roll-up from Activity Data.

The 14 ROPA template fields are: 1 Processing Activity Name, 2 Purpose, 3 Legal Basis, 4 Categories of Data Principals, 5 Categories of Personal Data (fills itself), 6 Source of Data, 7 Internal Recipients, 8 External Recipients and Processors (8a vendor IDs, 8b other recipients), 9 Retention Period, 10 Security Measures, 11 Cross-Border Transfer (11a yes/no, 11b countries), 12 Consent Status, 13 Last Updated, 14 Owner or DPO Contact.

**Data Classification catalogue: 254 elements in 20 groups.** 253 are personal data and 1 is not. 76 carry a "Split from" note. No element has a fixed-retention law filled in. No element is preloaded as Public.

| Group | Elements | Types used | Tiers used | High-risk type | Examples |
| --- | --- | --- | --- | --- | --- |
| Personal identifiers | 12 | Document, Field | Standard | None | Full name; Date of birth / age |
| Contact details | 10 | Field, Record | Standard | None | Mobile number; Email address |
| Demographic and personal attributes | 7 | Field | Standard | None | Preferred language; Occupation |
| Family and dependants | 18 | Document, Field, Record | Confidential, Internal | None | Dependant name; Dependant date of birth |
| Government and official identifiers | 27 | Document, Field | Confidential | Government ID | Aadhaar number; Virtual ID |
| Financial data | 29 | Document, Field, Record | Confidential | Financial | Bank account number; IFSC code |
| Employment and professional data | 23 | Document, Field, Record | Confidential, Internal | None | Job title; Department |
| Education and training | 21 | Document, Field, Record | Confidential, Internal | None | Qualifications and marksheets; Student academic records |
| Health and medical data | 24 | Document, Field, Record | Confidential | Health | Diagnosis; Prescriptions |
| Genetic data | 2 | Document, Record | Confidential | Health | Genetic / genomic data; DNA test result |
| Biometric data | 7 | Field | Confidential | Biometric | Fingerprint; Face template |
| Online and device identifiers | 10 | Field, Record | Internal | None | IP address; Device ID |
| Authentication and security data | 8 | Field | Confidential | None | One-time password; MFA secret |
| Behavioural and usage data | 13 | Record | Internal | None | Preferences and interests; Inferred segments |
| Location and travel data | 8 | Field, Record | Internal | Location | Precise GPS location; Cell-tower location |
| Communications | 10 | Record | Confidential, Internal | None | Email/chat content; Complaint text |
| Images, audio and video | 11 | Field, Record | Confidential, Internal | None | CCTV footage; Call recording |
| Criminal and legal data | 6 | Document, Record | Confidential | None | Criminal / court records; Allegations in investigations |
| Protected and sensitive attributes | 6 | Document, Field | Confidential | None | Religion / caste; Sexual orientation / gender identity |
| Consent and preference records | 2 | Record | Standard | None | Consent and notice records; Marketing opt-in and opt-out |

Definitions from DC Values:

| Term | Meaning |
| --- | --- |
| Type: Field | One fact that can be right or wrong, collected or deleted on its own |
| Type: Record | A bundle kept whole (CCTV footage, a clinical history) |
| Type: Document | A file or copy (a scan, certificate or report) |
| Tier: Public | Information the client has chosen to make public. Not preloaded; set per element from the client's response. Separate from the Act's "made public by the person" test (D2) |
| Tier: Standard | Identifies or contacts a person; limited harm if exposed on its own |
| Tier: Internal | For internal use only; can profile, locate, monitor or reveal circumstances of a person or family; also staff and student records |
| Tier: Confidential | Serious harm if exposed: government IDs, financial, health, genetic, biometric, credentials, criminal and legal, protected attributes, guardian or income proofs |
| High-risk type | Government ID, Financial, Health, Biometric, Location, None (checklist D5) |

The tier definitions are marked in the workbook as working proposals for review.

**The one sample activity** (marked "Sample: delete"): ACT-001 "Delivery scheduling", department Operations, legal basis Consent (Sec 6), three elements (DE-ID-001, DE-CON-001, DE-CON-003), and a three-step flow: DP-001 Customers, then DEP-001 Operations, then EXT-001 Courier partner. It refers to SYS-001 and APP-001, but those inventory rows are empty.

### Workbook 4: Legal Basis Review

- **Activity Review:** one row per activity, 45 columns: 13 pasted from the ROPA, the route we conclude and the Sec 7 clause, the route mismatch, 20 test answers (C1 to C10, L1 to L4, X1 to X3, K1 to K3), counts from the Element Check, tests failed, tests open, outcome, why, assessor notes, reviewed by, review date. Room for 200 activities.
- **Element Check:** one row per activity and element: the pasted element columns, E1 "Needed for the stated purpose?", E2 "Named in the notice?", and an automatic finding. Room for 1,000 rows.
- **Findings:** Finding ID, Activity ID, activity name (auto), department (auto), test ref, law reference (auto), what we found, evidence seen, client response, remediation owner, rating (left blank until Phase 5), status. Room for 300.
- **Tests:** the 23 tests.

| Ref | Applies to | Question (short) | Legal reference |
| --- | --- | --- | --- |
| R1 | All | Is there a legal basis for this purpose? | Sec 4(1) |
| C1 | Consent | Notice given before or when consent was asked? | Sec 5(1); Rule 3 |
| C2 | Consent | Notice stands alone and is itemised? | Rule 3 |
| C3 | Consent | Notice says how to withdraw, use rights, complain? | Rule 3; Sec 6(4) |
| C4 | Consent | Plain language, language choice, contact details? | Sec 6(3) |
| C5 | Consent | Free, specific, unbundled? | Sec 6(1) |
| C6 | Consent | Clear affirmative action? | Sec 6(1) |
| C7 | Consent | Only necessary data? | Sec 6(1) |
| C8 | Consent | Withdrawal easy and honoured? | Sec 6(4), 6(6); Rule 3 |
| C9 | Consent | Can prove notice and consent? | Sec 6(10) |
| C10 | Consent | Pre-Act consent re-noticed? | Sec 5(2) (verify) |
| L1 | Sec 7 use | Clause conditions met? | Sec 7(a)-(i) |
| L2 | Sec 7 use | Used only for that purpose? | Sec 7 |
| L3 | Sec 7 use | Evidence on file? | Sec 7 |
| L4 | Sec 7 use | For 7(a): no objection from the person? | Sec 7(a) |
| X1 | Exemption | Fits the exact limb and conditions? | Sec 17; Rule 12; Fourth Schedule |
| X2 | Exemption | Evidence on file? | Sec 17; Rule 12 |
| X3 | Exemption | Used only for the duties lifted? | Rule 12; Sec 9(1), 9(3) |
| K1 | Children | Verifiable parent or guardian consent? | Sec 9(1); Rule 10 |
| K2 | Children | No tracking, monitoring or targeted ads (or listed exception)? | Sec 9(3); Rule 12; Fourth Schedule |
| K3 | Children | No harm to well-being? | Sec 9(2) |
| E1 | Element | Needed for the stated purpose? | Sec 6(1) |
| E2 | Element | Named in the notice? | Rule 3 |

Each test also has a full question, a plain reading of the law and the evidence to ask for. Every test is worded so that Yes = passes.

- **Law Notes:** plain-word summaries of Sec 7(a) to 7(i), Fourth Schedule Part A (A1 to A5) and Part B (B1 to B5).
- **Values:** Route (Consent (Sec 6), Legitimate use (Sec 7), Exemption only (Sec 17), Out of scope, None identified); Sec 7 clause (7(a) to 7(i)); Answer (Yes, No, Not sure, Not applicable); Yes / No / Not sure; Finding status (Open, Client to respond, Agreed, Disputed, Closed); the test refs.

Outcomes as the workbook defines them: **Supported** when every test for the route is Yes or Not applicable; **Gap** when at least one test is No, or the ROPA says consent is Not captured, or an element is not needed or not in the notice; **Gap: no legal basis** when the route is None identified; **Cannot conclude yet** when there is no No but some tests are blank or Not sure; **Out of scope** with the reason recorded in the notes. Where one activity mixes routes, it is split into two activities.

## Things to know

1. **No demo data.** The template files hold no filled demo. Demo and acceptance data come from the three fictional clients supplied separately on 11 Nov 2026 (18).
2. **A real client name is present.** The Owners sheet of workbook 3 has a real client name as the client and document ID a real document ID, although the folder's README says the files hold no client data. This is why the Excel files are not committed.
3. **Workbook 1 was not in the Notion documents.** The organisation profile and the department list are new to the project scope.
4. **Two sets of refs both use the letter E.** E1 to E13 are entity questions in workbook 2; E1 and E2 are element tests in workbook 4.
5. **Phase 4 is not here.** Workbook 4 says the evidence testing of security controls is outside it. Nothing in these files defines the "five rows per system, Rule 6 (a) to (e)" review described in Notion.
6. **The workbook copies data between files by hand.** Workbook 4 asks the assessor to paste ROPA and Activity Data rows into it. In Comply these are the same records, so that step disappears.
7. **Legal content is marked as working summaries.** The workbooks repeat that law references must be checked against the Gazette before being quoted, and that dates (duties starting about 13 May 2027; Rule 4 about 13 Nov 2026) are to be verified.

## Part 2. Column reference

Generated from the files. "Kind": mandatory = header marked `*`; auto = filled by a formula (never imported, always computed by Comply); optional = everything else. The Department sheet marks no column as mandatory.

### 1 - Organisation Profile.xlsx


#### Sheet: Department

Header row 3, data from row 4.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | S.No | optional |  |
| B | Department Name | optional |  |
| C | Name | optional |  |
| D | Process | optional |  |
| E | Phone number | optional |  |
| F | Email-ID | optional |  |
| G | Handles Personal Data? | optional |  |

### 3 - Inventory, ROPA, Activity Data, Data Flow and Data Classification.xlsx


#### Sheet: System Inventory

Header row 2, data from row 3.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | System ID* | mandatory |  |
| B | System name* | mandatory |  |
| C | Type* | mandatory | Server, Database, Endpoint, Network device, Cloud service, Paper-to-digital |
| D | Owner (department or person)* | mandatory | from Owners sheet (owner names) |
| E | Hosting* | mandatory | On-premises, Cloud, Hybrid |
| F | Location* (state/city/country) | mandatory |  |
| G | Stores or processes personal data?* (Y/N) | mandatory | Yes, No |
| H | Data categories held (if Y) | optional |  |
| I | Data Principal categories (if Y) | optional |  |
| J | Encryption at rest | optional | Yes, Partial, No, Not applicable |
| K | Backup (Y/N, frequency) | optional | No, Yes - Daily, Yes - Weekly, Yes - Monthly, Yes - Other |
| L | Log retention period (Rule 6 needs at least 1 year) | optional | None, Less than 1 year, 1 year, More than 1 year |
| M | Linked applications | optional |  |
| N | Remarks | optional |  |
| O | Row alerts (auto - do not edit) | auto (formula) |  |

#### Sheet: Application Inventory

Header row 2, data from row 3.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | App ID* | mandatory |  |
| B | App name* | mandatory |  |
| C | Business purpose* | mandatory |  |
| D | Owner* | mandatory | from Owners sheet (owner names) |
| E | Type* | mandatory | In-house, Third-party, SaaS |
| F | Vendor (if third-party) | optional |  |
| G | Hosted on (System ID) | optional |  |
| H | Personal data processed?* (Y/N) | mandatory | Yes, No |
| I | Data elements collected (if Y) | optional |  |
| J | Purpose of processing (if Y) | optional |  |
| K | Collection point (form, app, paper, API) | optional | Web form, Mobile app, Paper form, API, Call or email, Walk-in, Other |
| L | Consent or notice shown at collection | optional | Yes, No, Partial, Not applicable |
| M | Children’s data (Y/N) | optional | Yes, No |
| N | Shares data with (vendor or external) | optional | from Vendor List (vendor names) |
| O | Cross-border transfer (Y/N, country) | optional |  |
| P | Retention period | optional |  |
| Q | Deletion method | optional | Automatic, Manual, Not defined |
| R | Users and access roles | optional |  |
| S | Login method (SSO, MFA) | optional | Password only, SSO, MFA, SSO + MFA, Other |
| T | Row alerts (auto - do not edit) | auto (formula) |  |

#### Sheet: Security Controls

Header row 2, data from row 3.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | Control ID* | mandatory |  |
| B | Control name* | mandatory |  |
| C | Category* | mandatory | Access control, Encryption, Logging and monitoring, Backup and recovery, Network security, Incident response, Vendor management, Physical security, Other |
| D | Applies to (System or App ID)* | mandatory |  |
| E | Implemented?* | mandatory | Yes, Partial, No, Not applicable |
| F | Control description (what is actually done) | optional |  |
| G | Owner* | mandatory | from Owners sheet (owner names) |
| H | Evidence available* | mandatory | Yes, Partial, No |
| I | Evidence reference or link | optional |  |
| J | Last reviewed date | optional |  |
| K | Linked DPDP requirement (Rule 6 item) | optional | Encryption or masking, Access control, Logging and monitoring, Backup and continuity, Log retention (1 year), Processor contract, Other measures |
| L | Gap or remarks | optional |  |
| M | Linked policy ID | optional | from Policy Inventory (IDs) |
| N | Row alerts (auto - do not edit) | auto (formula) |  |

#### Sheet: Vendor List

Header row 2, data from row 3.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | Vendor ID* | mandatory |  |
| B | Vendor name* | mandatory |  |
| C | Service provided* | mandatory |  |
| D | Role* | mandatory | Processor, Joint fiduciary, Other |
| E | Handles personal data?* | mandatory | Yes, No |
| F | Data categories shared (if Y) | optional |  |
| G | Data location* | mandatory | India, Outside India, Both, Unknown |
| H | Contract in place* | mandatory | Yes, No, Expired |
| I | Security clause in contract* | mandatory | Yes, No, Partial |
| J | Breach notification clause | optional | Yes, No, Partial |
| K | Deletion or return clause | optional | Yes, No, Partial |
| L | Sub-processors | optional | Yes, No, Unknown |
| M | Contract start and end dates | optional |  |
| N | Business owner* | mandatory | from Owners sheet (owner names) |
| O | Last review date | optional |  |
| P | Remarks | optional |  |
| Q | Row alerts (auto - do not edit) | auto (formula) |  |

#### Sheet: Policy Inventory

Header row 2, data from row 3.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | Policy ID* | mandatory |  |
| B | Policy name* | mandatory |  |
| C | Document type* | mandatory | Policy, SOP, Procedure, Guideline, Notice, Form |
| D | Category* | mandatory | Privacy notice, Consent, Retention and deletion, Information security, Access control, Incident and breach response, Vendor management, Data principal rights and grievance, Children's data, Other |
| E | Owner* | mandatory | from Owners sheet (owner names) |
| F | Version* | mandatory |  |
| G | Status* | mandatory | Draft, Approved, Under review, Expired, Not available |
| H | Approved by | optional | from Owners sheet (owner names) |
| I | Approval date | optional |  |
| J | Last review date | optional |  |
| K | Next review due (auto) | auto (formula) |  |
| L | Applies to | optional |  |
| M | Communicated to staff? | optional | Yes, No, Partial |
| N | Linked DPDP requirement | optional | Notice (Rule 3), Consent (Sec 6), Security safeguards (Rule 6), Breach response (Rule 7), Retention and erasure (Rule 8), Contact person (Rule 9), Children's data (Rule 10), Data principal rights (Rule 14), Other |
| O | Linked control IDs | optional | from Security Controls (IDs) |
| P | Evidence reference* | mandatory |  |
| Q | Remarks | optional |  |
| R | Row alerts (auto - do not edit) | auto (formula) |  |

#### Sheet: ROPA

Header row 5, data from row 6.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | Activity ID* | mandatory |  |
| B | 1. Processing Activity Name* | mandatory |  |
| C | Department* | mandatory |  |
| D | 2. Purpose* | mandatory |  |
| E | 3. Legal Basis* | mandatory | Consent (Sec 6), 7(a) Voluntarily provided for a stated purpose, 7(b) State benefit or service, 7(c) State function or security of India, 7(d) Legal duty to disclose to the State, 7(e) Court or tribunal order, 7(f) Medical emergency, 7(g) Epidemic or public health threat, 7(h) Disaster or public order, 7(i) Employment purposes, None identified yet |
| F | 4. Categories of Data Principals* | mandatory |  |
| G | 5. Categories of Personal Data (auto, from Activity Data) | auto (formula) |  |
| H | 6. Source of Data* | mandatory | From the person, From a third party, Both |
| I | 7. Internal Recipients (departments) | optional |  |
| J | 8a. External: Processors (Vendor IDs) | optional | IDs from the Vendor List sheet |
| K | 8b. External: other recipients (EXT IDs or names) | optional |  |
| L | 9. Retention Period* | mandatory |  |
| M | 10. Security Measures (summary or Control IDs) | optional |  |
| N | 11a. Cross-Border Transfer?* | mandatory | Yes, No, Not sure |
| O | 11b. Countries | optional |  |
| P | 12. Consent Status* | mandatory | Active, Partial, Not captured, Not applicable |
| Q | 13. Last Updated* | mandatory |  |
| R | 14. Owner / DPO Contact* | mandatory |  |
| S | Our role* | mandatory | Data Fiduciary, Joint Data Fiduciary, Data Processor |
| T | Exemption claimed | optional | Not claimed, 17(1)(a) Legal right or claim, 17(1)(b) Judicial, quasi-judicial, regulatory or supervisory function, 17(1)(c) Prevent, detect, investigate or prosecute offences, 17(1)(d) Outsourced processing of people outside India, 17(1)(e) Court-approved merger or arrangement, 17(1)(f) Trace a loan defaulter's finances and assets, 17(2)(b) Research, archiving or statistics, Rule 12(1) Children: Fourth Schedule Part A class and purpose, Rule 12(2) Children: Fourth Schedule Part B purpose |
| U | Exemption reason | optional |  |
| V | Children or guardian-held data?* | mandatory | Yes, No |
| W | Consent given before the Act? | optional | Yes, No, Not sure |
| X | Collection point* | mandatory | Web form, Mobile app, Paper form, API, Call or email, Walk-in, Other |
| Y | System IDs* | mandatory | IDs from the System Inventory sheet |
| Z | App IDs | optional | IDs from the Application Inventory sheet |
| AA | Law fixing the retention period | optional |  |
| AB | Deletion method | optional |  |
| AC | Control IDs | optional | IDs from the Security Controls sheet |
| AD | Process description (interview notes) | optional |  |
| AE | Interview date | optional |  |
| AF | Staff interviewed | optional |  |
| AG | Evidence seen | optional |  |
| AH | Side channels (WhatsApp, Excel, paper) | optional |  |
| AI | Say vs show difference | optional |  |
| AJ | Client confirmed? | optional | Yes, No |
| AK | Confirmed date | optional |  |
| AL | Shared outside the client?* | mandatory | Yes, No, Not sure |
| AM | Outside recipients in Data Flow (auto) | auto (formula) |  |
| AN | Path check (auto) | auto (formula) |  |
| AO | Leaves India per Activity Data or Data Flow (auto) | auto (formula) |  |
| AP | Cross-border check (auto) | auto (formula) |  |
| AQ | Elements (auto) | auto (formula) |  |
| AR | Highest tier (auto) | auto (formula) |  |
| AS | High-risk types present (auto) | auto (formula) |  |

#### Sheet: Activity Data

Header row 5, data from row 6.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | Activity ID* | mandatory |  |
| B | Activity name (auto) | auto (formula) |  |
| C | Element ID* | mandatory | IDs from the Data Classification sheet |
| D | Element name (auto) | auto (formula) |  |
| E | Group (auto) | auto (formula) |  |
| F | Type (auto) | auto (formula) |  |
| G | Tier (auto) | auto (formula) |  |
| H | High-risk type (auto) | auto (formula) |  |
| I | Made public by the person? (D2) | optional | Yes, No, Not sure |
| J | Child's data in this activity? (D3) | optional | Yes, No, Not sure |
| K | Used to decide about the person? (D4) | optional | Yes, No, Not sure |
| L | Leaves India? (D7) | optional | Yes, No, Not sure |
| M | Retention for this use | optional |  |
| N | Notes | optional |  |

#### Sheet: Data Flow

Header row 5, data from row 6.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | Activity ID* | mandatory |  |
| B | Activity name (auto) | auto (formula) |  |
| C | Node ID* | mandatory | IDs from the Flow Nodes sheet |
| D | Node name (auto) | auto (formula) |  |
| E | Node type (auto) | auto (formula) |  |
| F | System used for zone (auto) | auto (formula) |  |
| G | Zone (auto) | auto (formula) |  |
| H | Shared further?* | mandatory | Yes, No, Not sure |
| I | Shared with (node and activity IDs; separate with ;)* | mandatory |  |
| J | Channel | optional |  |
| K | Check (auto) | auto (formula) |  |

#### Sheet: Flow Nodes

Header row 4, data from row 5.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | Node ID* | mandatory |  |
| B | Node name* | mandatory |  |
| C | Node type* | mandatory | Data principal, Department, External party |
| D | Zone* | mandatory | Data principal, Client premises, Cloud or vendor (India), Other organisation (India), Outside India, Unknown |
| E | Country | optional |  |
| F | Remarks | optional |  |

#### Sheet: Data Classification

Header row 4, data from row 5.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | Element ID* | mandatory |  |
| B | Element name* | mandatory |  |
| C | Group* | mandatory | Personal identifiers, Contact details, Demographic and personal attributes, Family and dependants, Government and official identifiers, Financial data, Employment and professional data, Education and training, Health and medical data, Genetic data, Biometric data, Online and device identifiers, Authentication and security data, Behavioural and usage data, Location and travel data, Communications, Images, audio and video, Criminal and legal data, Protected and sensitive attributes, Consent and preference records |
| D | Type* | mandatory | Field, Record, Document |
| E | Personal data?* | mandatory | Yes, No |
| F | Risk tier* | mandatory | Public, Standard, Internal, Confidential |
| G | High-risk type | optional | Government ID, Financial, Health, Biometric, Location, None |
| H | Fixed-retention law (if any) | optional |  |
| I | Split from | optional |  |
| J | Notes | optional |  |

### 4 - Legal Basis Review.xlsx


#### Sheet: Activity Review

Header row 5, data from row 6.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | Activity ID* | mandatory |  |
| B | Activity name* | mandatory |  |
| C | Department | optional |  |
| D | Purpose | optional |  |
| E | Legal basis claimed (ROPA 3) | optional |  |
| F | Consent status (ROPA 12) | optional |  |
| G | Our role | optional |  |
| H | Exemption claimed (ROPA) | optional |  |
| I | Children's data? | optional |  |
| J | Consent given before the Act? | optional |  |
| K | Categories of data (ROPA 5) | optional |  |
| L | Highest tier | optional |  |
| M | High-risk types | optional |  |
| N | Basis route we conclude* | mandatory | Consent (Sec 6), Legitimate use (Sec 7), Exemption only (Sec 17), Out of scope, None identified |
| O | Sec 7 clause (if Sec 7) | optional | 7(a), 7(b), 7(c), 7(d), 7(e), 7(f), 7(g), 7(h), 7(i) |
| P | ROPA vs our route (auto) | auto (formula) |  |
| Q | C1 Notice given first? | optional | Yes, No, Not sure, Not applicable |
| R | C2 Notice stands alone and is itemised? | optional | Yes, No, Not sure, Not applicable |
| S | C3 Notice says how to withdraw, use rights, complain? | optional | Yes, No, Not sure, Not applicable |
| T | C4 Plain language, language choice, contact? | optional | Yes, No, Not sure, Not applicable |
| U | C5 Free, specific, unbundled? | optional | Yes, No, Not sure, Not applicable |
| V | C6 Clear affirmative action? | optional | Yes, No, Not sure, Not applicable |
| W | C7 Only necessary data? | optional | Yes, No, Not sure, Not applicable |
| X | C8 Withdrawal easy and honoured? | optional | Yes, No, Not sure, Not applicable |
| Y | C9 Can prove notice and consent? | optional | Yes, No, Not sure, Not applicable |
| Z | C10 Pre-Act consent re-noticed? | optional | Yes, No, Not sure, Not applicable |
| AA | L1 Clause conditions met? | optional | Yes, No, Not sure, Not applicable |
| AB | L2 Used only for that purpose? | optional | Yes, No, Not sure, Not applicable |
| AC | L3 Evidence on file? | optional | Yes, No, Not sure, Not applicable |
| AD | L4 7(a): no objection from the person? | optional | Yes, No, Not sure, Not applicable |
| AE | X1 Fits the exact limb and conditions? | optional | Yes, No, Not sure, Not applicable |
| AF | X2 Evidence on file? | optional | Yes, No, Not sure, Not applicable |
| AG | X3 Used only for duties lifted? | optional | Yes, No, Not sure, Not applicable |
| AH | K1 Verifiable parent or guardian consent? | optional | Yes, No, Not sure, Not applicable |
| AI | K2 No tracking, monitoring or targeted ads (or listed exception)? | optional | Yes, No, Not sure, Not applicable |
| AJ | K3 No harm to well-being? | optional | Yes, No, Not sure, Not applicable |
| AK | Elements not needed (auto) | auto (formula) |  |
| AL | Elements not in notice (auto) | auto (formula) |  |
| AM | Tests failed (auto) | auto (formula) |  |
| AN | Tests open (auto) | auto (formula) |  |
| AO | Outcome (auto) | auto (formula) |  |
| AP | Why (auto) | auto (formula) |  |
| AQ | Assessor notes | optional |  |
| AR | Reviewed by | optional |  |
| AS | Review date | optional |  |

#### Sheet: Element Check

Header row 5, data from row 6.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | Activity ID* | mandatory |  |
| B | Element ID* | mandatory |  |
| C | Element name | optional |  |
| D | Group | optional |  |
| E | Tier | optional |  |
| F | High-risk type | optional |  |
| G | Made public by the person (D2) | optional |  |
| H | Child's data (D3) | optional |  |
| I | Used to decide about the person (D4) | optional |  |
| J | Leaves India (D7) | optional |  |
| K | E1 Needed for the stated purpose?* | mandatory | Yes, No, Not sure |
| L | E2 Named in the notice?* | mandatory | Yes, No, Not sure |
| M | Activity name (auto) | auto (formula) |  |
| N | Route we concluded (auto) | auto (formula) |  |
| O | Finding (auto) | auto (formula) |  |
| P | Notes | optional |  |

#### Sheet: Findings

Header row 5, data from row 6.

| Col | Header | Kind | Allowed values |
| --- | --- | --- | --- |
| A | Finding ID | optional |  |
| B | Activity ID* | mandatory |  |
| C | Activity name (auto) | auto (formula) |  |
| D | Department (auto) | auto (formula) |  |
| E | Test ref* | mandatory | R1, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, L1, L2, L3, L4, X1, X2, X3, K1, K2, K3, E1, E2 |
| F | Law reference (auto) | auto (formula) |  |
| G | What we found* | mandatory |  |
| H | Evidence seen | optional |  |
| I | Client response | optional |  |
| J | Remediation owner | optional |  |
| K | Rating (set in Phase 5) | optional |  |
| L | Status | optional | Open, Client to respond, Agreed, Disputed, Closed |
