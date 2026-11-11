# Client C: Brannock Auto Components Pvt Ltd (fictional demo client)

> **Fiction notice.** Brannock Auto Components and everything below is invented for training and demo use. Any resemblance to a real organisation is coincidence.
>
> **What this file is for.** Every detail needed to fill the workbooks end to end for a manufacturer with a large contract workforce, paper records, biometric attendance and foreign customers. IDs link across sections. Legal statements marked *(verify)* are working readings, not confirmed law.

## 0. Why this client is different

| Dimension | Brannock |
| --- | --- |
| Sector | Manufacturing and export (precision auto parts) |
| Model | B2B; sells to vehicle makers in India, Germany and Japan |
| Data | Mostly workforce data: biometrics, health, wages, CCTV; some foreign customers' staff data |
| Role pattern | Fiduciary for permanent staff; **joint fiduciary or separate fiduciary** with 14 labour contractors for contract workers; processor for one German customer's quality data |
| Law pattern | Paper-heavy (outside the Act where never digitised); exemption claims; foreign-contract exemption (Sec 17(1)(d)) *(verify)*; medical emergency and employment bases |
| Cross-border | Group parent in Germany receives staff reports; Japanese customer portal |
| Children | None employed; apprentices are 18+. A trap: one contractor employs 17-year-olds |
| Likely outcomes | 4 Supported, 2 Gap, 1 Gap: no legal basis, 1 Cannot conclude yet, 2 Out of scope |
| Special flag | Not an SDF candidate |

## 1. Snapshot

| Item | Detail |
| --- | --- |
| Legal name | Brannock Auto Components Pvt Ltd |
| Type | Private limited company; subsidiary of a German group (Brannock Holding GmbH) |
| Registered office | Chakan, Pune, Maharashtra |
| Plants | Chakan (main), Pithampur (Madhya Pradesh), a small unit in Hosur (Tamil Nadu) |
| Headcount | 1,900 permanent; 3,400 contract workers supplied by 14 labour contractors; 220 trainees |
| Customers | 11 vehicle makers and tier-one suppliers |
| Assessment reference date | 2026-11-10 |
| Engagement scope | India entity, all three plants. German parent assessed as recipient. |
| Client contacts | Head of Plant Operations, Head of HR and IR, IT Manager |
| DPO | None; the IT Manager is the informal privacy contact |
| SDF status | Not notified; not expected |

## 2. How the business works

1. Customers send orders and drawings; Brannock plans production and buys materials.
2. Permanent staff and contract workers enter the plant through biometric gates. Attendance feeds wages.
3. Contract workers are paid by their contractor; Brannock verifies identity and statutory registrations and keeps registers on paper.
4. The plant has CCTV on shop floors, gates and the canteen. A medical room serves all workers; health check-ups are periodic.
5. Visitors (suppliers, auditors, customers) sign a paper register and get a badge.
6. Quality and traceability data go to customers, including a German customer whose engineers' contact data and test logs are processed by Brannock.
7. Drivers and trucks are tracked by a transport vendor.
8. HR reports headcount and incident data to the German parent every month.

## 3. Departments

| ID | Department | Head | Headcount | Owns activities |
| --- | --- | --- | --- | --- |
| DEP-001 | HR and Industrial Relations | Head of HR and IR | 38 | ACT-001, ACT-003 |
| DEP-002 | Plant Operations | Head of Plant Operations | 600 | ACT-002 |
| DEP-003 | Contract Labour Management | Contract Labour Manager | 12 | ACT-004 |
| DEP-004 | Health, Safety and Medical | EHS Manager | 25 | ACT-005 |
| DEP-005 | Security and Administration | Security Manager | 70 (own and agency guards) | ACT-006, ACT-007 |
| DEP-006 | Quality and Customer Engineering | Head of Quality | 90 | ACT-008 |
| DEP-007 | Logistics and Transport | Logistics Manager | 45 | ACT-009 |
| DEP-008 | Finance and Payroll | CFO | 22 | ACT-010 |
| DEP-009 | IT | IT Manager | 14 | none (runs systems) |
| DEP-010 | Procurement and Supplier Management | Head of Procurement | 20 | ACT-011 |
| DEP-011 | Legal and Compliance | Company Secretary | 3 | none |

## 4. Other laws

| Item | Note |
| --- | --- |
| Factories law | Registers of workers, health records and accident records must be kept; check formats and retention *(verify)* |
| Contract labour law | Principal employer duties for contractor workers; registers *(verify)* |
| Wage and provident fund laws | Statutory registers and returns *(verify)* |
| Occupational health rules | Periodic medical check-ups for hazardous work *(verify)* |
| Customer and group agreements | German parent's group policy; customer data clauses |

## 5. Part A: entity checklist answers

| Ref | Answer | Reasoning |
| --- | --- | --- |
| E1 | Yes | Plants in India |
| E2 | No | Does not offer goods or services to individuals outside India |
| E3 | Mixed | Biometric, CCTV, payroll digital; gate registers, wage registers, visit forms and medical room cards are paper and never scanned. Paper that is never digitised is outside the Act's scope *(verify)*; scanned or typed-in copies are in scope |
| E4 | Yes | Brannock is the main entity; contractors are separate employers; parent is a recipient |
| E5 | No | |
| E6 | No | |
| E7 | Not notified | |
| E8 | No | |
| E9 | Not known | |
| E10 | Yes | Factories and labour regulators have record rules |
| E11 | Yes | Germany (parent), Japan (customer portal) |
| E12 | Yes | Personal data of a German customer's engineers is processed in India under a contract with that foreign customer; Sec 17(1)(d) may apply to this activity *(verify)* |
| E13 | Reference date 2026-11-10 | Most duties start about 13 May 2027 *(verify)* |

## 6. Inventory

### 6.1 Owners

| Client | Entity | Sponsor | Reference date |
| --- | --- | --- | --- |
| Brannock Auto Components Pvt Ltd | Brannock Auto Components Pvt Ltd | Head of HR and IR | 2026-11-10 |

### 6.2 System Inventory

| ID | Name | Type | Owner | Hosting | Location | Personal data? | Categories | Principals | Encryption | Backup | Logs | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SYS-001 | ERP with HR and payroll modules | Server | IT Manager | On-premises | Chakan, India | Yes | Staff identity, wages, bank, statutory IDs | Permanent staff, trainees | Partial | Yes - Daily | 1 year | |
| SYS-002 | Biometric attendance controllers | Endpoint | Security Manager | On-premises | Three plants | Yes | Fingerprint templates, face templates, attendance | Staff, contract workers | No | No | None | Templates on the device |
| SYS-003 | Attendance server | Database | IT Manager | On-premises | Chakan, India | Yes | Attendance, shift, overtime, fingerprint IDs | Staff, contract workers | Partial | Yes - Daily | Less than 1 year | |
| SYS-004 | CCTV recorders | Server | Security Manager | On-premises | Three plants | Yes | Video of workers, visitors, drivers | Workers, visitors, drivers | No | No | None | 90 days footage; two cameras in the canteen and one near a changing area |
| SYS-005 | Medical room records (digital part) | File share | EHS Manager | On-premises | Chakan, India | Yes | Health check results, vaccination, first-aid logs | Staff, contract workers | No | Yes - Weekly | None | Plus paper cards |
| SYS-006 | Contractor portal | Cloud service | Contract Labour Manager | Cloud | Pune, India | Yes | Contract worker lists, IDs, wages | Contract workers | Yes | Yes - Daily | 1 year | |
| SYS-007 | Quality and traceability system | Database | Head of Quality | On-premises | Chakan, India | Yes | Test logs with operator IDs; customer engineer contacts | Operators, customer engineers | Partial | Yes - Daily | 1 year | |
| SYS-008 | Customer portal (Japan, vendor-hosted) | Cloud service | Head of Quality | Cloud | Tokyo, Japan | Yes | Operator names on inspection reports | Operators | Yes | Yes - Daily | 1 year | |
| SYS-009 | Visitor management (paper plus tablet) | Paper-to-digital | Security Manager | On-premises | Three plants | Yes | Visitor name, phone, ID, photo | Visitors | No | No | None | Paper register is the master; tablet photos for key visitors |
| SYS-010 | Vehicle tracking platform | Cloud service | Logistics Manager | Cloud | Mumbai, India | Yes | Driver ID, GPS trail, behaviour scores | Drivers | Yes | Yes - Daily | 1 year | |
| SYS-011 | Group reporting file share | Cloud service | Head of HR and IR | Cloud | Frankfurt, Germany | Yes | Monthly headcount, incidents, attrition | Staff | Yes | Yes - Daily | 1 year | Leaves India |
| SYS-012 | Gate and wage registers (paper) | Paper | Head of HR and IR | On-premises | Three plants | Yes | Entry, wages, overtime | Staff, contract workers | Not applicable | Not applicable | None | Never digitised |
| SYS-013 | Supplier portal | Cloud service | Head of Procurement | Cloud | Mumbai, India | Yes | Supplier contact persons, bank details of sole proprietors | Supplier contacts | Yes | Yes - Daily | 1 year | |

### 6.3 Application Inventory

| ID | Name | Purpose | Owner | Hosted on | Vendor | Personal data? |
| --- | --- | --- | --- | --- | --- | --- |
| APP-001 | ERP HR module | Records and leave | Head of HR and IR | SYS-001 | VEN-001 | Yes |
| APP-002 | Payroll module | Wages | CFO | SYS-001 | VEN-001 | Yes |
| APP-003 | Biometric attendance software | Gate access, attendance | Security Manager | SYS-002, SYS-003 | VEN-002 | Yes |
| APP-004 | CCTV management | Viewing and storage | Security Manager | SYS-004 | VEN-003 | Yes |
| APP-005 | Medical module | Check-up tracking | EHS Manager | SYS-005 | none | Yes |
| APP-006 | Contractor portal | Compliance uploads | Contract Labour Manager | SYS-006 | VEN-004 | Yes |
| APP-007 | Quality system | Traceability | Head of Quality | SYS-007 | VEN-005 | Yes |
| APP-008 | Customer inspection portal | Report sharing | Head of Quality | SYS-008 | VEN-006 | Yes |
| APP-009 | Visitor tablet app | Visitor badges | Security Manager | SYS-009 | VEN-007 | Yes |
| APP-010 | Fleet tracking app | Vehicle and driver tracking | Logistics Manager | SYS-010 | VEN-008 | Yes |
| APP-011 | Supplier portal | Onboarding suppliers | Head of Procurement | SYS-013 | VEN-009 | Yes |

### 6.4 Vendor List

| ID | Name | Service | Role | Personal data? | Data shared | Location | Contract | Security | Breach | Deletion | Sub-processors | Dates | Owner | Last review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VEN-001 | TerraERP Solutions | ERP support and hosting maintenance | Processor | Yes | All HR and payroll data | India | Yes | Partial | No | No | Unknown | 2021-04 to 2027-03 | IT Manager | Never |
| VEN-002 | BioGate Systems | Biometric hardware and software | Processor | Yes | Fingerprint and face templates | India | Yes | Partial | No | No | No | 2022-01 to 2026-12 | Security Manager | 2024-05 |
| VEN-003 | SentinelView | CCTV maintenance | Processor | Yes | Video access | India | Expired | No | No | No | No | 2020-05 to 2023-04 | Security Manager | Never |
| VEN-004 | ContractorDesk | Portal SaaS | Processor | Yes | Contract worker data | India | Yes | Yes | Yes | Yes | No | 2025-02 to 2027-01 | Contract Labour Manager | 2026-04 |
| VEN-005 | TraceLogic | Quality software | Processor | Yes | Operator IDs, engineer contacts | India | Yes | Yes | Partial | Partial | No | 2023-09 to 2027-08 | Head of Quality | 2025-10 |
| VEN-006 | Nippon Inspect Net | Customer portal | Other | Yes | Operator names | Outside India | Yes (customer terms) | Partial | No | No | Unknown | 2024-01 to open | Head of Quality | Never |
| VEN-007 | GateTab | Visitor tablets | Processor | Yes | Visitor details | India | Yes | Yes | Partial | Yes | No | 2025-06 to 2027-05 | Security Manager | 2026-01 |
| VEN-008 | RoadTrace | Fleet tracking | Processor | Yes | Driver ID, GPS | India | Yes | Yes | Yes | Yes | No | 2024-11 to 2027-10 | Logistics Manager | 2026-03 |
| VEN-009 | SupplyBridge | Supplier portal | Processor | Yes | Supplier contacts | India | Yes | Yes | Yes | Yes | No | 2025-03 to 2027-02 | Head of Procurement | 2026-05 |
| VEN-010 | Brannock Holding GmbH (parent) | Group reporting | Other | Yes | Monthly staff reports | Outside India | Intra-group | Partial | No | No | Not applicable | 2019 | Head of HR and IR | Never |
| VEN-011 to VEN-024 | 14 labour contractors (e.g. Apex Manpower, Ridgeline Staffing) | Supply of contract workers | **Joint fiduciary (to be decided)** | Yes | Worker identity, wages, medical fitness | India | Yes for 9; Expired for 3; None for 2 | Partial | No | No | Unknown | Various | Contract Labour Manager | Never |
| VEN-025 | MedCare Occupational Health | Visiting doctor and periodic check-ups | Processor | Yes | Check-up results | India | Yes | Partial | No | Partial | No | 2023-01 to 2026-12 | EHS Manager | 2024-11 |
| VEN-026 | Securenet Guard Services | Guards (agency staff) | Processor | Yes | Visitor register access, CCTV viewing | India | Yes | No | No | No | No | 2022-08 to 2026-07 (expired) | Security Manager | Never |

### 6.5 Security Controls

| ID | Name | Category | Applies to | Implemented | What is done | Owner | Evidence | Last reviewed | Rule 6 item | Gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CTL-001 | ERP user roles | Access control | SYS-001 | Yes | Roles per department | IT Manager | Yes | 2026-05 | Access control | |
| CTL-002 | Fingerprint template encryption | Encryption | SYS-002 | No | Templates stored in plain form on devices | Security Manager | No | Never | Encryption or masking | Biometric data unprotected |
| CTL-003 | CCTV access list | Access control | SYS-004 | Partial | Security office has access; agency guards share one login | Security Manager | Partial | 2025-10 | Access control | Shared login |
| CTL-004 | CCTV overwrite after 90 days | Retention | SYS-004 | Yes | Automatic overwrite | Security Manager | Yes | 2026-08 | Measures to follow safeguards | Footage kept for incidents indefinitely |
| CTL-005 | ERP database backup | Backup | SYS-001, SYS-003 | Yes | Nightly tape; off-site monthly | IT Manager | Yes | 2026-06 | Backup and continuity | |
| CTL-006 | Medical records lock | Access control | SYS-005 | Partial | Share open to EHS team of 25; paper cards in an unlocked cabinet | EHS Manager | No | Never | Access control | |
| CTL-007 | Log retention | Logging | SYS-001 | Partial | 6 months | IT Manager | Yes | 2026-05 | Log retention | Less than 1 year |
| CTL-008 | Visitor register custody | Physical | SYS-009, SYS-012 | Partial | Register at the gate; old volumes in a store room | Security Manager | Partial | Never | Access control | |

### 6.6 Policy Inventory

| ID | Policy | Owner | Version | Approved | Review due |
| --- | --- | --- | --- | --- | --- |
| POL-001 | IT security | IT Manager | 2.0 | 2023-02 | 2024-02 (overdue) |
| POL-002 | CCTV policy | Security Manager | 1.0 | 2021-07 | 2022-07 (overdue) |
| POL-003 | Biometric attendance policy | Head of HR and IR | 1.1 | 2022-03 | 2023-03 (overdue) |
| POL-004 | Record retention schedule | Company Secretary | 3.0 | 2025-04 | 2026-04 (overdue) |
| POL-005 | Contract labour compliance | Contract Labour Manager | 2.0 | 2026-01 | 2027-01 |
| POL-006 | Medical and first-aid | EHS Manager | 1.4 | 2024-09 | 2025-09 (overdue) |
| POL-007 | Group data protection (from parent) | Company Secretary | 1.0 | 2023-05 | 2026-05 (overdue) |

## 7. Flow Nodes (not in the Inventory)

| ID | Name | Type | Zone | Country |
| --- | --- | --- | --- | --- |
| DP-001 | Permanent staff | Data principal | Data principal | India |
| DP-002 | Contract workers | Data principal | Data principal | India |
| DP-003 | Trainees and apprentices | Data principal | Data principal | India |
| DP-004 | Visitors | Data principal | Data principal | India |
| DP-005 | Drivers (own and hired) | Data principal | Data principal | India |
| DP-006 | Supplier contact persons | Data principal | Data principal | India |
| DP-007 | Customer engineers (German customer) | Data principal | Data principal | Germany |
| DP-008 | Job applicants | Data principal | Data principal | India |
| DEP-001 to DEP-011 | As in section 3 | Department | Client premises | India |
| EXT-001 | Provident fund and ESI bodies | External party | Other organisation (India) | India |
| EXT-002 | Factory inspector and labour authorities | External party | Other organisation (India) | India |
| EXT-003 | Tax authorities | External party | Other organisation (India) | India |
| EXT-004 | Police | External party | Other organisation (India) | India |
| EXT-005 | Insurance company (group medical) | External party | Other organisation (India) | India |
| EXT-006 | German customer (fiduciary for DP-007) | External party | Outside India | Germany |
| EXT-007 | Group parent HR | External party | Outside India | Germany |

## 8. Processing activities (ROPA)

Common values: Last updated 2026-11-07. Owner contact = department head. Children's data = No unless stated.

### ACT-001 Permanent staff HR and payroll
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary |
| Department | HR and Industrial Relations |
| Purpose | Hire, pay and manage permanent staff and trainees |
| Legal basis claimed | 7(i) Employment |
| Data principals | Permanent staff, trainees, job applicants |
| Source | From the person; background check agency |
| Internal | HR (DEP-001), Finance (DEP-008) |
| External | VEN-001, EXT-001, EXT-003, EXT-005 |
| Retention | Employment plus 8 years |
| Security | CTL-001, CTL-005, CTL-007 |
| Cross-border | No |
| Consent status | Not applicable |
| Systems and apps | SYS-001; APP-001, APP-002 |
| Shared outside the client | Yes |

### ACT-002 Biometric attendance and gate access
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary |
| Department | Plant Operations (system owned by Security) |
| Purpose | Record entry, hours and overtime and control plant access |
| Legal basis claimed | 7(i) Employment |
| Data principals | Permanent staff, contract workers, trainees |
| Source | From the person |
| Internal | Plant Operations (DEP-002), HR (DEP-001), Finance (DEP-008) |
| External | VEN-002 BioGate |
| Retention | Templates kept after the worker leaves; attendance 8 years |
| Security | CTL-002 (not implemented) |
| Cross-border | No |
| Consent status | Not captured (workers told at joining) |
| Systems and apps | SYS-002, SYS-003; APP-003 |
| Used to decide about the person | Yes (wage deductions for late entry) |
| Shared outside the client | Yes |

### ACT-003 Employee welfare, canteen and group reporting
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary |
| Department | HR and Industrial Relations |
| Purpose | Send monthly staff reports to the German parent |
| Legal basis claimed | "Group requirement" |
| Data principals | Permanent staff |
| Source | From the person |
| External | EXT-007 / VEN-010 Parent (outside India) |
| Retention | Not defined |
| Cross-border | Yes: Germany |
| Consent status | Not captured |
| Systems and apps | SYS-011; APP-001 |
| Shared outside the client | Yes |

### ACT-004 Contract labour management
| Field | Value |
| --- | --- |
| Our role | Not sure: Brannock as principal employer and the 14 contractors each decide parts of the purpose. Record as **Joint Data Fiduciary (to be decided)** |
| Department | Contract Labour Management |
| Purpose | Verify contract workers' identity, registration and wages; keep statutory registers |
| Legal basis claimed | 7(i) Employment for staff; for contract workers "we are not their employer" |
| Data principals | Contract workers (including 17-year-olds at one contractor: children's data = Yes) |
| Source | From a third party (contractors) |
| Internal | Contract Labour (DEP-003), HR (DEP-001), Plant Operations (DEP-002) |
| External | VEN-004, contractors VEN-011 to VEN-024, EXT-002 |
| Retention | Not defined; registers kept indefinitely |
| Security | CTL-008 (paper) |
| Cross-border | No |
| Consent status | Not captured |
| Systems and apps | SYS-006, SYS-012; APP-006 |
| Shared outside the client | Yes |

### ACT-005 Occupational health and medical room
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary |
| Department | Health, Safety and Medical |
| Purpose | Fitness checks, first aid and medical emergencies |
| Legal basis claimed | 7(f) Medical emergency for first aid; "legal duty" for periodic check-ups |
| Data principals | Permanent staff, contract workers, visitors (first aid) |
| Source | From the person; VEN-025 doctor |
| External | VEN-025, EXT-002, EXT-005 |
| Retention | Not defined; paper cards indefinitely |
| Security | CTL-006 |
| Cross-border | No |
| Consent status | Not captured |
| Systems and apps | SYS-005 |
| Shared outside the client | Yes |

### ACT-006 CCTV and site security
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary |
| Department | Security and Administration |
| Purpose | Prevent theft and safety incidents; investigate incidents |
| Legal basis claimed | "Safety and security" (no Sec 7 clause named) |
| Data principals | Staff, contract workers, visitors, drivers |
| Source | From the person (captured) |
| Internal | Security (DEP-005), HR (DEP-001) for disciplinary reviews |
| External | VEN-003 (contract expired), VEN-026 guards, EXT-004 police |
| Retention | 90 days automatic; incident footage kept indefinitely |
| Security | CTL-003, CTL-004 |
| Cross-border | No |
| Consent status | Not captured; signage at gates only |
| Systems and apps | SYS-004; APP-004 |
| Shared outside the client | Yes |
| Walkthrough | Two canteen cameras and one near a changing area. Footage clips shared on a WhatsApp group of supervisors. |

### ACT-007 Visitor management
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary |
| Department | Security and Administration |
| Purpose | Record who enters the plant |
| Legal basis claimed | 7(a) Voluntarily provided |
| Data principals | Visitors |
| Source | From the person |
| External | VEN-007, VEN-026 |
| Retention | Paper register volumes kept indefinitely |
| Security | CTL-008 |
| Consent status | Not applicable |
| Systems and apps | SYS-009, SYS-012; APP-009 |
| Shared outside the client | No |
| Walkthrough | Paper register in full view at the gate shows previous visitors' names and phone numbers. Tablet photos only for key visitors. |

### ACT-008 Customer quality data (German customer)
| Field | Value |
| --- | --- |
| Our role | **Data Processor** for the German customer's engineers' data; Data Fiduciary for own operators' names on reports |
| Department | Quality and Customer Engineering |
| Purpose | Share inspection reports and traceability data with customers; hold the German customer's engineer contacts under its contract |
| Legal basis claimed | Contract |
| Data principals | Customer engineers (Germany), operators (India) |
| Source | From the customer (engineers); both (operators) |
| External | EXT-006 German customer, VEN-006 Japan portal (outside India), VEN-005 |
| Retention | 15 years for traceability (customer requirement) |
| Cross-border | Yes: Germany, Japan |
| Consent status | Not applicable |
| Systems and apps | SYS-007, SYS-008; APP-007, APP-008 |
| Shared outside the client | Yes |

### ACT-009 Driver and fleet tracking
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary |
| Department | Logistics and Transport |
| Purpose | Track vehicles and driver safety scores |
| Legal basis claimed | Consent (drivers sign a form) |
| Data principals | Drivers (own and hired) |
| Source | From the person |
| External | VEN-008 RoadTrace |
| Retention | 3 years |
| Cross-border | No |
| Consent status | Active (signed form, but form is in English only; withdrawal not described) |
| Systems and apps | SYS-010; APP-010 |
| Used to decide about the person | Yes (driver scores affect pay) |
| Shared outside the client | Yes |

### ACT-010 Wage payments and statutory returns
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary |
| Department | Finance and Payroll |
| Purpose | Pay wages and file returns |
| Legal basis claimed | 7(d) Legal duty to disclose to the State |
| Data principals | Permanent staff, contract workers (muster data) |
| Source | From the person and from contractors |
| External | EXT-001, EXT-002, EXT-003, bank |
| Retention | 8 years |
| Cross-border | No |
| Systems and apps | SYS-001, SYS-012; APP-002 |
| Shared outside the client | Yes |

### ACT-011 Supplier onboarding
| Field | Value |
| --- | --- |
| Our role | Data Fiduciary |
| Department | Procurement and Supplier Management |
| Purpose | Onboard and pay suppliers, including sole proprietors |
| Legal basis claimed | Consent |
| Data principals | Supplier contact persons |
| Source | From the person |
| External | VEN-009 |
| Retention | 7 years after last order |
| Cross-border | No |
| Consent status | Active |
| Systems and apps | SYS-013; APP-011 |
| Shared outside the client | No |

## 9. Activity Data

D2 public, D3 child's data, D4 used to decide about the person, D7 leaves India.

| Activity | Elements |
| --- | --- |
| ACT-001 | DE-ID-001; DE-ID-002; DE-ID-004; DE-ID-005; DE-ID-009; DE-CON-001; DE-CON-003; DE-CON-004-A; DE-CON-004-B; DE-GOV-001 Aadhaar number; DE-GOV-003 PAN; DE-GOV-009-A UAN; DE-GOV-009-B PF; DE-GOV-009-C ESIC; DE-FIN-001-A; DE-FIN-004; DE-EMP-001-A, -B, -C; DE-EMP-002; DE-EMP-004; DE-EMP-006; DE-EMP-007-A, -B; DE-EMP-009; DE-EMP-010; DE-EMP-011; DE-EMP-013-A Exit; DE-HLT-018 Pre-employment medical exam; DE-HLT-019 Sick-leave certificate; DE-SEN-006 Police verification; DE-FAM-001-A Dependant; DE-FAM-002 Nominee; DE-EDU-001; DE-EDU-005 Training |
| ACT-002 | DE-ID-001; DE-ID-009; DE-ID-004; DE-BIO-001 Fingerprint (D4); DE-BIO-002 Face template (D4); DE-EMP-004 Attendance (D4); DE-EMP-015 Shift and overtime (D4); DE-AUT-004 Access card or badge ID |
| ACT-003 | DE-ID-009; DE-EMP-001-A; DE-EMP-004; DE-EMP-003 Performance (D7); DE-EMP-005 Disciplinary (D7); DE-EMP-013-B Attrition reason (D7); DE-HLT-022 Medical room visits (D7); DE-EMP-007-A (D7) |
| ACT-004 | DE-ID-001; DE-ID-002 (D3 for 17-year-olds); DE-ID-004; DE-GOV-001; DE-GOV-009-A; DE-GOV-009-C; DE-FIN-001-A; DE-FIN-004; DE-HLT-010 Fitness certificate; DE-EMP-001-A; DE-EMP-004; DE-EMP-006 |
| ACT-005 | DE-ID-001; DE-ID-009; DE-ID-002; DE-HLT-010; DE-HLT-018; DE-HLT-022; DE-HLT-019; DE-HLT-001 (health check results); DE-EMP-004 |
| ACT-006 | DE-AV-001 CCTV footage; DE-ID-001 (when identified); DE-ID-004; DE-EMP-005 Disciplinary (when footage is used) |
| ACT-007 | DE-ID-013-A Visitor name; DE-ID-013-B Visitor phone; DE-ID-013-C Visitor ID proof; DE-AV-006 Visitor photo; DE-CON-006-A |
| ACT-008 | DE-ID-001; DE-CON-006-A Business email (D7); DE-CON-006-B Business phone (D7); DE-EMP-001-A Job title (D7); DE-ID-009 Operator ID |
| ACT-009 | DE-ID-001; DE-ID-009; DE-EMP-018-A Driver licence; DE-EMP-018-B Driver verification; DE-LOC-001 Precise GPS; DE-VEH-001 Telematics (D4); DE-DEV-002-A |
| ACT-010 | DE-ID-001; DE-ID-009; DE-GOV-003; DE-GOV-009-A, -B, -C; DE-FIN-001-A, -B; DE-FIN-004; DE-EMP-004; DE-EMP-015; DE-FIN-008 |
| ACT-011 | DE-ID-001; DE-CON-006-A; DE-CON-006-B; DE-GOV-003 (sole proprietors); DE-FIN-001-A; DE-FIN-001-B |

## 10. Data Flow

| Activity | Rows |
| --- | --- |
| ACT-001 | DP-001 Yes → DEP-001; DP-008 Yes → DEP-001; DEP-001 Yes → APP-001; APP-001 Yes → SYS-001, VEN-001; SYS-001 Yes → DEP-008, EXT-001, EXT-003, EXT-005; VEN-001 Not sure → (sub-processors unknown) |
| ACT-002 | DP-001, DP-002 Yes → APP-003; APP-003 Yes → SYS-002, VEN-002; SYS-002 Yes → SYS-003; SYS-003 Yes → SYS-001; SYS-001 No; VEN-002 No |
| ACT-003 | DEP-001 Yes → SYS-011 (monthly file); SYS-011 Yes → EXT-007; EXT-007 Not sure → (onward group use) |
| ACT-004 | VEN-011 to VEN-024 Yes → APP-006; APP-006 Yes → SYS-006; SYS-006 Yes → DEP-003; DEP-003 Yes → SYS-012 (printed registers), DEP-001, EXT-002; DEP-002 Yes → DEP-003 (muster); SYS-012 No |
| ACT-005 | DP-001, DP-002 Yes → DEP-004; DEP-004 Yes → SYS-005, VEN-025; VEN-025 Yes → EXT-005; SYS-005 No; paper cards: DEP-004 Yes → paper store (SYS-012 location) |
| ACT-006 | DP-001, DP-002, DP-004, DP-005 Yes → SYS-004; SYS-004 Yes → APP-004; APP-004 Yes → DEP-005, VEN-003, VEN-026; DEP-005 Yes → DEP-001, EXT-004; side channel: DEP-005 Yes → EXT-008 "Supervisors' WhatsApp group" (outside India) |
| ACT-007 | DP-004 Yes → SYS-012 (paper register); SYS-012 Yes → DEP-005; DP-004 Yes → APP-009; APP-009 Yes → SYS-009, VEN-007; VEN-026 Yes → SYS-012 (guards read register) |
| ACT-008 | EXT-006 Yes → DEP-006 (engineer contacts); DEP-006 Yes → SYS-007; SYS-007 Yes → APP-008; APP-008 Yes → VEN-006 (Japan), EXT-006; VEN-006 Not sure → (customer portal sub-processors) |
| ACT-009 | DP-005 Yes → APP-010; APP-010 Yes → SYS-010; SYS-010 Yes → VEN-008, DEP-007; DEP-007 Yes → DEP-008 (pay effect) |
| ACT-010 | SYS-001 Yes → DEP-008; DEP-008 Yes → EXT-001, EXT-003; bank EXT-009 Yes ← DEP-008; SYS-012 Yes → DEP-008 (muster) |
| ACT-011 | DP-006 Yes → APP-011; APP-011 Yes → SYS-013; SYS-013 Yes → DEP-010; DEP-010 No |

Add nodes: EXT-008 Supervisors' WhatsApp group (Outside India), EXT-009 Banks (Other organisation, India).

## 11. Hidden processing the walkthrough should surface

| What | Where | Effect |
| --- | --- | --- |
| Fingerprint templates stored unencrypted and kept after exit | ACT-002 | High-risk biometric data, retention gap |
| Canteen and changing-area cameras | ACT-006 | Over-collection; dignity concern; purpose test fails |
| CCTV clips in WhatsApp groups | ACT-006 | Uncontrolled sharing, outside India servers |
| Paper registers that are never digitised | SYS-012 | Possibly outside the Act; confirm they are never typed or scanned |
| Visitors' details visible on open register | ACT-007 | Exposure by physical access |
| 17-year-olds at one contractor | ACT-004 | Children's data; legality of employment itself needs separate check *(verify)* |
| Contractors with no or expired agreements | ACT-004 | No clarity on who is fiduciary |
| Operator names on reports in the Japan portal | ACT-008 | Cross-border; no basis recorded |
| Medical room health data open to 25 staff | ACT-005 | Access control gap |

## 12. Phase 3 expected review

| Activity | Route | Tests not Yes | Expected outcome | Why |
| --- | --- | --- | --- | --- |
| ACT-001 | Legitimate use 7(i) | L4 Not applicable | Supported | None |
| ACT-002 | Legitimate use 7(i) | L2 No (fingerprint and face are more than attendance needs; element E1 No for DE-BIO-002) ; L3 Not sure | Gap | L2; Element Check on DE-BIO-002 |
| ACT-003 | None identified | R1 No ("group requirement" is not a ground) | Gap: no legal basis | R1 |
| ACT-004 | Legitimate use 7(i) for staff; role undecided | L1 Not sure (role); C9 children not tested for this route | Cannot conclude yet | Role of contractor vs principal unresolved; children test open |
| ACT-005 | Legitimate use 7(f) for first aid; 7(i) for periodic check-ups | All Yes for first aid; L4 Not applicable | Supported | None; note access and retention for Phase 4 |
| ACT-006 | Exemption only (Sec 17(1)(c)? not clearly) *(verify)* | X1 No (canteen and changing-area cameras not needed for the purpose); X2 Yes; X3 Not sure | Gap | X1 |
| ACT-007 | Legitimate use 7(a) | L1 Yes; L4 Yes | Supported | None; paper register may be out of scope but tablet photos are in |
| ACT-008 | Out of scope (processor for German customer; foreign principals under foreign contract, Sec 17(1)(d)) | | Out of scope | Foreign-contract exemption; the Indian operators' names on reports are split into ACT-008b |
| ACT-008b | Legitimate use 7(i) | L4 Not applicable | Supported | Operators' names on inspection reports |
| ACT-009 | Consent | C4 Not sure (form in English only); C8 No (withdrawal not described); C10 Not applicable | Gap | C8 |
| ACT-010 | Legitimate use 7(d) | L4 Not applicable | Supported | None |
| ACT-011 | Consent | C1 Yes; C5 Yes; all Yes | Supported | None. Sole proprietors only |

Totals: Supported 4 (ACT-001, 005, 007, 010) plus ACT-008b and ACT-011 (6 in the full list); Gap 3 (ACT-002, 006, 009); Gap: no legal basis 1 (ACT-003); Cannot conclude yet 1 (ACT-004); Out of scope 1 (ACT-008). For a smaller demo, drop ACT-008b and ACT-011 and the counts become 4 Supported, 3 Gap, 1 no basis, 1 Cannot conclude, 1 Out of scope.

### Findings to log

| ID | Activity | Finding |
| --- | --- | --- |
| LB-001 | ACT-002 | Face template collected as well as fingerprint with no added need |
| LB-002 | ACT-003 | Group reporting to the parent has no stated basis; likely needs consent or aggregated data only |
| LB-003 | ACT-004 | Fiduciary role split between Brannock and 14 contractors is not settled |
| LB-004 | ACT-006 | Canteen and changing-area cameras |
| LB-005 | ACT-009 | Consent form is not understood by many drivers and has no withdrawal route |

## 13. Phase 4 expected checks

### 13.1 System security

| System | (a) Encryption | (b) Access | (c) Logs | (d) Backup | (e) Log retention 12 months+ |
| --- | --- | --- | --- | --- | --- |
| SYS-001 | Partial / Partial / Partial | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | No (6 months) / Yes / Gap (client confirms) |
| SYS-002 | No / Yes / Gap (client confirms) | Partial / No / Gap: claim not supported | No / Yes / Gap (client confirms) | No / Yes / Gap (client confirms) | No / Yes / Gap (client confirms) |
| SYS-003 | Partial / Not seen / Not tested | Yes / Yes / Pass | Yes / Partial / Partial | Yes / Yes / Pass | No / Yes / Gap (client confirms) |
| SYS-004 | No / Yes / Gap (client confirms) | Partial (shared login) / Yes / Gap (client confirms) | No / Yes / Gap (client confirms) | No / Yes / Gap (client confirms) | No / Yes / Gap (client confirms) |
| SYS-005 | No / Yes / Gap (client confirms) | Partial / No / Gap: claim not supported | No / Yes / Gap (client confirms) | Yes / Yes / Pass | No / Yes / Gap (client confirms) |
| SYS-006 | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass |
| SYS-010 | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass |
| SYS-012 (paper) | Not applicable | Partial (old volumes in store room) / Partial / Partial | Not applicable | Not applicable | Not applicable |

### 13.2 Vendor review

| Vendor | Contract | Security | Breach | Deletion | Result |
| --- | --- | --- | --- | --- | --- |
| VEN-001 TerraERP | Yes | Partial | No | No | Gap; sub-processors unknown |
| VEN-002 BioGate | Yes (expiring 2026-12) | Partial | No | No | Gap; biometric data |
| VEN-003 SentinelView | Expired | No | No | No | Gap |
| VEN-006 Nippon Inspect | Customer terms | Partial | No | No | Gap; outside India |
| VEN-010 Parent | Intra-group | Partial | No | No | Gap |
| VEN-011 to 024 (14 contractors) | 9 Yes, 3 Expired, 2 None | Partial | No | No | Gap; 5 have no valid contract |
| VEN-025 MedCare | Yes (expiring 2026-12) | Partial | No | Partial | Partial |
| VEN-026 Securenet | Expired | No | No | No | Gap |
| VEN-004, 005, 007, 008, 009 | Yes | Yes | Yes or Partial | Yes or Partial | Pass |

### 13.3 Client-level duties

| Duty | Evidence | Result |
| --- | --- | --- |
| Breach reporting (72 hours) | No process; IT Manager informal | Gap |
| Notice in plain language, including Hindi and Marathi | Gate signage in English only | Gap |
| Rights handling | None; grievances go to HR | Gap |
| Contact for questions | IT Manager informal | Partial |
| Retention schedule applied | POL-004 overdue; not applied to CCTV incidents, biometrics, paper registers | Gap |
| Log retention 1 year | 6 months on ERP; none elsewhere | Gap |
| Children's data (17-year-olds at contractor) | Contractor says "age checked by Aadhaar"; not verified | Not tested |
| Processor duties as processor for the German customer | Contract exists; no security audit done | Partial |

### 13.4 Activity-level duties

| Activity | Retention and deletion | Accuracy | Cross-border |
| --- | --- | --- | --- |
| ACT-002 | Templates kept after exit: Gap | Failed matches cause wage deductions with no review: Gap | None |
| ACT-004 | Registers indefinite: Gap | Contractor data not verified: Partial | None |
| ACT-005 | Paper cards indefinite: Gap | Not applicable | None |
| ACT-006 | Incident footage indefinite: Gap | Not applicable | None |
| ACT-003 | Not defined: Gap | Not applicable | Germany: recorded but no terms |
| ACT-008 | 15 years by customer requirement: Pass | Pass | Germany, Japan: recorded |

## 14. Data flow diagram: what it should show

| Feature | Where |
| --- | --- |
| Paper zones | SYS-012 and the paper medical cards shown as "Paper (outside the Act unless digitised)" |
| Arrows leaving India | SYS-011 to EXT-007 (Germany); VEN-006 (Japan); WhatsApp EXT-008 |
| Foreign principal | DP-007 customer engineers in Germany |
| Not sure | VEN-001 sub-processors, VEN-006 sub-processors, EXT-007 onward use |
| Role colouring | ACT-008 processor; ACT-004 undecided; rest fiduciary |
| Child data tag | ACT-004 |
| High-risk data | Biometric on ACT-002; health on ACT-005 |
| Inventory but in no flow | SYS-013 would be orphaned if ACT-011 is removed; test the check |

## 15. Edge cases the assessor should catch

1. Paper that is never digitised sits outside the Act; the assessor must check whether it is ever typed, scanned or photographed.
2. Role split with labour contractors: who is the fiduciary for contract workers?
3. Biometric data collected beyond what attendance needs.
4. Cameras in places that serve no stated purpose.
5. "Group requirement" and "we are not their employer" are not grounds.
6. Foreign customer's staff data processed under a foreign contract: likely outside most duties *(verify)*, but operators' names are separate.
7. Consent forms that exist but are not understood or withdrawable.
8. Under-18 workers at a contractor.
9. Legal duty (7(d)) used properly for wage returns, compared with Client A's misuse.
