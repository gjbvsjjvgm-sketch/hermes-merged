FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git && rm -rf /var/lib/apt/lists/*

# Copy both repositories
COPY repos/hermes-webui /app/hermes-webui
COPY repos/hermes-agent /app/hermes-agent

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/hermes-webui/requirements.txt
RUN pip install --no-cache-dir -r /app/hermes-agent/requirements.txt 2>/dev/null || \
    pip install --no-cache-dir openai anthropic httpx rich prompt_toolkit tenacity pydantic jinja2 requests python-dotenv fire

# Set environment variables
ENV HERMES_WEBUI_AGENT_DIR=/app/hermes-agent
ENV HERMES_WEBUI_HOST=0.0.0.0
ENV HERMES_WEBUI_PORT=8787
ENV HERMES_HOME=/root/.hermes
ENV HERMES_WEBUI_STATE_DIR=/root/.hermes/webui
ENV HERMES_WEBUI_DEFAULT_WORKSPACE=/root/workspace
ENV PYTHONPATH=/app/hermes-agent

# Create necessary directories
RUN mkdir -p /root/.hermes/webui/sessions /root/workspace

# Expose the webui port
EXPOSE 8787

# Set working directory to the webui
WORKDIR /app/hermes-webui

# Start the server
CMD ["python3", "-u", "server.py"]
