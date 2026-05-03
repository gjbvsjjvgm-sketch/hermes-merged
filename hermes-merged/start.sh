#!/usr/bin/env bash
# ============================================================
# Yusuf Mussa Merged Application - Startup Script
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Load .env if present
if [[ -f "${SCRIPT_DIR}/.env" ]]; then
  set -a
  source "${SCRIPT_DIR}/.env"
  set +a
fi

# Ensure YM_WEBUI_AGENT_DIR points to our bundled agent
export YM_WEBUI_AGENT_DIR="${YM_WEBUI_AGENT_DIR:-${SCRIPT_DIR}/hermes-agent}"

# Ensure YM_HOME is set
export YM_HOME="${YM_HOME:-${SCRIPT_DIR}/.ym-state}"

# Ensure state directories exist
mkdir -p "${YM_HOME}/webui/sessions"
mkdir -p "${YM_WEBUI_DEFAULT_WORKSPACE:-${SCRIPT_DIR}/workspace}"

# Find Python
PYTHON="${YM_WEBUI_PYTHON:-}"
if [[ -z "${PYTHON}" ]]; then
  if [[ -f "${SCRIPT_DIR}/venv/bin/python" ]]; then
    PYTHON="${SCRIPT_DIR}/venv/bin/python"
  elif command -v python3 >/dev/null 2>&1; then
    PYTHON="$(command -v python3)"
  elif command -v python >/dev/null 2>&1; then
    PYTHON="$(command -v python)"
  else
    echo "[XX] Python 3 is required" >&2
    exit 1
  fi
fi

echo "============================================"
echo "  Yusuf Mussa Merged Application"
echo "============================================"
echo "  Agent dir : ${YM_WEBUI_AGENT_DIR}"
echo "  Python    : ${PYTHON}"
echo "  App Home  : ${YM_HOME}"
echo "  Web UI    : http://${YM_WEBUI_HOST:-0.0.0.0}:${YM_WEBUI_PORT:-8788}"
echo "============================================"

# Start the server via start_server.py (which sets env vars properly)
exec "${PYTHON}" "${SCRIPT_DIR}/start_server.py" "$@"
