# 0007. People approve the irreversible, and hooks enforce it

- **Status:** Accepted
- **Context:** Agents act fast and people stop reading after many prompts. Some actions can't be undone or change who can do what: pushing live, deleting, granting access, creating keys, connecting apps.
- **Decision:**
  - **Reads run freely; writes need a plan a person approved.** Read-only actions are auto-allowed. Tenant writes need a numbered plan and a "yes".
  - **A short list is never automated.** Pushing live, deleting, access grants, API keys and connected-app changes are blocked for agents by `scripts/hooks/guard.py`, wired as a Claude Code `PreToolUse` hook (`.claude/settings.json`) and a Cursor hook (`.cursor/hooks.json`). A person does those in the 3B UI or terminal.
  - **Approval requests explain the risk plainly.** Each one shows what will change and a plain-language risk line, not the model's rationale.
- **Why:** instructions in prose are advisory, while hooks are deterministic ([Claude Code hooks](https://code.claude.com/docs/en/hooks-guide), [Cursor hooks](https://cursor.com/docs/agent/hooks)). A person should always be able to deny a tool call ([MCP spec, tools](https://modelcontextprotocol.io/specification/latest/server/tools)). Approval fatigue erodes review, so gate few things, clearly ([OWASP Agentic Top 10, ASI09](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)).
- **Consequences:**
  - A few more manual steps for the customer, each one a real control their security team will ask about.
  - The deny list blocks the publicly named `push_live` tool and matches other MCP tool names by pattern (publish, delete, grant, revoke, key, secret), because the full 3B MCP tool list isn't published. Tighten it once `tools/list` is recorded (see `docs/VERIFY.md`).
  - In Git-synced spaces, 3B itself refuses `push_live`, and Live moves only when a person merges a pull request to `main`. That gives two independent controls.
- **Revisit when:** the 3B MCP tool list is known (then match exact names), or the customer's own managed settings take over enforcement.
