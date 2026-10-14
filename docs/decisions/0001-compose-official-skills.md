# 0001. Use Tines' official plugin and skills, pinned; don't fork them

- **Status:** Accepted
- **Context:** Tines publishes two official, public building blocks:
  - [tines/skills](https://github.com/tines/skills) (Apache-2.0), 19 Agent Skills for 3B mirrored from the product's built-in skills and released as versioned tags (v1.0.28 on 2026-10-13). It includes `building-workflows`, `building-agents`, `mcp-builder`, `mcp-client`, `workflow-discovery`, `workflow-operations`, `workflow-review`, `workflow-volume-design` and `tines-export-to-3b`.
  - The [Tines 3B Cursor plugin](https://cursor.com/marketplace/tines-3b) ([source](https://github.com/tines/tines-3b-integrations)). It wires the tenant MCP server through one variable, `TINES_3B_MCP_URL`, and its bundled skill installs `tines/skills` from the default branch, which means unpinned.
- **Decision:**
  - **Connection.** Builders on Cursor install the official plugin. Claude Code users add the tenant MCP server from the snippet on Settings → MCP.
  - **Pinned official skills.** `scripts/bootstrap.sh` installs `tines/skills` pinned to the tag in `skills.lock` (`gh skill install tines/skills --all --pin <tag>`, which needs gh 2.90 or later). A pin upgrade is a pull request that re-runs the kit's golden tasks.
  - **No re-teaching.** Kit skills never re-teach *how* to build in 3B; they name the official skill to load. They add the onboarding programme (what to build, in what order, how to prove it's done), customer context, approvals, evals and handover.
  - **Fixes go upstream.** Changes to official skills go to Tines, not into a fork.
- **Why:** reuse the maintained source of product truth, and pin the supply chain, because skills are instructions an agent will follow ([OWASP Agentic Top 10, ASI04](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/); [Anthropic, Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)).
- **Consequences:**
  - The kit stays small and current.
  - The plugin's own unpinned install can pull a newer version than `skills.lock`. Readiness checks which version is loaded.
  - If Tines renames an official skill, the golden tasks catch it.
- **Revisit when:** the official skills start covering onboarding, or the plugin starts pinning versions.
