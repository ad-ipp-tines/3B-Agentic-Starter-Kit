# Governance record

Answers to the questions a security or risk review asks, with evidence links. Roles, not names. Kept current by the platform owner; `3b-readiness` and `3b-handover` read it.

## Controls in place

| Control | Enforced by | Verified on (date) | Evidence (link) |
|---|---|---|---|
| Builders don't hold push-live | 3B RBAC | | |
| `main` protected: required review, CODEOWNERS | GitHub branch protection | | |
| Production spaces Git-synced | 3B GitSync | | |
| Service accounts scoped to non-production | 3B RBAC | | |
| Editors connect over OAuth | 3B MCP | | |
| Guard hook installed in both editors | engagement repository | | |
| Audit logs forwarded | 3B settings | | |

## Vendor answers

| # | Question | 3B | Model provider | Editor vendor | Evidence |
|---|---|---|---|---|---|
| 1 | Attestations (SOC 2 Type II, ISO 27001) | | | | |
| 2 | Training on our data; retention; zero-retention option | | | | |
| 3 | Inference region; subprocessors | | | | |
| 4 | Isolation of AI-generated code at runtime | | | | |
| 5 | Vetting, pinning and revoking skills and MCP servers | | | | |
| 6 | Prompt-injection testing evidence | | | | |
| 7 | MCP authorization spec conformance | | | | |
| 8 | Tool-level authorization on MCP servers | | | | |
| 9 | Agent actions logged with identity; export; retention | | | | |

## Open items
<!-- link to the kit's VERIFY register items that apply to this tenant, with owners -->
