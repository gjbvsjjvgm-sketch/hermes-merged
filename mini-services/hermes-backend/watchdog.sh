#!/bin/bash
# Watchdog that keeps the Hermes server running
while true; do
    cd /home/z/my-project/repos/hermes-webui
    export HERMES_WEBUI_AGENT_DIR="/home/z/my-project/repos/hermes-agent"
    export HERMES_WEBUI_HOST="127.0.0.1"
    export HERMES_WEBUI_PORT="8787"
    export HERMES_WEBUI_STATE_DIR="$HOME/.hermes/webui"
    export HERMES_WEBUI_DEFAULT_WORKSPACE="$HOME/workspace"
    export HERMES_HOME="$HOME/.hermes"
    export PYTHONPATH="/home/z/my-project/repos/hermes-agent:$PYTHONPATH"
    
    echo "[$(date)] Starting Hermes server..." >> /tmp/hermes-watchdog.log
    python3 -u server.py 2>&1 | tee -a /tmp/hermes-watchdog.log
    EXIT_CODE=$?
    echo "[$(date)] Server exited with code $EXIT_CODE" >> /tmp/hermes-watchdog.log
    sleep 2
done
