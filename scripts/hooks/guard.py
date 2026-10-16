#!/usr/bin/env python3
"""Deterministic guard for agent tool calls. Defence in depth, not the primary control.

The enforced controls are 3B RBAC (builders don't hold push-live) and GitHub branch protection
(required review, CODEOWNERS). This hook stops an agent from *trying* the irreversible, in both
editors, so a mistake is caught before it reaches those controls
(docs/decisions/0007-people-approve-the-irreversible.md).

Claude Code: PreToolUse hook. Reads the event JSON on stdin; exit 2 + stderr = deny.
Cursor:      beforeShellExecution / beforeMCPExecution hook, called with --cursor.
             Prints a JSON permission decision; exit 2 = deny.
             Cursor's exact stdin and output keys are not in public docs we've verified
             (docs/VERIFY.md V7): the hook accepts several key spellings and emits both
             camelCase and snake_case message keys.

Denied (a person does these in the 3B UI, GitHub or a terminal):
  MCP tools whose names say they publish, delete, grant or revoke access, handle keys or
  secrets, or connect or disconnect connectors
  Shell: pushing to main/master, merging pull requests, 3b apps connect/disconnect,
  reading the 3B API key, force pushes, piping or process-substituting downloads into a
  shell, installing skills outside bootstrap.sh (keeps skills.lock the only pin), rm -rf /
"""
from __future__ import annotations

import json
import re
import sys

# Verb-ish segments at a token boundary: matches push_live, delete_workflow, revokeAccess,
# connectStepToApp; does not match list_deleted_workflows or get_connection.
MCP_DENY = re.compile(
    r"(?:^|[_.:\-\s])(?:delete|destroy|remove|purge|push_?live|promote|publish|grant|revoke|"
    r"rotate|connect|disconnect)(?:$|[_.:\-\s]|(?<=[a-z])[A-Z])"
    r"|(?:^|[_.:\-\s])(?:api_?keys?|secrets?|credentials?|connectors?)(?:$|[_.:\-\s])"
    r"|(?:push|publish|revoke|grant|delete|remove|rotate|connect|disconnect)(?=[A-Z])",
)
SHELL_DENY = [
    (re.compile(r"\bgit\b[^|;&]*\bpush\b[^|;&]*(\s(main|master)\b|HEAD:(main|master)\b)"),
     "Pushing to main moves Live. Open a pull request; a person merges."),
    (re.compile(r"\bgh\s+pr\s+merge\b|\bgh\s+api\b[^|;&]*\/merge\b|\bgit\s+merge\b"),
     "Merging is a person's decision. Ask them to merge the pull request."),
    (re.compile(r"\bgit\b[^|;&]*\bpush\b[^|;&]*(--force\b|-f\b|--force-with-lease)"),
     "No force pushes. Open a branch and a pull request."),
    (re.compile(r"\b3b\s+apps\s+(connect|disconnect)\b"),
     "Connecting or disconnecting connected apps is a person's call. Ask them to run it."),
    (re.compile(r"THREE_B_API_KEY|\b3b_sk_[A-Za-z0-9]"),
     "Never read, print or pass the 3B API key. The person configures it themselves."),
    (re.compile(r"\b(curl|wget)\b[^|]*\|\s*(sudo\s+)?(sh|bash|zsh)\b|\b(sh|bash|zsh)\s+<\(\s*(curl|wget)\b"),
     "Don't pipe or substitute downloads into a shell. Ask the person to run installers."),
    (re.compile(r"\bnpx\s+(-y\s+)?skills\s+add\b|\bgh\s+skill\s+install\b"),
     "Skills are installed by a person through scripts/bootstrap.sh, pinned by skills.lock."),
    (re.compile(r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*f?\s+(/|~|\$HOME)(\s|$)|\brm\s+-[a-zA-Z]*f[a-zA-Z]*r\s+(/|~|\$HOME)(\s|$)"),
     "Refusing a destructive delete."),
]


def _first(event: dict, *keys: str) -> str:
    for k in keys:
        v = event.get(k)
        if isinstance(v, str) and v:
            return v
    return ""


def decide(event: dict) -> tuple[bool, str]:
    tool = _first(event, "tool_name", "toolName", "tool", "name")
    tool_input = event.get("tool_input") or event.get("toolInput") or event.get("input") or {}
    command = _first(event, "command") or (
        _first(tool_input, "command", "cmd") if isinstance(tool_input, dict) else "")
    hook_event = _first(event, "hook_event_name", "hookEventName", "event")

    is_mcp = (tool.startswith("mcp__")
              or hook_event in ("beforeMCPExecution", "afterMCPExecution")
              or bool(_first(event, "server", "server_name", "serverName", "url")) and not command)
    if is_mcp and tool and MCP_DENY.search(tool):
        return False, (f"'{tool}' publishes, deletes, changes access or secrets, or changes a connector. "
                       "Show the person a plan and ask them to do it in the 3B UI.")
    if command:
        for pattern, reason in SHELL_DENY:
            if pattern.search(command):
                return False, reason
    return True, ""


def main() -> int:
    cursor = "--cursor" in sys.argv
    try:
        event = json.load(sys.stdin)
        if not isinstance(event, dict):
            event = {}
    except (json.JSONDecodeError, ValueError):
        event = {}
    allowed, reason = decide(event)
    if cursor:
        if allowed:
            print(json.dumps({"permission": "allow"}))
            return 0
        print(json.dumps({"permission": "deny", "userMessage": reason, "agentMessage": reason,
                          "user_message": reason, "agent_message": reason}))
        return 2
    if allowed:
        return 0
    print(reason, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
