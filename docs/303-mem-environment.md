# 303. Memory: environment

Checked on 10 Nov 2026. Re-check with the commands at the bottom if something looks different.

## The machine

- An **Instabox sandbox**: a cloud Linux VM (Firecracker), free tier. Name `e06`. `~/MACHINE.md` describes it.
- 4 vCPU, 8 GB memory, 4 GB swap, 16 GB root disk, 20 GB `/data`.
- User `user`, home `/data/home`, passwordless `sudo`.
- Outbound internet works. **Nothing on the machine is reachable from the internet** unless a port is published through Instabox.
- **SSH access expires about 17 Nov 2026** (seven days from 10 Nov, per the owner).
- Both disks survive a stop. A stop ends every process, including Docker containers.

- Git remote: `origin` = https://github.com/EswaranS-06/Comply (public). Because it exists, losing the sandbox no longer loses the work, as long as it was pushed (D-48).
- The outline demo server (`demo/`, port 3000) was running on 11 Nov but port 3000 was no longer published (`instabox-port list` empty). Restart and republish as in 302 if needed.

## If the sandbox stops (owner's instruction, 301 I-14)

1. Wait 5 to 20 minutes and reconnect; it starts again by itself.
2. `cd /srv/comply && git status` and `git log --oneline -5` to see where things are; read 302.
3. Once the Compose file exists: `docker compose --profile dev up -d`. Database and MinIO data are on named volumes and survive.
4. Continue from the last commit. Uncommitted edits in the working tree also survive a stop, but commit often anyway.

## Paths

| Path | What |
| --- | --- |
| `/srv/comply` | The repository. Owned by `user` |
| `/srv/comply/source-workbooks` | The four template workbooks. Ignored by git; one names a real client |
| `/data/home/REX` | The owner's REX brand repository (their own, separate git repo). **Read only for this project.** The parts needed are copied into `.skills/rex-brand` and `.skills/rex-website` |
| `/data/home/REX/DPDP-Workbooks`, `/data/home/DPDP-Workbooks-Clean.zip` | Where the owner uploaded the workbooks |
| `/data/workspace` | Instabox's suggested work directory; unused |
| `/data/home/.claude` | Claude Code config, plugins, and the assistant's private memory for this project (which only points here) |

## Tools installed

| Tool | Version | Note |
| --- | --- | --- |
| git | 2.47 | Global identity set to the owner |
| gh | present, signed in as `EswaranS-06` (scopes: repo, workflow, gist, read:org) | Used on 11 Nov 2026 to create the public repo `Comply` (301 I-24). Push only when the owner says so |
| Node | 22 | |
| pnpm | 12 | Package manager for the project |
| npm, bun | present | Not used |
| Python | 3.13 | |
| uv | 0.12 | Use `uv run --no-project --with <pkg> python script.py` for one-off scripts; nothing needs installing globally |
| Docker | 29, Compose v5 | No containers running yet |
| Java 21, Rust | present | Not used |
| `instabox-port` | present | `instabox-port publish 3000 --private` gives the owner an HTTPS link to look at the running app |
| Claude Code | 2.1 | Plugin `ponytail@ponytail` installed |

Not installed: `rsync` (use `cp -r`), `psql`, `redis`, `nginx`. PostgreSQL, MinIO and Mailpit run as containers, not on the host.

## Desktop

People can watch the machine's desktop on the Instabox dashboard. A browser launched by Playwright shows there (`DISPLAY=:1`); set `INSTABOX_HEADLESS=1` to keep test runs headless.

## Reading the workbooks

```bash
cd /tmp && uv run -q --no-project --with openpyxl python -I your_script.py /srv/comply/source-workbooks
```

`openpyxl` loads formulas with `load_workbook(path)` and cached values with `load_workbook(path, data_only=True)`. Header rows differ per sheet; they are listed in 10.

## Commands to re-check the environment

```bash
cat ~/MACHINE.md | head -20
```

```bash
cd /srv/comply && git status --short && git branch -v && git tag
```

```bash
docker ps
```
