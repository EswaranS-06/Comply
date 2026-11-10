# Comply

Comply is a web app that runs a DPDP (India) compliance assessment for a client Data Fiduciary as one connected flow, replacing separate Excel workbooks. Facts are entered once, linked by ID, and checked automatically.

## Branches

| Branch | Holds |
| --- | --- |
| `main` | Tested, working versions only. Every commit is a tagged release (`vX.Y.Z`). |
| `forge` | Day-to-day build branch. Always the newest code, plus project documents and agent skills. |

`main` is produced from `forge` by `scripts/release.sh`. Do not commit to `main` by hand.

## Status

Planning complete. No application code yet. The first release will be `v0.0.1`.
