#!/bin/bash
# Hermes Merged Application - Startup Script
# This starts both the Python backend (hermes-webui + hermes-agent) and the Next.js frontend

set -e

echo "========================================="
echo "  Hermes Merged Application"
echo "  Agent + WebUI + Next.js Frontend"
echo "========================================="
echo ""

# Create necessary directories
mkdir -p ~/.hermes/webui/sessions
mkdir -p ~/workspace

# Start the Python backend (hermes-webui with hermes-agent)
echo "[1/2] Starting Hermes Backend (Python)..."
cd /home/z/my-project/repos/hermes-webui
export HERMES_WEBUI_AGENT_DIR="/home/z/my-project/repos/hermes-agent"
export HERMES_WEBUI_HOST="0.0.0.0"
export HERMES_WEBUI_PORT="8787"
export HERMES_WEBUI_STATE_DIR="$HOME/.hermes/webui"
export HERMES_WEBUI_DEFAULT_WORKSPACE="$HOME/workspace"
export HERMES_HOME="$HOME/.hermes"
export PYTHONPATH="/home/z/my-project/repos/hermes-agent:$PYTHONPATH"

# Start in background with auto-restart
while true; do
    echo "  Starting Python server on port 8787..."
    python3 -u server.py
    echo "  Python server exited. Restarting in 3 seconds..."
    sleep 3
done &
BACKEND_PID=$!
echo "  Backend PID: $BACKEND_PID"

# Wait for backend to be ready
echo "  Waiting for backend to be ready..."
for i in $(seq 1 30); do
    if curl -s http://127.0.0.1:8787/health > /dev/null 2>&1; then
        echo "  Backend is ready!"
        break
    fi
    sleep 1
done

echo ""
echo "[2/2] Next.js Frontend is managed by the dev server on port 3000"
echo ""
echo "========================================="
echo "  Hermes is running!"
echo "  Backend:  http://localhost:8787"
echo "  Frontend: http://localhost:3000"
echo "========================================="
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for the backend process
wait $BACKEND_PID
