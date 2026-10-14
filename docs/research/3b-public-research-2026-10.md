# Tines 3B: public footprint and tooling (public web only)

Research date: 2026-10-14. Sources: public web pages, public GitHub repositories, and public docs only. No private sources were used.

How it was gathered:
- `github.com/tines/skills` and `github.com/tines/tines-3b-integrations` were cloned and read file by file. Skills repo commit `75841b8` (2026-10-13); integrations repo commit `9492b80` (2026-09-18).
- Every article listed in `https://docs.3b.tines.com/llms.txt` (130 articles) was downloaded as `.md` and searched.
- Cursor docs were read as `.md` from `https://cursor.com/llms.txt`.
- The `npx skills` README came from the GitHub API.

Copyright note: Tines and Cursor web pages are paraphrased, with one short direct quote. Text from the two Apache-2.0 Tines repos (SKILL.md frontmatter, config keys, commands) is reproduced verbatim, as that license allows.

Label key: **(inferred)** means a conclusion drawn from sources, not stated by them. **(not found)** means nothing public was located.

---

## 1. Tines 3B public footprint

**Headline finding: a lot of 3B is public.** There is a launch blog, a product page, monthly product updates, an examples gallery, a full public help center with an `llms.txt` index, published pricing structure, self-hosted install docs, an official Apache-2.0 skills repo, and an official Cursor Marketplace plugin.

### 1.1 Launch, status, and positioning

**Launch dates**
- "Making Tines 3B" was published 2026-07-28 (`datePublished` in page metadata): https://www.tines.com/blog/making-tines-3b/
- The CEO's "Introducing Tines 3B" post was published 2026-07-31: https://www.tines.com/blog/introducing-tines-3b/
- Press coverage is dated 2026-07-28 and 2026-07-29 (see 1.6).
- The July 2026 product-updates page has an entry marking the 3B launch: https://www.tines.com/3b/product-updates/2026-07/

**What it is.** An AI-native, code-first environment to build, run, and monitor agents, apps, and automations. Tines says Stories was no-code by design. With AI writing the code, 3B is "just code": steps are code in isolated containers, plus connectors and a simple data store. Sources: both blog posts and https://docs.3b.tines.com/en/articles/15871664-what-is-tines-3b

**GA or preview**
- No page labels 3B as beta, preview, or waitlist.
- The product is generally sellable today: a free self-serve tier, paid plans, and self-hosted install guides with versioned upgrade notes ("Upgrading from v2 to v3").
- Coverage describes it as available now.
- The word "GA" itself does not appear. **(inferred: generally available)**
- Docs still label some items as design proposals or roadmap. For example, the "Git ready" post lists running step tests in existing CI as a planned next step.

**Relationship to Stories**
- The existing product is now called **Tines Stories**. It continues in parallel and is still being invested in. Nothing changes for existing customers.
- Tines expects many Stories customers to migrate or adopt 3B alongside Stories.
- Direct quote, from the intro post: "all existing customers can explore Tines 3B at no additional cost."

### 1.2 Official pages and domains

| URL | What it is | Status |
|---|---|---|
| https://www.tines.com/3b/ | Product page: build / run / monitor, connectors, skills, Git, BYOM, self-hosted | Fetched |
| https://www.tines.com/3b/product-updates/ (+ `/2026-07/` through `/2026-10/`, RSS at `/rss/tines-3b-product-updates.xml`) | Monthly changelog | Fetched |
| https://www.tines.com/3b/product-updates/2026-08/git-ready/ | "Git ready" post (Git sync) | Fetched |
| https://www.tines.com/3b/product-updates/2026-09/nice-to-mcp-you/ | "Nice to MCP you" post (building via MCP) | Fetched |
| https://www.tines.com/3b/product-updates/2026-08/boringly-stable/ and https://www.tines.com/3b/product-updates/2026-09/self-hosting-doesnt-have-to-be-hard/ | Stability and self-host posts | Linked, not read in full |
| https://www.tines.com/3b/examples/ | Gallery of 314 examples: 186 automations, 147 apps, 110 sites/dashboards, 81 agents, 41 forms. No import mechanism is described. | Fetched |
| https://docs.3b.tines.com/ (redirects to `/en/`) | Public help center for 3B | Fetched |
| https://docs.3b.tines.com/llms.txt | Machine-readable index: 130 articles in 9 sections. Each article is available as `.md`. | Fetched in full |
| https://3b.dev/ | Redirects to https://www.tines.com/3b/ | HEAD checked |
| `https://<tenant>.3b.dev` | Tenant origin pattern used in docs examples (`https://acme.3b.dev`, MCP at `https://acme.3b.dev/mcp`). Self-hosted tenants use their own host. | From docs |
| https://sh.3b.dev | Serves the self-hosted single-server bootstrap script. Install: `sudo bash -c "$(curl --proto '=https' --tlsv1.2 -fsSL https://sh.3b.dev)"`. Air-gapped bundle at `https://sh.3b.dev/airgapped.sh`. | From docs; HEAD 200 |
| https://sh.3b.dev/cli/install.sh | 3B CLI installer referenced by the `building-workflows` skill | HEAD 200 (`text/x-sh`); not downloaded or run |
| https://login.tines.com/saml_idp/signup | Sign-up for the free Explore edition | Linked |
| https://www.tines.com/pricing/ | Pricing page lists a Free edition (one-time $50 AI allowance) and "Paid editions" with "Get pricing" (no list prices) | Fetched |

The docs index is organized into nine sections:
1. Is Tines 3B for me?
2. Core concepts (about 45 glossary-style articles)
3. Configuring Tines 3B
4. Role-based access control
5. Connecting to your tools
6. Build your workflows
7. Run your workflows
8. Monitor your workflows
9. Tines 3B Self Hosted (Helm; EKS, GKE, and OKE; air-gapped install; environment and Helm references)

### 1.3 Pricing and packaging (public)

Source: https://docs.3b.tines.com/en/articles/15872428-tines-3b-pricing-and-packaging-overview

**Licensing model.** A platform license with three parts: the environment (workflows, spaces, connectors, skills, users), the infrastructure, and runtime measured in **Tines Units (TUs)**. A TU reflects workflow complexity times run frequency.

**Paid plans.** No list prices are published; buyers are sent to "Book a demo".

| Plan | Infrastructure | Runtime |
|---|---|---|
| Core | Multi-tenant | 100K TU per month |
| Scale | Dedicated stack | 300K TU per month |
| Power | Premium dedicated stack | 900K TU per month |

**Explore edition (freemium):**
- Multi-tenant.
- 3 live workflows.
- 5,000 TU per month.
- One-time $50 AI allowance.
- No public website URLs.
- The product page calls Explore the 3B equivalent of Stories Community Edition.

**Other terms:**
- AI is **BYOM**: customers pay their own LLM tokens.
- TU overages are billed monthly, with a one-month grace period for new customers.
- October 2026 updates added TU visibility in Monitoring, plus a `/billable_usage` endpoint available through both the API and MCP.

### 1.4 Product updates relevant to tooling (Jul to Oct 2026)

Source: https://www.tines.com/3b/product-updates/ and its monthly pages.

- **Jul 2026:** 3B launched. MCP support for spaces using Git sync. Google Gemini added as an AI provider. Microsoft Foundry connector for Claude and OpenAI models.
- **Aug 2026:**
  - Built-in skills now published in the public repo (github.com/tines/skills is linked).
  - New MCP settings page.
  - SSO route auth for MCP servers.
  - MCP server connectors can skip authentication.
  - API endpoint to download a workflow as a ZIP.
  - GitHub connector supports GitHub Enterprise Server.
  - Unit tests (step tests) for workflow steps.
- **Sep 2026:**
  - "Nice to MCP you": early MCP only let external agents steer the in-product agent; workflow-building tools are now exposed directly, along with built-in skills.
  - Search workflow links via MCP.
  - `list_audit_logs` and reports via MCP.
  - Option to auto-sync skills imported from Git.
  - `/import` endpoint to create a workflow from a ZIP.
  - Create and delete tunnel networks via the API.
  - MCP server connector accepts a CA certificate for private MCPs.
  - 43 new connectors.
- **Oct 2026 (latest entry Oct 8):**
  - TUs via the API and MCP.
  - Links shared from other spaces visible in the API, MCP, and the Links page.
  - Calling-workflow identity on connector requests.
  - New connectors.

### 1.5 Core build model (public docs)

**Structure:** tenant, then spaces, then workflows, then steps.
- Each step is a directory with `README.md`, `config.toml`, a `Dockerfile` (`FROM 3b/base`), and source code.
- A step's stdout becomes the next step's stdin.
- Each execution runs in an isolated container: gVisor sandboxes per job, per the self-host docs.

**Triggers:** routes (HTTP), cron, inbound email, and links from upstream steps.

**Storage and versioning:**
- Storage uses named volumes under `/storage`.
- Branches: `main` is Live; drafts are isolated. Pushing live runs step tests, link-access diffs, and volume seeding.

**Credentials and networking:**
- Credentials sit behind a transparent credential proxy, through connectors.
- Tunnels reach private networks.

**AI features:**
- Autofix and Autotune branches.
- Chat with the in-product agent.
- Voice mode.

Sources: https://docs.3b.tines.com/en/articles/15877997-branches, https://docs.3b.tines.com/en/articles/16050928-build-a-workflow-in-your-own-coding-tools, https://docs.3b.tines.com/en/articles/16554462-system-overview

### 1.6 Third-party coverage (for reference only)

- SiliconANGLE, 2026-07-28: https://siliconangle.com/2026/07/28/tines-launches-3b-help-enterprises-govern-ai-built-apps-agents/
- Help Net Security, 2026-07-29: https://www.helpnetsecurity.com/2026/07/29/tines-introduces-ai-native-platform-for-secure-enterprise-workflow-automation/
- IT Brief: https://itbrief.news/story/tines-launches-3b-to-govern-ai-generated-workflows
- stork.ai review: https://www.stork.ai/en/tines-3b. Unverified compliance and pricing claims; not relied on.

Common framing: governing employee-built "Wild Code". Coverage names no MCP or CLI details.

---

## 2. github.com/tines/skills (most important)

### 2.1 Summary and license

| Item | Value |
|---|---|
| Repo | https://github.com/tines/skills (public). Description: "A collection of Agent Skills for working with Tines products." |
| License | **Apache-2.0** (`LICENSE`). `THIRD_PARTY_NOTICES.md` lists 5 skills adapted from Anthropic's `anthropics/skills`, modified for 3B: `claude-api`, `internal-comms`, `mcp-builder`, `skill-creator`, `webapp-testing`. The rest are original Tines content. |
| Created / last push | GitHub `created_at` 2026-08-18; first commit 2026-08-14; last push 2026-10-13. Topic: `agent-skills`. |
| Releases | 28 GitHub releases, **v1.0.1** (2026-08-21) through **v1.0.28** (2026-10-13). The whole repo is versioned as one unit; skills have no individual versions. |
| Target product | The README says all current skills target **Tines 3B**. Every SKILL.md has `compatibility: Tines 3B`. **None target Tines Stories.** `tines-cases` and `tines-export-to-3b` touch Stories only as an external API, or as an export to migrate from. |
| Official status | Linked from the 3B product-updates page. The August update says built-in skills now live in this public repo. The 3B docs article on built-in skills describes the same set. |

### 2.2 Sync from the internal 3B repo

- Content is generated from a **private** Tines monorepo named `tines/3B`. `https://api.github.com/repos/tines/3B` returns 404 publicly.
- Each sync arrives as an automated PR from branch `sync-from-3b`. Recent PRs (#26 to #30) are titled "Sync built-in product skills from 3B". Commits are authored by `skills-repo-pusher[bot]` with messages like `Sync skills from tines/3B@<sha>`. The PR body links the source commit in `tines/3B`.
- Tines engineers then merge each PR.
- Cadence: about 30 syncs between 2026-08-20 and 2026-10-13, often several per week.
- `.github/RELEASING.md`: merge the sync PR after the "Validate Agent Skills" check (`gh skill publish --dry-run`) passes. A push to `main` triggers `release-skills.yml`, which picks a semver bump:
  - major when a skill is removed;
  - minor when a skill is added;
  - patch for any other change.
- PR labels `release:major`, `release:minor`, and `release:patch` override the automatic choice.
- The workflow then runs `gh skill publish --tag vX.Y.Z` and smoke-tests `gh skill install tines/skills --all --pin vX.Y.Z`.
- RELEASING.md also notes that skills.sh has no upload endpoint: `npx skills add` reads the default branch, and skills.sh discovery is fed by install telemetry.
- History note: the repo first shipped a Claude Code plugin marketplace (`.claude-plugin/marketplace.json`, `/plugin marketplace add tines/skills`). It was **removed on 2026-08-14**, so there is no Claude Code plugin from this repo today.
- The `skills/` tree is a mirror of the skills built into the product. **(inferred)** Edits should go upstream to Tines, not into PRs against this repo.

### 2.3 Folder structure

```text
.github/
  RELEASING.md
  workflows/validate-skills.yml      # gh skill publish --dry-run on PRs
  workflows/release-skills.yml       # auto semver + gh skill publish --tag
AGENTS.md                            # repo guidance for agents (Agent Skills spec rules, compatibility: Tines 3B, run gh skill publish --dry-run)
LICENSE                              # Apache-2.0
README.md
THIRD_PARTY_NOTICES.md
skills.sh.json                       # skills.sh grouping schema (5 groups)
skills/
  <skill-name>/SKILL.md              # 19 skills, one SKILL.md each
  building-workflows/                # the only multi-file skill (45 files)
    SKILL.md
    agents/openai.yaml               # optional OpenAI client metadata
    references/interfaces.md         # Git / MCP / CLI / in-product editor
    references/testing.md            # step tests, fixtures
    assets/templates/{shell,python,typescript,react,agent}/   # FROM 3b/base step templates
    assets/image-templates/{shell,python,typescript,react,agent}/  # standard-image variants (oven/bun:1.4.3, python:3.13-slim, debian:13-slim); not referenced by SKILL.md
```

AGENTS.md rules for contributors:
- Directory name equals the frontmatter `name`: lowercase, hyphenated, at most 64 characters.
- Write a concrete `description`.
- Set `compatibility` to the target Tines product.
- Put supporting files in `scripts/`, `references/`, or `assets/`.
- Put OpenAI-specific metadata in `agents/openai.yaml`, never in SKILL.md.
- Keep derivative notices.

### 2.4 Install commands (as published)

```bash
npx skills add tines/skills                               # whole collection (README)
npx skills add tines/skills --skill workflow-discovery    # one skill (README)
gh skill install tines/skills --all --pin v1.0.0          # pinned install via GitHub CLI (RELEASING.md)
```

`npx skills add tines/skills --list` and `-a cursor` / `-a claude-code` follow from the generic `npx skills` flags in section 5. Tines does not show these forms.

### 2.5 Full skill list with frontmatter descriptions (verbatim, Apache-2.0)

All 19 skills have `license: Apache-2.0` and `compatibility: Tines 3B`. None use `allowed-tools` or `metadata`.

| # | Skill | `description` (verbatim) |
|---|---|---|
| 1 | `building-agents` | Build the AI parts of a 3B workflow — any step that calls a language model. Use whenever a task calls a model (Anthropic, OpenAI, Gemini, …) or is model-shaped — summarize, extract, classify, generate, rewrite, answer, converse, or a tool-using agent — even if “AI” or “agent” is never said. Covers choosing the shape, the agent step, the mandatory self-loop for async agents, tools, model choice, conversations, chat UIs, and single-request calls. Pair with the claude-api skill for Anthropic-native features (Batches, the Files API). |
| 2 | `building-workflows` | Build and modify Tines 3B workflows from a workflow or space Git checkout, the 3B MCP server, the 3B CLI, or the in-product editor. Use whenever an agent works with workflow.toml, step directories, config.toml, FROM 3b/base Dockerfiles, workflow routes, links, triggers, connectors, step tests, or needs to create, inspect, run, debug, commit, or publish a 3B workflow. |
| 3 | `claude-api` | Build, debug, and optimize code that calls the Claude (Anthropic) API. Use when writing a step or service that calls Claude — covers picking a surface, the Messages API, choosing a model, prompt caching, tool use, streaming, thinking, and batch. |
| 4 | `cross-tool-research` | Find, correlate, summarize, and investigate information across the user’s connectors. Use for cross-tool searches, conversation or ticket summaries, and investigations that need alerts, logs, messages, documents, or code context. |
| 5 | `daily-briefing` | Build a concise briefing from calendars, tasks, tickets, pull requests, messages, and documents. Use when the user asks what needs attention, what is assigned to them, or how to prepare for an upcoming meeting. |
| 6 | `dashboard-design` | Build polished, interactive analytics dashboards for any data source. Use this whenever the request involves a dashboard, data visualization, internal metrics, spend/usage/cost reporting, or any UI that shows data sliced across time, users, categories, or other dimensions — even if the word "dashboard" is never used. Covers cross-filtering, shareable URL state, filter models, legends, transitions, honest handling of incomplete data, and visualization craft. Not needed for a single static chart. |
| 7 | `frontend-design` | Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics. |
| 8 | `internal-comms` | Write internal communications — status reports, leadership updates, incident reports, project updates, FAQs, and newsletters — in clear, consistent formats. Use whenever drafting an internal update, announcement, or report for a team or company. |
| 9 | `mcp-builder` | Build high-quality MCP (Model Context Protocol) servers that let an AI interact with external services through well-designed tools. Use whenever you are building an MCP server to integrate an external API or service, in either Python (FastMCP) or TypeScript (MCP SDK). When the server is deployed as a 3B workflow, put it behind the built-in `space` or `tenant` route auth and let the platform authenticate clients instead of implementing the MCP OAuth handshake in the server. |
| 10 | `mcp-client` | Call tools on a remote MCP (Model Context Protocol) server over streamable HTTP. Use whenever a connector is an MCP server (e.g. the “MCP server” connector type), or the user asks to list or invoke an MCP server’s tools, prompts, or resources. |
| 11 | `skill-creator` | Write and improve 3B skills. Use when creating a new skill from scratch or refining an existing one — covers writing a description that triggers reliably, structuring clear instructions, and testing on realistic prompts. |
| 12 | `status-update` | Draft evidence-based status updates from recent work across the user’s connectors. Use for daily or weekly updates, project summaries, stakeholder notes, and progress reports. |
| 13 | `tines-cases` | Working with Tines Cases from a 3B workflow or chat — creating, updating, listing, and managing cases with their comments, subscribers, and activities, plus the Records store cases draw on. Use this whenever you’re asked to open, update, close, search, or manage a Tines case, to work with Tines records, or to call the Tines API for anything case- or record-related. |
| 14 | `tines-export-to-3b` | Your guide to reading a Tines story export JSON and rebuilding it as a 3B workflow. Use this whenever you see a Tines export JSON, are asked to migrate or convert a Tines story to 3B, or hit Tines concepts like actions, Event Transformation, formulas, credentials, teams, or links and need the 3B equivalent in order to build it. |
| 15 | `webapp-testing` | Interact with and test web applications using Playwright. Use to verify frontend behavior, drive UI flows, capture screenshots, and read browser logs from a code step — whenever a task involves checking what a web page actually does in a browser. |
| 16 | `workflow-discovery` | Turn an automation idea into a clear workflow brief and practical design. Use when the user is starting a workflow, wants questions that clarify it, or wants workflow ideas based on their connectors. |
| 17 | `workflow-operations` | Add production operating behavior to a workflow. Use for schedules and event triggers, completion or failure notifications, targeted retries, operational logging, and follow-on automation. |
| 18 | `workflow-review` | Explain, test, simplify, and improve an existing workflow. Use when reviewing behavior, finding edge cases or failure points, validating sample data, or improving reliability, clarity, and performance. |
| 19 | `workflow-volume-design` | Design reliable 3B workflows that use named volumes or filesystem state. Use whenever a workflow stores or shares files, persists state across runs, uses an embedded database, handles uploads, receives concurrent requests, builds reporting data, or needs temporary per-run files. |

`skills.sh.json` groups:
- Build workflows: `building-workflows`, `building-agents`, `mcp-builder`, `mcp-client`, `workflow-discovery`, `workflow-volume-design`.
- Operate workflows: `webapp-testing`, `workflow-operations`, `workflow-review`.
- Design: `dashboard-design`, `frontend-design`.
- Research and communication: `cross-tool-research`, `daily-briefing`, `internal-comms`, `status-update`.
- Tines and agent development: `claude-api`, `skill-creator`, `tines-cases`, `tines-export-to-3b`.

**Docs vs. repo mismatch.** The 3B docs article listing built-in skills (https://docs.3b.tines.com/en/articles/15886505-use-skills-to-give-tines-3b-new-expertise) names 16 skills. It omits `building-workflows`, `tines-cases`, and `tines-export-to-3b`, which are in the repo. **(inferred: the docs lag the repo)**

### 2.6 How the skills reference 3B primitives (exact strings)

**Four editing interfaces** (from `building-workflows/references/interfaces.md`):
1. **Git checkout.** In a 3B-hosted space clone, each top-level directory is a workflow.
   - Pushing to `main` publishes Live; a non-`main` branch is a draft.
   - In a Git-synced space, merging to `main` moves Live.
   - Pushes with binaries, executables, symlinks, or submodules are rejected.
   - The docs give the clone URL as `https://<your-tenant>/spaces/<space-slug>.git`, with a 3B API key as the password.
2. **3B MCP server.** External agents can create, inspect, edit, run, commit, and publish workflows, manage connectors, read 3B skills, and collaborate with the in-product agent.
   - Tools are found through MCP discovery.
   - The config lives at `<tenant-origin>/settings/mcp`.
   - Auth is OAuth or a 3B API key. Service-account keys can read, run, and build through chat, but cannot edit directly.
3. **3B CLI** (macOS and Linux). Inspect and run workflows, inspect executions, chat with the in-product agent, and manage connectors. It does not edit files: use Git or MCP for edits, commits, and publishing.
   ```bash
   curl --proto '=https' --tlsv1.2 -fsSL https://sh.3b.dev/cli/install.sh | sh
   3b auth login --host <tenant-host>      # opens tenant UI for approval; --no-browser prints the URL
   3b --help
   ```
4. **In-product editor.** Uses the tools `editFile` and `writeFile` (read the file first in the same turn), connector tools, an upload tool, and a publish tool (only on explicit request).

**CLI discrepancy.** The public docs article (https://docs.3b.tines.com/en/articles/16050928-build-a-workflow-in-your-own-coding-tools) gives different commands: `curl -fsSL https://<your-tenant>/cli/install.sh | sh`, then `3b configure` (API key), then `echo "Hello" | 3b run wf_abc123 --wait`. The skill uses `sh.3b.dev` and `3b auth login --host`. **Verify against `3b --help` on a real tenant.** Both installer URLs may work. **(inferred)**

**Files and layout:**
- `workflow.toml` is an identity file. Preserve its `id` and never copy it. A new directory without one creates a workflow on push.
- `README.md` at the workflow root and in every step.
- Each `<Step>/` holds `config.toml`, `Dockerfile`, and the entry point: `script.sh`, `script.py` (plus `requirements.txt`), `script.ts` (Bun, plus `package.json`), `App.tsx` (React with Tailwind, plus `render.ts`, `mount.tsx`, `globals.css`), or `agent.ts`.
- `api.json`: OpenAPI 3.1 Operation Objects keyed by lowercase method. Only allowed on a non-root `route_type = "api"` step.
- Step tests go in `<Step>/tests/step-tests/`, with optional `tests/serialize` and `tests/serialize-request` scripts.

**`config.toml` keys:**
- `color`: one of `pink`, `purple`, `teal`, `green`, `orange`, `red`, `sky`.
- `output`.
- `route`.
- `route_auth`: one of `space` (default), `tenant`, `sso`, `external_id`, `connector`, `public`.
- `route_type`: one of `webpage`, `api`, `webhook`, `other`.
- `title`.
- `cron`: only runs on Live.
- `email_address`.
- `timeout`: 1 to 300 seconds, default 45.
- `retry_seconds`: at most 10 values, each 1 to 1,800.
- `links`.
- `connectors`: managed by tooling, never hand-edited.
- `pinned`.
- `route_idp`.
- `route_sso_groups`: requires `sso`.

**Dockerfile:**
- `FROM 3b/base` only.
- Supported instructions: `RUN`, `COPY <src...> .`, `CMD`, `LABEL`, `VOLUME`.
- Cache mounts: `RUN --mount=type=cache,target=<name>`.
- Volume forms: `VOLUME ["state"]`, `["state:ro"]`, `["scratch:scope=run"]`, `["work:scope=run,ro"]`.
- Checkpoint opt-in: `LABEL io.3b.exec.checkpoint.v2=true` with `/opt/3b/next`.

**Runtime environment variables:**
- `_3B_WORKFLOW_BASE_URL`: the origin plus the draft prefix.
- `_3B_BRANCH_ID` and `ROUTE_PATH`, used in the React template.
- `window.__ROUTE_PATH__` in the browser.
- `ANTHROPIC_BASE_URL`, from the Anthropic connector.
- `TUNNEL_TOKEN`, for the tunnel exit node.

**Spoof-proof headers:**
- Identity: `x-3b-authenticated-email` and `x-3b-authenticated-groups` (a JSON array).
- Calling workflow: `x-3b-calling-workflow-id`, `x-3b-calling-space-id`, `x-3b-calling-branch`.
- OAuth consent (MCP or OAuth routes): `x-3b-consent-challenge`, `x-3b-consent-decision-url`, `x-3b-consent-client`, `x-3b-consent-email`, `x-3b-consent-scope`, `x-3b-consent-connectors`. The response header `x-3b-consent: rendered` tells 3B to serve the step's own consent page.

**Platform paths:**
- `/storage/<volume>`.
- `/__3b/branch/<id>` (draft prefix).
- `/__3b/connectors/grant/disconnect?app=<connector-id>&route=<route>`.
- `/settings/mcp`, `/settings/networking`, `/settings/networking/new`.

**Tool names that appear in skills:**
- `searchConnectors` and `connectStepToApp` (`tines-export-to-3b`, `tines-cases`).
- `editFile` and `writeFile` (in-product editor).
- `seedBranchStorage` (draft volume seeding).
- The Cursor plugin README (section 2.9) adds the MCP tool names `push_live` and `sync_git`.
- Product updates name `list_audit_logs`.

**Hard limits:**
- Per step: 1 vCPU, 2 GiB RAM, 25,000,000 bytes per second ingress and egress, and 10 KiB of stderr kept.
- Step timeout of 300 seconds maximum.
- Zero-byte stdout stops downstream steps.
- Only a nonzero exit counts as failure.

**Connector rules:**
- Never hand-write `Authorization` headers; the proxy injects credentials.
- Never ask for pasted credentials.
- A visitor-mode connector returns `403 {"error":"connector_not_connected", ..., "connect_url": ...}` when the caller has not connected an account.
- Never store secrets in volumes.

### 2.7 Deep dives on the requested skills

**`building-workflows`** (22 KB SKILL.md plus 2 references plus templates). This is the master 3B authoring skill. Beyond section 2.6:
- Each step is an isolated process.
- Fan-out runs in parallel. With several upstream steps, the most recent successful output is used.
- A route step receives a raw RFC 7230 HTTP request on stdin and must emit a complete HTTP response, using `\r\n`. Without an output step, the route returns `202`.
- Long work should return `202` with an operation ID and persist state in a volume.
- Drafts floor `public`, `sso`, `tenant`, and `external_id` routes to space access.
- External SSO group membership is a snapshot: 2 hours for browser sessions, a 30-day OAuth refresh chain otherwise.
- Tunnels: an exit-node container connects outbound. Setup needs the Network creator role, and the token is shown once.
- React apps: a descriptive `<title>` is required, plus an inline SVG favicon in a `data:` URL.
- Default to TypeScript.
- A step cannot import from a sibling step or the workflow root.
- `references/testing.md`:
  - Run every changed step before commit or publish.
  - Ask before side-effecting runs.
  - Step tests replay hermetically with no egress and compare byte-for-byte.
  - SQLite fixtures use `sqlite-dump`.
  - Update an expected output only after the user confirms the new behavior.
- `agents/openai.yaml` gives display name "Build 3B workflows" and default prompt `Use $building-workflows to build or modify this Tines 3B workflow.`

**`building-agents`**
- Pick between two shapes: single request (no tools), or agent (model plus tools in a loop).
- The test for an agent: you cannot list the inputs up front.
- Always copy the `agent` template; never hand-roll the model loop.
- You edit five things: `system.md`, `tools/` (one `tool({...})` per file, discovered by filename), `model.json`, `config.toml`, and `buildInput()` in `agent.ts`.
- **Interactive** agent: has a `route` plus `output = true`. Streams NDJSON `AgentEvent`s; the whole turn runs in one step run.
- **Async** agent (webhook, cron, or upstream trigger): MUST self-loop by listing its own name in `links`, and must NOT have a route. It makes one model request per run and writes an `AgentRunResult` with status `running`, `done`, or `error`. Downstream consumers act only on a terminal status.
- Naming: put `(AI Agent)` in agent step names and `(AI)` in single-request step names.
- Conversations are server-side, keyed by `conversation_id`, isolated per authenticated user. Never replay prior turns.
- Transcripts live in volume `conversations` at `/storage/conversations`.
- Single-request steps use the Vercel AI SDK, the connector placeholder `"set-by-connector"`, streaming, and caching or reasoning on by default.
- Template defaults:
  - `model.json`: `provider: anthropic`, `model: claude-opus-5-5`, `effort: high`, adaptive thinking (summarized), `maxSteps 100`, `tokenBudget 5,000,000`, `maxOutputTokens 64,000`, `timeout = 300`.
  - Dependencies: `ai 7.0.122`, `@ai-sdk/anthropic 4.0.65`, `zod 4.3.6`.
  - Only the Anthropic provider ships. `runtime/model.ts` says to add other providers there.

**`mcp-builder`** (adapted from Anthropic)
- Phases: research (MCP sitemap, SDK READMEs), implement (TypeScript SDK with streamable HTTP stateless JSON recommended; Zod schemas; prefixed tool names; annotations), review (MCP Inspector `npx @modelcontextprotocol/inspector`), and about 10 evaluation questions.
- **3B-specific deployment:**
  - Expose the server as a route step: `route = "/<name>/mcp"` (never bare `/mcp`), `route_type = "api"`, `route_auth = "space"` or `"tenant"`, `output = true`.
  - The platform runs the full client-facing **OAuth 2.1**: protected-resource and authorization-server metadata, dynamic client registration, consent, and token issue and verification.
  - The step never sees the bearer token; it gets `x-3b-authenticated-email` instead.
  - `route_auth = "sso"` serves external users through the tenant IdP (with a pinned email domain), optionally gated by `route_sso_groups`.
  - Every request becomes a run. Answer `405` to non-`POST` requests unless `x-3b-consent-challenge` is present; one server got a reconnect every 2 seconds per Claude Code session because it returned `200` on `GET`.
  - Render your own consent page: POST `challenge` plus `decision=approve|deny` to the decision URL. Challenges expire in 10 minutes. HTML-escape client and connector names.
  - Pass the `connector_not_connected` body through as `isError: true`.

**`mcp-client`**
- Talk to MCP with plain `fetch` POSTs.
- Headers: `Content-Type: application/json` and `Accept: application/json, text/event-stream`.
- Parse both JSON and SSE responses.
- Echo the `Mcp-Session-Id` header.
- Send `initialize` with `protocolVersion: "2025-06-18"`, then `notifications/initialized`, then `tools/list` (paging with `cursor`) and `tools/call`. Prompts and resources work the same way.
- Optionally send a DELETE at the end.
- The attached MCP connector injects auth; never set `Authorization` yourself.
- Any 401 or 403 other than `connector_not_connected` means the user must reconnect.
- Cache `tools/list` in a file.

**`workflow-discovery`** (short)
- Establish the outcome before designing steps.
- Ask only material questions: trigger, input, authoritative connectors and records, transformation or decision, success output or side effect, failure handling.
- Ground ideas in connectors the user actually has.
- Produce a buildable brief.

**`workflow-operations`** (short)
- Match the schedule or trigger to when data is ready.
- Notify only people who can act, with workflow, run, outcome, and next action.
- Use bounded retries.
- Log stable IDs, never secrets.
- Make follow-on automation a separate workflow when its trigger, owner, or lifecycle differs.
- For scheduled volume work, defer to `workflow-volume-design`. Verify pending work drains faster than it arrives.

**`workflow-review`** (short)
- Read the files and execution evidence first.
- Review the workflow as one program: explain it, test success, empty, malformed, duplicate, and dependency-failure cases, decide local vs. visible failures, simplify before adding retries, and rerun.
- Volume-specific checks: no scanning of growing directories on request paths, no overlapping writers, bounded batches.
- Compare latency, waiting executions, oldest pending age, and volume usage before and after a change.

**`dashboard-design`**
- Build as a structured project, not one file.
- Data pipeline: scheduled plus on-demand refresh with coalescing, incremental fetch with a backfill path, never overwrite good data with empty data, CSV export.
- Interaction: everything is a filter; selections cross-filter and dim; all view state goes in the URL; multi-select with include/exclude.
- Layout must be stable; animate values, not existence. Beware the React `key` remount trap.
- Show caveats about incomplete data in one banner; never show partial periods as complete.
- Craft: tabular numerals, log/linear toggle, top-N plus "Others", a categorical palette separate from UI chrome, accessibility.
- Visual identity comes from `frontend-design`.

**`tines-cases`**
- Reach Cases and Records through the **"Tines Stories" connector, identifier `tines`**.
- Call `searchConnectors` with identifier `tines` first. Only if none exists, use `connectStepToApp`.
- Read the per-endpoint markdown doc before each call.
- Records: types live under `record_types`, records under `records`, and a case's linked records under `cases/<case_id>/records`.
- Read `https://www.tines.com/llm/stories/docs/api/records/best-practices.md` before writing record calls.
- Base path: `{TINES_URL}/api/…`. Use the newest API version each endpoint offers; versions differ by endpoint.

**`tines-export-to-3b`** (30 KB). The Stories-to-3B migration guide.
- **The core rule: 3B has no per-event routing or fan-out.** An Explode becomes one run with the array on stdin, and every step loops over it.
- Always write a **migration report** in the workflow README:
  - a link to `story_url`;
  - what was migrated;
  - what changed shape;
  - what needs a human;
  - what to double-check;
  - remaining dependencies on Tines (Resources, Records).
- Flag the **300-second per-step ceiling** up front.
- Resolve `META`, `INFO`, and `RESOURCE` references from the export's `references` map. RESOURCE values are IDs, not resource values.
- **Send to Story:** expose the workflow as a connector with `route_type = "api"`, `route_auth = "connector"`, `api.json`, and `output = true` exits. If `parent_only_send_to_story = false`, add a second entry step with `route_auth = "external_id"`.
- Color map from Tines action colors to 3B colors: Indigo → purple, Blue → sky, Green → green, Mint → teal, Orange → orange, Magenta → pink, Red → red, Gold → orange.
- Mapping tables:
  - Formulas become code.
  - Credentials become connectors (search existing ones first).
  - Resources: fetch through the "Tines Stories" connector using `https://www.tines.com/llm/docs/api/resources/get.md`, then store in a volume.
  - Webhook becomes a route step; HTTP Request becomes a fetch step; Condition becomes code that emits both buckets.
  - Run Script copies across; Send Email uses the SMTP connector; receive email uses `email_address`.
  - AI Agent becomes a self-linking step with an iteration cap (300 seconds per iteration).
  - MCP and gRPC: MCP servers connect natively as connectors with OAuth, 3B is itself an MCP server, and you can expose custom MCP servers.
  - A Page form becomes one route step serving GET and POST.
  - Postgres, MySQL, and MongoDB have native database connectors.
  - Implode becomes a volume join; Deduplicate a seen-set (cross-run dedup is unproven); Throttle a queue plus cron; Delay a volume plus cron (never sleep).
  - Teams become spaces; roles map to 3B roles and groups.
  - Cases (create) and Records (create, update, delete, list, get, query) go through the "Tines Stories" connector and the `https://www.tines.com/llm/docs/api/...` docs.

**Other skills, briefly:**
- `workflow-volume-design`: concurrency model (writers are not serialized; each step publishes a private view on success), a request-path pattern of pending records plus a scheduled bounded writer, one writer per SQLite or DuckDB file, retention and limits, and draft seeding through `seedBranchStorage`.
- `skill-creator`: describes 3B skills as Agent Skills bundles. Scripts (`.sh`, `.py`, `.js`, `.ts`) run in an ephemeral sandbox using only connectors already authorized in the chat. `allowed-tools` is guidance only.
- `claude-api`: the connector-URL `/v1` stripping trick for the Anthropic SDK. Lists model IDs `claude-fable-5`, `claude-opus-5-5`, `claude-sonnet-5`, `claude-haiku-4-5`, and itself says to verify against current Anthropic docs.

### 2.8 Gotchas for anyone using these skills outside 3B

- These are **3B-in-product instructions**. Some steps assume in-product or MCP tools (`searchConnectors`, `connectStepToApp`, `editFile`, `seedBranchStorage`). In Cursor or Claude Code, those exist only if the 3B MCP server exposes equivalent tools. **(inferred; exact MCP tool names beyond `push_live` and `sync_git` are not publicly listed)**
- The **Git path is the one that works with no MCP at all**: clone the space, edit the files, push a branch.
- `building-workflows` tells agents to copy `assets/templates` when the interface supplies no templates, so the templates matter in a local checkout.
- Guidance differs on scripts in skills. The docs Skills article says to avoid attaching code files or scripts. `skill-creator` says sandboxed scripts are supported. **(inferred: the docs lag)**

### 2.9 Companion repo: github.com/tines/tines-3b-integrations (official Cursor plugin)

- https://github.com/tines/tines-3b-integrations is public. No license file. CODEOWNERS: `@tines/engineering @tines/security`. Last push 2026-09-18.
- Its description says it holds plugins and integrations that add 3B functionality to other platforms.
- **Listed on the Cursor Marketplace** as "Tines 3B": https://cursor.com/marketplace/tines-3b. The page title and meta description were checked; a fake slug returns "Plugin Not Found".
- The README installs it via Cursor Settings → Plugins → search "Tines 3B", or with `/add-plugin tines-3b` in chat.

Layout:
- `.cursor-plugin/marketplace.json`: plugin `tines-3b`, `source: "cursor"`.
- `cursor/plugin.json`: Agent Plugins 1.0.0 manifest.
- `cursor/.cursor-plugin/plugin.json`: Cursor manifest.
- `cursor/skills/tines-3b-skills/SKILL.md`.
- An empty `openai` placeholder file. **(inferred: an OpenAI/Codex integration is planned but unpublished)**

The Cursor manifest declares a required plugin variable, `TINES_3B_MCP_URL`, described as the 3B sign-in origin plus `/mcp`. MCP config:
```json
{ "mcpServers": { "tines-3b": { "type": "http", "url": "${TINES_3B_MCP_URL}" } } }
```

README facts:
- 3B supports **OAuth dynamic client registration and PKCE**, so no client ID or secret is needed.
- A team-marketplace admin can set the URL once; each member signs in individually.
- A service-account token cannot write or publish.
- Troubleshooting: "`push_live` is refused" means the space syncs with Git, so use `sync_git` and open a PR.
- The bundled skill `tines-3b-skills` tells the agent to run `npx skills add tines/skills` if `building-workflows` is missing. Guidance therefore tracks `main` and is not pinned inside the plugin.

---

## 3. 3B and MCP

### 3.1 3B tenant MCP server (3B as an MCP server)

Source: https://docs.3b.tines.com/en/articles/16050745-connect-an-ai-client-to-tines-3b-with-mcp (screenshot dated 2026-10-08)

**Endpoint**
- One endpoint per tenant: `<tenant origin>/mcp`, for example `https://acme.3b.dev/mcp`.
- Transport: remote **Streamable HTTP**.
- **Settings → MCP** (`/settings/mcp`) shows the URL and ready-made config snippets for **Claude Code, Codex, and Cursor**.

**Authentication**

| Credential | What it can do |
|---|---|
| **OAuth** (browser sign-in) | Full access. The only credential allowed to call build and publish tools. Supports DCR and PKCE (per the Cursor plugin README). |
| **Service-account token** (bearer) | Read, run, and ask the 3B agent to build. Build and publish tools are refused with an explanation. |

- Service accounts are the only supported way to get a static token.
- Personal API keys (`3b_sk_` prefix) expire after 24 hours, per the API docs article. The skill says MCP accepts "a 3B API key", but the MCP article steers static-token use to service accounts.

**Tool groups:**
- **Explore**: list spaces and workflows, read steps, inspect runs and executions, read skills and connectors.
- **Run and ask**: trigger runs, create a workflow, message the 3B editor agent.
- **Build and publish** (OAuth only): write and edit step files, run a step, run shell commands, connect a step to a connector, save a checkpoint, push live. For Git-synced spaces, GitSync publishes to the remote instead.

**Named tools seen publicly:** `push_live` and `sync_git` (Cursor plugin README) and `list_audit_logs` (Sep update). The full catalog is not published. **Use `tools/list`.** The blog says clients get an introduction to 3B on connect, guidance in tool descriptions, and access to the built-in skills.

**Governance:**
- MCP adds no privilege beyond the credential.
- Publishing needs the push-live permission.
- Mutating tools are audit-logged and tagged as MCP.

**Related surfaces:**
- REST API: `https://<tenant>/api/v1/docs` (Swagger) and `/api/v1/openapi.json`, with `Authorization: Bearer 3b_sk_...`. Example endpoint: `POST /api/v1/workflows/:id/run`.
- CLI: `3b`.
- Git: space clone URL.

### 3.2 3B workflows as MCP clients

Source: https://docs.3b.tines.com/en/articles/16050833-connect-a-workflow-to-a-remote-mcp-server, plus the `mcp-client` skill.

- Use the **"MCP server" connector type**. Set a Server URL (streamable HTTP) and one of three auth options:
  - **OAuth** (default): endpoint discovery plus automatic client registration. The client ID and secret are optional.
  - **Bearer token**.
  - **SSO route**: for a 3B route with `route_auth = 'sso'`.
- Saving the connector runs a connection test with `initialize`.
- Updates added skip-auth (Aug) and a CA certificate for private MCPs (Sep).
- Attach the connector to a step. 3B then injects auth on matching URLs, and step code uses the JSON-RPC protocol from section 2.7 (`mcp-client`).
- The 3B AI auto-loads `mcp-client` for steps with an MCP connector.
- The docs say MCP connectors work in both workflows and chat. The `tines-export-to-3b` skill says the same.

### 3.3 3B workflows as MCP servers

From `mcp-builder` (section 2.7):
- A route step at `/<name>/mcp` with `route_auth = "space"`, `"tenant"`, or `"sso"`.
- The platform handles OAuth 2.1 metadata, DCR, consent, and tokens.
- Tokens are bound to the route and revocable.
- The step owns its consent page through the `x-3b-consent-*` headers.
- Answer 405 on GET.
- The August product update added SSO route auth for MCP servers.
- External MCP clients should use the route URL after import. Routes come from `_3B_WORKFLOW_BASE_URL`; never hard-code hosts.

### 3.4 Contrast: the Tines Stories MCP server

The existing Tines Stories product has its own first-party MCP server at `https://<tenant>.tines.com/mcp`.
- **OAuth only, no API keys**, with a consent screen titled "Tines Stories MCP server".
- Lets AI clients (Claude Code, Claude Desktop, ChatGPT, Codex, Cursor) read and change stories and actions, validate, and run actions where permitted. In effect it exposes the Workbench story-building capability.
- Tool use is audit-logged as MCP activity.
- Announced 2026-06-02.
- Separate from **custom MCP servers built as stories**, which expose a team's own story logic.

The Stories server builds no-code stories. The 3B server builds code-first workflows (files, steps, Git), adds a service-account mode, and splits its tools into explore, run, and build groups. Sources: https://www.tines.com/docs/mcp-server/, https://www.tines.com/whats-new/the-tines-mcp-server/

---

## 4. Cursor setup (current docs)

All pages below were fetched as `.md` from cursor.com on 2026-10-14.

### 4.1 MCP

Doc: https://cursor.com/docs/mcp

**File locations:**
- `.cursor/mcp.json` (project).
- `~/.cursor/mcp.json` (global).
- The extension API `vscode.cursor.mcp.registerServer()`.

**Format:** a top-level `mcpServers` object.
- stdio entries: `command`, `args`, `env`, `envFile` (stdio only), and an optional `"type": "stdio"`.
- Remote entries (Streamable HTTP or SSE): `url` and optional `headers`.

**OAuth:**
- Remote servers support OAuth.
- For servers without dynamic client registration, add `"auth": {"CLIENT_ID": "...", "CLIENT_SECRET": "...", "scopes": [...]}`.
- Fixed redirect URIs: `https://www.cursor.com/agents/mcp/oauth/callback` (web and cloud) and `http://localhost:8787/callback` (desktop).

**Interpolation:** `${env:NAME}`, `${userHome}`, `${workspaceFolder}`, `${workspaceFolderBasename}`, `${pathSeparator}` / `${/}`. These resolve in `command`, `args`, `env`, `url`, and `headers`.

**Supported protocol features:** tools, prompts, resources, roots, elicitation, and the MCP Apps extension.

**Approval and admin:**
- Tool approval follows Run Modes.
- Enterprise admins get an MCP Allowlist (command, URL, and per-tool patterns).
- Team MCP is distributed through the Dashboard (Plugins & MCPs).

**3B config.** Two options:
- Easiest: install the official plugin (section 4.6), which sets up the same thing.
- Manual OAuth config, mirroring the plugin's own MCP block. Cursor registers through DCR, then opens the 3B sign-in.
  ```json
  { "mcpServers": { "tines-3b": { "type": "http", "url": "https://<tenant>.3b.dev/mcp" } } }
  ```
- Manual service-account variant **(inferred from Cursor and 3B docs)**. It cannot build or publish.
  ```json
  { "mcpServers": { "tines-3b-svc": { "url": "https://<tenant>.3b.dev/mcp",
      "headers": { "Authorization": "Bearer ${env:TINES_3B_TOKEN}" } } } }
  ```

### 4.2 Agent Skills

Doc: https://cursor.com/docs/skills

**Discovery paths:**
- Project: `.agents/skills/`, `.cursor/skills/`.
- User: `~/.agents/skills/`, `~/.cursor/skills/`.
- Compatibility: `.claude/skills/`, `.codex/skills/`, `~/.claude/skills/`, `~/.codex/skills/`.

**Directory behavior:**
- Nested category folders are walked recursively.
- `.cursor/skills/` or `.agents/skills/` inside a subdirectory is auto-scoped to that directory.

**SKILL.md frontmatter:**
- Required: `name` (matches the folder) and `description`.
- Optional: `paths` (glob scoping; legacy `globs`), `disable-model-invocation`, `icon`, `color`, `metadata`.
- Optional folders: `scripts/`, `references/`, `assets/`.

**Invocation:** type `/skill-name`, or use the skill as a Custom Mode.

**Cloud agents:** only `~/.cursor/skills/` syncs (opt-in setting "Sync Skills for Cloud Agents"). Project skills come from the repo.

**Importing from GitHub:** Cursor imports skills from a repo only through a **plugin** with `.cursor-plugin/marketplace.json`, or through a team marketplace. `npx skills` sidesteps this by writing files into `.agents/skills/`.

### 4.3 Rules and AGENTS.md

Doc: https://cursor.com/docs/rules

**Project rules:**
- Location: `.cursor/rules/*.mdc`. **Only the `.mdc` extension counts; plain `.md` is ignored there.** Folders are allowed.
- Frontmatter: `description`, `globs` (comma-separated), `alwaysApply`.
- Four rule types: Always Apply, Apply Intelligently, Apply to Specific Files, Apply Manually (`@rule`).
- `@file` references are read on demand, not inlined.

**AGENTS.md:**
- Plain markdown at the project root and in subdirectories (nested files are supported and merged; more specific wins).
- Cloud agents read AGENTS.md.

**Precedence:** Team Rules, then Project Rules, then User Rules. Team Rules are free text with optional globs and can be enforced.

**Built-in helpers:** `/create-rule`; `/migrate-to-skills` converts dynamic rules and commands into skills.

### 4.4 Subagents

Doc: https://cursor.com/docs/subagents

**Locations:**
- Project: `.cursor/agents/`, `.claude/agents/`, `.codex/agents/`.
- User: `~/.cursor/agents/`, `~/.claude/agents/`, `~/.codex/agents/`.
- `.cursor/` wins on name conflicts, and project wins over user.

**Format:** Markdown with YAML frontmatter, then the prompt body.

**Supported frontmatter fields (all optional):**

| Field | Type | Default | Notes |
|---|---|---|---|
| `name` | string | from filename | |
| `description` | string | | Drives delegation; "use proactively" encourages it |
| `model` | string | `inherit` | Or a model ID with bracket params, e.g. `claude-opus-5[effort=high,context=300k]` |
| `readonly` | boolean | false | Restricts writes |
| `is_background` | boolean | false | |

Not in Cursor's field list: Claude Code-style fields such as `tools`. **(inferred: ignored)** Subagents inherit all parent tools, including MCP.

**Built-in subagents:** `explore` and `browser`.

**Invocation and runtime:**
- Invoke with `/name`.
- Subagents can nest one level (since 2.5).
- They can run in isolated worktrees, or in the cloud via `/in-cloud`.
- They can be resumed by agent ID.
- Background output goes to `~/.cursor/subagents/`.

**Cloud subagents** use team MCP from cursor.com/agents, not local MCP.

### 4.5 Hooks

Doc: https://cursor.com/docs/hooks

**Config file:** `hooks.json` with `{"version": 1, "hooks": {"<event>": [ {...} ]}}`.

**Locations, highest priority first:**
1. Enterprise: macOS `/Library/Application Support/Cursor/hooks.json`, Linux `/etc/cursor/hooks.json`, Windows `C:\ProgramData\Cursor\hooks.json`.
2. Team: dashboard, Enterprise plans.
3. Project: `<repo>/.cursor/hooks.json`. Runs from the repo root, so use `.cursor/hooks/x.sh` paths.
4. User: `~/.cursor/hooks.json`.

All matching hooks run. `deny` beats `ask`, which beats `allow`.

**Per-hook options:** `command`, `type` (`command` or `prompt`), `timeout`, `loop_limit` (default 5), `failClosed`, `matcher` (regex).

**Exit codes:** `0` uses the JSON output; `2` blocks; anything else fails open.

**Events:**
- Agent:
  - Session: `sessionStart`, `sessionEnd`.
  - Tool use: `preToolUse`, `postToolUse`, `postToolUseFailure`.
  - Subagents: `subagentStart`, `subagentStop`.
  - Shell: `beforeShellExecution`, `afterShellExecution`.
  - MCP: `beforeMCPExecution`, `afterMCPExecution`.
  - Files: `beforeReadFile`, `afterFileEdit`.
  - Other: `beforeSubmitPrompt`, `preCompact`, `stop`, `afterAgentResponse`, `afterAgentThought`.
- Tab: `beforeTabFileRead`, `afterTabFileEdit`.
- App: `workspaceOpen`.

**Matchers:**
- Tool hooks match tool types, e.g. `Shell|Read|Write|Grep|Delete|Task` or `MCP:<tool_name>`.
- Shell hooks match the command string.
- Subagent hooks match the subagent type.

**Cloud agents:**
- They run only command-type project, team, and enterprise hooks.
- Not available there: `sessionStart`, `sessionEnd`, `beforeMCPExecution`, `afterMCPExecution`, the Tab hooks, `workspaceOpen`, and user hooks.

**Claude Code hooks:** Cursor also loads hooks from `.claude/settings.json`, `.claude/settings.local.json`, and `~/.claude/settings.json` when the "Third-Party Imports" setting is on (the default). Doc: https://cursor.com/docs/reference/third-party-hooks

### 4.6 Plugins

Docs: https://cursor.com/docs/plugins and https://cursor.com/docs/reference/plugins

**Two plugin formats:**
- **Agent Plugin** (open standard, https://agent-plugins.org): a root `plugin.json` with `$schema: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`. Carries skills and MCP only.
- **Cursor Plugin**: a `.cursor-plugin/plugin.json` manifest. Adds rules, agents, commands, hooks, and variables.

**Cursor Plugin manifest fields:**
- Required: `name`.
- Optional:
  - Metadata: `description`, `version`, `author{name,email}`, `homepage`, `repository`, `license`, `keywords`, `logo`.
  - Component paths: `rules`, `agents`, `skills`, `commands`, `hooks`, `mcpServers`.
  - `variables`: a JSON Schema; values are set in Dashboard → Plugins → Configure and substituted as `${VAR}`.

**Default discovery:**
- `skills/` (each subdirectory with a SKILL.md).
- `rules/` (`.md`, `.mdc`, `.markdown`).
- `agents/`.
- `commands/` (also `.txt`).
- `hooks/hooks.json`.
- `mcp.json`.
- A root `SKILL.md` makes a single-skill plugin.
- A manifest path replaces folder discovery for that component.

**Plugin MCP variables:** `${CURSOR_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_ROOT}` expand. The standard's `${PLUGIN_ROOT}` and `${PLUGIN_DATA}` do not.

**Multi-plugin repos and distribution:**
- Multi-plugin repos use `.cursor-plugin/marketplace.json`; an entry's `source` resolves to `<source>/.cursor-plugin/plugin.json`.
- Local testing: `~/.cursor/plugins/local/<name>`. Enterprise admins can disable this.
- Submit at https://cursor.com/marketplace/publish. Listings are manually reviewed.
- Team marketplaces exist on Teams and Enterprise plans.

**The Tines 3B plugin is an example of this pattern:** Agent Plugin core plus a Cursor overlay with a `TINES_3B_MCP_URL` variable (section 2.9).

### 4.7 Cloud agents (formerly Background Agents)

Doc: https://cursor.com/docs/cloud-agent. The page says Cloud Agents were formerly called Background Agents.

**Runtime:**
- Isolated cloud VMs that clone the repo from GitHub, GitLab, Bitbucket, or Azure DevOps, work on a branch, and open PRs.
- Can be started from the desktop, cursor.com/agents, iOS, Slack, GitHub/Bitbucket `@cursor`, Linear, or the API.
- Billed at API pricing.
- Self-hosted machines are an option.

**Environment** (https://cursor.com/docs/cloud-agent/setup):
- Agent-led setup, a snapshot, or a Dockerfile, configured through `.cursor/environment.json`.
- Example fields: `"build": {"dockerfile": "Dockerfile", "context": ".."}`, `"install": "..."`, `"snapshot": "..."`.

**MCP** (https://cursor.com/docs/cloud-agent/capabilities):
- Uses team or personal MCP configured at cursor.com/agents, not local `~/.cursor/mcp.json`.
- HTTP and stdio transports. SSE and `mcp-remote` are not supported.
- OAuth is per user.
- HTTP is recommended, because credentials never enter the VM.
- A built-in "Cursor Cloud MCP" provides run diagnostics.

**Skills, rules, and hooks:**
- Skills: project skills come from the repo; personal skills need sync.
- Rules: AGENTS.md is read.
- Hooks: project `.cursor/hooks.json` only (command type).

---

## 5. The `npx skills` CLI

| Item | Value |
|---|---|
| Maker | **Vercel Labs**. npm package `skills` (v1.7.2, modified 2026-10-09; maintainers include `rauchg`), MIT license. Repo: https://github.com/vercel-labs/skills. Directory: https://skills.sh. Tines' page: https://skills.sh/tines/skills (HTTP 200). |
| What it does | Installs Agent Skills (https://agentskills.io) from GitHub shorthand, a full GitHub, GitLab, or Azure Repos URL, a tree path, any git URL, a local path, or a direct `SKILL.md` or archive URL. Auto-detects installed agents. The README names OpenCode, Claude Code, Codex, and Cursor "and 75 more" (79 in total). |
| Commands | `add`, `use` (prompt-only or `--agent` to launch), `list`/`ls`, `find [query]` (`--owner`), `update [skills]` (`-g`/`-p`/`-y`), `init [name]`, `remove`/`rm` |
| `add` flags | `-g, --global`; `-a, --agent <agents...>` (`'*'` = all); `-s, --skill <skills...>` (`'*'` = all); `-l, --list`; `--copy` (instead of symlinks); `-y, --yes`; `--all` (all skills to all agents). Also `--full-depth` for discovery. |
| Install paths | Project scope by default; `-g` for global. Symlink to one canonical copy (recommended) or `--copy`. |
| Discovery inside a repo | Repo root `SKILL.md`, `skills/` (plus `.curated`, `.experimental`, `.system`), and every agent's skills folder, walked 3 levels deep. Also reads `.claude-plugin/marketplace.json` and `plugin.json` skill lists. |
| Env vars | `INSTALL_INTERNAL_SKILLS`, `DISABLE_TELEMETRY` / `DO_NOT_TRACK`, `GITHUB_TOKEN` / `GH_TOKEN`. Telemetry is anonymous; repo IDs are sent only for confirmed-public GitHub repos. |
| Private repos | Uses existing Git credentials, then `gh repo clone`, then SSH. Never reads the gh token. |

Install paths per agent:

| Agent | Project path | Global path |
|---|---|---|
| **Cursor** | `.agents/skills/` | `~/.cursor/skills/` |
| **Claude Code** | `.claude/skills/` | `~/.claude/skills/` |
| **Codex** (shares paths with Cline, Warp, Zed, …) | `.agents/skills/` | `~/.agents/skills/` |

Both Cursor paths are in Cursor's discovery list (section 4.2).

**Alternative: GitHub CLI `gh skill`** (public preview, announced April 2026; https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/).
- Commands: `install` (with `--pin`, `--agent`, `--scope`), `search`, `preview`, `update`, `publish` (validates against the spec, creates a release, offers immutable releases).
- Tines' release pipeline uses `gh skill`.
- It needs **gh 2.90 or later**. The gh 2.88 tested during this research has no `skill` command.

---

## 6. Available vs. not

| Capability | Publicly documented | Source URL | Notes |
|---|---|---|---|
| 3B product launch and positioning | yes | https://www.tines.com/blog/introducing-tines-3b/ | Launched late July 2026; Stories continues |
| Explicit "GA" label | no | https://www.tines.com/3b/product-updates/2026-07/ | Says "launched" and has paid plans and self-host; GA status is **inferred** |
| Public 3B docs site | yes | https://docs.3b.tines.com/llms.txt | 130 articles; `.md` per article |
| `3b.dev` domain | partial | https://3b.dev/ | Redirects to tines.com/3b; tenant hosts `*.3b.dev` appear in docs examples; `sh.3b.dev` installers |
| Pricing structure (plans, TUs, Explore limits) | yes | https://docs.3b.tines.com/en/articles/15872428-tines-3b-pricing-and-packaging-overview | Core/Scale/Power = 100K/300K/900K TU; Explore = 3 live workflows, 5K TU, $50 AI |
| List prices | no | https://www.tines.com/pricing/ | "Get pricing" / book a demo |
| Free tier for existing Stories customers | yes | https://www.tines.com/blog/introducing-tines-3b/ | No additional cost to explore |
| Official Agent Skills repo | yes | https://github.com/tines/skills | Apache-2.0, 19 skills, all `compatibility: Tines 3B` |
| Skills sync from internal 3B repo | yes | https://github.com/tines/skills/pull/30 | Bot PRs from private `tines/3B`; source not public |
| Skills targeting Tines Stories | no | https://github.com/tines/skills | None; `tines-export-to-3b` migrates from Stories |
| Install via `npx skills add tines/skills` | yes | https://github.com/tines/skills#install | Also `gh skill install tines/skills --all --pin vX` |
| Claude Code plugin marketplace for tines/skills | no (removed) | https://github.com/tines/skills/commit/1dd467133ff33d51d6c351757e19f2f6c3bc9796 | Removed 2026-08-14 |
| Official Cursor plugin for 3B | yes | https://cursor.com/marketplace/tines-3b | Source: https://github.com/tines/tines-3b-integrations |
| Official Codex/OpenAI integration | no | https://github.com/tines/tines-3b-integrations | Only an empty `openai` placeholder (**inferred** planned); `agents/openai.yaml` metadata exists in one skill |
| 3B MCP server endpoint (`<tenant>/mcp`) | yes | https://docs.3b.tines.com/en/articles/16050745-connect-an-ai-client-to-tines-3b-with-mcp | Streamable HTTP; Settings → MCP snippets for Claude Code, Codex, Cursor |
| 3B MCP auth (OAuth vs. service account) | yes | same | OAuth required for build and publish; DCR and PKCE per the plugin README |
| 3B MCP full tool list | partial | same; https://github.com/tines/tines-3b-integrations/blob/main/cursor/README.md | Only groups plus `push_live`, `sync_git`, `list_audit_logs` named; discover with `tools/list` |
| 3B workflows calling remote MCP servers | yes | https://docs.3b.tines.com/en/articles/16050833-connect-a-workflow-to-a-remote-mcp-server | MCP server connector (OAuth, bearer, SSO route); `mcp-client` skill |
| 3B workflows serving MCP (custom servers) | yes | https://github.com/tines/skills/blob/main/skills/mcp-builder/SKILL.md | Platform-run OAuth 2.1 on `space`/`tenant`/`sso` routes |
| Space as Git repo (clone, push) | yes | https://docs.3b.tines.com/en/articles/16050928-build-a-workflow-in-your-own-coding-tools | `https://<tenant>/spaces/<slug>.git`, API key as password |
| GitSync to GitHub (GitHub App) | yes | https://docs.3b.tines.com/en/articles/16441033-sync-your-workflows-to-github-with-a-github-app | Bidirectional and event-driven; default branch must be `main` |
| Workflow file format (`config.toml`, Dockerfile, `api.json`) | yes | https://github.com/tines/skills/blob/main/skills/building-workflows/SKILL.md | Most complete spec is in the skill, not the docs |
| 3B CLI | partial | https://docs.3b.tines.com/en/articles/16050928-build-a-workflow-in-your-own-coding-tools | **Two inconsistent install and auth flows** (docs vs. skill); no CLI reference page found |
| 3B REST API | yes (in-tenant) | https://docs.3b.tines.com/en/articles/16151250-find-and-use-the-tines-3b-api-documentation | `/api/v1/docs` and `/api/v1/openapi.json` on each tenant; readable without auth on a tenant; no public copy outside a tenant found |
| Step tests | yes | https://docs.3b.tines.com/en/articles/17431715-capture-a-step-s-correct-behavior-with-step-tests | Run automatically on push-live |
| Step tests in external CI | no (planned) | https://www.tines.com/3b/product-updates/2026-08/git-ready/ | Listed as a next step |
| Custom skills (UI, Git import, resync, auto-sync) | yes | https://docs.3b.tines.com/en/articles/15886505-use-skills-to-give-tines-3b-new-expertise | Limits: 500 files, 5 MB per file, 25 MB per bundle |
| Tunnels or private networks | yes | https://docs.3b.tines.com/en/articles/16050736-reach-a-private-network-through-a-secure-tunnel | Exit-node container; tunnel API (Sep) |
| Self-hosted (Helm, single-server, air-gapped) | yes | https://docs.3b.tines.com/en/articles/16595907-installation-guide | `sh.3b.dev` bootstrap; EKS, GKE, OKE guides |
| BYOM AI providers | yes | https://docs.3b.tines.com/en/articles/16050726-connect-your-ai-provider | OpenAI, Anthropic, Azure OpenAI, OCI, optional "Managed by 3B"; Gemini added Jul; NVIDIA and Hugging Face Sep |
| Story export to 3B importer (automated) | partial | https://github.com/tines/skills/blob/main/skills/tines-export-to-3b/SKILL.md | AI-guided rebuild skill, not a one-click importer (**inferred**); API `/import` takes a 3B workflow ZIP (Sep), not a Stories export |
| Examples importable into a tenant | no | https://www.tines.com/3b/examples/ | 314 examples; no import mechanism shown |
| Cursor: MCP via `.cursor/mcp.json` with remote OAuth | yes | https://cursor.com/docs/mcp | DCR, or a static `auth` block |
| Cursor: skills in `.cursor/skills`, `.agents/skills`, `.claude/skills` | yes | https://cursor.com/docs/skills | Plus `~/.cursor/skills`, `~/.agents/skills`, `~/.claude/skills`, and the Codex paths |
| Cursor: rules (`.cursor/rules/*.mdc`, AGENTS.md) | yes | https://cursor.com/docs/rules | `.md` files in `.cursor/rules` are ignored |
| Cursor: subagents (`.cursor/agents`) | yes | https://cursor.com/docs/subagents | Fields: `name`, `description`, `model`, `readonly`, `is_background` |
| Cursor: hooks (`.cursor/hooks.json`) | yes | https://cursor.com/docs/hooks | 21 events; cloud subset |
| Cursor: plugins (`.cursor-plugin/plugin.json`) | yes | https://cursor.com/docs/reference/plugins | Plus the Agent Plugins `plugin.json` standard |
| Cursor: cloud agents | yes | https://cursor.com/docs/cloud-agent | Formerly Background Agents; `.cursor/environment.json`; team MCP only |
| `npx skills` CLI | yes | https://github.com/vercel-labs/skills | Vercel Labs; Cursor project path `.agents/skills/` |
| `gh skill` CLI | yes (preview) | https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/ | Needs gh 2.90 or later |

### Not fetched or not verified

- **Not downloaded or run:** the 3B CLI installer at `https://sh.3b.dev/cli/install.sh`. It was HEAD-checked only. CLI subcommands beyond those quoted in the skill and docs are unverified.
- **Not read in full:** two 3B product-update posts ("Boringly stable", "Self hosting doesn't have to be hard").
- **Not opened past title and meta tags:** the Cursor Marketplace listing (client-rendered).
- **No public Tines source found for:**
  - a 3B MCP tool reference;
  - a 3B CLI reference page;
  - 3B list prices;
  - an explicit "GA" statement.
