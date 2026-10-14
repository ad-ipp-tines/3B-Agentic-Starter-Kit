# 0008. Git to change, MCP for tenant context and actions, CLI to run and inspect

- **Status:** Accepted
- **Context:** An editor agent can reach 3B through four interfaces. Tines' `building-workflows` skill describes them ([interfaces reference](https://github.com/tines/skills/tree/main/skills/building-workflows)):
  - a **Git checkout** of the space;
  - the **3B MCP server**, which can create, inspect, edit, run, commit and publish workflows, manage connectors and read skills;
  - the **3B CLI**, which can inspect and run workflows, inspect executions, chat with the in-product agent and manage connectors, but doesn't edit files;
  - the **in-product editor**.

  Only OAuth sign-in can call the MCP build and publish tools. Service-account tokens can explore, run and ask the in-product agent, but can't edit or publish ([connect an AI client with MCP](https://docs.3b.tines.com/en/articles/16050745-connect-an-ai-client-to-tines-3b-with-mcp)).
- **Decision:**
  - **Changes go through Git.** The agent edits workflow files in the checkout, so every change is a diff in a pull request (decision 0004).
  - **MCP is for context and tenant actions.** Use it to list spaces, workflows, runs, connectors and skills, to run a step, and to connect a step to a connector (with approval). Use it over OAuth only for builders, and over service accounts only for read and run automation.
  - **The CLI is for scripted runs and diagnostics** (runs, executions, output, logs) where predictable output matters.
  - **Discover tools before using them.** The full MCP tool list isn't published, so `3b-readiness` records what `tools/list` returns, and no skill calls a tool by name until it's on that list.
- **Why:** reviewable changes and the cheapest reliable interface for each job. CLI output is the most context-efficient, and MCP tool definitions cost tokens on every call ([Claude Code costs](https://code.claude.com/docs/en/costs), [Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)). OAuth keeps every action attributed to a person.
- **Consequences:** builders need three things set up: the Git checkout, the MCP connection and the CLI. The CLI has two documented sign-in flows (`3b configure` in the docs, `3b auth login --host` in the skill), so check `3b --help` on the tenant (`docs/VERIFY.md`).
- **Revisit when:** Tines publishes the MCP tool reference. Then skills can name tools directly.
