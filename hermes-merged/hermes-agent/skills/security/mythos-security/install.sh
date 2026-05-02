#!/usr/bin/env bash
# Install mythos-agent for AI-powered security scanning
set -euo pipefail

echo "[mythos-security] Checking for mythos-agent..."

if command -v mythos-agent &>/dev/null; then
    echo "[mythos-security] mythos-agent already installed: $(mythos-agent --version 2>/dev/null || echo 'unknown version')"
    exit 0
fi

if command -v npx &>/dev/null; then
    echo "[mythos-security] Installing mythos-agent via npx..."
    npm install -g mythos-agent 2>/dev/null || echo "[mythos-security] Note: npx mythos-agent can be used without global install"
    echo "[mythos-security] Installation complete"
else
    echo "[mythos-security] Node.js/npm not found. Install Node.js first for mythos-agent support."
    echo "[mythos-security] Alternatively, use: npx mythos-agent scan [path]"
fi
