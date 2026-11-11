# 305. Memory: lessons

Things that were non-obvious or cost time. Add to this whenever something surprises you. Format: what happened, then what to do.

## About the source material

| # | Lesson |
| --- | --- |
| L-1 | **Notion is a summary; the workbooks are the truth.** Notion's description of the outcome rule was incomplete (it left out that exemption tests count whenever an exemption is claimed, that children tests count when children's data is present, that consent status "Not captured" fails, and that a blank Sec 7 clause is open). When Notion and a workbook formula disagree, follow the formula and note it in 15 |
| L-2 | **Result texts must match the workbook character for character** ("Cannot conclude yet", "Gap: no legal basis", "Out of scope: record reason", "ROPA says: ..."). Exports and parity tests depend on it. Copy them from 06, do not retype from memory |
| L-3 | **Route names differ between Notion and the workbook.** Use the workbook's: "Consent (Sec 6)", "Legitimate use (Sec 7)", "Exemption only (Sec 17)", "Out of scope", "None identified". The ROPA's claimed legal basis uses a different list, ending in "None identified yet" |
| L-4 | **The letter E means two things.** E1 to E13 are entity questions in the checklist; E1 and E2 are element tests in the legal basis review. Always carry the checklist part (A-E1) |
| L-5 | **"Rule 6 item" has seven values in the workbook, not five (a) to (e).** F21 is not designed. Do not invent it |
| L-6 | **The workbook's zone rule is a text search for "India"** in the system's location. Follow it for parity; the app adds a country field on top (06 R-2) |
| L-7 | **The Data Flow sheet's Node ID dropdown only lists Flow Node IDs**, but SYS-, APP- and VEN- IDs are valid there. Do not treat the dropdown as the allowed set |
| L-8 | **Files described as "clean" were not.** One sheet carried a real client name. Before committing any file derived from owner material (templates, fixtures, screenshots), search it for client names. `source-workbooks/` stays ignored |
| L-9 | **Each inventory sheet pre-fills about 990 rows with formulas.** A row counts as data only when its ID cell is filled. Counting "non-empty rows" naively gives nonsense |
| L-10 | **Some dropdowns could not be read by `openpyxl`** (it warns "Data Validation extension is not supported"). Affected: sections 1 to 6 of the Organisation sheet. Confirm those in Excel or by reading the sheet XML (15, O-29) |
| L-11 | Header rows differ per sheet (2, 3, 4, 5 or 17). The table is in 10. Never assume row 1 |

## About the owner's messages

| # | Lesson |
| --- | --- |
| L-12 | When the owner picks a recommended option and adds a sentence, the sentence is a requirement. Example: accepting Next.js "but it should be fast" became a measured performance budget |
| L-13 | A button answer means only what the button said. "Review docs first" meant the owner will read; it was not a request to start anything |
| L-14 | The owner sometimes sends a follow-up while work is running. Fold it into the current task and say that you did |
| L-15 | "Wait until I tell you" is an instruction to stop, not a pause to fill with preparation work. Do the thing asked and nothing more |

## About the tools and the machine

| # | Lesson |
| --- | --- |
| L-16 | `rsync` is not installed. Use `cp -r` and remove unwanted folders afterwards |
| L-17 | `/srv/comply` was created by root. It has been `chown`ed to `user`; if a new folder under `/srv` is ever needed, expect the same |
| L-18 | When vendoring a skill from GitHub, clone with `--depth 1` into a scratch folder, copy only the skill folder, and leave out `.git` and large asset folders (taste-skill's `assets/` was 37 MB) |
| L-19 | Third-party skill folders contain scripts. Read a script before running it. The ponytail plugin's hooks were checked: they call local `git` and `node` only |
| L-20 | Run one-off Python with `uv run --no-project --with <pkg>`; write the script to a scratch folder, not inside the repository or next to downloaded files |
| L-21 | A shell command that deletes its own working directory ends with a harmless `getcwd` error; it does not mean the earlier steps failed. Check the real output |

## About the git workflow

| # | Lesson |
| --- | --- |
| L-22 | `main` is rebuilt by `scripts/release.sh` as a snapshot of `forge` minus `docs`, `.skills`, `CLAUDE.md`. It is not a merge. Never commit on `main` by hand and never move a tag |
| L-23 | `release.sh` refuses to run unless you are on `forge` with a clean tree. Commit everything, including document updates, first |
| L-24 | The script was dry-run in a clone, not in the real repository, so the first real release is `v0.0.1`. If a release goes wrong, fix on `forge` and release the next number |
| L-25 | Use `git add <paths>` for what you mean to commit. `source-workbooks/` and `.env` files are ignored, but do not rely on that alone when adding fixtures |

## About writing the documents

| # | Lesson |
| --- | --- |
| L-26 | Generate tables of columns, dropdowns and counts from the source files by script. Hand-typed versions of these had errors on the first pass (a question count was wrong) |
| L-27 | When a rule document is renumbered, search every other document for the old numbers in the same commit |
| L-28 | Mark anything not taken from the owner or the workbooks as an app addition or "to confirm", and list it in 15, so the owner can see what was assumed |

## About the demo data and the demo page

| # | Lesson |
| --- | --- |
| L-29 | When the owner says to remove a name, remove it from every file, including logs and changelogs, and check with a search that returns nothing. Do not quote the removed name when recording the instruction |
| L-30 | The demo client files are descriptions, not workbooks: answers are given by exception, some rows stand for many records, and one file's summary table disagrees with its own detail table. Follow the detail table and list the difference in 15 |
| L-31 | Installing a system service (`sudo` writing under `/etc/systemd`) was refused by the permission check. The outline demo runs as a plain background process and must be restarted by hand after a sandbox stop (303) |
| L-32 | `instabox-port publish 3000` without `--private` gives a public link. Say so when publishing |
| L-33 | Before a repository is made public, scan the whole history, not only the tree, for client names and secrets (`git grep ... $(git rev-list --all)`). Removing a name from the latest commit does not remove it from earlier ones. Redaction rewrites history, so do it before the first push, never after |
| L-34 | The model, effort and plugin modes (ponytail lite, full, ultra) are session settings. They are not project rules and are not recorded as instructions |
