# Tool design rules for MCP servers built in 3B

Sources: [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents), [MCP spec: tools](https://modelcontextprotocol.io/specification/latest/server/tools), [Claude connector review criteria](https://claude.com/docs/connectors/building/review-criteria).

1. **Shape tools like workflows, not endpoints.** One `triage_alert` beats `get_alert` + `get_host` + `get_user`.
2. **Few tools.** Every definition costs context on every call, and selection gets worse as the list grows. Start with three or fewer.
3. **Names:** `service_resource_verb`, at most 64 characters, `[a-z0-9_]`. Unambiguous parameter names (`alert_id`, not `id`).
4. **Descriptions** say what the tool does, when to use it and when not, what each parameter means, and what it returns. No instructions to the model about how to behave.
5. **Split reads from writes.** Mark read-only tools as read-only and destructive ones as destructive (clients use these hints to decide when to ask the person).
6. **Results:** only the 3–5 fields the next decision needs, well under 10k tokens. Return structured content plus a text copy. Use semantic identifiers, not opaque ones, where you can.
7. **Errors** are tool results with `isError: true`, a category, a retryable flag and a next step. Never return an empty or generic error.
8. **Long work** returns a random handle bound to the caller, plus a status tool. State the handle's lifetime in the description.
9. **Pagination and filtering** with sensible defaults (`limit`, `cursor`).
10. **Deterministic order** for the tool list, so clients can cache it.
11. **Evaluate** with 10–20 realistic multi-call tasks before rollout. Measure success, calls per task and tokens, then improve descriptions before adding tools.
