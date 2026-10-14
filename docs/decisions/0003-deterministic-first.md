# 0003. Deterministic workflows first; AI only where a step needs judgment

- **Status:** Accepted
- **Context:** Customers ask for "agents". Most of their use cases are predictable sequences with one or two judgment calls in them. An agent loop on a predictable path adds cost, latency and new failure modes.
- **Decision:** every use case gets an `agentic_fit` in the backlog (`deterministic`, `ai-step`, `workflow-of-ai`, `agent`), and the spec must justify any step up that ladder. The default build is a deterministic 3B workflow, written by the builder AI, with an AI call inside a step only where that step needs judgment. That call has a strict output schema the next step validates. Agent loops need explicit stopping conditions, tool limits and approval gates.
- **Why:** Anthropic's guidance is to find the simplest solution that works and add complexity only when it measurably helps, using workflows for predictable paths and agents for open-ended ones ([Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)). It's also 3B's own frame: build with AI, run deterministically.
- **Consequences:** fewer "wow, an agent" demos early on, and more workflows that survive production. Agentic work moves to phase 3, once the customer has a working deterministic baseline to compare against.
- **Revisit when:** evals show an agent outperforming the workflow on a use case by a margin worth its cost.
