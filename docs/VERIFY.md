# VERIFY register

Things the kit relies on, or mentions, that aren't confirmed yet. Close an item by testing it on a sandbox tenant (or finding a public source), then update `docs/02-availability.md` and remove the row here.

| # | Item | Why it matters | How to verify | Owner |
|---|---|---|---|---|
| V1 | The full 3B MCP tool list (names, read/run/build/publish, schemas) | Guard patterns; skills can't name tools until known | Connect with OAuth, run `tools/list`, record it in `docs/02-availability.md`; then anchor `guard.py` to exact names | Kit maintainer |
| V2 | CLI sign-in: `3b configure` vs `3b auth login --host` | Setup docs and readiness | Install the CLI on a sandbox tenant; read `3b --help` | Kit maintainer |
| V3 | Per-tool authorization on workflow-served MCP servers | Whether one server can mix read and write tools safely | Build a two-tool server; test with two users in different groups | Kit maintainer |
| V4 | The same skill bundle behaving identically in 3B and in Cursor/Claude Code | ADR 0012 | Import `tenant-skills/enterprise-conventions` into a sandbox space; run golden task conventions-01 in both | Kit maintainer |
| V5 | Whether dot-folders (`.github`, `.claude`) are allowed at the top of a space repository | Whether any config can live in the space repo | Push a branch containing `.github/` to a sandbox space; observe | Kit maintainer |
| V6 | Pinning with `npx skills` (tag or tree path); `gh skill install --agent/--scope` destinations | Fallback when gh is older than 2.90; where pinned skills land | Try `npx skills add https://github.com/tines/skills/tree/<tag>/skills`; run `gh skill install` and list the result | Kit maintainer |
| V7 | Cursor hook contract: stdin keys (`tool_name`? `command`? `hook_event_name`?), output keys (`userMessage` vs `user_message`), `failClosed` behaviour, and whether imported Claude Code hooks run alongside `.cursor/hooks.json` | Guard reliability in Cursor | Trigger allowed and denied shell and MCP calls in Cursor with a logging wrapper around `guard.py`; record the payloads | Kit maintainer |
| V8 | Where autofix and autotune branches land in Git-synced spaces | Review flow for proposals | Break a sandbox workflow; watch the GitHub repository | Kit maintainer |
| V9 | Audit log retention and export path | Governance evidence | Ask the account team; test the export | Customer platform owner |
| V10 | Hosting region and data residency per plan | Governance evidence | Account team | Customer platform owner |
| V11 | The 3B CLI command surface beyond `3b run <id> --wait`: `spaces`, `runs`, `executions --status --step`, `output`, `logs`, `run --type --branch`, `apps`, `version` | Skills and runbooks cite these; no public CLI reference exists | `3b --help` and each subcommand's `--help` on a sandbox; record the real names and flags, then update every skill and template | Kit maintainer |
| V12 | An on-demand way to run step tests before a pull request (CLI, MCP tool or UI) | The build loop wants a pre-PR gate; only automatic runs at push-live are documented | Look for a test runner in the CLI, MCP tool list and UI on a sandbox | Kit maintainer |
| V13 | How a GitHub branch in a Git-synced space maps to a 3B draft, and how an agent finds the draft id to run fixtures against it | The build loop runs fixtures "on the draft branch" | Push a branch to a synced sandbox space; observe the draft; find the id in the UI, MCP and CLI | Kit maintainer |
| V14 | Claude Code subagent frontmatter: `disallowedTools` honoured; MCP tools inherited when `tools` is omitted | Read-only subagents in Claude Code | Run `solution-architect` and `reviewer` in Claude Code; attempt a Write; list available tools | Kit maintainer |
