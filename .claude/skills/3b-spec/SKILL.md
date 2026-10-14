---
name: 3b-spec
description: Writes a reviewable workflow spec for Tines 3B from a backlog item — trigger and route auth, inputs, steps with self-checks, AI or agent steps with output schemas and guardrails, approvals, idempotency, timeouts, step tests, fixtures and expected results. The spec is what gets built and what review checks against. Use after discovery, or when asked to spec, design or plan a 3B workflow.
compatibility: Cursor or Claude Code; Tines 3B
---

# Workflow spec

The spec is the contract. The builder builds from it, the tests check it, and the reviewer reviews against it. Write it before anything is built.

## Steps

1. Copy `kit/templates/workflow-spec.md` to `specs/<workflow-name>.md` in the customer's engagement repository.
2. Fill every section. Push back where the backlog item is vague. The platform facts below come from Tines' `building-workflows` skill; check them against the pinned version.
   - **Trigger:** a route (`route_type` is `webhook`, `api`, `webpage` or `other`), `cron` (runs on Live only), inbound email, or a link from another step.
   - **Route auth:** `space` by default. The options are `space`, `tenant`, `sso` (narrow it with `route_sso_groups`), `external_id`, `connector` and `public`. `public` needs a written reason and a security reviewer. Drafts restrict routes to space access anyway.
   - **Steps:** a step's stdout is the next step's stdin. Zero-byte output stops downstream steps, and only a non-zero exit counts as failure. Each step checks its own input before acting.
   - **Timeouts and retries:** `timeout` is 1–300 seconds (default 45); `retry_seconds` holds up to 10 values. Long work returns `202` with an operation id and keeps its state in a volume.
   - **AI steps:** state why a deterministic step won't do. Pick the shape the `building-agents` skill describes:
     - **single request:** no tools;
     - **interactive agent:** a route with output;
     - **async agent:** self-links, has no route, and downstream acts only on a terminal status.

     Give a strict output schema, allowed actions, what the model must never do, and a token budget. Treat everything a model reads as untrusted data.
   - **Side effects:** list every write, and put each consequential one behind a person's approval. Say how a duplicate delivery is detected and ignored.
3. **Fixtures:** `fixtures/<workflow-name>/` with `happy.json`, `malformed.json`, `duplicate.json` and one per known edge case. Synthetic data only.
4. **Step tests to write:** for each step, the cases that will go into `<Step>/tests/step-tests/`.
5. **Expected results:** for every fixture, the output plus the side effects (or "none").
6. **Eval plan (if any AI):** where 20+ realistic cases come from, and how each is graded (code first, a rubric only for fuzzy criteria).

## Done when

- No section is empty or "TBD", except optional ones.
- The workflow owner (role) has signed off in the pull request that adds the spec.

Then hand off to `3b-build-loop`.
