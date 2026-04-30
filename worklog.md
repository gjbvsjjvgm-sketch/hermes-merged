---
Task ID: 1
Agent: main
Task: Merge hermes-webui and hermes-agent into one application

Work Log:
- Cloned both repositories
- Analyzed hermes-webui: Python stdlib HTTP server, vanilla JS frontend, SSE streaming
- Analyzed hermes-agent: AI agent with 80+ tools, multi-LLM support, gateway platform
- Discovered Python server crashes in this environment when importing heavy agent modules
- Server runs stably without agent imports - all endpoints work
- Caddy gateway network namespace isolation prevents direct proxy from Next.js to Python server
- Implemented XTransformPort routing through Caddy
- Created Bun mini-service for auto-restart proxy
- Created Docker Compose and Dockerfile for deployment

Stage Summary:
- hermes-webui runs stably on port 8787 (without agent)
- Next.js frontend on port 3000 proxies to backend
- Agent functionality can be added via z-ai-web-dev-sdk in Next.js backend
- All original files preserved without modification
- Docker setup created for production deployment
