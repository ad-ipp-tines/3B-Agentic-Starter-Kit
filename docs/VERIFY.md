# VERIFY register

Things the kit relies on, or mentions, that aren't confirmed yet. Close an item by testing it on a sandbox tenant (or finding a public source), then update `docs/02-availability.md` and remove the row here.

| # | Item | Why it matters | How to verify | Owner |
|---|---|---|---|---|
| V1 | The full 3B MCP tool list (names, read/write, schemas) | Guard hook patterns; skills can't name tools until known | Connect with OAuth, run `tools/list`, record it in `docs/02-availability.md` | Kit maintainer |
| V2 | CLI sign-in: `3b configure` vs `3b auth login --host` | Setup docs and readiness | Install the CLI on a sandbox tenant; read `3b --help` | Kit maintainer |
| V3 | Per-tool authorization on workflow-served MCP servers | Whether one server can mix read and write tools safely | Build a two-tool server; test with two users in different groups | Kit maintainer |
| V4 | The same skill bundle behaving identically in 3B and in Cursor/Claude Code | ADR 0012 | Import `tenant-skills/enterprise-conventions` into a sandbox space, run golden task conventions-01 in both | Kit maintainer |
| V5 | Whether dot-folders (`.github`, `.claude`) are allowed at the top of a space repository | Whether any config can live in the space repo | Push a branch containing `.github/` to a sandbox space; observe | Kit maintainer |
| V6 | Pinning with `npx skills` (tag or tree path) | Fallback when gh is older than 2.90 | Try `npx skills add https://github.com/tines/skills/tree/<tag>/skills` | Kit maintainer |
| V7 | Cursor hook behaviour: `failClosed`, output on allow, double-run with imported Claude hooks | Guard reliability | Trigger allowed and denied calls in Cursor; read the hook logs | Kit maintainer |
| V8 | Where autofix and autotune branches land in Git-synced spaces | Review flow for proposals | Break a sandbox workflow; watch the GitHub repository | Kit maintainer |
| V9 | Audit log retention and export path | Governance evidence | Ask the account team; test the export | Customer platform owner |
| V10 | Hosting region and data residency per plan | Governance evidence | Account team | Customer platform owner |
