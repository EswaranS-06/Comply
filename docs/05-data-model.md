# 05. Data model

Entities, key fields and links. Human IDs (SYS-001, ACT-001) are unique within an assessment. Every record below the Access and Catalogue groups carries `assessmentId`. Derived values are computed (see 06), not stored. Every table also has a database `id` (UUID), `createdAt`, `updatedAt`.

Fields marked **(workbook)** are taken column for column from the Excel workbooks once they are uploaded (D-11); the lists here are the minimum known from Notion.

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
| Client | legal name, display name, sector, active | belongs to the Firm; has many Assessments and client Users |
| Assessment | name, reference date, status (Draft, In review, Locked), lockedBy, lockedAt, catalogueVersion, testCatalogueVersion | belongs to a Client; has many Members |
| Member | user, assessment, role | joins a firm User and an Assessment |

## Inventory

| Entity | Key fields | Links |
| --- | --- | --- |
| Owner | name, contact | owns Systems, Vendors, Controls, Activities |
| System (SYS-) | name, type, hosting, location with country, stores personal data, data categories, encryption at rest, backup, log retention, remarks **(workbook)** | Owner |
| Application (APP-) | name, details as in the Application Inventory sheet **(workbook)** | hosted on a System |
| Vendor (VEN-) | name, service, role, handles personal data, data categories shared, data location, contract in place, security clause, breach clause, deletion clause, sub-processors, contract dates, last review **(workbook)** | Owner |
| Security control | name, category, applies to (System or App), implemented, description, evidence available, evidence reference, last reviewed, Rule 6 item, gap **(workbook)** | Owner, Policy |
| Policy | fields as in the Policy Inventory sheet **(workbook)** | Owner |

## Catalogue (shared across assessments, versioned)

| Entity | Key fields | Links |
| --- | --- | --- |
| Element group | name, default tier, default high-risk type, order | has many Elements (20 groups) |
| Data element (DE-) | name, type (Field, Record, Document), tier, high-risk type, is personal, note, version, retiredAt | Group (254 elements) |
| Tier override | assessment, element, tier | per assessment; only used to set Public |
| Test definition | ref (R1, C1 to C10, L1 to L4, X1 to X3, K1 to K3, E1, E2), applies to, question, plain reading, legal reference, evidence to ask for, verified (the Verify tag), version | used by Test answers |
| Checklist question | scope (entity or activity), question, law reference, outcome mapping **(workbook)**, version | Phase 1 (F5) |
| Catalogue history | entity, record, version, before, after, changedBy, changedAt | every catalogue edit |

Tiers: Public, Standard, Internal, Confidential. High-risk types: Government ID, Financial, Health, Biometric, Location, None.

An assessment records the catalogue version it was created with. Editing a catalogue row creates a new version; assessments that are not locked may be moved to the new version by an assessor, and locked assessments keep theirs.

## Discovery (ROPA family)

| Entity | Key fields | Links |
| --- | --- | --- |
| Activity (ACT-) | The 14 ROPA template fields: name, purpose, legal basis claimed, categories of data principals, source of data, internal recipients, retention, security summary, cross-border (Yes, No, Not sure) and countries, consent status, last updated, owner contact (exact 14 **(workbook)**). Plus: our role, exemption claimed and reason, children's data, consent before the Act, collection point, retention law, deletion method, process description, shared outside the client. Walkthrough fields: interview date, staff, evidence seen, side channels, say versus show, client confirmed, confirmed date | Owner |
| Activity link | activity to system, app, vendor (processor) or control | many to many |
| Activity element | activity, element, made public (D2), child's data (D3), used to decide (D4), leaves India (D7), retention for this use, notes | joins Activity and Data element |
| Flow node (DP-, DEP-, EXT-) | name, type, zone, country, remarks | people, departments and outside organisations not in the Inventory |
| Data flow step | activity, order, node (System, App, Vendor or Flow node), shared further (Yes, No, Not sure), shared with (nodes and activities), channel | Activity |
| Checklist answer | assessment, activity (empty for entity questions), question, answer, note | Phase 1 (F5) |

A data flow step points to exactly one of four node kinds. This is stored as a node kind plus four nullable foreign keys with a database check that exactly one is set, so the database itself blocks a dangling node and rule 4 of 03 (blocked delete) can be enforced by foreign keys.

Derived: categories of data, highest tier, high-risk types, number of elements, trust zone (Data principal, Client premises, Cloud or vendor in India, Other organisation in India, Outside India, Unknown), path check, cross-border check.

## Review

| Entity | Key fields | Links |
| --- | --- | --- |
| Activity review | route (Consent, Sec 7 use, Exemption only, Out of scope, None identified), Sec 7 clause, notes (internal), reviewed by, review date | Activity (one to one) |
| Test answer | activity, test ref, test version, answer (Yes, No, Not sure, Not applicable, blank), note | Activity, Test definition |
| Element check | activity element, needed for the purpose, named in the notice, notes | Activity element |
| System security check | system, Rule 6 item (a) to (e), evidence seen (Yes, Partial, No, blank), note | System (F21) |
| Finding (LB-) | test ref, description, evidence seen, client response, remediation owner, rating (blank until Phase 5), status (Open, Client to respond, Agreed, Disputed, Closed), shared with client, department and law reference (filled by the system) | exactly one of Activity, System or Vendor |
| Finding comment | finding, author, text | reviewer comments |
| Evidence | file name, content type, original size, stored size, storage key, wrapped data key, checksum, uploaded by, date | attached to exactly one of Finding, Test answer or Control |

Derived: outcome (Supported, Gap, Gap: no legal basis, Cannot conclude yet, Out of scope), why, route mismatch; for F21: client says, how we test it, result (Pass, Partial, Gap, Not tested).

The finding prefix `LB-` comes from the Legal Basis workbook. Whether findings from the security review use the same prefix is an open item (15).

## System

| Entity | Key fields | Links |
| --- | --- | --- |
| Audit log | user, assessment (empty for admin actions), entity, record id, human id, action (create, update, delete, lock, unlock, share, sign-in events, settings changes), before, after, reason, time, ip | append-only; no update or delete permission for the app's database role |
| Import run | file name, checksum, summary, started, finished, status, errors (sheet, row, reason) | Assessment |
| Id counter | assessment, prefix, next number | allocates human IDs |

## Main links

- Client has many Assessments; an Assessment owns every record below it.
- Activity has many Activity elements, many Data flow steps, and one Activity review with many Test answers.
- Data flow step points to a System, App, Vendor or Flow node.
- System, App and Vendor are shared by every Activity that uses them, so each is entered once.
- Finding points to the Activity, System or Vendor it is about, and to a test ref.

## Deleting

- Assessment data uses hard deletes guarded by foreign keys (`ON DELETE RESTRICT`); the audit log keeps the deleted values.
- Users and clients are never deleted, only deactivated.
- Catalogue rows are retired, not deleted.
