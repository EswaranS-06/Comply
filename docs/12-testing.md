# 12. Testing

"Working" has a definition. A version reaches `main` only when every check in the release gate passes.

## Layers

| Layer | Tool | Covers |
| --- | --- | --- |
| Static | TypeScript strict, ESLint, Prettier | Types, unused code, formatting |
| Unit | Vitest | `lib/rules` (every rule, every branch), validation schemas, compress + encrypt round trip, token and password helpers |
| Integration | Vitest against a real PostgreSQL and MinIO from Compose | Server actions, permission checks, audit writing, import and export, human ID allocation under concurrency |
| End to end | Playwright (Chromium), production build | The main flows in 09, in dark and light themes |
| Performance | Playwright timings + Lighthouse | The budget in 04 |
| Accessibility | axe via Playwright | No serious or critical issues on any screen |

## Tests that must always exist

1. **Workbook parity.** (a) Every rule in 06 has table-driven unit tests written from the workbook formulas, one case per branch, asserting the exact result text. (b) Import compares Comply's computed values with the values cached in the workbook's auto columns and must report no parity warning for the sample activity. (c) Auklet School: outcomes are exactly 1 Supported, 3 Gap, 2 Gap: no legal basis, 2 Cannot conclude yet, and each activity matches the workbook. Part (c) is added when the filled demo workbooks are supplied; (a) and (b) do not wait for it.
2. **Isolation.** A client user of client A requests every route and server action with IDs belonging to client B and gets "not found" each time. A firm user who is not a member of an assessment gets the same.
3. **Role matrix.** One test per row of the table in 03, for all five roles.
4. **Lock.** After sign-off no role except admin can change anything, and an admin change without a reason is refused.
5. **Client view.** The data sent to a client contributor contains no assessor note, test, route or outcome field (checked on the response, not on the page).
6. **Import is all-or-nothing.** A workbook with one bad row writes zero rows.
7. **Round trip.** Export then import reproduces the same records with no parity warnings, for all four workbooks.
8. **Reset link.** Works once, expires on time, ends other sessions, and a tampered token is refused.
9. **Lockout and settings.** Each security setting changes behaviour when switched, and the last admin cannot be locked out.
10. **Evidence.** Stored bytes are not readable as the original; download returns the identical file; a user without permission is refused.
11. **Audit.** Every write action in the role matrix produces an audit entry with before and after values.
12. **Template hygiene.** No committed template or fixture contains a known client name.

## Release gate

Run by `pnpm verify` before `scripts/release.sh`:

1. `pnpm lint` and `pnpm typecheck` are clean.
2. `pnpm test` (unit and integration) passes.
3. `pnpm build` succeeds.
4. `pnpm e2e` passes against the production build.
5. `pnpm perf` meets the budget (from S2 onward, when there are data screens to measure).
6. The stage's exit checks in 14 are met.
7. `/docs` matches what was built, and the changelog has the entry.

A sub-version that only adds part of a stage must still pass 1 to 4. If a check cannot pass, the work stays on `forge` and is not released.

## Test data

- `fixtures/auklet/`: the demo, pseudo names only.
- `fixtures/stress/`: generated, 500 activities and 2,000 inventory rows, for performance.
- No real client data in tests, ever.
