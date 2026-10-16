# What Tines 3B is, for builders

Tines 3B is an AI-native, code-first environment to build, run and monitor agents, apps and automations ([what is Tines 3B](https://docs.3b.tines.com/en/articles/15871664-what-is-tines-3b); [Introducing Tines 3B](https://www.tines.com/blog/introducing-tines-3b/)). AI writes the code, steps run as code in isolated containers, and the platform supplies identity, credentials, storage, networking, monitoring and governance around it. The kit's working frame: build with AI, run deterministically, review like code.

It sits alongside **Tines Stories** (the no-code product). Stories continues and is still being invested in, and existing customers can explore 3B at no additional cost ([Introducing Tines 3B](https://www.tines.com/blog/introducing-tines-3b/)).

## The model in eight lines

1. **Structure:** tenant → spaces → workflows → steps. A space is where a team collaborates, and access is granted to it.
2. **A step** is a directory with `README.md`, `config.toml`, a `Dockerfile` (`FROM 3b/base`) and its code: TypeScript (the default), Python, shell, a React app, or an agent template. Its stdout is the next step's stdin.
3. **Triggers:** HTTP routes (`webhook`, `api`, `webpage`), cron (on Live only), inbound email, or links from upstream steps. Route auth is `space` by default; the other options are `tenant`, `sso`, `external_id`, `connector` and `public`.
4. **Branches:** `main` is Live and every other branch is an isolated draft. Pushing live runs the step tests ([branches](https://docs.3b.tines.com/en/articles/15877997-branches)).
5. **Connectors** hold credentials. A transparent credential proxy injects them on outbound requests, so neither the code nor the model ever sees a secret.
6. **Storage** is named volumes under `/storage`, with per-run or shared scope.
7. **AI** is bring-your-own-model: you connect your provider and pay for its tokens. There's an agent step template, plus single-request AI steps.
8. **Operations:** step tests; autofix and autotune branches; a monitoring view including Tines Units consumption; audit logs, including actions taken over MCP.

Full file-format details are in Tines' public [`building-workflows` skill](https://github.com/tines/skills/tree/main/skills/building-workflows), the most complete description of the format.

## Four ways to build

| Interface | Good for | Notes |
|---|---|---|
| **Git** (space repository, or a GitHub repository synced to it) | Reviewable changes, pull requests, CI | Push to `main` publishes; a branch is a draft. GitSync uses a GitHub App |
| **3B MCP server** at `<tenant origin>/mcp` | Editor agents acting on the tenant: explore, run, build, publish | Building and publishing need OAuth; service accounts can explore and run |
| **3B CLI** | Scripted runs, executions, logs, chatting with the in-product agent | Doesn't edit files |
| **In-product editor and agent** | Building by conversation in the browser | Uses the same built-in skills |

## Skills: the shared know-how

3B's in-product agent uses **skills** ([use skills in 3B](https://docs.3b.tines.com/en/articles/15886505-use-skills-to-give-tines-3b-new-expertise)). The built-in ones are published as [tines/skills](https://github.com/tines/skills) (Apache-2.0, versioned releases) and work in Cursor, Claude Code and other agents too. You can add your own skills, import them from Git, and keep them in sync automatically.

## Plans (public structure)

The license covers the environment, the infrastructure, and runtime measured in **Tines Units**. There are three paid plans:

| Plan | Infrastructure | Runtime per month |
|---|---|---|
| Core | Multi-tenant | 100K TU |
| Scale | Dedicated stack | 300K TU |
| Power | Premium dedicated stack | 900K TU |

A free **Explore** edition covers 3 live workflows and 5,000 TU a month, plus a one-time AI allowance. AI tokens are billed by your provider. Self-hosted installs are supported. Source: [pricing and packaging](https://docs.3b.tines.com/en/articles/15872428-tines-3b-pricing-and-packaging-overview). There are no public list prices, so ask the account team.

## Ten terms, used the same way everywhere in this kit

| Term | Means |
|---|---|
| **Space** | A team's collaboration scope in 3B; access is granted to it. Each production space is Git-synced to a **space repository** |
| **Space repository** | The GitHub repository a space syncs to. Workflows only; `main` is Live |
| **Engagement repository** | The customer's repository for specs, fixtures, runbooks and onboarding records, with the space repository cloned at `space/` |
| **Draft** | Any branch other than `main`; isolated from Live |
| **Live** | What runs in production. **Live moves** when a person merges to `main`; we don't say "publish" or "push live" for that, because in Git-synced spaces the `push_live` tool is refused |
| **Step test** | A captured input/output pair under `Step/tests/step-tests/`, replayed by 3B at push-live |
| **Fixture** | A whole-workflow synthetic input in `fixtures/<workflow>/`, run end to end on a draft |
| **Connector** | 3B's credentialed integration; credentials are injected by the platform and never reach code or the model |
| **Status label** | Every 3B capability claim is **Available**, **Verify** or **Not available** |
| **Guard hook** | `scripts/hooks/guard.py`, run by both editors before shell and MCP calls; defence in depth behind 3B RBAC and branch protection |

## Where to keep up

- Monthly product updates: https://www.tines.com/3b/product-updates/
- Docs index for AI agents: https://docs.3b.tines.com/llms.txt
- Examples gallery (ideas, not importable): https://www.tines.com/3b/examples/
