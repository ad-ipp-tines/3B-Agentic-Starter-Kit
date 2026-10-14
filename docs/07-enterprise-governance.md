# Enterprise governance checklist

What a security, risk or platform team will ask, what the kit does about it, and the evidence to collect. Confirm 3B specifics on your tenant (`docs/02-availability.md`).

| Area | What to require | Evidence |
|---|---|---|
| **Identity** | SSO for 3B and for the editors; a known provisioning mode; new users have no access until added to a group | IdP configuration; a test login; a joiner test showing no access before a group grant |
| **Access** | One space per team with one dedicated group; builders aren't tenant admins; push-live, connector-admin, network-creator and key permissions held by named roles | Role and permission export; a negative test (a builder can't publish) |
| **Change control** | Production spaces Git-synced; `main` protected and requiring review; Live moves only by a merged PR; step tests run at push-live | Branch protection settings; a merged PR linked to the Live change; a failed-test-blocks-release drill |
| **Agent guardrails** | Editors use OAuth; guard hooks installed; agents can't publish, delete, grant or handle keys | `.claude/settings.json` and `.cursor/hooks.json`; a transcript of a denied `push_live` |
| **Secrets** | Credentials only in connectors; none in repos, prompts, skills, volumes or logs; service accounts for automation | Secret-scan results (`scripts/validate.py`, `scripts/check_specs.py`); connector list per space |
| **MCP exposure** | Workflow-served MCP behind `space`, `tenant` or `sso` routes; read-only tools first; an approved tool list per server | The route config; the approved tool list; the audit trail of calls |
| **AI use** | A provider connector and model per workflow; output schemas; approvals on consequential actions; eval results before Live | Spec section 5; the eval report with pass rate and cost per run |
| **Audit** | Audit logs forwarded to the SIEM; MCP actions attributed to users | A sample audit export showing MCP-tagged actions; retention policy (confirm with the account team) |
| **Cost** | Tines Units and AI spend reviewed weekly; alert on unusual growth | The monitoring view; provider usage reports; weekly review notes |
| **Data** | Data-flow map: which systems, which model provider, which region | The provider's terms; the residency answer from the account team |

## Questions to ask vendors (3B, the model provider, the editor vendor)

1. Which attestations cover the service (SOC 2 Type II, ISO 27001)?
2. Is our data used for training? What's the retention, and is zero-retention available?
3. Where does inference run, and who are the subprocessors?
4. How is AI-generated code isolated at runtime?
5. How are third-party skills and MCP servers vetted, pinned and revoked?
6. Is there evidence of prompt-injection testing?
7. Do MCP endpoints follow the MCP authorization spec (audience-bound tokens, no passthrough)?
8. Is tool-level authorization available on MCP servers?
9. Are agent actions logged with identity, exportable, and retained for how long?

## Crosswalk to OWASP

| Risk ([LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/), [Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)) | Kit control |
|---|---|
| Prompt injection / goal hijack (LLM01, ASI01) | Untrusted-input rule in every skill; approvals before side effects; allow-listed AI actions |
| Excessive agency (LLM03, ASI02/ASI03) | Read-only subagents; guard hooks; read-only MCP tools first; people-only publishing |
| Supply chain (LLM04, ASI04) | Official skills pinned in `skills.lock`; skill changes by PR; golden tasks re-run on bumps |
| Unbounded consumption (LLM06) | Token budgets on AI steps; weekly cost review; TU monitoring |
| Hidden context exposure (LLM08) | No secrets or authorization logic in prompts or skills |
| Cascading failures (ASI08) | Step tests at push-live; one workflow per PR; autofix proposals reviewed before merge |
