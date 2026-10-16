# Workflow spec: edr-alert-triage

<!-- Demo scenario. Synthetic throughout. Copy to specs/edr-alert-triage.md in the engagement repository. -->

## 1. Purpose
- **What it does, in one sentence:** receives EDR alerts, drops duplicates, checks the indicator against a block list, assigns a priority and opens a ticket.
- **Owner (role, not name):** SOC lead
- **Success metric:** every unique high-severity alert has a ticket within 2 minutes; zero duplicate tickets.

## 2. Trigger
- **Type:** route, `route_type = "webhook"`
- **Route auth:** `space` for the sandbox demo. In production, `external_id` for the EDR's webhook sender (the id is minted in 3B and configured in the EDR by a person). Never `public`.
- **Expected volume and burstiness:** tens per hour; bursts of 50 within a minute during an outbreak, with redeliveries.

## 3. Inputs
- **Shape:**
  ```json
  { "event_id": "string, unique per alert",
    "source": "string, e.g. edr",
    "severity": "low | medium | high | critical",
    "host": "string",
    "indicator": { "type": "sha256 | ip | domain", "value": "string" },
    "observed_at": "ISO 8601" }
  ```
- **Fixtures:** `fixtures/edr-alert-triage/happy.json`, `malformed.json`, `duplicate.json`.

## 4. Steps

| # | Step name | Does | Kind | Connector (by name) | On failure | Runs only when |
|---|---|---|---|---|---|---|
| 1 | `normalize_alert` | Validates the shape, lowercases the indicator, derives `dedupe_key = event_id` | deterministic | — | structured error `{status:"error", error_category:"malformed_input", retryable:false, message}`; non-zero exit | always |
| 2 | `check_duplicate` | Looks up `dedupe_key` in volume `seen`; records it if new | deterministic | — | structured error, retryable | input has a `dedupe_key` |
| 3 | `check_blocklist` | Matches the indicator against the static list in the step's assets; emits `known_bad: true/false` | deterministic | — | structured error | `check_duplicate` emitted `is_new: true` |
| 4 | `decide_priority` | `known_bad && severity in [high, critical]` → P1; `known_bad` → P2; `severity == critical` → P2; else P3 | deterministic | — | structured error | always (after step 3) |
| 5 | `create_ticket` | Opens a ticket with host, indicator, priority, `event_id`; writes the ticket id back to volume `seen` | deterministic | `ticketing` (sandbox fallback: write JSON to volume `tickets`) | retry per `retry_seconds`, then structured error and an owner notification | priority is P1 or P2, or severity is high |

Every step checks its input before acting; a step may be triggered when an earlier step emitted nothing for it. Zero-byte output from `check_duplicate` on a duplicate stops downstream steps by design.

## 5. AI steps
None in this version. (Stretch: `summarize_alert (AI)`, single request, output schema `{summary: string, recommended_priority: "P1"|"P2"|"P3"}`; `decide_priority` treats it as a recommendation and still applies the rules above.)

## 6. Side effects and approvals
- **Writes or irreversible actions:** ticket creation; volume writes to `seen` and `tickets`.
- **Which need a person to approve first:** none in this version; ticket creation is reversible (a ticket can be closed). Any future "isolate host" step waits for a person.
- **Idempotency:** `dedupe_key = event_id` in volume `seen`; a second delivery emits nothing and ends the run.
- **Retries and timeouts:** `timeout = 45`; `retry_seconds = [5, 30, 120]` on `create_ticket` only.

## 7. Expected results

- **Safe to re-run fixtures:** yes (sandbox: the ticket goes to the `tickets` volume or a sandbox ticketing project)

| Fixture | Expected output | Expected side effects |
|---|---|---|
| `happy.json` | `{priority:"P1", known_bad:true, ticket_id: a non-empty string}` | one ticket; `seen` contains `evt-0001` |
| `malformed.json` | `{status:"error", error_category:"malformed_input", retryable:false}` | none |
| `duplicate.json` | no output from `check_duplicate`; downstream steps don't run | none; `seen` unchanged |

## 8. Observability
- Each step logs `event_id`, step name, outcome and timing. Never the raw payload, never credentials.
- Failures surface to the SOC lead through the step-failure notification; autofix is on after Live.

## 9. Step tests
| Step | Cases |
|---|---|
| `normalize_alert` | happy · missing indicator · bad severity · uppercase hash normalised |
| `check_duplicate` | new key · seen key (zero-byte output) |
| `check_blocklist` | listed hash · unlisted hash · ip indicator |
| `decide_priority` | each rule branch (4 cases) |
| `create_ticket` | happy · connector unavailable (retry path) |

## 10. Rollout
1. Build on `build/edr-alert-triage` (a draft).
2. Step tests pass; fixtures pass end to end on the draft.
3. Pull request with results; fresh-session review scorecard passes.
4. A person merges to `main`; 3B runs the step tests at push-live.

## 11. Non-goals
No host isolation, no analyst chat, no enrichment beyond the block list. Those are separate use cases with their own specs and approvals.
