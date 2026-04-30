"""Hermes Backend Wrapper - runs hermes-webui server with agent integration"""
import os, sys

# Set environment
os.environ['HERMES_WEBUI_AGENT_DIR'] = '/home/z/my-project/repos/hermes-agent'
os.environ['HERMES_WEBUI_HOST'] = '127.0.0.1'
os.environ['HERMES_WEBUI_PORT'] = '8787'
os.environ['HERMES_WEBUI_STATE_DIR'] = os.path.expanduser('~/.hermes/webui')
os.environ['HERMES_WEBUI_DEFAULT_WORKSPACE'] = os.path.expanduser('~/workspace')
os.environ['HERMES_HOME'] = os.path.expanduser('~/.hermes')

# Add both repos to path
WEBUI_DIR = '/home/z/my-project/repos/hermes-webui'
AGENT_DIR = '/home/z/my-project/repos/hermes-agent'
sys.path.insert(0, AGENT_DIR)
sys.path.insert(0, WEBUI_DIR)

# Patch ThreadingHTTPServer for address reuse
from http.server import ThreadingHTTPServer
ThreadingHTTPServer.allow_reuse_address = True

# Change to webui directory
os.chdir(WEBUI_DIR)

# Now just run the server directly
import server
server.main()
