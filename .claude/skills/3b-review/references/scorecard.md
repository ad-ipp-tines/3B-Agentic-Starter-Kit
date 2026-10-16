# Review scorecard

Each row is **Pass**, **Fix** or **Unverified**, with one line of evidence.

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Built behaviour matches every section of the spec | | |
| 2 | Step tests exist for each changed step (happy, malformed, duplicate, plus each bug fixed), and no expected output changed without the owner's confirmation | | |
| 3 | Fixtures pass end to end on the draft, and the results match **Expected results** | | |
| 4 | Malformed input gives a structured error and no side effects | | |
| 5 | Duplicate delivery is detected and ignored | | |
| 6 | Each step checks its input. Zero-byte output is used deliberately to stop downstream steps; failures exit non-zero | | |
| 7 | Route auth matches the spec: `space` (default), `tenant`, `sso` (with `route_sso_groups`), `external_id` or `connector`. `public` only with a written reason and a named reviewer. Workflow-served MCP never `public` | | |
| 8 | Credentials come only from connectors: no hand-written `Authorization` headers, no secrets in code, volumes, logs or outputs | | |
| 9 | AI steps: the right shape (single request, interactive agent, or async agent that self-links), a strict output schema validated downstream, allowed actions, a token budget | | |
| 10 | Every consequential action waits for a person's approval | | |
| 11 | Timeouts within 1–300 s. Long work returns an operation id and keeps state in a volume, with one writer per file | | |
| 12 | Logs record stable ids and outcomes, never secrets or personal data | | |
| 13 | The runbook exists and matches the workflow | | |
| 14 | Every 3B capability relied on is Available (`docs/02-availability.md`), not Verify | | |
| 15 | What breaks first under load or a vendor outage, and is that acceptable? | | |

**Top three fixes:**
1.
2.
3.

**Verdict:** ready to merge / not ready, because …
