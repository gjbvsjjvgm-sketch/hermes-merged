#!/usr/bin/env bash
# ============================================================
# Yusuf Mussa — Termux Quick Installer
# Runs on Android via Termux (F-Droid version)
# ============================================================
set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
GOLD='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

echo ""
echo -e "${GOLD}╔══════════════════════════════════════════╗${NC}"
echo -e "${GOLD}║      Yusuf Mussa — Termux Installer      ║${NC}"
echo -e "${GOLD}║     وكيل الذكاء الاصطناعي المتقدم       ║${NC}"
echo -e "${GOLD}╚══════════════════════════════════════════╝${NC}"
echo ""

# Detect Termux
IS_TERMUX=false
if [ -d "/data/data/com.termux" ] || [ -n "$TERMUX_VERSION" ] || [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    IS_TERMUX=true
    echo -e "${CYAN}[✓] Running on Termux${NC}"
else
    echo -e "${BLUE}[i] Not running on Termux — continuing anyway${NC}"
fi

# Step 1: Update packages
echo ""
echo -e "${BLUE}[1/7] Updating packages...${NC}"
pkg update -y 2>/dev/null || sudo apt-get update -y
pkg upgrade -y 2>/dev/null || sudo apt-get upgrade -y

# Step 2: Install dependencies
echo ""
echo -e "${BLUE}[2/7] Installing dependencies...${NC}"
if [ "$IS_TERMUX" = true ]; then
    pkg install -y git python python-pip build-essential binutils openssl curl wget nano
else
    sudo apt-get install -y git python3 python3-pip build-essential curl wget nano
fi

# Step 3: Setup Python
echo ""
echo -e "${BLUE}[3/7] Setting up Python...${NC}"
PYTHON_CMD="python3"
if [ "$IS_TERMUX" = true ]; then
    PYTHON_CMD="python"
fi

$PYTHON_CMD -m pip install --upgrade pip
$PYTHON_CMD -m pip install pyyaml

# Step 4: Clone repository
echo ""
echo -e "${BLUE}[4/7] Cloning Yusuf Mussa...${NC}"
INSTALL_DIR="$HOME/hermes-merged"
if [ -d "$INSTALL_DIR" ]; then
    echo -e "${GOLD}[i] Directory exists — pulling latest...${NC}"
    cd "$INSTALL_DIR"
    git pull --ff-only 2>/dev/null || echo -e "${RED}[!] Pull failed — using existing code${NC}"
else
    git clone https://github.com/gjbvsjjvgm-sketch/hermes-merged.git "$INSTALL_DIR"
    cd "$INSTALL_DIR"
fi

# Step 5: Setup environment
echo ""
echo -e "${BLUE}[5/7] Setting up environment...${NC}"
mkdir -p "$HOME/.hermes"
mkdir -p "$INSTALL_DIR/workspace"
mkdir -p "$INSTALL_DIR/.hermes-state/webui/sessions"

# Create .env if it doesn't exist
if [ ! -f "$INSTALL_DIR/.env" ]; then
    cat > "$INSTALL_DIR/.env" << 'ENVEOF'
# Yusuf Mussa Configuration
# Add your API keys below:

# OpenAI
# OPENAI_API_KEY=sk-your-key-here

# Anthropic
# ANTHROPIC_API_KEY=sk-ant-your-key-here

# DeepSeek
# DEEPSEEK_API_KEY=your-key-here

# OpenRouter (200+ models)
# OPENROUTER_API_KEY=your-key-here

# Google/Gemini
# GOOGLE_API_KEY=your-key-here

# Default provider and model
HERMES_WEBUI_HOST=0.0.0.0
HERMES_WEBUI_PORT=8788
ENVEOF
    echo -e "${GREEN}[✓] Created .env file — edit it to add your API keys${NC}"
fi

# Step 6: Make scripts executable
echo ""
echo -e "${BLUE}[6/7] Making scripts executable...${NC}"
chmod +x "$INSTALL_DIR/start.sh"

# Step 7: Done!
echo ""
echo -e "${GREEN}╔══════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║         Installation Complete!            ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════╝${NC}"
echo ""
echo -e "${GOLD}To start Yusuf Mussa:${NC}"
echo ""
echo -e "  ${CYAN}cd $INSTALL_DIR${NC}"
echo -e "  ${CYAN}./start.sh${NC}"
echo ""
echo -e "${GOLD}Or directly:${NC}"
echo ""
echo -e "  ${CYAN}$PYTHON_CMD $INSTALL_DIR/start_server.py${NC}"
echo ""
echo -e "${GOLD}Then open in browser:${NC}"
echo ""
echo -e "  ${CYAN}http://localhost:8788${NC}"
echo ""
echo -e "${GOLD}To add API keys, edit:${NC}"
echo ""
echo -e "  ${CYAN}nano $INSTALL_DIR/.env${NC}"
echo ""
echo -e "${GOLD}To run in background:${NC}"
echo ""
echo -e "  ${CYAN}nohup $PYTHON_CMD $INSTALL_DIR/start_server.py &${NC}"
echo ""
echo -e "${RED}Important: Add at least one API key in .env before starting!${NC}"
echo ""
