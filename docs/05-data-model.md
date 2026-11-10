# 05. Data model

Entities, key fields and links. Human IDs (SYS-001, ACT-001) are unique within an assessment. Every record below the Access and Catalogue groups carries `assessmentId`. Derived values are computed (see 06), not stored. Every table also has a database `id` (UUID), `createdAt`, `updatedAt`.

Field lists for workbook-backed entities were taken from the workbooks on 10 Nov 2026. The exact headers and allowed values are in [17-workbook-summary.md](17-workbook-summary.md), Part 2; this document names the fields and says how they link. Dropdown values are stored as enums with the workbook's exact text as the label, so export reproduces it.

## Access

| Entity | Key fields | Links |
| --- | --- | --- |
| Firm | name | has many Users and Clients. One row in version 1 (D-02) |
| User | name, email (unique, lower-cased), role, active, passwordHash, mustChangePassword, failedCount, lockedUntil, mfaSecret (encrypted), mfaEnabled, themePreference, lastLoginAt | belongs to the Firm (admin, assessor, reviewer) or to one Client (contributor, viewer) |
| Session | tokenHash, userId, createdAt, lastSeenAt, expiresAt, ip, userAgent | User |
| AuthToken | purpose (invite, reset), jti, userId, expiresAt, usedAt | User. Makes reset JWTs single-use |
| RecoveryCode | userId, codeHash, usedAt | User (MFA) |
| PasswordResetRequest | userId, requestedAt, handledBy, handledAt | shown to the admin |
| SecuritySettings | one row; fields in 07 | Firm |
| Client | legal name, display name, sector, active | belongs to the Firm; has many Assessments and client Users. **One client = one legal entity** (see note) |
| Assessment | name, reference date, status (Draft, In review, Locked), lockedBy, lockedAt, catalogueVersion, testCatalogueVersion; document control: document ID, version, classification, prepared by, reviewed by, approved by, effective date | belongs to a Client; has many Members |
| Member | user, assessment, role | joins a firm User and an Assessment |

Note on legal entities: the checklist says each legal entity is its own Data Fiduciary and gets its own Part A. In Comply a group of companies is therefore entered as several clients, one per legal entity, each with its own assessments. A "group" link between clients is not built in version 1.

## Organisation (workbook 1)

| Entity | Key fields | Links |
| --- | --- | --- |
| Organisation profile | The 37 answers of the Organization sheet, as typed columns: identity (registered legal name, CIN, PAN, GSTIN, entity type), classification (industry sector, organisation size), primary contact (name, email, designation, phone), detail (registered office address, website, number of locations), personal data scope (approximate Data Principals, children's data, health or financial data, data sent outside India, uses vendors), compliance position (privacy notice published, data protection contact, sector regulators, certifications, breach in last 12 months), applicability (7.1 to 7.13) | one per Assessment |
| Department | number, name, contact name, process, phone, email, handles personal data | Assessment. Picked on activities, owners and findings |

Registered legal name and sector on the profile are copied from the Client when the assessment is created and can then be corrected for that assessment.

## Inventory (workbook 3)

| Entity | Key fields | Links |
| --- | --- | --- |
| Owner | name (unique in the assessment), type (Person, Department), department, designation, email, phone | Department. Owns Systems, Apps, Vendors, Controls, Policies |
| System (SYS-) | name, type, hosting, location (text), country (see 06 R-2), stores personal data, data categories held, Data Principal categories, encryption at rest, backup, log retention period, remarks | Owner; has many Applications ("Linked applications" is shown from the apps hosted on it, and kept as text on import if it names anything else) |
| Application (APP-) | name, business purpose, type (In-house, Third-party, SaaS), personal data processed, data elements collected (text), purpose of processing, collection point, consent or notice shown, children's data, cross-border transfer (text), retention period, deletion method, users and access roles, login method | Owner; Vendor (if third-party); hosted on a System; shares data with a Vendor |
| Vendor (VEN-) | name, service provided, role (Processor, Joint fiduciary, Other), handles personal data, data categories shared, data location (India, Outside India, Both, Unknown), contract in place (Yes, No, Expired), security clause, breach notification clause, deletion or return clause, sub-processors, contract start and end dates (text), last review date, remarks | Owner (business owner) |
| Security control | control ID, name, category, implemented, description, evidence available, evidence reference, last reviewed date, linked DPDP requirement (Rule 6 item, seven values), gap or remarks | Owner; applies to one System or Application; linked Policy |
| Policy | policy ID, name, document type, category, version, status (Draft, Approved, Under review, Expired, Not available), approval date, last review date, applies to, communicated to staff, linked DPDP requirement, evidence reference, remarks | Owner; approved by (an Owner); linked Controls (many) |

Control ID and Policy ID have no prefix in the workbook. The app allocates `CTL-` and `POL-` for new rows and keeps whatever ID an imported row carries. **(to confirm with owner)**

## Catalogue (shared across assessments, versioned)

| Entity | Key fields | Links |
| --- | --- | --- |
| Element group | name, default type, default tier, default high-risk type, order | has many Elements (20 groups) |
| Data element | element ID (`DE-<group code>-<number>`, for example DE-ID-001), name, type (Field, Record, Document), personal data (Yes, No), tier, high-risk type, fixed-retention law, split from, notes, version, retiredAt | Group (254 elements) |
| Client element | same fields as a data element | Assessment. The workbook lets a client add its own elements at the bottom of the sheet; these stay inside the assessment and never enter the shared catalogue |
| Tier override | assessment, element, tier | per assessment; only used to set Public |
| Test definition | ref (R1, C1 to C10, L1 to L4, X1 to X3, K1 to K3, E1, E2), applies to (All, Consent, Sec 7 use, Exemption, Children, Element), question, short label (the column header in the workbook), plain reading, legal reference, evidence to ask for, verified, version | used by Test answers and Findings (23 tests) |
| Checklist question | part (A Entity, B Activity, C Element), group, ref (E1 to E13, P0 to P14, D1 to D7), question, what the answer decides, legal reference, evidence to ask for, source, answer list, version | Phase 1 (35 questions) |
| Reference list | Sec 7 clauses and Fourth Schedule items in plain words (Law Notes); Fourth Schedule classes; other laws and regulators with their "checked" status | read-only reference shown beside the relevant fields |
| Catalogue history | entity, record, version, before, after, changedBy, changedAt | every catalogue edit |

Tiers, highest first: Confidential, Internal, Standard, Public. High-risk types: Government ID, Financial, Health, Biometric, Location, None.

**Ref clash.** Checklist refs E1 to E13 and test refs E1, E2 are different things. Checklist questions are always identified by part and ref together and are shown as "A-E1", "B-P3", "C-D2". Test refs stay exactly as in the workbook, because findings and the "Why" text quote them.

An assessment records the catalogue version it was created with. Editing a catalogue row creates a new version; assessments that are not locked may be moved to the new version by an assessor, and locked assessments keep theirs.

## Discovery (workbook 3: ROPA, Activity Data, Data Flow, Flow Nodes)

| Entity | Key fields | Links |
| --- | --- | --- |
| Activity (ACT-) | **Template fields:** 1 name, 2 purpose, 3 legal basis claimed (Consent (Sec 6), 7(a) to 7(i), None identified yet), 4 categories of Data Principals, 6 source of data, 7 internal recipients (text), 8b other external recipients (text), 9 retention period, 10 security measures (text), 11a cross-border transfer (Yes, No, Not sure), 11b countries, 12 consent status (Active, Partial, Not captured, Not applicable), 13 last updated, 14 owner or DPO contact. **More detail:** our role (Data Fiduciary, Joint Data Fiduciary, Data Processor), exemption claimed (Not claimed or one of nine limbs), exemption reason, children or guardian-held data, consent given before the Act, collection point, law fixing the retention period, deletion method. **Notes:** process description. **Walkthrough:** interview date, staff interviewed, evidence seen, side channels, say versus show difference, client confirmed, confirmed date. **Path:** shared outside the client | Department |
| Activity link | activity to System, Application, Vendor (8a processors) or Control | many to many |
| Activity element | made public by the person (D2), child's data (D3), used to decide about the person (D4), leaves India (D7) (each Yes, No, Not sure or blank), retention for this use, notes | joins Activity and a Data element or Client element |
| Flow node (DP-, DEP-, EXT-) | name, type (Data principal, Department, External party), zone (six values), country, remarks | Assessment |
| Data flow step | order, shared further (Yes, No, Not sure), channel | Activity; the node it is at (exactly one of System, Application, Vendor, Flow node); shared with (many: any node kind, or another Activity) |
| Checklist answer | part, ref, answer, client note | Assessment; Activity (for Part B) |

Field 5, categories of personal data, is derived (06 R-1) and has no column.

A data flow step points to exactly one of four node kinds, stored as a node kind plus four nullable foreign keys with a database check that exactly one is set. "Shared with" is a join table with the same shape plus an activity key. The database itself therefore blocks a dangling ID, and rule 4 of 03 (blocked delete) is enforced by foreign keys.

Derived (06): categories of personal data, number of elements, highest tier, high-risk types, node name and type, system used for zone, zone, step check, outside recipients, path check, leaves India per data, cross-border check, row alerts.

## Review (workbook 4)

| Entity | Key fields | Links |
| --- | --- | --- |
| Activity review | route (Consent (Sec 6), Legitimate use (Sec 7), Exemption only (Sec 17), Out of scope, None identified), Sec 7 clause (7(a) to 7(i)), assessor notes (internal), reviewed by, review date | Activity (one to one) |
| Test answer | test ref, test version, answer (Yes, No, Not sure, Not applicable, or blank), note | Activity review, Test definition. Only C, L, X and K tests |
| Element check | E1 needed for the stated purpose, E2 named in the notice (Yes, No, Not sure, or blank), notes | Activity element (one to one) |
| Finding (LB-) | test ref, what we found, evidence seen, client response, remediation owner, rating (blank until Phase 5), status (Open, Client to respond, Agreed, Disputed, Closed), shared with client | Activity (workbook); System or Vendor also allowed (Notion F18) |
| Finding comment | author, text | Finding |
| Evidence | file name, content type, original size, stored size, storage key, wrapped data key, checksum, uploaded by, date | exactly one of Finding, Test answer or Control |
| System security check | Phase 4, F21. **Not designed**: see 06 R-12 and 15 | System |

In the workbook the review sheet repeats 13 ROPA columns that are pasted in by hand. In Comply these are read from the Activity; nothing is copied.

Derived (06): route mismatch, elements not needed, elements not in notice, tests failed, tests open, outcome, why, element finding, a finding's activity name, department and law reference.

The workbook's Finding ID has no fixed format; `LB-` comes from Notion. Whether findings from other phases use the same prefix is an open item (15).

## System

| Entity | Key fields | Links |
| --- | --- | --- |
| Audit log | user, assessment (empty for admin actions), entity, record id, human id, action (create, update, delete, lock, unlock, share, sign-in events, settings changes), before, after, reason, time, ip | append-only; no update or delete permission for the app's database role |
| Import run | file name, checksum, summary, started, finished, status, errors (sheet, row, reason) | Assessment |
| Id counter | assessment, prefix, next number | allocates human IDs |

## Main links

- Client has many Assessments; an Assessment owns every record below it.
- Assessment has one Organisation profile and many Departments.
- Activity belongs to a Department and has many Activity elements, many Data flow steps, one Activity review with many Test answers, and many Checklist answers.
- Data flow step points to a System, Application, Vendor or Flow node.
- System, Application and Vendor are shared by every Activity that uses them, so each is entered once.
- Finding points to the Activity, System or Vendor it is about, and to a test ref.

## Deleting

- Assessment data uses hard deletes guarded by foreign keys (`ON DELETE RESTRICT`); the audit log keeps the deleted values.
- Users and clients are never deleted, only deactivated.
- Catalogue rows are retired, not deleted.
