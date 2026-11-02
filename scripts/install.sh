#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_SKILL_DIR="${1:-$HOME/.claude/skills}"

# 1. Scrub any sensitive political files if accidentally copied from external folders
find "$REPO_ROOT/personas" -type f \( -iname "*mao*" -o -iname "*stalin*" -o -iname "*hitler*" -o -iname "*lenin*" \) -delete 2>/dev/null || true

# 2. Build/refresh the 200-persona catalog and registry.json
PYTHON_BIN="$(command -v python3 || command -v python)"
"$PYTHON_BIN" "$REPO_ROOT/scripts/build_200_personas.py"

# 3. Register ONLY the single gateway folder (1 skill install, 200 internal personas)
mkdir -p "$TARGET_SKILL_DIR"
ln -sfn "$REPO_ROOT" "$TARGET_SKILL_DIR/greatest-persons" 2>/dev/null || cp -R "$REPO_ROOT" "$TARGET_SKILL_DIR/greatest-persons"

echo "[OK] Installed 'greatest-persons' as a single unified skill at: $TARGET_SKILL_DIR/greatest-persons"
echo "[OK] 200 textbook personas indexed in: $REPO_ROOT/config/registry.json"
