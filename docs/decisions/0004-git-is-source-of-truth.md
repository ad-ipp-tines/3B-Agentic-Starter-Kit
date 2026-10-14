# 0004. Git is the source of truth: GitSync to the customer's GitHub, changes by pull request

- **Status:** Accepted
- **Context:** Every 3B space is a Git repository. Pushing to `main` publishes Live, and any other branch is a draft. GitSync, set up with a GitHub App, mirrors a space to a GitHub repository in both directions, and in a Git-synced space merging to `main` moves Live ([build in your own coding tools](https://docs.3b.tines.com/en/articles/16050928-build-a-workflow-in-your-own-coding-tools), [GitSync](https://docs.3b.tines.com/en/articles/16441033-sync-your-workflows-to-github-with-a-github-app)). When a space syncs with Git, the MCP `push_live` tool is refused and changes go through `sync_git` and a pull request ([Tines 3B Cursor plugin](https://github.com/tines/tines-3b-integrations)). Enterprises expect code review, CI and change control on anything that runs in production.
- **Constraint that shapes the layout:**
  - In a space repository, **every top-level directory is a workflow**, and a new directory without a `workflow.toml` creates one on push.
  - Pushes containing binaries, executables, symlinks or submodules are rejected (`building-workflows`, interfaces reference).

  So specs, onboarding records, hooks and agent configuration can't live in the space repository.
- **Decision:** each customer gets two repositories.
  - **Space repository.** Every production space is Git-synced to a repository in the customer's GitHub org. It holds workflows only, in 3B's format, with step tests inside each step. The default branch is `main`, and branch protection requires a review.
  - **Engagement repository.** Created from `kit/engagement-repo-template/`. It holds `specs/`, `fixtures/`, `runbooks/`, `onboarding/`, `AGENTS.md`, hooks and the kit skills. The space repository is cloned inside it at `space/` and gitignored, so the agent works from one root with the rules loaded.
  - **The PR is the change process.** Spec PR in the engagement repository, then branch, build, step tests and PR on the space repository, CI and a fresh-context review, then a person merges, which moves Live.
  - **The kit's own role.** This kit repository holds only the reusable layer: skills, templates, evals and guides.
- **Why:** reviewable diffs and a person's approval on every production change; "every loop has a runnable check" ([Claude Code best practices](https://code.claude.com/docs/en/best-practices)); change management for goal and config changes ([OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)).
- **Consequences:**
  - GitSync setup needs a GitHub App installed by a customer GitHub admin; phase 0 checks this.
  - Personal 3B API keys expire after 24 hours ([API docs](https://docs.3b.tines.com/en/articles/16151250-find-and-use-the-tines-3b-api-documentation)), so automation uses service accounts.
  - Spaces without GitSync (sandboxes) can still be cloned directly, or built through the in-product agent; treat those as non-production.
- **Revisit when:** 3B supports running step tests in external CI (listed as planned in [Git ready](https://www.tines.com/3b/product-updates/2026-08/git-ready/)). Then add them to the workflow-repo CI.
