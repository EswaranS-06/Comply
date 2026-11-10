# 09. Screens and flows

No wireframes were supplied; this list is the agreed starting point and is refined as each stage is built. Routes are indicative.

## Layout

- **Top bar:** REX logo and "Comply", assessment switcher (client and assessment name, status), search, theme toggle, user menu.
- **Left rail (inside an assessment):** the stage rail, grouped by assessment phase, each with a completeness mark.
- **Main area:** one grid or one form per screen. Record edit opens in a right-hand drawer.
- **Right gutter (firm users only):** flags for the current screen.

## Public

| Screen | Route | Notes |
| --- | --- | --- |
| Sign in | `/sign-in` | The single sign-in page for all roles. Email, password, "Forgot password". The one screen with REX brand graphics |
| MFA step | `/sign-in/verify` | Code or recovery code |
| Forgot password | `/forgot` | Always the same answer |
| Set / reset password | `/reset?token=` | Shows the active password rules live |

## Administration (admin only)

| Screen | Route | Notes |
| --- | --- | --- |
| Overview | `/admin` | Counts: users by role, clients, assessments by status, pending reset requests, locked accounts |
| Firm users | `/admin/users` | Admins, assessors, reviewers. Create, edit, role, deactivate, send invite, force reset, reset MFA, end sessions |
| Clients | `/admin/clients` | Create and edit clients; activate / deactivate |
| Client detail | `/admin/clients/[id]` | Tabs: Details, Employees (client contributors and viewers), Assessments |
| Client employees | tab of client detail | Same actions as firm users, limited to the two client roles |
| Reset requests | `/admin/reset-requests` | Pending "forgot password" requests; copy link or reissue |
| Security settings | `/admin/security` | Every setting in 07, grouped: Lockout, Passwords, Sessions, MFA, Links |
| Data catalogue | `/admin/catalogue/elements` | 20 groups, 254 elements; edit with history |
| Test catalogue | `/admin/catalogue/tests` | Question, plain reading, law reference, evidence to ask for; Verify tag |
| Audit log | `/admin/audit` | All events, filter by user, client, entity, action, date |

## Firm users

| Screen | Route | Notes |
| --- | --- | --- |
| My assessments | `/assessments` | Cards or rows: client, name, reference date, status, outcome counts |
| New client / assessment | dialog | F2 |
| Assessment home (coverage dashboard) | `/assessments/[id]` | F13: what is missing, counts by outcome, quick links to the rows |
| Members | `/assessments/[id]/members` | Who is assessor and reviewer |
| Import / export | `/assessments/[id]/excel` | Upload, preview of problems, confirm; export buttons; import history |

### Phase 1: Scope and Role

| Screen | Route | Notes |
| --- | --- | --- |
| Entity checklist | `/assessments/[id]/scope` | Entity questions once; result panel: duties that can apply, exemptions to test |
| Activity checklist | tab on the activity | Per-activity questions |

### Phase 2: Discover Data

| Screen | Route | Notes |
| --- | --- | --- |
| Owners | `.../inventory/owners` | |
| Systems | `.../inventory/systems` | Grid; missing required fields flagged |
| Applications | `.../inventory/applications` | Hosted-on picks a system |
| Vendors | `.../inventory/vendors` | |
| Security controls | `.../inventory/controls` | Applies-to picks a system or app |
| Policies | `.../inventory/policies` | |
| Data catalogue (read) | `.../catalogue` | Browse and search by group; set Public tier for this client |
| Activities (ROPA) | `.../activities` | Grid: ID, name, purpose, owner, number of elements, highest tier, outcome |
| Activity detail | `.../activities/[actId]` | Tabs: ROPA fields, Walkthrough, Elements, Data flow, Checklist, Legal basis, Findings |
| Elements tab | | Catalogue picker (search, group filter, multi-select); per-use flags D2, D3, D4, D7; roll-ups shown above |
| Flow nodes | `.../flow-nodes` | People, departments, outside organisations |
| Data flow tab | | Ordered steps; node picker across systems, apps, vendors and flow nodes; zone shown, not editable; path checks beside the steps |

### Phase 3: Legal Basis

| Screen | Route | Notes |
| --- | --- | --- |
| Legal basis overview | `.../legal-basis` | All activities: route, outcome, why, mismatch flag |
| Legal basis tab | on the activity | Route picker; only the tests for that route; each test shows question, plain reading, law reference (Verify tag), evidence to ask for; outcome and why update as answers change; "not a legal opinion" note |
| Element check | inside the legal basis tab | Needed, Named in notice per element |

### Phase 4: Duties

| Screen | Route | Notes |
| --- | --- | --- |
| System security review | `.../security-review` | Five rows per system, Rule 6 (a) to (e); client says, evidence seen, result; highest data tier per row |

### Findings, evidence, sign-off

| Screen | Route | Notes |
| --- | --- | --- |
| Findings log | `.../findings` | One list for all phases; filter by status, activity, system, vendor; share toggle; export |
| Finding detail | drawer | Fields, evidence list, reviewer comments |
| Evidence | within finding, test answer, control | Upload, list, download |
| Audit log | `.../audit` | This assessment only; before and after values |
| Review and sign-off | `.../sign-off` | Send for review; reviewer checklist of open flags; sign off and lock; admin unlock with reason |

## Client users

| Screen | Route | Notes |
| --- | --- | --- |
| Client home | `/client` | Their assessment, what they are asked to fill, how much is done |
| Inventory and activities entry | same routes, reduced | Same grids with fact fields only; no notes, tests, outcomes or flags (D-09) |
| Shared findings | `/client/findings` | After sign-off only (D-10); read-only; viewer and contributor |

## Main flows

1. **Set up:** admin creates firm users and the client, adds client employees; assessor creates the assessment and adds a reviewer.
2. **Bring in existing work:** assessor imports the Inventory workbook, reads the problem list, confirms.
3. **Discover:** assessor (or client contributor) completes inventory, adds activities from walkthroughs, picks elements, records the data flow; flags guide what is missing.
4. **Scope:** assessor answers the Phase 1 checklist.
5. **Legal basis:** assessor picks a route per activity and answers its tests; outcomes appear.
6. **Security review:** assessor records evidence seen per system.
7. **Findings:** assessor logs gaps, attaches evidence, marks which to share.
8. **Sign-off:** assessor sends for review; reviewer comments, signs off and locks.
9. **Client reads:** client viewer signs in and reads shared findings.
10. **Export:** assessor exports workbooks and the findings list at any point.

## States every screen handles

Loading (skeleton rows, never a blank page), empty (one sentence, one action), error (what failed and what to do), read-only (locked assessment or no edit permission: fields visibly disabled with the reason on hover), and unsaved changes (warning before leaving).
