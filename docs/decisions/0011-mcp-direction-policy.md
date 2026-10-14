# 0011. MCP in all three directions, least privilege first

- **Status:** Accepted
- **Context:** 3B supports MCP in three directions, all publicly documented:
  1. **Editors → 3B.** The tenant MCP server at `<tenant origin>/mcp` (Streamable HTTP). OAuth is needed for the build and publish tools; service accounts can explore and run ([connect an AI client](https://docs.3b.tines.com/en/articles/16050745-connect-an-ai-client-to-tines-3b-with-mcp)).
  2. **AI clients → a workflow.** A route step at `/<name>/mcp` serves MCP. The platform runs the whole client-facing OAuth 2.1 flow (metadata, dynamic client registration, consent, tokens) for `space`, `tenant` or `sso` route auth. The step never sees the bearer token; it gets the caller's verified email in a header ([`mcp-builder` skill](https://github.com/tines/skills/tree/main/skills/mcp-builder)).
  3. **A workflow → external MCP servers.** The "MCP server" connector type, with OAuth, bearer or SSO-route auth, plus a CA certificate option for private servers ([connect a workflow to a remote MCP server](https://docs.3b.tines.com/en/articles/16050833-connect-a-workflow-to-a-remote-mcp-server); `mcp-client` skill).
- **Decision:**
  - **Direction 1 is phase 0.** Builders connect with OAuth, through the official Cursor plugin or the snippet on the tenant's Settings → MCP page. Automation uses a service account limited to read and run. Never commit a token.
  - **Direction 2 is phase 4.**
    - Start with read-only tools.
    - Run one server per trust boundary, because access is per route.
    - Use `space` or `sso` route auth, and narrow access with SSO groups. Never use `public` for an MCP server.
    - Long work returns `202` with an operation id plus a status tool.
    - Answer `405` to `GET`.
    - Pass `connector_not_connected` errors through as `isError` results.
    - Whether per-tool authorization exists is **Verify**; until confirmed, assume every caller sees every tool on the server.
  - **Direction 3 is available wherever a vendor runs an MCP server.** Prefer the vendor's MCP server when its tools match the job. Otherwise call the API through a regular connector. Either way, credentials stay in the connector and out of code and the model.
- **Why:**
  - Act in the user's context.
  - No token passthrough, and tokens are audience-bound ([MCP security best practices](https://modelcontextprotocol.io/specification/latest/basic/security_best_practices)).
  - Minimise tools and permissions ([OWASP LLM Top 10 2026, LLM03](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)).
  - Few, workflow-shaped tools with structured errors ([Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)).
- **Consequences:** MCP becomes a first-class onboarding outcome. Builders work from their editors (direction 1). The customer's own workflows become tools their AI assistants can call safely (direction 2). Agents built in 3B reach the customer's other tools (direction 3).
- **Revisit when:** Tines publishes an MCP tool reference, or per-tool authorization for servers built in 3B.
