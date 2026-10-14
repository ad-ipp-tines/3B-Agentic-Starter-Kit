#!/usr/bin/env python3
"""Deterministic guard for agent tool calls (see docs/decisions/0007-people-approve-the-irreversible.md).

Prose rules in AGENTS.md are advisory; this hook enforces the few that must never break.

Claude Code: PreToolUse hook. Reads the event JSON on stdin; exit 2 + stderr = deny.
Cursor:      beforeShellExecution / beforeMCPExecution hook, called with --cursor.
             Prints {"permission": ...} JSON; exit 2 = deny.

Blocked (a person does these in the 3B UI or terminal instead):
  - pushing live, deleting, granting or revoking access, creating or rotating keys, via MCP tools
  - connecting or disconnecting connected apps from the CLI
  - reading or echoing the 3B API key
  - force-pushing, or piping a downloaded script into a shell
"""
from __future__ import annotations

import json
import re
import sys

MCP_DENY = re.compile(
    r"(delete|destroy|remove|purge|push_?live|promote|publish|grant|revoke|"
    r"api_?key|rotate|secret|credential|connector_(create|update|delete))",
    re.I,
)
SHELL_DENY = [
    (re.compile(r"\b3b\s+apps\s+(connect|disconnect)\b"), "Connecting or disconnecting connected apps is a person's call. Ask them to run it."),
    (re.compile(r"THREE_B_API_KEY"), "Never read, print or pass the 3B API key. The person configures it with `3b configure`."),
    (re.compile(r"\bgit\s+push\b.*(--force\b|-f\b|--force-with-lease)"), "No force pushes. Open a branch and a pull request."),
    (re.compile(r"\b(curl|wget)\b[^|]*\|\s*(sh|bash|zsh)\b"), "Don't pipe downloads into a shell. Ask the person to run installers."),
    (re.compile(r"\brm\s+-rf\s+(/|~|\$HOME)(\s|$)"), "Refusing a destructive delete."),
]


def decide(event: dict) -> tuple[bool, str]:
    tool = str(event.get("tool_name") or event.get("toolName") or "")
    tool_input = event.get("tool_input") or event.get("toolInput") or {}
    command = str(event.get("command") or (tool_input.get("command") if isinstance(tool_input, dict) else "") or "")

    is_mcp = tool.startswith("mcp__") or "server" in event or "url" in event and not command
    if is_mcp and MCP_DENY.search(tool):
        return False, (f"'{tool}' changes production, access or secrets. Show the person a plan "
                       "and ask them to do it in the 3B UI.")
    for pattern, reason in SHELL_DENY:
        if command and pattern.search(command):
            return False, reason
    return True, ""


def main() -> int:
    cursor = "--cursor" in sys.argv
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        event = {}
    allowed, reason = decide(event)
    if cursor:
        if allowed:
            print(json.dumps({"permission": "allow"}))
            return 0
        print(json.dumps({"permission": "deny", "userMessage": reason, "agentMessage": reason}))
        return 2
    if allowed:
        return 0
    print(reason, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
