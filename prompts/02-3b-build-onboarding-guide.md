# Prompt for 3B: build the interactive onboarding walkthrough ("Launchpad")

Give this to the 3B in-product agent, in **plan mode first**, inside a **sandbox** space that is Git-synced to a GitHub repository. You can also give it to an editor agent connected to the 3B MCP server with OAuth.

Before you start, a person sets up four things:
- a GitHub connector with **read-only** access to the kit repository;
- the kit's `tenant-skills/enterprise-conventions` skill, imported into the space from Git with auto-sync on;
- an SSO group for the pilot users;
- confirmation that the official built-in skills are available.

---

You're building **Launchpad**, an interactive walkthrough of the 3B Agentic Starter Kit's onboarding programme for a customer team. Follow the built-in skills `building-workflows`, `frontend-design`, `dashboard-design` and `workflow-volume-design`, plus the space's `enterprise-conventions` skill.

## What it does

1. Shows the six onboarding phases (Readiness, Discover, First workflow, Agentic, MCP, Operate and scale), each with its goal, its exit-criteria checklist, and the kit skill to run next.
2. Lets each signed-in user tick checklist items for their team. Progress is stored per team and shown as a simple progress view.
3. Renders the walkthrough chapters from the kit repository's `docs/guide/` (Markdown) and the reference pages in `docs/`, with links to the public 3B docs.
4. Shows a "what's next" panel: the first phase with unmet criteria, and its next action.

## How to build it

- **Workflow name:** `launchpad`.
- **Steps:**
  - `refresh_content`: cron, Live only, plus on demand. Reads `docs/guide/*.md` and the programme checklist (`.claude/skills/3b-onboard/references/programme.md`) through the GitHub connector, and writes them to a named volume `launchpad`. Never overwrites good content with empty content. Logs the commit SHA it read.
  - `app`: `route_type = "webpage"`, a React app from the template, `route_auth = "sso"` with `route_sso_groups` set to the pilot group (or `"space"` for the sandbox). It needs a descriptive `<title>` and an inline SVG favicon.
  - `progress_api`: `route_type = "api"`, the same auth. Saves checklist ticks keyed by team and item, attributed to the caller from `x-3b-authenticated-email`. It's the only writer to the progress file.
- **No `public` routes.** No secrets in code or volumes. The GitHub token lives only in the connector.
- **Step tests** for every step: happy, malformed and duplicate tick; empty-content refresh; unauthorised caller.
- Work on a **draft branch**. Open a pull request through Git sync. **Don't push live**: a person merges after review.

## Process

1. Plan mode: propose the step list, the volume layout, the checklist data shape and the page layout as a short spec. Wait for approval.
2. Build on a draft branch. Run every step. Add step tests.
3. Open a pull request with the results and screenshots of the draft route.
4. Tell the person what to review, including the route auth and the connector scope.

## Also

If the walkthrough chapters in `docs/guide/` are missing or thin, draft the missing chapters as Markdown in your pull request description, following the outline in `docs/guide/README.md`. A person or Cursor moves them into the kit repository through a PR. Use synthetic examples only.
