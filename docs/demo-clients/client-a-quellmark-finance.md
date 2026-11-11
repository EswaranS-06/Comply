# Client A: Quellmark Finance Ltd (fictional demo client)

> **Fiction notice.** Quellmark Finance, every person, vendor, system and number below is invented for training and demo use. Any resemblance to a real organisation is coincidence. Do not mix this file with real client data.
>
> **What this file is for.** It holds every detail needed to fill the workbooks end to end: Organisation Profile, Inventory, ROPA, Activity Data, Data Flow, Phase 3 Legal Basis Review and Phase 4 Duties checks. IDs link across sections. Legal statements marked *(verify)* are working readings, not confirmed law.

## 0. Why this client is different

| Dimension | Quellmark |
| --- | --- |
| Sector | Regulated financial services (digital lending NBFC) |
| Model | B2C, app-first, very high volume, partners and agents bring in customers |
| Data | Financial and government ID heavy; credit scoring on behaviour data |
| Role pattern | Data Fiduciary for almost everything; **joint fiduciary** with a co-lending bank for one activity |
| Law pattern | Another regulator's rules (RBI) overlap; a "legal duty so no consent" belief that the Act does not support *(verify)* |
| Cross-border | Scoring vendor in Singapore and Ireland, marketing in Ireland, support in the USA, email in Germany |
| Likely outcomes | Mixed: 4 Supported, 5 Gap, 1 Gap: no legal basis, 1 Cannot conclude yet |
| Special flag | Possible Significant Data Fiduciary (not notified at the reference date) |

## 1. Snapshot

| Item | Detail |
| --- | --- |
| Legal name | Quellmark Finance Ltd |
| Type | Public limited company; RBI-registered non-banking finance company *(verify classification layer)* |
| Group | Wholly owned subsidiary: Quellmark Technology Services Pvt Ltd (separate legal entity; builds the app and data platform) |
| Registered office | Andheri East, Mumbai, Maharashtra |
| Other sites | Operations centre in Hyderabad; five collection hubs (Pune, Jaipur, Lucknow, Kochi, Bhopal) |
| Headcount | 740 employees; about 310 recovery agents supplied by an agency (not on payroll) |
| Customers | About 4.2 million registered users; 1.1 million active loans |
| Products | Personal loans, salary advance, credit line through partner platforms, co-lent loans |
| Channels | Own Android and iOS app, website, 40 direct selling agents, three partner platforms |
| Assessment reference date | 2026-11-10 |
| Engagement scope | Whole entity. Subsidiary assessed as a vendor only; it needs its own Part A if it decides purposes. |
| Client contacts | Head of Compliance (sponsor), CISO, Head of Credit, Head of Collections |
| DPO | None appointed. Grievance Officer published for RBI purposes. |
| SDF status | Not notified at the reference date. Volume and sensitivity make it a candidate; track the notification. |

## 2. How the business works

1. A person downloads the app and signs up with mobile number and OTP.
2. The app asks for permissions (SMS, contacts, location) and shows one combined consent screen.
3. The person completes e-KYC (Aadhaar offline XML or PAN plus selfie liveness) and, for some loan sizes, a video KYC call.
4. The credit scoring platform (run by a vendor outside India) scores the person from bureau data, bank statement data and device data, and returns an offer.
5. The person accepts, signs electronically and sets up an auto-debit mandate.
6. The loan is disbursed. Statements and reminders go by SMS, WhatsApp and email.
7. If a payment is missed, the collections team and an outsourced agency call the borrower, references and sometimes the employer, and make field visits.
8. Marketing sends offers for top-up loans using inferred segments.
9. Reports go to RBI, the Financial Intelligence Unit and the credit bureaus on a schedule.

## 3. Departments

| ID | Department | Head title | Headcount | Owns activities |
| --- | --- | --- | --- | --- |
| DEP-001 | Customer Onboarding and KYC | Head of Onboarding | 60 | ACT-001, ACT-011 |
| DEP-002 | Credit and Underwriting | Chief Credit Officer | 85 | ACT-002 |
| DEP-003 | Loan Operations | Head of Operations | 120 | ACT-003, ACT-005 |
| DEP-004 | Collections and Recovery | Head of Collections | 140 | ACT-004 |
| DEP-005 | Customer Support | Head of Support | 95 | ACT-008 |
| DEP-006 | Marketing and Growth | Chief Marketing Officer | 40 | ACT-007 |
| DEP-007 | Partnerships and Co-lending | Head of Partnerships | 25 | ACT-009 |
| DEP-008 | Compliance, Risk and Audit | Head of Compliance | 30 | ACT-006 |
| DEP-009 | Legal | General Counsel | 12 | none (supports ACT-004, ACT-006) |
| DEP-010 | IT and Engineering | CTO | 70 | none (runs systems) |
| DEP-011 | Information Security | CISO | 14 | none (controls) |
| DEP-012 | Finance and Accounts | CFO | 28 | none (uses ACT-003 data) |
| DEP-013 | HR and Administration | Head of HR | 21 | ACT-010 |

## 4. Other laws and regulators

| Item | Note |
| --- | --- |
| RBI directions for NBFCs and digital lending | Cover KYC, data storage in India, grievance redress, recovery practice, outsourcing. Check which parts conflict with or add to the Act (Sec 38) *(verify)* |
| Prevention of money laundering rules | KYC record retention periods after the relationship ends *(verify the period)* |
| Credit information reporting law | Reporting to credit bureaus *(verify whether it supports a legitimate use)* |
| Information technology law | Existing rules on sensitive data and reasonable security continue until replaced *(verify)* |
| Local rules for recovery agents | Calling hours and conduct *(verify)* |

## 5. Part A: entity checklist answers (E1 to E13)

| Ref | Answer | Reasoning and evidence |
| --- | --- | --- |
| E1 | Yes | Offices, staff, servers and customers in India. Registered office, hub list. |
| E2 | No | Does not serve people outside India. |
| E3 | Yes | All customer data is digital. Hub paper forms are scanned. |
| E4 | Yes, two entities | Quellmark Finance Ltd is the fiduciary. The subsidiary is a processor for the app; if it uses data for its own purposes it needs its own Part A. |
| E5 | No | Not a clinical or educational body. |
| E6 | No | Not a notified startup or class. |
| E7 | Not notified | Candidate SDF. Volume of 4.2 million people and financial data. Track the Gazette. |
| E8 | No | Private company. |
| E9 | Not known | No other notification found at the reference date *(verify)*. |
| E10 | Yes | RBI directions overlap. |
| E11 | Yes | Singapore, Ireland, Germany, USA. Transfer check needed on ACT-002, ACT-007, ACT-008. |
| E12 | No | No foreign-located data principals under a foreign contract. |
| E13 | Reference date 2026-11-10 | Most client duties start about 13 May 2027 *(verify)*; findings are readiness gaps. |

## 6. Inventory

### 6.1 Owners

| Client name | Entity | Sponsor | Reference date |
| --- | --- | --- | --- |
| Quellmark Finance Ltd | Quellmark Finance Ltd | Head of Compliance | 2026-11-10 |

Owner list for dropdowns: Chief Credit Officer, Head of Operations, Head of Collections, Head of Support, Chief Marketing Officer, Head of Partnerships, Head of Compliance, General Counsel, CTO, CISO, CFO, Head of HR, Head of Onboarding.

### 6.2 System Inventory

| ID | Name | Type | Owner | Hosting | Location | Personal data? | Data categories | Data principals | Encryption at rest | Backup | Log retention | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SYS-001 | Loan management system | Cloud service | Head of Operations | Cloud | Mumbai, Maharashtra, India | Yes | Identity, contact, financial, loan | Borrowers, guarantors | Yes | Yes - Daily | 1 year | Core system |
| SYS-002 | Customer data lake | Database | CTO | Cloud | Mumbai, Maharashtra, India | Yes | All customer data, behaviour, scoring features | Borrowers, applicants | Yes | Yes - Weekly | Less than 1 year | Feeds scoring and marketing |
| SYS-003 | Credit scoring platform (vendor-hosted) | Cloud service | Chief Credit Officer | Cloud | Singapore; Dublin, Ireland (backup) | Yes | Identity, bank statement data, SMS and device data, scores | Applicants, borrowers | Partial | Yes - Daily | Less than 1 year | Leaves India |
| SYS-004 | Collections dialer and CRM | Cloud service | Head of Collections | Hybrid | Hyderabad, Telangana, India | Yes | Contact, loan, call notes, references | Borrowers, references | No | No | None | No encryption; no backup |
| SYS-005 | KYC document vault | Cloud service | Head of Onboarding | Cloud | Mumbai, Maharashtra, India | Yes | Aadhaar XML, PAN, photo, selfie, video KYC | Applicants, borrowers | Yes | Yes - Daily | 1 year | |
| SYS-006 | Call recording server | Server | Head of Support | On-premises | Hyderabad, Telangana, India | Yes | Voice recordings of customers | Borrowers, applicants | No | Yes - Weekly | Less than 1 year | Recordings kept indefinitely |
| SYS-007 | HRMS and payroll (vendor SaaS) | Cloud service | Head of HR | Cloud | Not known | Yes | Employee identity, salary, bank, statutory IDs | Employees, job applicants | Partial | Yes - Daily | Less than 1 year | Vendor has not stated region |
| SYS-008 | Email and collaboration suite | Cloud service | CTO | Cloud | Frankfurt, Germany | Yes | Staff mail; customer data pasted in mail | Employees, borrowers | Yes | Yes - Daily | 1 year | Leaves India |
| SYS-009 | Marketing automation platform | Cloud service | Chief Marketing Officer | Cloud | Dublin, Ireland | Yes | Contact, segments, campaign responses | Borrowers, applicants | Yes | Yes - Daily | Less than 1 year | Leaves India |
| SYS-010 | Support ticketing platform | Cloud service | Head of Support | Cloud | Oregon, USA | Yes | Tickets, chat transcripts, contact | Borrowers | Yes | Yes - Daily | 1 year | Leaves India |
| SYS-011 | Mobile app backend | Cloud service | CTO | Cloud | Mumbai, Maharashtra, India | Yes | App events, device data, session | App users | Yes | Yes - Daily | 1 year | |
| SYS-012 | Finance ERP | Server | CFO | On-premises | Andheri East, Mumbai, India | Yes | Vendor, agent and employee payments | Employees, agents | Partial | Yes - Daily | 1 year | |
| SYS-013 | Hub paper files | Paper-to-digital | Head of Collections | On-premises | Five hubs, India | Yes | Receipts, visit forms | Borrowers | No | No | None | Scanned weekly |

### 6.3 Application Inventory

| ID | Name | Purpose | Owner | Hosted on | Vendor | Personal data? | Remarks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| APP-001 | Quellmark Lending app | Sign-up, loans, repayment | CTO | SYS-011 | VEN-007 | Yes | Asks for SMS, contacts and location permissions |
| APP-002 | Loan management console | Servicing | Head of Operations | SYS-001 | VEN-001 | Yes | |
| APP-003 | Underwriting workbench | Credit decisions | Chief Credit Officer | SYS-001 | VEN-007 | Yes | Automated decisions |
| APP-004 | Scoring API | Scores applicants | Chief Credit Officer | SYS-003 | VEN-002 | Yes | |
| APP-005 | Collections workbench and dialer | Recovery | Head of Collections | SYS-004 | VEN-006 | Yes | Agency staff log in |
| APP-006 | e-KYC and video KYC module | Identity checks | Head of Onboarding | SYS-005 | VEN-003 | Yes | |
| APP-007 | Marketing automation | Campaigns | Chief Marketing Officer | SYS-009 | VEN-008 | Yes | |
| APP-008 | Support desk | Tickets and chat | Head of Support | SYS-010 | VEN-009 | Yes | Chatbot transcripts kept |
| APP-009 | HRMS | Payroll and HR | Head of HR | SYS-007 | VEN-010 | Yes | |
| APP-010 | Partner portal | Co-lending and agent leads | Head of Partnerships | SYS-001 | VEN-007 | Yes | |
| APP-011 | Finance ERP | Payments | CFO | SYS-012 | none | Yes | |
| APP-012 | Customer web portal | Self service | CTO | SYS-011 | VEN-007 | Yes | |
| APP-013 | Messaging console | SMS and WhatsApp | Head of Operations | SYS-001 | VEN-014 | Yes | |

### 6.4 Vendor List

| ID | Name | Service | Role | Personal data? | Data shared | Data location | Contract | Security clause | Breach clause | Deletion clause | Sub-processors | Dates | Business owner | Last review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VEN-001 | NimbusGrid Cloud | Cloud hosting | Processor | Yes | All customer data | India | Yes | Yes | Yes | Partial | Unknown | 2024-04 to 2027-03 | CTO | 2025-10 |
| VEN-002 | ScoreSight Analytics Pte Ltd | Credit scoring models | Processor | Yes | Identity, bank data, SMS data, device data | Outside India | Yes | Partial | No | No | Unknown | 2025-01 to 2027-12 | Chief Credit Officer | Never |
| VEN-003 | VeriKYC Rail | e-KYC, video KYC | Processor | Yes | Aadhaar XML, selfie, video | India | Yes | Yes | Yes | Yes | No | 2025-06 to 2027-05 | Head of Onboarding | 2026-06 |
| VEN-004 | PayRelay | Auto-debit and UPI mandates | Other | Yes | Bank account, UPI ID, mandate details | India | Yes | Yes | Yes | Partial | No | 2024-08 to 2027-07 | CFO | 2026-02 |
| VEN-005 | BureauLink Information Services | Credit bureau | Other | Yes | Identity, loan, repayment data | India | Yes | Yes | Yes | No | No | 2023-01 to 2026-12 | Chief Credit Officer | 2025-12 |
| VEN-006 | CallWave Recovery Services | Collection agency | Processor | Yes | Contact, loan, due amounts, references | India | Expired | No | No | No | Yes: field agent partners | 2023-04 to 2025-03 | Head of Collections | Never |
| VEN-007 | Quellmark Technology Services Pvt Ltd | App and data engineering | Processor | Yes | All app and platform data | India | Yes | Partial | Partial | Partial | No | Intra-group 2022 | CTO | 2025-05 |
| VEN-008 | MailForge | Marketing automation | Processor | Yes | Contact, segments | Outside India | Yes | Yes | Partial | Yes | Yes | 2025-02 to 2026-12 | Chief Marketing Officer | 2026-01 |
| VEN-009 | HelpNest | Support ticketing | Processor | Yes | Tickets, chat, recordings links | Outside India | Yes | Yes | Yes | Yes | Yes | 2024-10 to 2026-10 | Head of Support | 2025-09 |
| VEN-010 | TalentPay HRMS | Payroll SaaS | Processor | Yes | Employee identity, salary, bank | Unknown | Yes | Partial | No | No | Unknown | 2025-04 to 2027-03 | Head of HR | Never |
| VEN-011 | SecureSign | e-signature | Processor | Yes | Name, Aadhaar-linked signature | India | Yes | Yes | Yes | Yes | No | 2025-03 to 2027-02 | Head of Operations | 2026-03 |
| VEN-012 | Harbourline Bank | Co-lending partner | Joint fiduciary | Yes | Applicant file, loan data | India | Yes | Yes | Yes | Partial | Not applicable | 2024-09 to 2027-08 | Head of Partnerships | 2026-04 |
| VEN-013 | Direct selling agents (40) | Lead sourcing | Other | Yes | Applicant leads | India | Expired (12 of 40) | No | No | No | Unknown | Various | Head of Partnerships | Never |
| VEN-014 | Orbit Messaging | SMS and WhatsApp gateway | Processor | Yes | Mobile, message text | India | Yes | Yes | Yes | Partial | No | 2025-05 to 2027-04 | Head of Operations | 2026-05 |
| VEN-015 | WorkMail Suite | Email and collaboration | Processor | Yes | Staff mail, attachments | Outside India | Yes | Yes | Yes | Yes | Yes | 2024-12 to 2027-11 | CTO | 2026-07 |

### 6.5 Security Controls

| ID | Name | Category | Applies to | Implemented | What is actually done | Owner | Evidence available | Evidence ref | Last reviewed | Rule 6 item | Gap or remarks | Policy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CTL-001 | Database encryption | Encryption | SYS-001 | Yes | Disk and column encryption on loan data | CISO | Yes | Config export 2026-10 | 2026-10 | Encryption or masking | | POL-001 |
| CTL-002 | Aadhaar masking | Encryption | SYS-005 | Yes | Aadhaar masked to last four digits in all screens | CISO | Yes | Screenshots | 2026-09 | Encryption or masking | | POL-001 |
| CTL-003 | Scoring vendor encryption | Encryption | SYS-003 | Partial | Vendor says encrypted in transit only | CISO | No | None | Never | Encryption or masking | At rest not evidenced | POL-001 |
| CTL-004 | Role-based access | Access control | SYS-001 | Yes | Roles reviewed quarterly | CISO | Yes | Access review sheet | 2026-09 | Access control | | POL-002 |
| CTL-005 | Collections shared logins | Access control | SYS-004 | No | Agency staff share team logins | Head of Collections | No | None | Never | Access control | Shared accounts | POL-002 |
| CTL-006 | Privileged access vault | Access control | SYS-001, SYS-002 | Yes | Admin sessions recorded | CISO | Yes | Vault report | 2026-10 | Access control | | POL-002 |
| CTL-007 | Central log monitoring | Logging and monitoring | SYS-001, SYS-011 | Yes | Logs to SIEM, alerts reviewed | CISO | Yes | SIEM screenshot | 2026-10 | Logging and monitoring | | POL-003 |
| CTL-008 | Collections activity logs | Logging and monitoring | SYS-004 | No | Dialer logs not reviewed | Head of Collections | No | None | Never | Logging and monitoring | | POL-003 |
| CTL-009 | Daily backup and restore test | Backup and recovery | SYS-001, SYS-005 | Yes | Restore tested half-yearly | CTO | Yes | Restore report 2026-07 | 2026-07 | Backup and continuity | | POL-004 |
| CTL-010 | Log retention setting | Logging and monitoring | SYS-001 | Yes | Logs kept 13 months | CISO | Yes | Retention config | 2026-10 | Log retention | | POL-003 |
| CTL-011 | Vendor security review | Third party | VEN-002 | No | Questionnaire sent, never returned | CISO | No | None | Never | Processor contract | | POL-006 |
| CTL-012 | Incident response plan | Incident | All | Partial | Plan exists; last drill 2024 | CISO | Yes | Plan v3 | 2026-02 | Measures to follow safeguards | Not drilled this year | POL-005 |

### 6.6 Policy Inventory

| ID | Policy | Owner | Version | Approved | Review due |
| --- | --- | --- | --- | --- | --- |
| POL-001 | Information security and encryption | CISO | 4.1 | 2026-03 | 2027-03 |
| POL-002 | Access control | CISO | 3.2 | 2026-03 | 2027-03 |
| POL-003 | Logging and monitoring | CISO | 2.0 | 2025-11 | 2026-11 |
| POL-004 | Business continuity and backup | CTO | 2.4 | 2026-01 | 2027-01 |
| POL-005 | Incident and breach response | CISO | 3.0 | 2026-02 | 2027-02 |
| POL-006 | Outsourcing and vendor management | Head of Compliance | 1.5 | 2025-07 | 2026-07 (overdue) |
| POL-007 | Privacy notice (customers) | Head of Compliance | 5.0 | 2025-08 | 2026-08 (overdue) |
| POL-008 | Data retention schedule | Head of Compliance | 1.0 | 2024-06 | 2025-06 (overdue) |
| POL-009 | Grievance redressal | Head of Support | 2.2 | 2026-04 | 2027-04 |
| POL-010 | Fair practices and recovery code | Head of Collections | 3.0 | 2026-01 | 2027-01 |

## 7. Flow Nodes (not in the Inventory)

| ID | Name | Type | Zone | Country |
| --- | --- | --- | --- | --- |
| DP-001 | Loan applicants | Data principal | Data principal | India |
| DP-002 | Borrowers | Data principal | Data principal | India |
| DP-003 | Guarantors and co-applicants | Data principal | Data principal | India |
| DP-004 | Borrowers' references and phone contacts | Data principal | Data principal | India |
| DP-005 | Employees | Data principal | Data principal | India |
| DP-006 | Job applicants | Data principal | Data principal | India |
| DEP-001 to DEP-013 | As in section 3 | Department | Client premises | India |
| EXT-001 | Reserve Bank of India | External party | Other organisation (India) | India |
| EXT-002 | Financial Intelligence Unit | External party | Other organisation (India) | India |
| EXT-003 | Tax authorities | External party | Other organisation (India) | India |
| EXT-004 | Courts and arbitrators | External party | Other organisation (India) | India |
| EXT-005 | Statutory auditors | External party | Other organisation (India) | India |
| EXT-006 | Law enforcement | External party | Other organisation (India) | India |
| EXT-007 | Borrowers' employers | External party | Other organisation (India) | India |

## 8. Processing activities (ROPA)

Common values: Our role = Data Fiduciary unless stated. Children's data = No (age check at sign-up: 18 or older). Consent before the Act = Not sure for ACT-001, ACT-007; No elsewhere. Last updated 2026-11-09. Owner contact as the department head.

### ACT-001 Customer onboarding and KYC
| Field | Value |
| --- | --- |
| Department | Customer Onboarding and KYC |
| Purpose | Verify identity and eligibility before offering a loan |
| Legal basis claimed | "Legal obligation under RBI KYC rules" (no Sec 7 clause named) |
| Data principals | Loan applicants, guarantors |
| Source | From the person |
| Internal recipients | Credit and Underwriting (DEP-002), Compliance (DEP-008) |
| External | VEN-003 VeriKYC Rail (processor), VEN-011 SecureSign |
| Retention | Not defined; policy says "as per law"; retention schedule overdue |
| Security | CTL-001, CTL-002, CTL-004 |
| Cross-border | No |
| Consent status | Partial (consent screen exists; notice outdated) |
| Collection point | Mobile app |
| Systems and apps | SYS-005, SYS-011; APP-001, APP-006 |
| Shared outside the client | Yes |
| Walkthrough | Interviewed Head of Onboarding 2026-11-04. Saw sign-up flow on a test phone. Side channel: staff ask applicants to WhatsApp Aadhaar copies when the app fails. |

### ACT-002 Credit assessment and scoring
| Field | Value |
| --- | --- |
| Department | Credit and Underwriting |
| Purpose | Decide whether to lend and at what limit and price |
| Legal basis claimed | Consent (Sec 6) |
| Data principals | Loan applicants, borrowers |
| Source | Both (person, bureaus, bank statement aggregator) |
| Internal | Underwriting (DEP-002), Risk (DEP-008) |
| External | VEN-002 ScoreSight (processor, outside India), VEN-005 BureauLink |
| Retention | Scores kept 8 years; raw SMS data kept indefinitely |
| Security | CTL-003, CTL-011 |
| Cross-border | Yes: Singapore, Ireland |
| Consent status | Partial |
| Collection point | Mobile app |
| Systems and apps | SYS-002, SYS-003, SYS-011; APP-003, APP-004 |
| Used to decide about the person | Yes (automated decision) |
| Shared outside the client | Yes |
| Walkthrough | Interviewed Chief Credit Officer. Saw model feature list: includes counts of loan-app SMS and number of contacts. Say vs show: told "we only read bank SMS"; the app reads the whole inbox. |

### ACT-003 Loan servicing and repayment
| Field | Value |
| --- | --- |
| Department | Loan Operations |
| Purpose | Disburse loans, collect EMIs, send statements and reminders |
| Legal basis claimed | Consent (Sec 6) |
| Data principals | Borrowers, guarantors |
| Source | From the person |
| Internal | Operations (DEP-003), Finance (DEP-012) |
| External | VEN-004 PayRelay, VEN-014 Orbit Messaging, VEN-001 NimbusGrid |
| Retention | Loan life plus 8 years |
| Security | CTL-001, CTL-004, CTL-006, CTL-007 |
| Cross-border | No |
| Consent status | Active |
| Systems and apps | SYS-001, SYS-011; APP-002, APP-013 |
| Shared outside the client | Yes |

### ACT-004 Collections and recovery
| Field | Value |
| --- | --- |
| Department | Collections and Recovery |
| Purpose | Recover overdue amounts |
| Legal basis claimed | "Contract and legal claim" (Sec 17(1)(a) relied on) |
| Data principals | Borrowers, guarantors, references and phone contacts |
| Source | Both: from the borrower, and from the app's contacts list |
| Internal | Collections (DEP-004), Legal (DEP-009) |
| External | VEN-006 CallWave (processor, contract expired), EXT-004 courts, EXT-007 employers |
| Retention | Call recordings kept indefinitely |
| Security | CTL-005, CTL-008 |
| Cross-border | No |
| Consent status | Not captured |
| Exemption claimed | 17(1)(a) legal right or claim |
| Systems and apps | SYS-004, SYS-006, SYS-013; APP-005 |
| Shared outside the client | Yes |
| Walkthrough | Interviewed Head of Collections. Saw agents' WhatsApp groups where borrower lists are shared. Hub staff keep field visit forms in cabinets. Agency staff share three team logins. |

### ACT-005 Credit bureau reporting
| Field | Value |
| --- | --- |
| Department | Loan Operations |
| Purpose | Report loan and repayment behaviour to credit bureaus |
| Legal basis claimed | "Legal obligation" |
| Data principals | Borrowers, guarantors |
| Source | From the person (data created by loan servicing) |
| Internal | Operations (DEP-003) |
| External | VEN-005 BureauLink |
| Retention | Reports kept 8 years |
| Security | CTL-001 |
| Cross-border | No |
| Consent status | Active (consent text names bureau reporting) |
| Systems and apps | SYS-001; APP-002 |
| Shared outside the client | Yes |

### ACT-006 Regulatory and law-enforcement reporting
| Field | Value |
| --- | --- |
| Department | Compliance, Risk and Audit |
| Purpose | File mandatory returns and answer lawful requests |
| Legal basis claimed | 7(d) Legal duty to disclose to the State |
| Data principals | Borrowers, employees |
| Source | From the person |
| Internal | Compliance (DEP-008), Legal (DEP-009) |
| External | EXT-001 RBI, EXT-002 FIU, EXT-003 tax, EXT-006 law enforcement, EXT-005 auditors |
| Retention | As per law (periods to confirm) |
| Cross-border | No |
| Consent status | Not applicable |
| Systems and apps | SYS-001, SYS-008; APP-002 |
| Shared outside the client | Yes |

### ACT-007 Marketing and cross-sell
| Field | Value |
| --- | --- |
| Department | Marketing and Growth |
| Purpose | Offer top-up loans and new products |
| Legal basis claimed | Consent (Sec 6) |
| Data principals | Borrowers, past applicants |
| Source | From the person |
| Internal | Marketing (DEP-006) |
| External | VEN-008 MailForge (outside India), VEN-014 Orbit Messaging |
| Retention | Kept until the customer unsubscribes; no deletion run |
| Security | None documented |
| Cross-border | Yes: Ireland |
| Consent status | Partial |
| Systems and apps | SYS-009, SYS-002; APP-007 |
| Used to decide about the person | Yes (offers withheld from low-score segments) |
| Shared outside the client | Yes |
| Walkthrough | Opt-in box is pre-ticked on the sign-up screen. Unsubscribe works only for email, not SMS. |

### ACT-008 Customer support and grievances
| Field | Value |
| --- | --- |
| Department | Customer Support |
| Purpose | Answer questions and resolve complaints |
| Legal basis claimed | 7(a) Voluntarily provided |
| Data principals | Borrowers, applicants |
| Source | From the person |
| Internal | Support (DEP-005) |
| External | VEN-009 HelpNest (outside India) |
| Retention | Tickets kept 5 years; call recordings indefinitely |
| Cross-border | Yes: USA |
| Consent status | Not applicable |
| Systems and apps | SYS-006, SYS-010; APP-008 |
| Walkthrough | Support lead says chat transcripts are also used to train the chatbot. Not in the privacy notice. |

### ACT-009 Partner and agent leads, co-lending
| Field | Value |
| --- | --- |
| Department | Partnerships and Co-lending |
| Purpose | Take loan applications from partners and agents; co-lend with a bank |
| Legal basis claimed | Consent (Sec 6) |
| Role | **Joint Data Fiduciary** with Harbourline Bank for co-lent loans |
| Data principals | Loan applicants |
| Source | From a third party (agents, partner platforms) |
| Internal | Partnerships (DEP-007), Underwriting (DEP-002) |
| External | VEN-012 Harbourline Bank, VEN-013 DSAs |
| Retention | Not defined |
| Cross-border | No |
| Consent status | Partial |
| Systems and apps | SYS-001; APP-010 |
| Shared outside the client | Yes |
| Walkthrough | Agents collect data on their own phones and WhatsApp. No notice is shown at that point. 12 of 40 agent contracts expired. |

### ACT-010 Employee HR and payroll
| Field | Value |
| --- | --- |
| Department | HR and Administration |
| Purpose | Hire, onboard, pay and manage staff |
| Legal basis claimed | 7(i) Employment purposes |
| Data principals | Employees, job applicants |
| Source | From the person and from third parties (background check agency) |
| Internal | HR (DEP-013), Finance (DEP-012) |
| External | VEN-010 TalentPay (location unknown), EXT-003 tax, statutory funds |
| Retention | Employment plus 8 years |
| Cross-border | Not sure |
| Consent status | Not applicable |
| Systems and apps | SYS-007, SYS-012; APP-009, APP-011 |
| Shared outside the client | Yes |

### ACT-011 Fraud detection and device analytics
| Field | Value |
| --- | --- |
| Department | Customer Onboarding and KYC |
| Purpose | Detect identity fraud and fake accounts |
| Legal basis claimed | "Legitimate interest" |
| Data principals | Loan applicants, app users |
| Source | From the person (device) |
| Internal | Onboarding (DEP-001), Information Security (DEP-011) |
| External | VEN-007 Quellmark Technology Services |
| Retention | 3 years |
| Cross-border | No |
| Consent status | Not captured |
| Systems and apps | SYS-002, SYS-011; APP-001 |
| Used to decide about the person | Yes (blocks accounts) |
| Shared outside the client | No |

## 9. Activity Data (elements per activity)

Format: ID Name. Flags apply only where shown: D2 made public by the person, D3 child's data, D4 used to decide about the person, D7 leaves India. Retention for this use is "Not defined" unless stated.

| Activity | Elements |
| --- | --- |
| ACT-001 | DE-ID-001 Full name; DE-ID-002 Date of birth; DE-ID-004 Photograph; DE-ID-005 Signature; DE-CON-001 Mobile; DE-CON-002 Email; DE-CON-003 Postal address; DE-GOV-003 PAN; DE-GOV-015-A Offline Aadhaar XML; DE-GOV-001 Aadhaar number (D4); DE-GOV-011 CKYC number; DE-BIO-007 Selfie or liveness; DE-AV-003 Video KYC recording; DE-FIN-001-A Bank account number; DE-COM-004 Consent records |
| ACT-002 | DE-ID-001; DE-ID-002; DE-CON-001; DE-GOV-003; DE-FIN-004 Income (D4,D7); DE-FIN-005-A Credit score (D4,D7); DE-FIN-005-B Bureau report (D4,D7); DE-FIN-006 Transaction history (D4,D7); DE-FIN-011-B Bank statement copy (D4,D7); **DE-DEV-006 SMS inbox data (D4,D7)**; **DE-DEV-007 Phone contacts list (D4,D7)**; DE-LOC-002 IP-derived location (D7); DE-DEV-002-A Device ID (D7); DE-BEH-002 Inferred segments (D4,D7) |
| ACT-003 | DE-ID-001; DE-ID-009 Customer ID; DE-CON-001; DE-CON-002; DE-CON-003; DE-FIN-001-A; DE-FIN-001-B IFSC; DE-FIN-016-A eNACH mandate; DE-FIN-016-B UPI AutoPay; DE-FIN-003 UPI ID; DE-FIN-007-A Loan details; DE-FIN-007-B EMI details; DE-FIN-006 Transaction history; DE-COM-005 SMS and WhatsApp content |
| ACT-004 | DE-ID-001; DE-CON-001; DE-CON-003; DE-CON-004-A Emergency contact name; DE-CON-004-B Emergency contact number; DE-FIN-007-A; DE-FIN-007-B; DE-FIN-006; DE-EMP-001-A Job title (borrower's employer); DE-AV-002 Call recording (retention: indefinite); DE-COM-005; **DE-DEV-007 Phone contacts list (D4)** |
| ACT-005 | DE-ID-001; DE-ID-002; DE-GOV-003; DE-CON-001; DE-FIN-007-A; DE-FIN-007-B; DE-FIN-006 |
| ACT-006 | DE-ID-001; DE-GOV-003; DE-GOV-011; DE-FIN-006; DE-FIN-007-A; DE-FIN-004; DE-EMP-007-A Compensation (employee returns) |
| ACT-007 | DE-ID-001; DE-CON-001; DE-CON-002; DE-BEH-002 Inferred segments (D4); DE-BEH-004 Purchase history; DE-BEH-009 Campaign responses; DE-FIN-007-A (D7); DE-COM-009 Marketing opt-in choices; DE-DEV-003 Cookies |
| ACT-008 | DE-ID-001; DE-CON-001; DE-CON-002; DE-COM-002 Complaint text; DE-COM-006 Chat transcripts (D7); DE-COM-008 Ticket history (D7); DE-AV-002 Call recording; DE-ID-009 |
| ACT-009 | DE-ID-001; DE-CON-001; DE-CON-003; DE-GOV-003; DE-FIN-004; DE-FIN-011-A Cancelled cheque; DE-COM-005 WhatsApp content; DE-ID-004 Photograph |
| ACT-010 | DE-ID-001; DE-ID-002; DE-ID-005; DE-CON-001; DE-CON-002; DE-CON-003; DE-GOV-003; DE-GOV-009-A UAN; DE-GOV-009-B PF number; DE-FIN-001-A; DE-EMP-001-A, -B, -C; DE-EMP-002 Employment history; DE-EMP-004 Attendance and leave; DE-EMP-006 Background verification report; DE-EMP-007-A Compensation; DE-SEN-006 Police verification certificate; DE-SEN-005 POSH allegations; DE-FAM-002 Nominee details |
| ACT-011 | DE-ID-001; DE-CON-001; DE-DEV-002-A Device ID; DE-DEV-002-B Advertising ID; DE-DEV-011 Device fingerprint; DE-DEV-001 IP address; DE-DEV-009 Access logs; DE-BIO-006 Behavioural biometrics (D4); DE-BIO-007 Selfie or liveness (D4); DE-LOC-001 Precise GPS (D4) |

## 10. Data Flow (one row per place the data passes through)

Each row: node, shared further, shared with, channel.

| Activity | Rows |
| --- | --- |
| ACT-001 | DP-001 Yes → APP-001; APP-001 Yes → SYS-011, VEN-003, VEN-011; VEN-003 Yes → SYS-005; SYS-011 No; SYS-005 Yes → DEP-001 (channel: console); DEP-001 Yes → DEP-002 (shared drive); VEN-011 No. Side channel: DP-001 Yes → DEP-001 by WhatsApp (not in any system) |
| ACT-002 | DP-001 Yes → APP-001; APP-001 Yes → SYS-011; SYS-011 Yes → SYS-002; SYS-002 Yes → SYS-003, VEN-005 (API); SYS-003 Yes → VEN-002; VEN-002 Not sure → (sub-processors unknown); DEP-002 No |
| ACT-003 | DP-002 Yes → APP-001; APP-001 Yes → SYS-001; SYS-001 Yes → VEN-004, VEN-014, DEP-003; DEP-003 Yes → DEP-012; VEN-004 No; VEN-014 No; DEP-012 No |
| ACT-004 | DP-002 Yes → APP-001; APP-001 Yes → SYS-001; SYS-001 Yes → SYS-004; SYS-004 Yes → VEN-006, DEP-004; VEN-006 Yes → EXT-007 (calls to employers), DP-004 (calls to contacts); DEP-004 Yes → SYS-006, SYS-013, DEP-009; DEP-009 Yes → EXT-004; SYS-006 No; SYS-013 No. Side channel: VEN-006 Yes → agents' WhatsApp groups |
| ACT-005 | SYS-001 Yes → DEP-003; DEP-003 Yes → VEN-005; VEN-005 No |
| ACT-006 | SYS-001 Yes → DEP-008; DEP-008 Yes → EXT-001, EXT-002, EXT-003, EXT-005; DEP-008 Yes → DEP-009; DEP-009 Yes → EXT-006 |
| ACT-007 | SYS-002 Yes → SYS-009; SYS-009 Yes → VEN-008, VEN-014; VEN-008 No; VEN-014 No; DEP-006 No; reuse: SYS-002 Yes → ACT-003 data reused (ACT-003 marked in "shared with" on the SYS-002 row) |
| ACT-008 | DP-002 Yes → SYS-010 (chat), SYS-006 (call); SYS-010 Yes → VEN-009; VEN-009 Not sure → (chatbot training); SYS-006 No; DEP-005 No |
| ACT-009 | DP-001 Yes → VEN-013 (agent WhatsApp); VEN-013 Yes → APP-010; APP-010 Yes → SYS-001, VEN-012; VEN-012 No |
| ACT-010 | DP-005 Yes → DEP-013; DEP-013 Yes → SYS-007, SYS-012; SYS-007 Yes → VEN-010; VEN-010 Not sure → (location unknown); SYS-012 Yes → EXT-003 |
| ACT-011 | DP-001 Yes → APP-001; APP-001 Yes → SYS-011; SYS-011 Yes → SYS-002; SYS-002 Yes → VEN-007; VEN-007 No |

## 11. Hidden processing the walkthrough should surface

| What | Where it shows | Effect |
| --- | --- | --- |
| Aadhaar copies sent by WhatsApp | ACT-001 side channel | Unlisted copy of Confidential data; retention unknown |
| Whole SMS inbox and phone contacts read | ACT-002, ACT-004 | Over-collection (test C7 and E1 fail); third-party people never gave consent |
| Borrower lists in agents' WhatsApp groups | ACT-004 | Uncontrolled sharing; agency contract expired |
| Chat transcripts used to train the chatbot | ACT-008 | Second purpose not in notice; reuse needs its own basis |
| Data lake feeds marketing from loan data | ACT-007 to ACT-003 | Reuse for another purpose |
| Staff paste customer data into email hosted in Germany | SYS-008 | Cross-border flow not in the ROPA |
| Scoring vendor's sub-processors unknown | ACT-002 | Path has no end (Not sure) |
| HRMS location unknown | ACT-010 | Unknown zone |

## 12. Phase 3 expected review

Route, then answers by exception. All other tests in the active blocks are Yes. Children tests do not apply.

| Activity | Route | Tests that are not Yes | Expected outcome | Why |
| --- | --- | --- | --- | --- |
| ACT-001 | Consent | C3 No (no Board complaint route in notice); C8 No (withdrawal by email only); C7 Not sure; C10 Not applicable | Gap | C3; C8. Route mismatch: ROPA says legal obligation |
| ACT-002 | Consent | C5 No (bundled with sign-up); C7 No; C3 No; E1 No on DE-DEV-006 and DE-DEV-007; E2 No on DE-DEV-006 | Gap | C3; C5; C7; Element Check |
| ACT-003 | Consent | C10 Not applicable | Supported | None |
| ACT-004 | Exemption only (Sec 17(1)(a)) | X1 No (references, contacts and employers are not needed to enforce the claim); X2 Yes; X3 Not sure | Gap | X1 |
| ACT-005 | Consent | C10 Yes | Supported | None. Route mismatch: ROPA says legal obligation *(verify whether another route fits)* |
| ACT-006 | Legitimate use 7(d) | L4 Not applicable | Supported | None |
| ACT-007 | Consent | C5 No; C6 No (pre-ticked box); C8 No; C9 Not sure; ROPA consent status Partial | Gap | C5; C6; C8 |
| ACT-008 | Legitimate use 7(a) | L2 Not sure (training reuse); L4 Yes | Cannot conclude yet | One open test |
| ACT-009 | Consent | C1 No (agents show no notice); C9 No; C8 Not sure | Gap | C1; C9 |
| ACT-010 | Legitimate use 7(i) | L4 Not applicable | Supported | None |
| ACT-011 | None identified | none | Gap: no legal basis | R1. "Legitimate interest" is not an option under the Act |

Totals: 4 Supported (ACT-003, 005, 006, 010), 5 Gap (001, 002, 004, 007, 009), 1 Gap: no legal basis (011), 1 Cannot conclude yet (008).

### Findings to log

| ID | Activity | Test | Finding | Owner |
| --- | --- | --- | --- | --- |
| LB-001 | ACT-002 | C7, E1 | App reads the whole SMS inbox and phone contacts, which scoring does not need | Chief Credit Officer |
| LB-002 | ACT-004 | X1 | Recovery calls reach people who are not the borrower | Head of Collections |
| LB-003 | ACT-011 | R1 | No legal basis for device and behaviour analytics | Head of Onboarding |
| LB-004 | ACT-007 | C6 | Pre-ticked marketing consent box | Chief Marketing Officer |
| LB-005 | ACT-009 | C1 | Agents collect data without notice | Head of Partnerships |
| LB-006 | ACT-001 | C3, C8 | Notice lacks complaint route; withdrawal by email only | Head of Compliance |
| LB-007 | ACT-008 | L2 | Chat transcripts reused to train a chatbot | Head of Support |

## 13. Phase 4 expected checks

### 13.1 System security (Rule 6 items a to e)

Cells read: client says / evidence seen / result.

| System | (a) Encryption | (b) Access control | (c) Access logs | (d) Backup | (e) Log retention 12 months or more |
| --- | --- | --- | --- | --- | --- |
| SYS-001 | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Yes (13 months) / Yes / Pass |
| SYS-002 | Yes / Partial / Partial | Yes / Yes / Pass | Yes / Partial / Partial | Yes / Yes / Pass | No (under 1 year) / Yes / Gap (client confirms) |
| SYS-003 | Partial / No / Gap: claim not supported | Not sure / not seen / Not tested | No / not seen / Gap (client confirms) | Yes / No / Gap: claim not supported | No / not seen / Gap (client confirms) |
| SYS-004 | No / Yes / Gap (client confirms) | No (shared logins) / Yes / Gap (client confirms) | No / Yes / Gap (client confirms) | No / Yes / Gap (client confirms) | No (none) / Yes / Gap (client confirms) |
| SYS-005 | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass |
| SYS-006 | No / Yes / Gap (client confirms) | Yes / Partial / Partial | No / Yes / Gap (client confirms) | Yes / Yes / Pass | No / Yes / Gap (client confirms) |
| SYS-007 | Partial / Not seen / Not tested | Yes / No / Gap: claim not supported | Not sure / not seen / Not tested | Yes / Not seen / Not tested | No / not seen / Gap (client confirms) |
| SYS-011 | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass | Yes / Yes / Pass |

### 13.2 Vendor review

| Vendor | Contract seen | Security clause | Breach clause | Deletion clause | Result |
| --- | --- | --- | --- | --- | --- |
| VEN-002 ScoreSight | Yes | Partial | No | No | Gap: no breach or deletion terms; sub-processors unknown; transfer to Singapore and Ireland |
| VEN-006 CallWave | Expired | No | No | No | Gap: no valid contract |
| VEN-007 Technology subsidiary | Yes (intra-group) | Partial | Partial | Partial | Partial |
| VEN-010 TalentPay | Yes | Partial | No | No | Gap; location unknown |
| VEN-013 DSAs | Expired for 12 of 40 | No | No | No | Gap |
| VEN-003, 011, 014 | Yes | Yes | Yes | Yes or Partial | Pass |

### 13.3 Client-level duties

| Duty | Client says | Evidence | Result |
| --- | --- | --- | --- |
| Breach: tell people and the Board, detailed report within 72 hours | Plan exists | Plan v3 seen; last drill 2024; no template for the 72-hour report | Partial |
| Grievance handling | Grievance officer, published | Website and app page seen | Pass |
| Contact for questions about processing | Grievance officer only; no DPO contact in notice | Notice POL-007 outdated | Gap |
| Rights handling (access, correction, erasure, nominee) | Access and correction by email; no erasure process | Tested one request: no reply in 30 days | Gap |
| Governance: measures to show compliance | Compliance owns privacy | No privacy risk register | Partial |
| Log retention at least one year | Set to 13 months on SYS-001 only | See 13.1 | Partial |
| SDF duties (only if notified) | Not notified | Track notification | Not applicable now |

### 13.4 Activity-level duties

| Activity | Retention and deletion | Accuracy | Cross-border |
| --- | --- | --- | --- |
| ACT-002 | Raw SMS data kept indefinitely: Gap | Scores drive decisions; no appeal route: Gap | Singapore, Ireland: recorded and checked |
| ACT-004 | Call recordings indefinite: Gap | Borrower contact details not verified: Partial | None |
| ACT-007 | No deletion run on unsubscribed: Gap | Segment scores not validated: Partial | Ireland |
| ACT-008 | Recordings indefinite: Gap | Not applicable | USA |
| ACT-001, 003, 005 | Retention "as per law" with no schedule: Partial | Pass | None |

## 14. Data flow diagram: what it should show

| Feature | Where |
| --- | --- |
| Arrows leaving India | ACT-002 to VEN-002 (Singapore, Ireland); ACT-007 to VEN-008 (Ireland); ACT-008 to VEN-009 (USA); SYS-008 email in Germany |
| Unknown zone | SYS-007 and VEN-010 (HRMS) |
| Not sure | VEN-002, VEN-009, VEN-010 |
| Reuse arrow | ACT-007 reuses ACT-003 loan data |
| Path with no end | VEN-002 sub-processors |
| Inventory but in no flow | SYS-013 appears only in ACT-004; none orphaned. Add a test: remove SYS-012 flow to see an orphan |
| Side channel | WhatsApp in ACT-001, ACT-004, ACT-009 (not in Inventory, so add as flow nodes EXT-008 "WhatsApp (staff and agents)" outside India) |

## 15. Edge cases the assessor should catch

1. A "legal duty, so no consent" belief that the Act does not support for collection; only disclosure to the State fits 7(d) *(verify)*.
2. Consent bundled into the sign-up and permissions the product does not need.
3. Over-collection (SMS inbox, contacts) that also affects people who never dealt with the client.
4. An exemption (Sec 17(1)(a)) claimed for a whole process although only part of it fits.
5. A joint fiduciary activity where neither party gives the notice.
6. "Legitimate interest" used as a basis. The Act has no such ground.
7. Expired vendor contracts for the processors with the most data.
8. Secondary use of support chats for model training.
9. Possible SDF status: duties not yet in force for this client, but the volume suggests planning for them.
