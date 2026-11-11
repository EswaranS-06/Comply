# Client B: Halvorn Systems Pvt Ltd (fictional demo client)

> **Fiction notice.** Halvorn Systems and everything below is invented for training and demo use. Any resemblance to a real organisation is coincidence.
>
> **What this file is for.** Every detail needed to fill the workbooks end to end for a client whose main role is **Data Processor**. IDs link across sections. Legal statements marked *(verify)* are working readings, not confirmed law.

## 0. Why this client is different

| Dimension | Halvorn |
| --- | --- |
| Sector | Business software (payroll, HR and attendance SaaS) |
| Model | B2B; about 650 customer companies; end users are their employees |
| Data | Salary, bank, statutory IDs, attendance, some health and minors' data, all belonging to the customers' staff |
| Role pattern | **Data Processor** for most activities (the customer decides purposes). **Data Fiduciary** only for its own staff, its own sales leads, a campus test platform and product benchmarking |
| Law pattern | Phase 3 is mostly "Out of scope" for processor activities; the work moves to Phase 4 (contracts, security, breach help). Role creep: benchmarking turns Halvorn into a fiduciary |
| Cross-border | Engineering team in Poland with production access; US email vendor; data hosted in India |
| Children | Campus assessment platform used by 16 and 17 year olds; some customers pay minor apprentices |
| Likely outcomes | 3 Supported, 2 Gap, 1 Gap: no legal basis, 1 Cannot conclude yet, 4 Out of scope (processor) |
| Special flag | Not an SDF candidate on size; check if notified later |

## 1. Snapshot

| Item | Detail |
| --- | --- |
| Legal name | Halvorn Systems Pvt Ltd |
| Type | Private limited company, founded 2016 |
| Registered office | Whitefield, Bengaluru, Karnataka |
| Other sites | Pune development office; a subsidiary in Warsaw, Poland (Halvorn Sp. z o.o.) with 35 engineers |
| Headcount | 310 in India, 35 in Poland |
| Customers | About 650 companies, 1.9 million employee records |
| Products | Payroll engine, attendance app, HR portal, expense claims, campus assessment platform |
| Assessment reference date | 2026-11-10 |
| Engagement scope | India entity; Polish subsidiary assessed as a vendor and cross-border recipient |
| Client contacts | CTO (sponsor), Head of Legal and Compliance, Head of Security |
| DPO | None |
| SDF status | Not notified |

## 2. How the business works

1. A customer signs a master services agreement and an order form.
2. Customer HR uploads employee data (or connects its HR system). Halvorn stores it and runs payroll each month.
3. Employees use the mobile attendance app (GPS, selfie check-in for field staff) and the self-service portal.
4. Halvorn generates payslips, statutory returns and bank payment files for the customer.
5. The support team accesses customer tenants to fix issues, on request and with a ticket.
6. Halvorn's product team also builds an industry salary benchmark from customers' data, de-identified, and sells it as a report *(trap: is it truly anonymous?)*.
7. Separately, Halvorn runs a campus assessment platform, selling skills tests to colleges and employers; test takers are students, some under 18.
8. Sales and marketing run on the website and events.

## 3. Departments

| ID | Department | Head | Headcount | Owns activities |
| --- | --- | --- | --- | --- |
| DEP-001 | Product Engineering | VP Engineering | 140 | ACT-001, ACT-002 (as processor) |
| DEP-002 | Customer Success and Support | Head of Support | 55 | ACT-003 |
| DEP-003 | Implementation and Data Migration | Head of Delivery | 30 | ACT-004 |
| DEP-004 | Data and Analytics | Head of Data | 18 | ACT-005 |
| DEP-005 | Campus and Assessments | Product Head, Campus | 15 | ACT-006 |
| DEP-006 | Sales and Marketing | CMO | 25 | ACT-007 |
| DEP-007 | People Operations | Head of People | 9 | ACT-008 |
| DEP-008 | Security and Compliance | Head of Security | 12 | ACT-009 |
| DEP-009 | Finance | CFO | 11 | none |
| DEP-010 | Legal | Head of Legal | 4 | none |
| DEP-011 | Infrastructure and DevOps | Head of Infrastructure | 20 | none (runs systems) |
| DEP-012 | Poland Engineering (subsidiary) | Engineering Manager | 35 | works on ACT-001 |

## 4. Other laws

| Item | Note |
| --- | --- |
| Labour and wage laws | Payroll records retention set by the customer's own obligations, not Halvorn's *(verify)* |
| Provident fund and ESI rules | Returns filed on behalf of customers |
| IT law and rules | Existing reasonable-security rules continue until replaced *(verify)* |
| Contract terms with customers | Many customers use their own data processing schedules |

## 5. Part A: entity checklist answers

| Ref | Answer | Reasoning |
| --- | --- | --- |
| E1 | Yes | India-incorporated, Bengaluru servers |
| E2 | No | No offering to people outside India |
| E3 | Yes | Fully digital |
| E4 | Yes, two entities | India entity is the main assessed entity; Poland entity is a related processor |
| E5 | Yes | Campus assessments process students' data, some under 18 |
| E6 | No | |
| E7 | Not notified | Not expected on size; track |
| E8 | No | |
| E9 | Not known | |
| E10 | No | No sector regulator of its own |
| E11 | Yes | Poland (engineering access), USA (email vendor) |
| E12 | No | |
| E13 | Reference date 2026-11-10 | Most duties start about 13 May 2027 *(verify)* |

Role note: for ACT-001 to ACT-004 the **role is Data Processor**. The assessor must record the customer as the Data Fiduciary. Phase 3 records "Out of scope" with the reason "processor; the customer decides purpose". Rule-based processor duties are tested in Phase 4 under vendor and contract checks.

## 6. Inventory

### 6.1 Owners

| Client | Entity | Sponsor | Reference date |
| --- | --- | --- | --- |
| Halvorn Systems Pvt Ltd | Halvorn Systems Pvt Ltd | CTO | 2026-11-10 |

### 6.2 System Inventory

| ID | Name | Type | Owner | Hosting | Location | Personal data? | Categories | Principals | Encryption | Backup | Logs | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SYS-001 | Production payroll platform (multi-tenant) | Cloud service | Head of Infrastructure | Cloud | Mumbai, India | Yes | Employee identity, salary, bank, statutory IDs | Customer employees | Yes | Yes - Daily | 1 year | Core |
| SYS-002 | Attendance and mobile backend | Cloud service | VP Engineering | Cloud | Hyderabad, India | Yes | GPS, selfies, attendance | Customer employees | Yes | Yes - Daily | Less than 1 year | |
| SYS-003 | Data warehouse for analytics | Database | Head of Data | Cloud | Mumbai, India | Yes | Salary and role data copied from tenants | Customer employees | Partial | Yes - Weekly | Less than 1 year | Source of benchmark |
| SYS-004 | Support console with tenant impersonation | Application server | Head of Support | Cloud | Mumbai, India | Yes | Any tenant data | Customer employees | Yes | Yes - Daily | 1 year | |
| SYS-005 | Migration staging area | File share | Head of Delivery | Cloud | Pune, India | Yes | Raw spreadsheets from customers | Customer employees | No | No | None | Files stay after go-live |
| SYS-006 | Campus assessment platform | Cloud service | Product Head, Campus | Cloud | Mumbai, India | Yes | Student identity, test answers, proctoring video | Students (some under 18) | Yes | Yes - Daily | Less than 1 year | |
| SYS-007 | CRM | Cloud service | CMO | Cloud | Oregon, USA | Yes | Leads, business contacts | Prospects, customer contacts | Yes | Yes - Daily | 1 year | |
| SYS-008 | HRMS (own staff) | Cloud service | Head of People | Cloud | Mumbai, India | Yes | Staff identity, salary, bank | Employees, candidates | Yes | Yes - Daily | 1 year | |
| SYS-009 | Developer laptops (Poland) | Endpoint | Engineering Manager | On-premises | Warsaw, Poland | Yes | Local copies of production extracts | Customer employees | Partial | No | None | Production extracts used for debugging |
| SYS-010 | Email suite | Cloud service | Head of Infrastructure | Cloud | Virginia, USA | Yes | Payslips sent by email to employees | Customer employees | Yes | Yes - Daily | 1 year | |
| SYS-011 | Backup vault | Cloud service | Head of Infrastructure | Cloud | Chennai, India | Yes | Encrypted backups of SYS-001, SYS-002 | Customer employees | Yes | Not applicable | 1 year | |

### 6.3 Application Inventory

| ID | Name | Purpose | Owner | Hosted on | Vendor | Personal data? |
| --- | --- | --- | --- | --- | --- | --- |
| APP-001 | Payroll engine | Salary and tax calculation | VP Engineering | SYS-001 | none | Yes |
| APP-002 | Attendance app (mobile) | Check-in, leave | VP Engineering | SYS-002 | none | Yes |
| APP-003 | Employee self-service portal | Payslips, declarations | VP Engineering | SYS-001 | none | Yes |
| APP-004 | Benchmark builder | Salary benchmark reports | Head of Data | SYS-003 | none | Yes |
| APP-005 | Support console | Tenant support | Head of Support | SYS-004 | none | Yes |
| APP-006 | Assessment engine and proctoring | Online tests | Product Head, Campus | SYS-006 | VEN-005 | Yes |
| APP-007 | CRM | Sales pipeline | CMO | SYS-007 | VEN-006 | Yes |
| APP-008 | HRMS | Own staff | Head of People | SYS-008 | VEN-007 | Yes |
| APP-009 | Migration toolkit | Data load | Head of Delivery | SYS-005 | none | Yes |
| APP-010 | Email gateway | Payslip email | Head of Infrastructure | SYS-010 | VEN-004 | Yes |

### 6.4 Vendor List

| ID | Name | Service | Role | Personal data? | Data shared | Location | Contract | Security | Breach | Deletion | Sub-processors | Dates | Owner | Last review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VEN-001 | StratoCloud India | Cloud hosting | Processor | Yes | All production data | India | Yes | Yes | Yes | Yes | Yes (listed) | 2023-06 to 2027-05 | Head of Infrastructure | 2026-07 |
| VEN-002 | Halvorn Sp. z o.o. (Poland) | Engineering | Processor | Yes | Production extracts, tenant access | Outside India | Yes (intra-group) | Partial | No | No | No | 2021 | VP Engineering | Never |
| VEN-003 | SMSGate | OTP and SMS | Processor | Yes | Mobile numbers | India | Yes | Yes | Yes | Yes | No | 2025-01 to 2027-12 | Head of Infrastructure | 2026-03 |
| VEN-004 | PostBox Mail | Transactional email | Processor | Yes | Payslip PDFs, emails | Outside India | Yes | Yes | Partial | Partial | Yes | 2024-02 to 2026-12 | Head of Infrastructure | 2025-11 |
| VEN-005 | ProctorView | Exam proctoring | Processor | Yes | Student video, ID photos | Outside India | Yes | Partial | No | No | Unknown | 2025-08 to 2026-08 | Product Head, Campus | Never |
| VEN-006 | LeadHub CRM | CRM | Processor | Yes | Business contact data | Outside India | Yes | Yes | Yes | Yes | Yes | 2024-04 to 2027-03 | CMO | 2026-02 |
| VEN-007 | PeopleCore HRMS | Own HR | Processor | Yes | Own staff data | India | Yes | Yes | Yes | Yes | No | 2025-04 to 2027-03 | Head of People | 2026-04 |
| VEN-008 | BankRail | Salary payment files | Other | Yes | Bank account, amounts | India | Yes | Yes | Yes | Partial | No | 2024-09 to 2027-08 | CFO | 2026-05 |
| VEN-009 | BenchmarkBuyer Consulting | Buys salary reports | Other | Yes (claimed none) | Aggregated salary tables | India | No | No | No | No | Not applicable | Verbal | Head of Data | Never |

### 6.5 Security Controls

| ID | Name | Category | Applies to | Implemented | What is done | Owner | Evidence | Last reviewed | Rule 6 item | Gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CTL-001 | Tenant isolation | Access control | SYS-001 | Yes | Row-level isolation, tested | Head of Security | Yes (pen test 2026-06) | 2026-06 | Access control | |
| CTL-002 | Column encryption for bank and PAN | Encryption | SYS-001 | Yes | Field-level encryption | Head of Security | Yes | 2026-06 | Encryption or masking | |
| CTL-003 | Support impersonation approvals | Access control | SYS-004 | Partial | Ticket required; approver sometimes same person | Head of Support | Partial | 2026-04 | Access control | Weak approval |
| CTL-004 | Support access logs | Logging | SYS-004 | Yes | Every impersonation logged for 13 months | Head of Security | Yes | 2026-10 | Log retention | |
| CTL-005 | Staging area cleanup | Retention | SYS-005 | No | No deletion after go-live | Head of Delivery | No | Never | Measures to follow safeguards | Raw files stay |
| CTL-006 | Developer laptop encryption | Encryption | SYS-009 | Partial | Disk encryption on 60 percent | Engineering Manager | No | Never | Encryption or masking | |
| CTL-007 | Production data masking for debugging | Data masking | SYS-009 | No | Real data used | VP Engineering | No | Never | Encryption or masking | |
| CTL-008 | Backup restore test | Backup | SYS-011 | Yes | Quarterly | Head of Infrastructure | Yes | 2026-09 | Backup and continuity | |
| CTL-009 | Breach runbook with customer notification | Incident | All | Yes | Customer informed within 24 hours by contract | Head of Security | Yes | 2026-08 | Measures to follow safeguards | |

### 6.6 Policy Inventory

| ID | Policy | Owner | Version | Approved | Review due |
| --- | --- | --- | --- | --- | --- |
| POL-001 | Information security | Head of Security | 5.0 | 2026-02 | 2027-02 |
| POL-002 | Data processing standard (as processor) | Head of Legal | 2.1 | 2025-09 | 2026-09 (overdue) |
| POL-003 | Access control | Head of Security | 3.0 | 2026-02 | 2027-02 |
| POL-004 | Retention and deletion | Head of Legal | 1.2 | 2025-01 | 2026-01 (overdue) |
| POL-005 | Privacy notice (website and campus) | Head of Legal | 1.0 | 2024-11 | 2025-11 (overdue) |
| POL-006 | Incident response | Head of Security | 4.0 | 2026-03 | 2027-03 |

## 7. Flow Nodes (not in the Inventory)

| ID | Name | Type | Zone | Country |
| --- | --- | --- | --- | --- |
| DP-001 | Customer employees (all tenants) | Data principal | Data principal | India |
| DP-002 | Minor apprentices of customers | Data principal | Data principal | India |
| DP-003 | Students (campus platform) | Data principal | Data principal | India |
| DP-004 | Own staff | Data principal | Data principal | India |
| DP-005 | Job candidates (own) | Data principal | Data principal | India |
| DP-006 | Sales prospects and customer contacts | Data principal | Data principal | India |
| DEP-001 to DEP-012 | As in section 3 | Department | Client premises (DEP-012: Outside India) | India (DEP-012: Poland) |
| EXT-001 | Customer companies (fiduciaries) | External party | Other organisation (India) | India |
| EXT-002 | Provident fund and ESI bodies | External party | Other organisation (India) | India |
| EXT-003 | Tax authorities | External party | Other organisation (India) | India |
| EXT-004 | Colleges and employers (campus buyers) | External party | Other organisation (India) | India |

## 8. Processing activities (ROPA)

Common values: Last updated 2026-11-08. Owner contact = department head. Children's data = No unless stated.

### ACT-001 Payroll processing for customers
| Field | Value |
| --- | --- |
| Our role | **Data Processor** (customer is the fiduciary) |
| Department | Product Engineering |
| Purpose | Calculate salary and tax and produce payslips on the customer's instruction |
| Legal basis claimed | Not applicable; customer's responsibility |
| Data principals | Customer employees; minor apprentices of customers (children's data = Yes) |
| Source | From the customer (EXT-001) |
| Internal | Engineering (DEP-001), Poland Engineering (DEP-012), Support (DEP-002) |
| External | VEN-001, VEN-002, VEN-004, VEN-008, EXT-002, EXT-003 |
| Retention | Customer's choice; default 7 years after contract end; deletion on request is manual |
| Security | CTL-001, CTL-002, CTL-008 |
| Cross-border | Yes: Poland, USA |
| Consent status | Not applicable |
| Systems and apps | SYS-001, SYS-009, SYS-010, SYS-011; APP-001, APP-003, APP-010 |
| Shared outside the client | Yes |

### ACT-002 Attendance and field tracking for customers
| Field | Value |
| --- | --- |
| Our role | Data Processor |
| Department | Product Engineering |
| Purpose | Record check-ins, leave and field locations for the customer's HR |
| Data principals | Customer employees |
| Source | From the person (via the app) |
| Internal | Engineering (DEP-001) |
| External | VEN-001, VEN-003 |
| Retention | Customer's choice; GPS trail default 3 years |
| Security | CTL-001 |
| Cross-border | No |
| Consent status | Not applicable |
| Systems and apps | SYS-002; APP-002 |
| Shared outside the client | Yes |
| Walkthrough | The app collects continuous background GPS even outside shifts when the customer has not turned off tracking. Selfie images stored with check-ins. |

### ACT-003 Customer support with tenant access
| Field | Value |
| --- | --- |
| Our role | Data Processor |
| Department | Customer Success and Support |
| Purpose | Fix issues on customer instruction |
| Data principals | Customer employees |
| Source | From the customer |
| Internal | Support (DEP-002), Engineering (DEP-001) |
| Retention | Tickets 3 years; screenshots attached to tickets kept indefinitely |
| Security | CTL-003, CTL-004 |
| Cross-border | No |
| Systems and apps | SYS-004; APP-005 |
| Shared outside the client | No |

### ACT-004 Data migration for new customers
| Field | Value |
| --- | --- |
| Our role | Data Processor |
| Department | Implementation and Data Migration |
| Purpose | Load customers' historical employee data into the platform |
| Data principals | Customer employees |
| Source | From the customer |
| Internal | Delivery (DEP-003) |
| Retention | Not defined; raw spreadsheets stay in staging after go-live |
| Security | CTL-005 |
| Cross-border | No |
| Systems and apps | SYS-005; APP-009 |
| Shared outside the client | No |

### ACT-005 Salary benchmarking
| Field | Value |
| --- | --- |
| Our role | **Data Fiduciary** (Halvorn decides purpose and means; role has crept from processor) |
| Department | Data and Analytics |
| Purpose | Build and sell industry salary benchmarks |
| Legal basis claimed | "Anonymised, so the Act does not apply" |
| Data principals | Customer employees |
| Source | From a third party (customer tenants) |
| Internal | Data (DEP-004) |
| External | VEN-009 BenchmarkBuyer (no contract) |
| Retention | Warehouse copy kept indefinitely |
| Security | None specific; SYS-003 encryption partial |
| Cross-border | No |
| Consent status | Not captured |
| Systems and apps | SYS-003; APP-004 |
| Used to decide about the person | No |
| Shared outside the client | Yes |
| Walkthrough | Reports include roles in small companies, so a person can be picked out. Customer contracts do not clearly allow secondary use. |

### ACT-006 Campus assessments
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary (for students; colleges are recipients) |
| Department | Campus and Assessments |
| Purpose | Run online skills tests and share scores with colleges and employers |
| Legal basis claimed | Consent (Sec 6) |
| Data principals | Students, including those under 18 (children's data = Yes) |
| Source | From the person |
| Internal | Campus (DEP-005) |
| External | VEN-005 ProctorView (outside India, contract expiring), EXT-004 |
| Retention | Video kept 5 years |
| Security | Encryption yes; no breach clause with proctoring vendor |
| Cross-border | Yes: proctoring vendor location outside India |
| Consent status | Partial (checkbox ticked by the student; no parental step) |
| Systems and apps | SYS-006; APP-006 |
| Used to decide about the person | Yes (test score shared with employers) |
| Shared outside the client | Yes |

### ACT-007 Sales and marketing
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary |
| Department | Sales and Marketing |
| Purpose | Contact prospects and customer contacts about products |
| Legal basis claimed | 7(a) Voluntarily provided (business cards, form fills) |
| Data principals | Sales prospects and customer contacts |
| Source | Both |
| External | VEN-006 LeadHub (outside India) |
| Retention | 5 years after last contact |
| Cross-border | Yes: USA |
| Consent status | Not applicable |
| Systems and apps | SYS-007; APP-007 |
| Shared outside the client | Yes |
| Walkthrough | Purchased lead lists are also loaded (third party source). |

### ACT-008 Own staff HR
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary |
| Department | People Operations |
| Purpose | Hire, pay and manage Halvorn's own employees |
| Legal basis claimed | 7(i) Employment |
| Data principals | Own staff, job candidates |
| Source | From the person |
| External | VEN-007, EXT-002, EXT-003 |
| Retention | Employment plus 8 years |
| Cross-border | Yes (Polish staff data shared with India HR) |
| Systems and apps | SYS-008; APP-008 |
| Shared outside the client | Yes |

### ACT-009 Security monitoring
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary (own staff devices and logs) and Data Processor (customer logs) |
| Department | Security and Compliance |
| Purpose | Detect misuse of systems |
| Legal basis claimed | None stated |
| Data principals | Own staff |
| Source | From the person (device activity) |
| Retention | 13 months |
| Systems and apps | SYS-004, SYS-008 |
| Shared outside the client | No |

## 9. Activity Data

Retention for this use is "Not defined" unless stated. D3 = child's data; D7 = leaves India.

| Activity | Elements |
| --- | --- |
| ACT-001 | DE-ID-001 Full name; DE-ID-002 Date of birth (D3 for apprentices); DE-ID-009 Employee ID; DE-CON-001; DE-CON-002; DE-CON-003; DE-GOV-003 PAN; DE-GOV-001 Aadhaar number; DE-GOV-009-A UAN; DE-GOV-009-B PF number; DE-GOV-009-C ESIC number; DE-FIN-001-A; DE-FIN-001-B; DE-FIN-004 Income and salary; DE-EMP-007-A Compensation; DE-EMP-007-B Benefits; DE-EMP-004 Attendance and leave; DE-HLT-019 Sick-leave certificate (D7); DE-FIN-008 Tax details; DE-FAM-002 Nominee details; DE-FAM-001-A Dependant name (D7) |
| ACT-002 | DE-ID-001; DE-ID-009; DE-ID-004 Photograph (selfie check-in); DE-BIO-007 Selfie or liveness; DE-LOC-001 Precise GPS; DE-DEV-002-A Device ID; DE-DEV-010-B IMEI; DE-EMP-004; DE-EMP-015 Shift and overtime |
| ACT-003 | DE-ID-001; DE-ID-009; DE-CON-002; DE-FIN-004; DE-FIN-001-A (via screen visibility); DE-COM-008 Ticket history |
| ACT-004 | DE-ID-001; DE-ID-002; DE-CON-001; DE-CON-003; DE-GOV-003; DE-GOV-001; DE-FIN-001-A; DE-FIN-004; DE-EMP-002 Employment history; DE-EMP-011 Offer or contract |
| ACT-005 | DE-EMP-001-A Job title; DE-FIN-004 Salary (D4: no); DE-EMP-007-A; DE-EMP-003 Performance rating; DE-ID-002 (age band) |
| ACT-006 | DE-ID-001; DE-ID-002 (D3); DE-CON-001; DE-CON-002; DE-EDU-001 Qualifications; DE-ID-004 Photograph (D3); DE-AV-007 Screen recording (D3); DE-AV-001 Proctoring video (D3, D7); DE-BEH-008 Test answers and scores (D3, D4); DE-DEV-001 IP address; DE-FAM-003-A Guardian name (missing for most) |
| ACT-007 | DE-ID-001; DE-CON-006-A Business email; DE-CON-006-B Business phone; DE-EMP-001-A Job title; DE-DEV-003 Cookies; DE-COM-009 Marketing opt-in; DE-BEH-009 Campaign responses |
| ACT-008 | DE-ID-001; DE-ID-002; DE-CON-001; DE-CON-002; DE-GOV-003; DE-GOV-009-A; DE-FIN-001-A; DE-EMP-001-A, -B, -C; DE-EMP-006 Background verification; DE-EMP-007-A; DE-EMP-009 CV; DE-EMP-010 Interview notes; DE-HLT-018 Pre-employment medical exam; DE-SEN-006 Police verification |
| ACT-009 | DE-ID-001; DE-DEV-001; DE-DEV-009 Access logs; DE-AUT-001-A Username; DE-EMP-008 Workplace monitoring |

## 10. Data Flow

| Activity | Rows |
| --- | --- |
| ACT-001 | EXT-001 Yes → DEP-003 (file upload); DEP-003 Yes → SYS-005, SYS-001; SYS-001 Yes → APP-001; APP-001 Yes → APP-003, VEN-008, EXT-002, EXT-003; APP-003 Yes → APP-010; APP-010 Yes → VEN-004; VEN-004 Yes → DP-001 (payslip); SYS-001 Yes → SYS-011; SYS-001 Yes → VEN-002 (debug extracts); VEN-002 Yes → SYS-009 (laptops); SYS-009 No |
| ACT-002 | DP-001 Yes → APP-002; APP-002 Yes → SYS-002; SYS-002 Yes → VEN-003; VEN-003 No; SYS-002 Yes → SYS-001 |
| ACT-003 | EXT-001 Yes → DEP-002; DEP-002 Yes → APP-005; APP-005 Yes → SYS-001, DEP-001; DEP-001 No |
| ACT-004 | EXT-001 Yes → DEP-003; DEP-003 Yes → SYS-005; SYS-005 Yes → SYS-001; SYS-001 No |
| ACT-005 | SYS-001 Yes → SYS-003; SYS-003 Yes → APP-004; APP-004 Yes → DEP-004; DEP-004 Yes → VEN-009 (reports); VEN-009 Not sure → (reports onward sale) |
| ACT-006 | DP-003 Yes → APP-006; APP-006 Yes → SYS-006, VEN-005; VEN-005 Not sure → (sub-processors unknown); SYS-006 Yes → EXT-004 |
| ACT-007 | DP-006 Yes → APP-007; APP-007 Yes → SYS-007; SYS-007 Yes → VEN-006; VEN-006 No; purchased list: EXT-005 "Lead list vendor" Yes → APP-007 |
| ACT-008 | DP-004 Yes → DEP-007; DEP-007 Yes → SYS-008; SYS-008 Yes → VEN-007, EXT-002, EXT-003; DEP-012 Yes → DEP-007 (Polish staff data) |
| ACT-009 | DP-004 Yes → SYS-004 (logs); SYS-004 Yes → DEP-008; DEP-008 No |

Add node EXT-005 Lead list vendor (Other organisation, India).

## 11. Hidden processing the walkthrough should surface

| What | Where | Effect |
| --- | --- | --- |
| Real salary data on developer laptops in Poland | ACT-001, SYS-009 | Cross-border; encryption on 60 percent; no masking |
| "Anonymous" benchmark with small cells | ACT-005 | Re-identifiable; Halvorn becomes a fiduciary; no basis |
| Raw migration files never deleted | ACT-004 | Retention gap; processor must delete on instruction |
| Background GPS outside work hours | ACT-002 | Customer default; processor should warn customer |
| Under-18 apprentices and students | ACT-001, ACT-006 | Children's data; parental consent for ACT-006 |
| Purchased lead lists | ACT-007 | Third-party source; basis unclear |
| Support screenshots with bank details attached to tickets | ACT-003 | Indefinite retention |

## 12. Phase 3 expected review

| Activity | Route | Tests not Yes | Expected outcome | Why |
| --- | --- | --- | --- | --- |
| ACT-001 | Out of scope (processor) | | Out of scope | Customer decides purpose; record the customer as fiduciary |
| ACT-002 | Out of scope (processor) | | Out of scope | Same; note GPS default for Phase 4 |
| ACT-003 | Out of scope (processor) | | Out of scope | |
| ACT-004 | Out of scope (processor) | | Out of scope | |
| ACT-005 | None identified | R1 No | Gap: no legal basis | "Anonymised" claim fails; role is fiduciary |
| ACT-006 | Consent | C1 Yes; C2 Yes; C5 Yes; C7 Yes; C9 No (parental consent missing); C10 No (no verifiable parent check; tracking of behaviour of children) | Gap | C9; C10 |
| ACT-007 | Legitimate use 7(a) | L1 No for purchased lists (not voluntary); other tests Yes | Gap | L1 on purchased leads. Split the activity |
| ACT-008 | Legitimate use 7(i) | L4 Not applicable | Supported | None |
| ACT-009 | Legitimate use 7(i) (safeguarding the employer from loss) | L2 Not sure (staff device activity scope) | Cannot conclude yet | One open test |
| (additional) ACT-008b Polish staff data into India HR | Legitimate use 7(i) | None | Supported | |
| (additional) ACT-007b Business contact enquiries inbound | Legitimate use 7(a) | None | Supported | Split from ACT-007 for demo |

Totals using ACT-001 to 009 only: 1 Supported (ACT-008), 2 Gap (ACT-006, ACT-007), 1 Gap: no legal basis (ACT-005), 1 Cannot conclude yet (ACT-009), 4 Out of scope. To reach 3 Supported, add the two additional rows (ACT-008b, ACT-007b) in the demo.

### Findings to log

| ID | Activity | Finding |
| --- | --- | --- |
| LB-001 | ACT-005 | Benchmarking is Halvorn's own purpose with no legal basis; anonymisation not proven |
| LB-002 | ACT-006 | No parental consent for under-18 test takers; behaviour tracked |
| LB-003 | ACT-007 | Purchased lead lists have no voluntary source |
| LB-004 | ACT-009 | Scope of staff device monitoring undefined |

## 13. Phase 4 expected checks

### 13.1 System security

| System | (a) Encryption | (b) Access | (c) Logs | (d) Backup | (e) Log retention 12 months+ |
| --- | --- | --- | --- | --- | --- |
| SYS-001 | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass |
| SYS-002 | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Partial / Partial | Yes / Yes / Pass | No (under 1 year) / Yes / Gap (client confirms) |
| SYS-003 | Partial / Yes / Partial | Yes / Not seen / Not tested | Not sure / not seen / Not tested | Yes / Yes / Pass | No / Yes / Gap (client confirms) |
| SYS-004 | Yes / Yes / Pass | Yes / Partial / Partial (weak approvals) | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass |
| SYS-005 | No / Yes / Gap (client confirms) | Yes / No / Gap: claim not supported | No / Yes / Gap (client confirms) | No / Yes / Gap (client confirms) | No / Yes / Gap (client confirms) |
| SYS-009 | Partial / No / Gap: claim not supported | Yes / Not seen / Not tested | No / Yes / Gap (client confirms) | No / Yes / Gap (client confirms) | No / Yes / Gap (client confirms) |
| SYS-011 | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Not applicable | Yes / Yes / Pass |

### 13.2 Vendor review (processor contract, Sec 8(2)) *(verify)*

| Vendor | Contract | Security | Breach | Deletion | Result |
| --- | --- | --- | --- | --- | --- |
| VEN-001 StratoCloud | Yes | Yes | Yes | Yes | Pass |
| VEN-002 Poland subsidiary | Intra-group | Partial | No | No | Gap |
| VEN-004 PostBox Mail | Yes | Yes | Partial | Partial | Partial |
| VEN-005 ProctorView | Expires 2026-08 (expired by reference date) | Partial | No | No | Gap |
| VEN-009 BenchmarkBuyer | No contract | No | No | No | Gap |
| VEN-003, 006, 007, 008 | Yes | Yes | Yes | Yes or Partial | Pass |

### 13.3 Client-level duties

| Duty | Evidence | Result |
| --- | --- | --- |
| Help customer (fiduciary) report breaches within the required time | Runbook notifies customers within 24 hours by contract | Pass |
| Process only on documented customer instructions | Master agreement says so; GPS default and benchmarking go beyond | Partial |
| Delete data on customer instruction | Manual, undocumented; staging files remain | Gap |
| Help customer with rights requests | Support ticket route exists; no SLA | Partial |
| Children's data protections (campus) | No age check or parental step | Gap |
| Retention policy | POL-004 overdue | Partial |
| Cross-border (Poland, USA) | Recorded; Poland has no breach or deletion terms | Partial |
| Grievance route and notice for own fiduciary activities | Website notice outdated | Gap |

### 13.4 Activity-level duties

| Activity | Retention and deletion | Accuracy | Cross-border |
| --- | --- | --- | --- |
| ACT-001 | Default 7 years; manual deletion: Partial | Customer data accuracy is the customer's duty: note | Poland, USA recorded |
| ACT-004 | Raw files kept after go-live: Gap | Not applicable | None |
| ACT-005 | Indefinite: Gap | Not applicable | None |
| ACT-006 | Video 5 years with no reason: Gap | Test scores drive employer decisions: Partial | Proctoring vendor location unknown: Gap |

## 14. Data flow diagram: what it should show

| Feature | Where |
| --- | --- |
| Customer as source arrow | EXT-001 → DEP-003 for all processor activities (fiduciary on the left) |
| Arrows leaving India | SYS-001 → VEN-002 → SYS-009 (Poland); SYS-010 USA; VEN-005; VEN-006 |
| Role colouring | Processor activities (ACT-001 to 004) vs fiduciary activities (ACT-005 to 009) |
| Not sure | VEN-009, VEN-005 |
| Path with no end | VEN-009 onward sale |
| Child data tag | ACT-006 and ACT-001 for apprentices |
| Inventory but in no flow | None. Remove SYS-011 from ACT-001 to test the orphan check |

## 15. Edge cases the assessor should catch

1. Processor scope: Phase 3 says Out of scope, but Phase 4 still applies.
2. Role creep: a processor that reuses customer data for its own product becomes a fiduciary for that use.
3. "Anonymised" claims that do not hold for small groups.
4. Production data in a development office abroad with no masking.
5. Children's data in a service that only asks the student to tick a box.
6. Purchased lead lists as a source.
7. Customer-controlled defaults (GPS) that Halvorn should flag.
8. An expired contract with a proctoring vendor holding video of minors.
