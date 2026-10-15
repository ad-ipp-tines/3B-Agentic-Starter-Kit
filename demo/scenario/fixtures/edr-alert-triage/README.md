# Fixtures: edr-alert-triage

Synthetic. The sha256 of all zeros is the one entry on the demo block list.

| File | Scenario | Expected |
|---|---|---|
| `happy.json` | High-severity alert with a listed hash | P1, one ticket |
| `malformed.json` | No indicator, no severity, bad timestamp | structured `malformed_input` error, no side effects |
| `duplicate.json` | Same `event_id` as `happy.json`, delivered 5 s later | `check_duplicate` emits nothing; no second ticket |

Run on the draft branch (ask first on a shared sandbox):

```bash
cat fixtures/edr-alert-triage/happy.json | 3b run <workflow-id> --wait --type application/json --branch <draft-branch-id>
```
