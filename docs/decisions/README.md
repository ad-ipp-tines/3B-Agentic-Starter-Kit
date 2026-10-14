# Architecture decisions

Each decision records what we chose, why (with the principle and its source), what it costs, and when to revisit it. Add one for every change that alters how the kit works.

| # | Decision | Status |
|---|---|---|
| [0001](0001-compose-official-skills.md) | Use Tines' official plugin and skills, pinned; don't fork them | Accepted |
| [0002](0002-skills-over-one-big-prompt.md) | Skills and a short AGENTS.md, not one big prompt | Accepted |
| [0003](0003-deterministic-first.md) | Deterministic workflows first; AI only where a step needs judgment | Accepted |
| [0004](0004-git-is-source-of-truth.md) | Git is the source of truth: GitSync to the customer's GitHub, changes by pull request | Accepted |
| [0005](0005-one-orchestrator-few-subagents.md) | One working session plus read-only subagents; no multi-agent swarm in v1 | Accepted |
| [0006](0006-fresh-context-review.md) | The builder never reviews its own work | Accepted |
| [0007](0007-people-approve-the-irreversible.md) | People approve the irreversible, and hooks enforce it | Accepted |
| [0008](0008-git-to-build-mcp-for-context-cli-to-run.md) | Git to change, MCP for tenant context and actions, CLI to run and inspect | Accepted |
| [0009](0009-step-tests-and-evals-are-acceptance.md) | Step tests and evals are the acceptance test | Accepted |
| [0010](0010-private-repo-status-labels.md) | Private repo, status labels, no internal or customer content | Accepted |
| [0011](0011-mcp-direction-policy.md) | MCP in all three directions, least privilege first | Accepted |
| [0012](0012-same-skills-in-editor-and-product.md) | The same conventions in the editor and in the product | Accepted |

Template:

```markdown
# NNNN. Title
- Status: Proposed | Accepted | Superseded by NNNN
- Context: what forces the decision
- Decision: what we do
- Why: the principle, with a source link
- Consequences: what it costs, what it enables
- Revisit when: the condition that would change it
```
