# 0005. One working session plus read-only subagents; no multi-agent swarm in v1

- **Status:** Accepted
- **Context:** Multi-agent setups look impressive in demos. Building one workflow is mostly sequential and shares a lot of context: the spec, the tenant state, the test results.
- **Decision:** one working session (driven by the `onboarding-lead` subagent or the `3b-onboard` skill) does the work. Specialist subagents are read-only and used for exactly two jobs:
  - investigation that reads a lot (`solution-architect`);
  - fresh-context checking (`reviewer`).

  Only the `builder` changes the tenant, and only after a person approves the plan.
- **Why:** multi-agent systems use about 15× the tokens of chat and are a poor fit when agents share context or depend on each other, which describes most coding tasks. Subagents earn their place when work is read-heavy and their condensed result is all that returns ([Anthropic, multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system); [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)). They also widen the attack surface (OWASP ASI07, ASI08).
- **Consequences:** lower cost and simpler failure analysis. Parallel work is limited to genuinely independent research, such as reading the API docs for several connectors at once.
- **Revisit when:** evals show a parallel design beating the single session on a class of tasks by enough to justify the cost.
