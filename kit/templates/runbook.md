# Runbook: <workflow name>

- **Owner (role):**
- **What it does:** <one sentence, from the spec>
- **Trigger and auth:**
- **Connectors (by name):**
- **Live since:** <date>, pushed live by <role>

## Normal operation
- Expected volume:
- Expected duration per run:
- Where to look: `3b runs <workflow-id>`, `3b executions <workflow-id> --status error`

## When it fails
1. Find the failing execution: `3b executions <workflow-id> --status error --step <step>`
2. Read its output and logs: `3b output <execution-id>`, `3b logs <execution-id>`
3. If autofix opened a fix, review it in a fresh session before approving.
4. Reproduce with the matching fixture on a draft branch: `3b run <workflow-id> --wait --branch <branch-id>`
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
