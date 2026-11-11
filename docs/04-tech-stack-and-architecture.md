# 04. Tech stack and architecture

## Stack

Exact versions are pinned in `package.json` and the compose file when S0 is built; the newest stable release of each is used at that time and recorded in the changelog.

| Layer | Choice | Why |
| --- | --- | --- |
| Language | TypeScript (strict) everywhere | One language for screens, server and rules |
| Runtime, package manager | Node 22 LTS, pnpm | Already on the server |
| Framework | Next.js, App Router, React Server Components | Pages render on the server and send little JavaScript, which is the main lever for speed |
| Styling | Tailwind CSS driven by REX CSS variables | Tokens come from the REX kit; no hand-typed colours |
| UI primitives | Radix UI primitives, styled in-house to REX | Accessible menus, dialogs and selects without an off-the-shelf look |
| Tables | TanStack Table + TanStack Virtual | Large editable grids stay smooth |
| Forms and validation | React Hook Form + Zod | One schema validates in the browser, on the server and during Excel import |
| Database | PostgreSQL 17 | Records link by ID; relational fit |
| Data access | Prisma | Typed models that mirror 05 |
| Sign-in | Own credentials flow: Argon2id password hashes, server-side sessions in PostgreSQL, `jose` for reset JWTs, `otplib` for TOTP | Server-side sessions are needed for instant revoke, idle timeout and admin-adjustable rules (D-24), which stateless JWT sessions cannot give. See 07 |
| Email | Nodemailer over SMTP; Mailpit in development | D-23 |
| Excel | ExcelJS | Reads and writes .xlsx and keeps dropdowns |
| Evidence storage | MinIO through the S3 API | D-25; swaps to any S3-compatible store later |
| Reverse proxy | Caddy | Automatic HTTPS on the real server |
| Packaging | Docker Compose | D-26 |
| Tests | Vitest (unit, integration), Playwright (end to end) | See 12 |

**Change from the Notion proposal:** Notion suggested Auth.js. It is replaced by a small in-house credentials flow because the owner's requirements (admin-switchable lockout, password policy, idle timeout, forced sign-out, MFA) all need server-side session records, and Auth.js with a credentials provider only supports stateless JWT sessions. The reset link is still a JWT, as asked (D-22).

## Services

```
browser --HTTPS--> caddy --> app (Next.js, port 3000)
                              |-- postgres   (data, sessions, audit log)
                              |-- minio      (evidence objects, encrypted)
                              `-- mailpit    (SMTP in dev; real SMTP in production)
```

Only Caddy is exposed. PostgreSQL, MinIO and Mailpit listen on the internal Docker network only.

## Code layout

```
app/                    routes (server components by default)
  (auth)/               sign-in, reset, invite, MFA
  (app)/                everything behind sign-in
    admin/              administration area
    assessments/[id]/   one assessment: inventory, activities, flow, review, findings ...
  api/                  route handlers: file upload/download, Excel import/export
components/             REX-styled UI: ui/ (primitives), data-grid/, forms/, layout/
lib/
  rules/                pure functions: outcomes, checks, roll-ups, zones (no database, no React)
  authz/                the one permission check
  auth/                 sessions, passwords, reset tokens, MFA, lockout
  db/                   Prisma client, assessment-scoped query helpers, audit writer
  excel/                workbook mapping, import, export
  storage/              MinIO client, compress + encrypt pipeline
  mail/                 templates and sender
prisma/                 schema, migrations, seed (catalogues, demo data)
fixtures/               The three demo clients (18) as JSON, expected outcomes
tests/                  unit, integration, e2e
scripts/                release.sh and maintenance scripts
```

## Design decisions that matter

1. **Rules live in code, not in the database.** Route mismatch, outcome, why, path checks, roll-ups and zones are pure functions in `lib/rules` with unit tests. The three demo clients in 18 are the acceptance case.
2. **Derived values are computed, never typed and never stored by hand.** They are computed on read. If a list becomes slow, a derived value may be cached in a column, but only the rules module writes it, in the same transaction as the change that affects it.
3. **Catalogues are versioned.** Data elements and test definitions carry a version so a locked assessment keeps the wording it used.
4. **Everything is scoped to an assessment.** Every record carries an assessment ID and every query goes through the scoped helper.
5. **One write path.** All changes to assessment data go through server actions that (a) check permission, (b) validate with Zod, (c) write, and (d) write the audit entry, in one transaction.
6. **Human IDs are allocated by the server** per assessment and prefix (SYS-001), inside the transaction, so two users cannot get the same ID.
7. **No third-party calls at run time.** Fonts, icons and scripts are served by the app (D-28).

## Performance budget (D-21)

Measured with Playwright and Lighthouse against the production build on a 4 vCPU / 8 GB server holding the three demo clients (18) plus a 500-activity stress fixture. A release is blocked if a number is missed.

| Measure | Budget |
| --- | --- |
| Sign-in page: largest paint | under 1.0 s |
| Any app page: server response (TTFB) | under 200 ms at the 95th percentile |
| Any app page: largest paint | under 1.5 s |
| Moving between screens of one assessment | under 300 ms to usable |
| Saving a cell or a form | feedback under 100 ms (optimistic), confirmed under 400 ms |
| Table of 2,000 rows | scrolls at 60 frames per second (virtualised) |
| JavaScript sent on first load of any route | under 180 kB compressed |
| Excel import of the Inventory workbook | under 5 s |
| Excel export | under 5 s |

How the budget is met:

- Server components by default; client components only where there is interaction (grids, forms, menus).
- Data is fetched on the server, next to the database, in parallel, with pagination or virtualised windows for long lists.
- Indexes on every foreign key and on `(assessment_id, human_id)`; no query without an assessment filter.
- Optimistic updates for edits; only the changed row is re-fetched.
- Self-hosted fonts, preloaded, `font-display: swap`; only the weights in use (Space Grotesk 500 and 700, IBM Plex Mono 400 and 500). Arial is a system font and costs nothing.
- SVG logo and motifs; no raster decoration on app screens.
- Next.js standalone build in a small production image; Caddy serves compressed responses and long-lived cache headers for static files.
- Heavy libraries (ExcelJS) run on the server only and never enter the browser bundle.

## Environments

| Environment | Where | Mail | HTTPS |
| --- | --- | --- | --- |
| Development | This sandbox, `docker compose up` for services, `pnpm dev` for the app | Mailpit | Not needed locally; `instabox-port publish --private` gives an HTTPS URL when the owner wants to look |
| Production | Owner's Linux server or VPS, India region | Real SMTP | Caddy with automatic certificates |
