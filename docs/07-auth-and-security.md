# 07. Sign-in and security

## Sign-in flow

There is one sign-in page for every role (D-06).

1. User enters email and password at `/sign-in`.
2. Server checks lockout, then the Argon2id hash. The error message is the same for a wrong email and a wrong password.
3. If MFA is on for the user, a second step asks for the 6-digit code (or a recovery code).
4. Server creates a Session row and sets the session cookie.
5. User lands on the home for their role: admin on Administration, firm users on their assessments, client users on their client's assessment.

If `mustChangePassword` is set, step 5 is replaced by the change-password screen.

## Sessions

- The cookie holds a random 256-bit token; the database stores only its SHA-256 hash.
- Cookie flags: `HttpOnly`, `Secure`, `SameSite=Lax`, path `/`, name prefixed `__Host-`.
- Each request loads the session, checks idle and absolute expiry against Security settings, and updates `lastSeenAt` (at most once a minute, to keep requests fast).
- Sign-out, deactivation, password change, password reset and "end sessions" delete the rows, so they take effect on the next request.

Sessions are server-side rather than JWT because instant revoke and admin-adjustable timeouts need a record to check. JWTs are used where the owner asked for them: the reset and invite links.

## Password reset and invites (D-22, D-23)

- The link is `https://<host>/reset?token=<JWT>`.
- The JWT is signed with HS256 using `AUTH_TOKEN_SECRET`, and carries: user id, purpose (`reset` or `invite`), a unique `jti`, and `exp` (30 minutes for reset, 72 hours for invite; both adjustable).
- The `jti` is stored in AuthToken. The link works once: using it marks the row used. A new request cancels older unused links for that user.
- The token travels only over HTTPS. The reset page has `Referrer-Policy: no-referrer`, loads no third-party resource, and the token is removed from the address bar once read.
- After a reset, every session of that user is ended.
- "Forgot password" always answers "If the account exists, a link has been sent", creates a PasswordResetRequest, emails the link, and shows the request to the admin, who can copy the link or issue a fresh one.
- Admins never see or set a password. They can only send an invite or reset link.

## Security settings (D-24)

One screen under Administration. Every change is written to the audit log.

| Setting | Default | Range |
| --- | --- | --- |
| Lockout enabled | On | on / off |
| Failed tries before lockout | 5 | 3 to 20 |
| Lockout length | 15 minutes | 1 minute to 24 hours |
| Password minimum length | 12 | 8 to 64 |
| Block common passwords | On | on / off (bundled list of the most common passwords) |
| Require change on first login | On | on / off |
| Password expiry | Off | off, or 30 to 365 days |
| Idle timeout | 30 minutes | 5 minutes to 8 hours, or off |
| Maximum session length | 8 hours | 1 hour to 30 days |
| MFA | Optional | Off, Optional, Required; "Required" can be set per role |
| Reset link lifetime | 30 minutes | 10 minutes to 24 hours |
| Invite link lifetime | 72 hours | 1 hour to 14 days |

Guard rail: the screen refuses a combination that would lock the last active admin out (for example Required MFA while no admin has MFA set up).

Sign-in attempts are also rate-limited per IP address regardless of settings, so switching lockout off does not open unlimited guessing.

## MFA (A5)

TOTP (RFC 6238), 30-second step, 6 digits, one step of clock drift allowed. Setup shows a QR code and a manual key, asks for one code to confirm, then shows 10 single-use recovery codes once. The secret is stored encrypted with the app key. An admin can reset a user's MFA; the user sets it up again at next sign-in.

## Protections applied everywhere

- Permission check on the server for every action and every file download (03).
- All input validated with Zod on the server; Prisma parameterises every query.
- Server actions verify the Origin header; cookie is SameSite=Lax (CSRF).
- Response headers from Caddy and Next.js: Content-Security-Policy with no third-party sources, `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `frame-ancestors 'none'`, `Referrer-Policy: same-origin`.
- Secrets come only from environment variables; `.env` is never committed; `.env.example` lists the names.
- Sign-in, failed sign-in, lockout, reset, MFA changes, role changes, deactivation, lock and unlock are all audit events.

## Evidence files (D-25)

Upload pipeline, streamed so a large file never sits whole in memory:

1. Check permission, size (25 MB limit, admin-adjustable later) and type. Allowed: PDF, PNG, JPEG, WebP, DOCX, XLSX, PPTX, TXT, CSV, EML, MSG, ZIP. The type is checked from the file's leading bytes, not only its name.
2. **Compress** with Zstandard (Node's built-in zlib). Skipped for types that are already compressed (JPEG, PNG, WebP, ZIP, DOCX, XLSX, PPTX), where it would cost time and save nothing.
3. **Encrypt** with AES-256-GCM using a fresh random data key per file. The data key is itself encrypted with the master key (`EVIDENCE_MASTER_KEY`) and stored on the Evidence row. Compression comes before encryption because encrypted bytes do not compress.
4. Store in the private MinIO bucket under a random key: `<assessmentId>/<uuid>`. The original file name is kept only in the database.
5. Record original size, stored size and a SHA-256 checksum.

Download reverses the steps on the server after a permission check and streams the file with `Content-Disposition: attachment`. The browser never gets a MinIO address. Deleting the Evidence row deletes the object.

The bucket is private, MinIO is not exposed outside the Docker network, and losing `EVIDENCE_MASTER_KEY` makes the files unreadable, so the key is part of the backup notes in 11.

## Not in version 1

Single sign-on, WebAuthn or passkeys, IP allow-lists, virus scanning of uploads (noted as a risk in 15).
