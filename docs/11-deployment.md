# 11. Deployment

One portable Docker Compose project (D-26). The same files run on the sandbox, a laptop and the production server; only the `.env` file and the compose profile differ.

## Services

| Service | Image | Purpose | Exposed |
| --- | --- | --- | --- |
| `app` | built from `Dockerfile` (Next.js standalone, non-root user) | The application | internal 3000 |
| `postgres` | `postgres:17` | Data, sessions, audit log | internal only |
| `minio` | `minio/minio` | Evidence objects | internal only (console on a dev-only port) |
| `mailpit` | `axllent/mailpit` | Catches all mail in development | dev profile only, web UI on 8025 |
| `caddy` | `caddy:2` | HTTPS and compression | 80, 443 (prod profile only) |
| `migrate` | same image as `app` | Runs `prisma migrate deploy` then exits | -- |

Profiles: `dev` (postgres, minio, mailpit; the app runs with `pnpm dev` on the host for fast reload) and `prod` (everything in containers behind Caddy).

## Environment variables

Listed in `.env.example`; real values are never committed.

| Variable | Purpose |
| --- | --- |
| `APP_URL` | Public address, used in emailed links |
| `DATABASE_URL` | PostgreSQL connection |
| `SESSION_SECRET` | Signs short-lived cookies such as the MFA step |
| `AUTH_TOKEN_SECRET` | Signs reset and invite JWTs |
| `APP_ENCRYPTION_KEY` | Encrypts MFA secrets |
| `EVIDENCE_MASTER_KEY` | Wraps the per-file evidence keys |
| `S3_ENDPOINT`, `S3_BUCKET`, `S3_ACCESS_KEY`, `S3_SECRET_KEY` | MinIO or any S3-compatible store |
| `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `MAIL_FROM` | Mailpit in dev; a real mail provider in production |
| `INITIAL_ADMIN_EMAIL` | The first admin, created on first start with an invite link printed to the log |

`scripts/gen-secrets.sh` writes fresh random values for the secret variables.

## On the sandbox

- `docker compose --profile dev up -d` then `pnpm dev`.
- To let the owner look: `instabox-port publish 3000 --private` gives an HTTPS link. Mailpit's inbox is published the same way when needed.
- The sandbox has no public address, so Caddy is not used here.
- If the sandbox stops, containers stop too. After it restarts (D-44): `docker compose --profile dev up -d`. PostgreSQL and MinIO data are on named volumes and survive.

## On the production server

1. A Linux server in an India region (for example 2 vCPU, 4 GB, 40 GB disk as a minimum), Docker installed, a domain name pointing to it.
2. Copy the repository at a release tag from `main`, create `.env`, run `scripts/gen-secrets.sh`.
3. `docker compose --profile prod up -d`. Caddy obtains the certificate; `migrate` applies the schema; the first admin's invite link appears in the app log.
4. Set real SMTP values and send a test email from Administration.

Upgrading: check out the new tag, `docker compose --profile prod up -d --build`. Migrations run automatically and are written to be backward compatible within one minor version.

## Backups (production)

Not automated in version 1; the commands are documented and scripted:

| What | How | Notes |
| --- | --- | --- |
| Database | `scripts/backup-db.sh` (`pg_dump`, compressed) | Daily |
| Evidence | `mc mirror` of the MinIO bucket | Files are already encrypted |
| Keys | `.env` kept in a password manager | Without `EVIDENCE_MASTER_KEY` the evidence cannot be read; without `APP_ENCRYPTION_KEY` MFA must be reset |

A restore is rehearsed once in S10.

On this sandbox no backup is made, by the owner's decision (D-43). The repository exists only on this machine.

## Health and logs

`/api/health` reports app, database and storage status. Containers log JSON to stdout with a request ID; no personal data or secrets are logged.
