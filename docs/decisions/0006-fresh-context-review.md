# 0006. The builder never reviews its own work

- **Status:** Accepted
- **Context:** A session that just built a workflow is biased toward its own choices, and its context is full of the build.
- **Decision:** every workflow, skill change and kit release is reviewed by the `reviewer` subagent, or in a new session running `3b-review`. The review returns a scorecard against the spec and the AGENTS.md rules. It reports correctness gaps, not style. The builder fixes them and the reviewer re-checks: an evaluator–optimizer loop with a deterministic half (fixtures pass) and a judgment half (the scorecard).
- **Why:** an evaluator–optimizer loop works when the criteria are clear, and a fresh context isn't biased toward code it just wrote ([Building effective agents](https://www.anthropic.com/engineering/building-effective-agents); [Claude Code best practices](https://code.claude.com/docs/en/best-practices)). LLM judges are noisy on their own, so the deterministic checks come first ([Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)).
- **Consequences:** one extra pass per change. The reviewer is read-only, so it can't "fix" things quietly.
- **Revisit when:** never for production changes. For throwaway sandboxes, the person may skip it.
