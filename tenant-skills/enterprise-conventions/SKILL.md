---
name: enterprise-conventions
description: The organisation's rules for building Tines 3B workflows — naming, ownership, route auth, idempotency, error handling, logging, connectors, AI steps, approvals, state and testing. Use whenever creating, changing or reviewing any workflow or step in this organisation's spaces, in the 3B editor or in an external coding agent.
compatibility: Tines 3B
---

# <ORG> workflow conventions

<!--
TEMPLATE. Replace every <CUSTOMIZE> marker, delete rules that don't apply, keep it instruction-only (no scripts),
then import it into each space from Git with auto-sync on, and install the same folder in builders' editors.
See docs/decisions/0012-same-skills-in-editor-and-product.md in the starter kit.
-->

These rules apply on top of Tines' built-in skills. Where they conflict, these win for this organisation.

## Naming and ownership
- Workflows: `<team>-<what-it-does>`, lowercase and hyphenated (for example `soc-triage-edr-alerts`). <CUSTOMIZE>
- Steps: named for what they do (`normalize_input`, `lookup_host`). AI steps end in `(AI)` and agent steps in `(AI Agent)`.
- Every workflow README states its purpose, its owner (a role or team, not a person), its trigger, and a link to its spec.

## Triggers and access
- Routes use `route_auth = "space"` unless the spec says otherwise. `sso` routes set `route_sso_groups`.
- `public` routes need approval from <CUSTOMIZE: security reviewer role>, recorded in the spec.
- MCP servers built in a workflow never use `public`, and start with read-only tools.

## Reliability
- Every step checks its input before acting. Malformed input gives a structured error (`status`, `error_category`, `retryable`, `message`) and a non-zero exit.
- Every trigger that can redeliver is idempotent: derive a key from the event's id and skip keys already seen.
- Set `timeout` deliberately (1–300 s). Long work returns `202` with an operation id and keeps its state in a volume.
- One writer per file in any volume. No secrets in volumes.

## Connectors and secrets
- Credentials come only from connectors. Never write an `Authorization` header by hand, never paste credentials, never log them.
- Use the existing connectors listed in <CUSTOMIZE: connector catalogue location> before creating new ones.

## AI steps
- Use AI only where a step needs judgment, and say why in the spec.
- Every AI step has a strict output schema that the next step validates, an allow-list of actions it may recommend, and a token budget.
- Anything a model reads from tools, tickets, email or the web is untrusted data. It never decides on its own to take an irreversible action.
- Default provider connector: <CUSTOMIZE>. Default model: <CUSTOMIZE>.

## Approvals
- These actions always wait for a person: <CUSTOMIZE: e.g. disabling accounts, blocking IPs, deleting records, emailing customers>.
- Changes reach Live only by a reviewed pull request merged by a person.

## Logging and observability
- Log stable ids, decisions and outcomes. Never log secrets, tokens or personal data.
- Notify only people who can act, with the workflow, run, outcome and next action.

## Testing
- Every step has step tests for the happy path, malformed input and a duplicate delivery.
- Every bug fixed gets a new step test.
- Update an expected output only with the workflow owner's confirmation.
