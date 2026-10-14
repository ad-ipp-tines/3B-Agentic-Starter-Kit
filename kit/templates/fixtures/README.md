# Fixtures

Fixtures are whole-workflow test inputs. They complement 3B **step tests** (per-step, hermetic, run automatically at push-live).

One folder per workflow: `fixtures/<workflow-name>/`, with at least:

| File | Purpose |
|---|---|
| `happy.json` | A realistic, valid input |
| `malformed.json` | Missing or wrong fields → structured error, no side effects |
| `duplicate.json` | The same event delivered twice → the second is ignored |

Add one for every bug you fix — and a step test for the step that broke.

Run one end to end on a draft branch (ask first if the workflow has side effects):

```bash
cat fixtures/<workflow-name>/happy.json | 3b run <workflow-id> --wait --type application/json --branch <draft-branch-id>
```

Synthetic data only — no real customer payloads, personal data or secrets.
