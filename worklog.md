---
Task ID: 1
Agent: Main Agent
Task: Merge hermes-webui and hermes-agent into a single complete application

Work Log:
- Cloned both repositories: hermes-webui (frontend/web server) and hermes-agent (Python AI agent backend)
- Analyzed both repository structures in detail
- Discovered hermes-webui is a Python stdlib HTTP server with static HTML/JS frontend and API routes
- Discovered hermes-agent is a Python AI agent with tool calling capabilities (AIAgent class)
- Found that hermes-webui's api/config.py has a discovery mechanism (_discover_agent_dir) that searches for hermes-agent
- Created merged project at /home/z/my-project/hermes-merged/
- Copied ALL files from hermes-webui to merged project root (preserving all files unmodified)
- Copied ALL files from hermes-agent to merged project/hermes-agent/ subdirectory (preserving all files unmodified)
- Created Python virtual environment with Python 3.12
- Installed hermes-webui dependencies (pyyaml)
- Installed hermes-agent as editable package with all core dependencies
- Created .env configuration file with HERMES_WEBUI_AGENT_DIR pointing to the bundled agent
- Created .hermes-state/ directory for Hermes state storage
- Created config.yaml for Hermes agent configuration
- Created start_server.py wrapper script that sets environment and starts the server
- Created run.sh bash startup script
- Tested and verified all API endpoints working
- Verified run_agent import works correctly (Imports OK: True)
- Used port 8788 to avoid conflict with existing service on 8787

Stage Summary:
- Merged project successfully created at /home/z/my-project/hermes-merged/
- ALL files from both repositories preserved without modification
- hermes-webui works as the frontend (unchanged)
- hermes-agent works as the backend (unchanged, in hermes-agent/ subdirectory)
- Server starts successfully with all endpoints working
- API verification: health, models, providers, settings, onboarding all return correct responses
- Static files (HTML, JS, CSS, favicon) all served correctly
- Application is in "needs_provider" state (ready for LLM provider configuration)
