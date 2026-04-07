#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
VENV_PYTHON="${REPO_ROOT}/.venv/bin/python"

if [[ -n "${PYTHON_BIN:-}" ]]; then
  PYTHON_EXEC="$PYTHON_BIN"
elif [[ -x "$VENV_PYTHON" ]]; then
  PYTHON_EXEC="$VENV_PYTHON"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_EXEC="python3"
elif command -v uv >/dev/null 2>&1; then
  PYTHON_EXEC="uv"
else
  echo "No usable Python runner found. Expected ${VENV_PYTHON}, python3, or uv." >&2
  exit 1
fi

cd "$REPO_ROOT"
if [[ "$PYTHON_EXEC" == "uv" ]]; then
  uv run --project "$REPO_ROOT" pytest tests_hidden/test_onboarding_hidden.py -q
  uv run --project "$REPO_ROOT" python scripts/check_layer_rules.py
else
  "$PYTHON_EXEC" -m pytest tests_hidden/test_onboarding_hidden.py -q
  "$PYTHON_EXEC" scripts/check_layer_rules.py
fi
