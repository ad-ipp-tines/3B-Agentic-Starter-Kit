# What's available, what to verify, what isn't there yet

Status as of the last update to this file. Labels:
- **Available:** in public docs or official repositories (source given).
- **Verify:** seen but not confirmed; test it on a tenant before relying on it.
- **Not available:** documented as planned, removed, or absent.

Re-check this page when `skills.lock` moves and every month against the [product updates](https://www.tines.com/3b/product-updates/).

| Capability | Status | Source / note |
|---|---|---|
| 3B product (launched July 2026), paid plans, self-hosted | Available | [Introducing Tines 3B](https://www.tines.com/blog/introducing-tines-3b/); no explicit "GA" label |
| Public docs with an `llms.txt` index | Available | https://docs.3b.tines.com/llms.txt |
| Space as a Git repository (clone, branch, push) | Available | [Build in your own coding tools](https://docs.3b.tines.com/en/articles/16050928-build-a-workflow-in-your-own-coding-tools) |
| GitSync to GitHub through a GitHub App | Available | [GitSync](https://docs.3b.tines.com/en/articles/16441033-sync-your-workflows-to-github-with-a-github-app). Default branch must be `main` |
| Tenant MCP server at `<tenant origin>/mcp` (Streamable HTTP) | Available | [Connect an AI client](https://docs.3b.tines.com/en/articles/16050745-connect-an-ai-client-to-tines-3b-with-mcp) |
| MCP build and publish tools over OAuth; service accounts limited to explore and run | Available | same |
| Full MCP tool list | **Verify** | Not published. Only `push_live`, `sync_git` and `list_audit_logs` are named publicly. Record `tools/list` per tenant |
| Official Cursor plugin "Tines 3B" | Available | [Cursor Marketplace](https://cursor.com/marketplace/tines-3b), [source](https://github.com/tines/tines-3b-integrations) |
| Claude Code plugin from tines/skills | Not available | Removed from the repository on 2026-08-14. Use the Settings → MCP snippet and install the skills |
| Codex/OpenAI plugin | Not available | Placeholder only in the integrations repository |
| Official skills (19), versioned releases | Available | [tines/skills](https://github.com/tines/skills): `npx skills add tines/skills`, or pinned with `gh skill install tines/skills --all --pin <tag>` (gh 2.90+) |
| Custom skills: create, import from Git, resync, auto-sync | Available | [Use skills in 3B](https://docs.3b.tines.com/en/articles/15886505-use-skills-to-give-tines-3b-new-expertise). Limits: 500 files, 5 MB per file, 25 MB per bundle |
| The same skill bundle behaving identically in 3B and in an editor | **Verify** | Keep shared skills instruction-only |
| Step tests (per step, hermetic, run at push-live) | Available | [Step tests](https://docs.3b.tines.com/en/articles/17431715-capture-a-step-s-correct-behavior-with-step-tests) |
| Running step tests in your own CI | Not available | Listed as a next step in [Git ready](https://www.tines.com/3b/product-updates/2026-08/git-ready/) |
| Workflows serving MCP (route step, platform-run OAuth 2.1 on `space`, `tenant` or `sso`) | Available | [`mcp-builder` skill](https://github.com/tines/skills/tree/main/skills/mcp-builder); SSO route auth for MCP added in August |
| Per-tool authorization on a workflow-served MCP server | **Verify** | Not documented. Assume all callers see all tools |
| Workflows calling remote MCP servers (MCP server connector: OAuth, bearer, SSO route; CA certificate) | Available | [Connect a workflow to a remote MCP server](https://docs.3b.tines.com/en/articles/16050833-connect-a-workflow-to-a-remote-mcp-server) |
| 3B CLI (inspect, run, logs, chat, connectors) | Available | [Build in your own coding tools](https://docs.3b.tines.com/en/articles/16050928-build-a-workflow-in-your-own-coding-tools) |
| CLI sign-in: `3b configure` (docs) or `3b auth login --host` (skill) | **Verify** | Check `3b --help` on your tenant |
| REST API (OpenAPI at `/api/v1/openapi.json` on each tenant) | Available | [API docs](https://docs.3b.tines.com/en/articles/16151250-find-and-use-the-tines-3b-api-documentation). Personal API keys expire after 24 h |
| Tines Units visible in Monitoring and through the API and MCP | Available | October 2026 product updates |
| Tunnels to private networks | Available | [Reach a private network](https://docs.3b.tines.com/en/articles/16050736-reach-a-private-network-through-a-secure-tunnel) |
| Bring-your-own-model AI providers | Available | [Connect your AI provider](https://docs.3b.tines.com/en/articles/16050726-connect-your-ai-provider) |
| Stories → 3B migration | Available, as an AI-guided rebuild | The `tines-export-to-3b` skill. Not a one-click importer |
| Importing gallery examples into a tenant | Not available | The gallery is ideas only |
| List prices | Not available publicly | Ask the account team |
