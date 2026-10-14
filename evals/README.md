# Evals

Evals are how we know the kit's skills actually work, and keep working when the official `tines/skills` pin moves (decision 0009).

## What's here

| Path | What it is |
|---|---|
| `golden-tasks/<skill>.yaml` | Per skill: prompts that should and shouldn't trigger it, plus scenarios with an expected outcome and a grader |
| `rubric.md` | How to grade scenarios marked `grader: rubric` |

## How to run (v1: manual)

1. Open a **clean** session in a sandbox engagement repository, with no customer data and a sandbox 3B space.
2. **Trigger check.** Paste each `should_trigger` prompt and confirm the skill loads. Paste each `should_not_trigger` prompt and confirm it doesn't.
3. **Scenarios.** Set up the `setup` state, paste the `prompt`, and grade the outcome:
   - `grader: code`: a check you can run, such as the file existing, the CLI output, or `scripts/validate.py`;
   - `grader: rubric`: score with `rubric.md`, one dimension per judge, "Unknown" allowed.
4. Record results in a pull request: pass rate per skill, plus anything that failed and why.
5. **Baseline.** For new skills, also run the scenarios with the skill disabled. If the skill doesn't beat the baseline, it isn't earning its tokens.

Release rule: a pull request that changes a skill, or bumps `skills.lock`, re-runs that skill's golden tasks. Regressions block the merge.

## Roadmap

Automate the trigger checks and the code-graded scenarios with headless editor runs (`PLAN.md`, milestone M3).
