#!/usr/bin/env bash
# 3B Agentic Starter Kit bootstrap.
#   scripts/bootstrap.sh skills              Install Tines' official skills at the tag in skills.lock
#   scripts/bootstrap.sh engagement <path>   Create or update a customer engagement repository from the template
#   scripts/bootstrap.sh check               Run the kit's validator
set -euo pipefail

KIT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cmd="${1:-help}"

pinned_tag() {
  awk '$1 == "tines/skills" { print $2 }' "$KIT_ROOT/skills.lock"
}

install_skills() {
  local tag
  tag="$(pinned_tag)"
  if gh skill --help >/dev/null 2>&1; then
    echo "Installing tines/skills ${tag} with gh skill (pinned)..."
    gh skill install tines/skills --all --pin "${tag}"
  else
    echo "gh skill is not available (needs gh 2.90+)." >&2
    echo "Fallback (UNPINNED, installs the default branch):" >&2
    echo "  npx skills add tines/skills -g" >&2
    echo "Record the installed version in your readiness report." >&2
    exit 1
  fi
}

copy_if_missing() {  # copy_if_missing <src> <dest>
  local src="$1" dest="$2"
  if [ -e "$dest" ]; then
    echo "  keep   ${dest#$TARGET/}"
  else
    mkdir -p "$(dirname "$dest")"
    cp -R "$src" "$dest"
    echo "  add    ${dest#$TARGET/}"
  fi
}

create_engagement() {
  TARGET="${1:?usage: bootstrap.sh engagement <path>}"
  mkdir -p "$TARGET"
  TARGET="$(cd "$TARGET" && pwd)"
  echo "Engagement repository: $TARGET"

  # Template files (never overwrite customer edits)
  (cd "$KIT_ROOT/kit/engagement-repo-template" && find . -type f) | while read -r f; do
    copy_if_missing "$KIT_ROOT/kit/engagement-repo-template/${f#./}" "$TARGET/${f#./}"
  done

  # Kit skills, subagents, hooks (refresh these: they're kit-owned)
  mkdir -p "$TARGET/.claude/skills" "$TARGET/.claude/agents" "$TARGET/.cursor" "$TARGET/scripts/hooks"
  for skill in "$KIT_ROOT"/.claude/skills/*/; do
    skill="${skill%/}"   # no trailing slash: macOS cp -R would copy the contents, not the folder
    rm -rf "$TARGET/.claude/skills/$(basename "$skill")"
    cp -R "$skill" "$TARGET/.claude/skills/"
  done
  cp "$KIT_ROOT"/.claude/agents/*.md "$TARGET/.claude/agents/"
  cp "$KIT_ROOT/.claude/settings.json" "$TARGET/.claude/settings.json"
  cp "$KIT_ROOT/.cursor/hooks.json" "$TARGET/.cursor/hooks.json"
  cp "$KIT_ROOT/.cursor/mcp.json.example" "$TARGET/.cursor/mcp.json.example"
  cp "$KIT_ROOT/scripts/hooks/guard.py" "$TARGET/scripts/hooks/guard.py"

  # Kit templates the skills copy from
  mkdir -p "$TARGET/kit"
  rm -rf "$TARGET/kit/templates"
  cp -R "$KIT_ROOT/kit/templates" "$TARGET/kit/templates"

  # Conventions skill: customer-owned after the first copy
  copy_if_missing "$KIT_ROOT/tenant-skills/enterprise-conventions" "$TARGET/.claude/skills/enterprise-conventions"

  if [ ! -d "$TARGET/.git" ]; then
    git -C "$TARGET" init -q -b main
    echo "  git init (main)"
  fi

  cat <<EOF

Next steps (a person does these):
  1. Clone the space repository into $TARGET/space  (the GitHub repo your space syncs to)
  2. Connect your editor to https://<your-tenant>/mcp with OAuth (docs/04-setup-cursor-and-claude-code.md)
  3. Customise .claude/skills/enterprise-conventions and import it into your 3B spaces from Git (auto-sync on)
  4. Open $TARGET in Cursor or Claude Code and run /3b-onboard
EOF
}

case "$cmd" in
  skills) install_skills ;;
  engagement) shift; create_engagement "$@" ;;
  check) python3 "$KIT_ROOT/scripts/validate.py" ;;
  *) sed -n '2,5p' "$0" ;;
esac
