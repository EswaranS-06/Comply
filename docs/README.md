# Comply: project documents

These documents define version 1 of Comply and how it is built. They live only on the `forge` branch.

Source: the Notion page "DPDP Assessment App: Project Documents" (read 10 Nov 2026) plus the owner's answers recorded in [00-decisions.md](00-decisions.md). Where this folder and Notion differ, this folder wins, because it holds the later decisions.

## Reading order

| # | Document | What it answers |
| --- | --- | --- |
| 00 | [Decisions](00-decisions.md) | What was decided, when, and why |
| 01 | [Product requirements](01-product-requirements.md) | What Comply is and what version 1 covers |
| 02 | [Features and user stories](02-features-and-user-stories.md) | Each feature, its acceptance criteria and the stage that builds it |
| 03 | [Roles and permissions](03-roles-and-permissions.md) | Who can see and do what |
| 04 | [Tech stack and architecture](04-tech-stack-and-architecture.md) | What it is built with and how the parts fit |
| 05 | [Data model](05-data-model.md) | Entities, fields and links |
| 06 | [Rules engine](06-rules-engine.md) | How outcomes, checks, roll-ups and zones are worked out |
| 07 | [Sign-in and security](07-auth-and-security.md) | Login, reset, MFA, admin security settings, evidence encryption |
| 08 | [Design system](08-design-system.md) | REX theme, fonts, colours, components |
| 09 | [Screens and flows](09-screens-and-flows.md) | Every screen and how users move between them |
| 10 | [Excel import and export](10-excel-import-export.md) | Workbook mapping and import rules |
| 11 | [Deployment](11-deployment.md) | Docker Compose, services, environment, backups |
| 12 | [Testing](12-testing.md) | What must pass before a release |
| 13 | [Git workflow and versioning](13-git-workflow-and-versioning.md) | Branches, commits, version numbers, releases |
| 14 | [Build plan](14-build-plan.md) | Stages, sub-versions, timeline, exit checks |
| 15 | [Open items](15-open-items.md) | What is still missing or unverified |
| 16 | [Skills log](16-skills-log.md) | Which agent skills are installed and when each was used |
| -- | [Changelog](CHANGELOG.md) | Every change to these documents and to the plan |

## Keeping these documents true

Plans change during a build. The rule is simple: **when the build departs from a document, the document is changed in the same commit as the code**, and one line is added to [CHANGELOG.md](CHANGELOG.md) saying what changed and why. A decision that reverses an earlier one is added to [00-decisions.md](00-decisions.md); the old entry is marked superseded, not deleted.

## Naming used in these documents

- **Phase 1 to 7** always means a phase of the *assessment method* (Scope and Role, Discover Data, Legal Basis, Duties, Rate, Remediate, Report).
- **Stage S0 to S10** always means a step of the *build* (see the build plan).
- **Must / Should / Later** are the feature priorities from the Notion documents.
- No emojis in any project file (REX brand rule).
