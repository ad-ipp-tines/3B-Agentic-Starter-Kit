# 0009. Step tests and evals are the acceptance test

- **Status:** Accepted
- **Context:** "It looks right" is how AI-built work fails in production. 3B has native **step tests**: captured input and output pairs in `<Step>/tests/step-tests/`, replayed hermetically with no network access, compared byte for byte, and run automatically when a workflow is pushed live ([step tests](https://docs.3b.tines.com/en/articles/17431715-capture-a-step-s-correct-behavior-with-step-tests); `building-workflows` testing reference).
- **Decision:**
  - **Deterministic layer.** Every step has step tests covering the happy path, malformed input and a duplicate delivery, plus one test per bug fixed. Update an expected output only after the workflow owner confirms the new behaviour.
  - **Workflow layer.** Run the spec's fixtures end to end on a draft branch before the pull request. Ask before any run with side effects.
  - **AI layer.** Every AI or agent step needs an eval set of at least 20 realistic cases before it goes live, with the pass rate and cost per run recorded. Grade with code first. LLM judges score one dimension each, with a rubric and an "Unknown" option, and use a different model from the one being tested.
  - **Kit layer.** Every kit skill has golden tasks in `evals/golden-tasks/` with should-trigger and should-not-trigger prompts and a reference outcome.
- **Why:** start with 20–50 tasks drawn from real failures; grade outcomes, not paths; prefer deterministic graders; keep capability and regression suites separate ([Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents); [Agent Skills best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)). Step tests make the deterministic layer native and enforced at push-live.
- **Consequences:** writing tests takes time up front and saves the first incident. Step tests can't run in external CI yet (planned), so pull-request CI checks structure and specs, and the platform runs the step tests at push-live.
- **Revisit when:** step tests can run in CI. Then add them to `kit/engagement-repo-template/.github/workflows/`.
