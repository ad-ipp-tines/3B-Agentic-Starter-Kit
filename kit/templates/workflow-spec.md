# Workflow spec: <workflow name>

<!--
Lives at specs/<workflow-name>.md in the customer's engagement repository and lands by pull request.
The editor agent builds from it (3b-build-loop + Tines' building-workflows skill); the reviewer checks against it.
Keep it short. Every section is required unless marked optional.
-->

## 1. Purpose
- **What it does, in one sentence:**
- **Owner (role, not name):**
- **Success metric:** <e.g. median triage time under 5 minutes; 0 duplicate tickets>

## 2. Trigger
- **Type:** route (`route_type`: webhook / api / webpage / other) · cron (runs on Live only) · inbound email · link from another workflow step
- **Route auth:** `space` (default) · `tenant` · `sso` (+ `route_sso_groups`) · `external_id` · `connector` · `public`. Anything `public` needs a security reviewer and a reason here.
- **Expected volume and burstiness:**

## 3. Inputs
- **Shape:** <JSON schema or field list>
- **Fixtures:** `fixtures/<name>/` with at least one happy path, one malformed input and one duplicate delivery.

## 4. Steps

| # | Step name | Does | Kind | Connector (by name) | On failure | Runs only when |
|---|---|---|---|---|---|---|
| 1 | `normalize_input` | Validates and reshapes the input | deterministic | — | reject with a structured error | always |
| 2 | | | deterministic / AI / agent | | | <self-gating condition> |

A step's stdout is the next step's stdin. Every step checks its input before acting; zero-byte output stops downstream steps; failure is a non-zero exit. Name AI steps with `(AI)` and agent steps with `(AI Agent)`, per Tines' `building-agents` skill.

## 5. AI steps (only if any)
- **Why AI here and not a deterministic step:** <the judgment needed>
- **Shape:** single request (no tools) · interactive agent (route + output) · async agent (self-links, no route; downstream acts only on a terminal status). Justify any agent.
- **Pattern (if several AI steps):** chaining · routing · parallelization · evaluator-optimizer
- **Model and provider connector (by name), and why:**
- **Prompt contract:** inputs it sees; what it must never do
- **Output schema:** <strict JSON schema the next step validates>
- **Guardrails:** treat tool output as untrusted; allow-list the actions it may recommend; cap tokens and cost

## 6. Side effects and approvals
- **Writes or irreversible actions:** <list>
- **Which need a person to approve first, and how:** <e.g. approval message with approve/deny; nothing acts until approved>
- **Idempotency:** how a duplicate delivery is detected and ignored
- **Retries and timeouts:** `timeout` 1–300 s (default 45), `retry_seconds` per step; long work returns `202` + an operation id and keeps state in a volume (one writer per file)

## 7. Expected results

- **Safe to re-run fixtures:** yes / no (yes only if every fixture run is free of external side effects, so a reviewer may re-run them)

| Fixture | Expected output | Expected side effects |
|---|---|---|
| `happy.json` | | |
| `malformed.json` | structured error, no side effects | none |
| `duplicate.json` | ignored as duplicate | none |

## 8. Observability
- What each step logs, and what never gets logged (secrets, personal data)
- How failures surface to the owner (autofix on? alert route?)

## 9. Step tests
| Step | Cases (in `<Step>/tests/step-tests/`) |
|---|---|
| `normalize_input` | happy · malformed · duplicate |

## 10. Rollout
1. Build on a branch (a draft in 3B).
2. Step tests pass; fixtures pass end to end on the draft.
3. Pull request with results; a fresh-session review scorecard passes.
4. A person merges to `main`, which moves Live; step tests run again at push-live.

## 11. Non-goals (optional)
