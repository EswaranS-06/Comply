# 00. Decisions

Each row is a decision the build relies on. "Owner" means the project owner (EswaranS-06). Newer decisions go at the bottom. A reversed decision is marked `Superseded by D-xx`, never deleted.

## Product

| ID | Date | Decision | Source |
| --- | --- | --- | --- |
| D-01 | 10 Nov 2026 | The app is named **Comply**. | Owner |
| D-02 | 10 Nov 2026 | One firm per installation. The Firm table exists so several firms are possible later; there are no firm-management screens. | Owner |
| D-03 | 10 Nov 2026 | Version 1 includes all Must features plus these Should features: F5 (Phase 1 checklist), F13 (coverage dashboard), F17 (test catalogue editing), F19 (evidence), F20 (audit log), F21 (system security review), F23 and F24 (client access). | Owner |
| D-04 | 10 Nov 2026 | **F22 (vendor, client and activity duties) is dropped from version 1.** Its design is unfinished. | Owner |
| D-05 | 10 Nov 2026 | **Processor (vendor) logins are dropped from version 1.** Vendors are records, not users. | Owner |
| D-06 | 10 Nov 2026 | Client users do log in during version 1. There is **one sign-in page for every role**; the role decides what opens after sign-in. | Owner |
| D-07 | 10 Nov 2026 | The firm admin gets a full administration area to manage clients, each client's employees (client users) and firm users. This is a first-class part of the product, not an afterthought. | Owner |
| D-08 | 10 Nov 2026 | Only a reviewer or admin can sign off and lock an assessment. An assessor can never sign off their own work. | Owner (accepts Notion recommendation) |
| D-09 | 10 Nov 2026 | Client contributors only enter facts. They never see legal tests, routes or outcomes. | Owner (accepts Notion recommendation) |
| D-10 | 10 Nov 2026 | A client viewer sees shared findings only after the assessment is signed off. | Owner (accepts Notion recommendation) |
| D-11 | 10 Nov 2026 | The Excel workbooks are the source of truth for catalogue content, test wording, and column layouts. Demo and acceptance data come from the three fictional clients in 18 (D-46). Nothing that depends on them is invented. The four template workbooks were supplied on 10 Nov 2026 and copied to `/srv/comply/source-workbooks/`; the Excel files stay out of git and are summarised in 17. | Owner |
| D-12 | 10 Nov 2026 | Workbook 1 (organisation profile and departments) is part of version 1, although Notion did not list it, because the other workbooks refer to it. | Claude, from the workbooks. Owner to confirm |
| D-13 | 10 Nov 2026 | One client is one legal entity. A group of companies is entered as several clients. | Claude, from the checklist's rule that each legal entity gets its own Part A. Owner to confirm |
| D-14 | 10 Nov 2026 | Result texts (outcomes, checks, alerts) use the workbook's exact words, and the rules follow the workbook formulas even where they could be stricter. Additions are marked as app additions in 06. | Claude, so exports and the parity test match |
| D-15 | 10 Nov 2026 | Checklist questions are shown with their part letter (A-E1, B-P3, C-D2) so they cannot be confused with element tests E1 and E2. Test refs are unchanged. | Claude. Owner to confirm |

## Technology

| ID | Date | Decision | Source |
| --- | --- | --- | --- |
| D-20 | 10 Nov 2026 | Stack: TypeScript, Next.js, PostgreSQL, Prisma, ExcelJS, Docker Compose. | Owner (accepts Notion proposal) |
| D-21 | 10 Nov 2026 | **The app must load fast.** Speed is a requirement with a measured budget (see 04, "Performance budget"), checked before every release. | Owner |
| D-22 | 10 Nov 2026 | Sign-in is email and password. Password reset uses a signed, short-lived, single-use JWT link. All traffic is HTTPS. | Owner |
| D-23 | 10 Nov 2026 | Reset and invite links are delivered two ways: by email, and as a link the admin can copy. **Mailpit** is the mail server in development and on the sandbox. | Owner |
| D-24 | 10 Nov 2026 | Lockout after failed tries, strong password policy, idle session timeout and optional TOTP MFA are all built, and **each one is switchable and adjustable from the admin area**. | Owner |
| D-25 | 10 Nov 2026 | Evidence files are stored in **MinIO** (S3-compatible), compressed then encrypted before upload, to save space and protect personal data. | Owner |
| D-26 | 10 Nov 2026 | Target host is the owner's own Linux server or VPS in an India region. The setup must stay a portable Docker Compose project that runs unchanged on the sandbox, a laptop and the server. | Owner |
| D-27 | 10 Nov 2026 | Desktop first. Tablets are usable. Phones can sign in and read findings; data tables are not optimised for phones. | Owner |
| D-28 | 10 Nov 2026 | Fonts are self-hosted. The app makes no request to Google Fonts or any other third-party host at run time. | Claude (speed, and client data stays in one place) |

## Design

| ID | Date | Decision | Source |
| --- | --- | --- | --- |
| D-30 | 10 Nov 2026 | The only theme is REX (`/data/home/REX`): its palette, fonts, tokens and diagonal-cut motif. No other colours or typefaces. | Owner |
| D-31 | 10 Nov 2026 | Dark is the default; each user can switch to the REX light variant. The choice is remembered per user. | Owner |
| D-32 | 10 Nov 2026 | Design skills are kept in `/.skills` and committed. Every use of a skill is written to `16-skills-log.md`. | Owner |

## Process

| ID | Date | Decision | Source |
| --- | --- | --- | --- |
| D-40 | 10 Nov 2026 | Git is local only. Commits carry only `EswaranS-06 <eswaransk06@gmail.com>`; no co-author or tool attribution lines. | Owner |
| D-41 | 10 Nov 2026 | Two branches. `main` is the timeline of working versions and sub-versions and holds no `/docs` or `/.skills`. `forge` is the always-current build branch and holds everything. | Owner (branch name chosen by Claude) |
| D-42 | 10 Nov 2026 | `/docs` is updated whenever the build departs from the plan. | Owner |
| D-43 | 10 Nov 2026 | No extra backup is made. The owner handles backup of the sandbox. | Owner |
| D-44 | 10 Nov 2026 | If the sandbox stops, wait 5 to 20 minutes and reconnect; it restarts by itself and work continues from the last commit. | Owner |
| D-45 | 11 Nov 2026 | **Plain interim theme.** Until the functionality is good, every screen is white background, black lines and black text. Colour is added only where it is needed to indicate something (a status, an error). The REX theme (D-30, dark default with light toggle) is applied afterwards, when the owner says so. Details in 08. | Owner |
| D-46 | 11 Nov 2026 | The earlier single demo client is removed from the project. Demo data and the acceptance case are three fictional clients supplied by the owner: Quellmark Finance, Halvorn Systems, Brannock Auto Components. Their files are in `docs/demo-clients/`; summary and expected outcomes in 18. | Owner |
| D-47 | 11 Nov 2026 | Excel import and export are available on every screen that holds sheet data (F30), and one Excel page handles the whole assessment (F31). Every import first checks sheet names and headers against a single sheet map and stops with an error when one is missing. Plan in 19. | Owner |
