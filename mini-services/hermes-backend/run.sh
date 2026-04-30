#!/bin/bash
# Hermes Unified Backend - runs hermes-webui server with hermes-agent integration
# NO files are modified - we only set environment variables and run the original server

export HERMES_WEBUI_AGENT_DIR="/home/z/my-project/repos/hermes-agent"
export HERMES_WEBUI_HOST="0.0.0.0"
export HERMES_WEBUI_PORT="8787"
export HERMES_WEBUI_STATE_DIR="$HOME/.hermes/webui"
export HERMES_WEBUI_DEFAULT_WORKSPACE="$HOME/workspace"
export HERMES_HOME="$HOME/.hermes"

# Ensure directories exist
mkdir -p "$HERMES_WEBUI_STATE_DIR"
mkdir -p "$HERMES_WEBUI_STATE_DIR/sessions"
mkdir -p "$HOME/workspace"

# Add hermes-agent to PYTHONPATH so the webui can import it
export PYTHONPATH="/home/z/my-project/repos/hermes-agent:$PYTHONPATH"

# Run the original hermes-webui server from its repo directory
cd /home/z/my-project/repos/hermes-webui
exec python3 server.py
