# 03. Roles and permissions

## Roles

| Role | Who | Belongs to |
| --- | --- | --- |
| Firm admin | Runs the installation: users, clients, client employees, security settings, catalogues | The firm |
| Assessor | Does the assessment work (the auditor) | The firm, per assessment |
| Reviewer | Checks and signs off the assessor's work | The firm, per assessment |
| Client contributor | Client staff who enter facts | One client |
| Client viewer | Client lead who reads shared findings | One client |

A user has one role. A firm user (assessor, reviewer) sees only assessments they are a member of; an admin sees all. A client user sees only their own client.

## What each role can do

| Action | Admin | Assessor | Reviewer | Client contributor | Client viewer |
| --- | --- | --- | --- | --- | --- |
| Manage users, roles and client employees | Yes | No | No | No | No |
| Change security settings | Yes | No | No | No | No |
| Create clients and assessments | Yes | Yes | No | No | No |
| Add members to an assessment | Yes | Own assessments | No | No | No |
| Edit Data Classification and Test catalogues | Yes | No | No | No | No |
| View the catalogues | Yes | Yes | Yes | Elements only | No |
| Import and export workbooks | Yes | Yes | Export only | No | No |
| Enter inventory facts (systems, apps, vendors, controls) | Yes | Yes | No | Own client | No |
| Enter activities, elements and data flow | Yes | Yes | No | Own client | No |
| Answer the Phase 1 checklist | Yes | Yes | No | No | No |
| Choose the basis route and answer tests | Yes | Yes | No | No | No |
| Record the system security review | Yes | Yes | No | No | No |
| Write internal assessor notes | Yes | Yes | Yes | No | No |
| Log and edit findings | Yes | Yes | Comment only | No | No |
| Mark a finding Shared with the client | Yes | Yes | Yes | No | No |
| Send an assessment for review | Yes | Yes | No | No | No |
| Sign off and lock an assessment | Yes | No | Yes | No | No |
| Unlock a locked assessment (reason required) | Yes | No | No | No | No |
| View findings marked Shared | Yes | Yes | Yes | After sign-off | After sign-off |
| View all findings, outcomes and notes | Yes | Yes | Yes | No | No |
| Upload and open evidence | Yes | Yes | Open | Upload to own items | Open shared only |
| View the audit log | Yes | Yes | Yes | No | No |

## Rules

1. A client user never sees another client's data, assessor notes, tests, routes, outcomes, or findings that are not marked Shared.
2. A locked assessment cannot be edited by anyone except an admin, who must give a reason that is written to the audit log.
3. Outcomes (Supported, Gap) reach the client only through findings the assessor shares, and only after sign-off (D-10).
4. Deleting an activity, system or vendor that other records point to is blocked until the links are removed. The message lists the records that still point to it.
5. An assessor cannot sign off any assessment, including one they did not work on (D-08).
6. Client contributors enter facts only (D-09). Fields that hold assessor judgement are not sent to their browser at all; hiding them in the page is not enough.
7. Deactivating a user ends their sessions at once and keeps their name on past audit entries.

## How this is enforced

Permissions are checked on the server for every read and write, in one place (`lib/authz`), using three inputs: the user's role, the assessment the record belongs to, and the assessment's status. The page only decides what to draw; it is never the guard. Every database query for assessment data goes through a helper that adds the assessment filter, so a forgotten filter cannot leak another client's rows. Tests in S1 attack this directly (see 12).

## Resolved questions

| Question from Notion | Answer |
| --- | --- |
| May an assessor sign off their own work? | No, always a reviewer or admin (D-08) |
| Do client contributors see tests for their answers? | No, facts only (D-09) |
| Does a client viewer see outcomes before sign-off? | No (D-10) |
