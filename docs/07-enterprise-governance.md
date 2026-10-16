# Enterprise governance

What a security, risk or platform team will ask, which control answers it, where that control is enforced, and the evidence to collect. Confirm 3B specifics on your tenant ([availability](02-availability.md)).

## The control matrix

Read the "Enforced by" column first. Hooks appear in it only as "early catch": they live in files the builder owns, and Cursor cloud agents don't run MCP hooks, so they're defence in depth, not the control.

| Control | Enforced by | Early catch | Evidence |
|---|---|---|---|
| Live moves only when a person merges | GitHub branch protection on `main` (required review, CODEOWNERS); 3B refuses `push_live` in Git-synced spaces | `guard.py` denies `git push … main`, `gh pr merge`, merge API calls | Branch protection export; a merged PR linked to the Live change; a denied-push transcript |
| Builders can't publish directly | 3B RBAC: push-live permission held by named roles, not builders | `guard.py` denies publish-shaped MCP tools | Role matrix; a negative test from `3b-readiness` (a builder's `push_live` is refused) |
| Agents act as a person, with that person's permissions | 3B MCP over OAuth; audit logs tag MCP actions | — | Audit export showing MCP-tagged actions with user identity |
| Automation can't edit or publish | 3B: service-account tokens explore, run, and ask the in-product agent to build drafts; they can't edit or publish. Scope them to non-production spaces | — | Service-account inventory with space scope |
| Credentials never reach code or the model | 3B connectors and the credential proxy | `guard.py` denies reading the API key; `validate.py` and `check_specs.py` scan for secrets | Connector list per space; secret-scan results in CI |
| Connector and access changes need a person | 3B RBAC (connector-admin, group managers) | `guard.py` denies connect/disconnect and grant/revoke-shaped calls | Change log of connector grants; approval records in PRs |
| Changes are specified before they're built | Spec PR with the owner's approval; `check_specs.py` in CI | — | Merged spec PRs |
| Every step is tested | 3B step tests run at push-live; a failing test blocks the release | Build loop writes tests before the PR | Step-test files per step; a blocked-release drill |
| Nothing ships without a fresh review | Branch protection's required review; the kit's `reviewer` subagent scorecard on every PR | — | Scorecards on merged PRs |
| Skills and MCP servers are pinned | `skills.lock` reviewed by PR; managed MCP allowlists in the editors | `guard.py` denies ad-hoc `npx skills`/`gh skill install` | `skills.lock` history; the editor's allowlist export |
| Workflow-served MCP is behind platform OAuth, never public | 3B route auth (`space`, `tenant`, `sso`); the platform runs OAuth 2.1 | `3b-review` scorecard row 7 | Route configs; approved tool list per server |
| No customer or internal data in the kit | `validate.py` denylist (local file or the `HYGIENE_DENYLIST` CI secret) | — | CI logs |

**Honest limits:** GitSync is documented for GitHub only. A GitLab or Azure DevOps customer's path today is the direct space clone, where a push to `main` publishes with no pull-request gate; the compensating control is 3B RBAC on who may push, plus review in the engagement repository before anyone pushes. Say this in phase 0.

## What to require, by area

| Area | Require | Evidence |
|---|---|---|
| **Identity** | SSO for 3B and for the editors; a known provisioning mode; new users have no access until added to a group | IdP configuration; a test login; a joiner test |
| **Access** | One space per team with one dedicated group; builders aren't tenant admins; push-live, connector-admin, network-creator and key permissions held by named roles | Role export; negative tests from `3b-readiness` |
| **Change control** | Production spaces Git-synced to GitHub; `main` protected; Live moves only by a merged PR; step tests at push-live | Branch protection settings; merged PRs; a blocked-release drill |
| **Agent guardrails** | OAuth for builders; hooks installed in both editors; a written list of people-only actions | Hook configs; a denied-call transcript; the list |
| **Secrets** | Credentials only in connectors; none in repos, prompts, skills, volumes or logs; service accounts scoped to non-production | Secret scans; connector list; service-account inventory |
| **MCP exposure** | Workflow-served MCP behind `space`, `tenant` or `sso`; read-only tools first; an approved tool list per server | Route config; tool list; audit trail |
| **AI use** | A provider connector and model per workflow; output schemas; approvals on consequential actions; eval results before Live | Spec §5; eval report with pass rate and cost per run |
| **Audit** | Audit logs forwarded to the SIEM; MCP actions attributed to users | Sample export; retention policy (account team) |
| **Cost** | Tines Units and AI spend reviewed weekly | Monitoring view; weekly notes |
| **Data** | Data-flow map: systems, model provider, region | Provider terms; the residency answer |

## Questions to ask vendors (3B, the model provider, the editor vendor)

Record the answers in the engagement repository's `onboarding/governance.md`.

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
| Prompt injection / goal hijack (LLM01, ASI01) | Untrusted-input rule in `AGENTS.md` and every skill; approvals before side effects; allow-listed AI actions |
| Excessive agency (LLM03, ASI02/ASI03) | Builders without push-live; read-only subagents; read-only MCP tools first; people-only merge |
| Supply chain (LLM04, ASI04) | Official skills pinned in `skills.lock`; ad-hoc installs denied for agents; golden tasks re-run on bumps |
| Unbounded consumption (LLM06) | Token budgets on AI steps; weekly cost review; TU monitoring |
| Hidden context exposure (LLM08) | No secrets or authorization logic in prompts or skills |
| Cascading failures (ASI08) | Step tests at push-live; one workflow per PR; autofix proposals reviewed before merge |
