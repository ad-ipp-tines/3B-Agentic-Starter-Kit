# Runbook: <workflow name>

- **Owner (role):**
- **What it does:** <one sentence, from the spec>
- **Trigger and auth:**
- **Connectors (by name):**
- **Live since:** <date>, pushed live by <role>

## Normal operation
- Expected volume:
- Expected duration per run:
- Where to look: the workflow's runs in the 3B UI or over MCP. CLI examples (confirm with `3b --help`, VERIFY V11): `3b runs <workflow-id>`, `3b executions <workflow-id> --status error`

## When it fails
1. Find the failing execution in the UI or over MCP (CLI example: `3b executions <workflow-id> --status error --step <step>`)
2. Read its output and logs (CLI examples: `3b output <execution-id>`, `3b logs <execution-id>`)
3. If autofix opened a fix, review it in a fresh session before approving.
4. Reproduce with the matching fixture on a draft (documented: `cat fixture.json | 3b run <workflow-id> --wait`; targeting a draft branch from the CLI is VERIFY V13)
5. Escalate to: <role>, if <condition>

## Known failure modes
| Symptom | Likely cause | Fix |
|---|---|---|
| | | |

## Cost
- AI calls per run and the model used:
- Spend limit that applies:

## Change process
Changes start as a spec edit in git, are built on a draft branch, pass the fixtures and a fresh-session review, and go live only when a person pushes them.
