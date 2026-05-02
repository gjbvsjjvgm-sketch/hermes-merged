#!/usr/bin/env python3
"""Start the Yusuf Mussa Web UI server with correct Python environment."""
import os
import sys

# Set environment variables
os.environ['HERMES_WEBUI_AGENT_DIR'] = os.environ.get(
    'HERMES_WEBUI_AGENT_DIR', 
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hermes-agent')
)
os.environ.setdefault('HERMES_WEBUI_HOST', '0.0.0.0')
os.environ.setdefault('HERMES_WEBUI_PORT', '8787')
os.environ.setdefault('HERMES_WEBUI_STATE_DIR', 
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '.hermes-state', 'webui'))
os.environ.setdefault('HERMES_WEBUI_DEFAULT_WORKSPACE',
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'workspace'))
os.environ.setdefault('HERMES_HOME',
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '.hermes-state'))

# Make sure we're using the right Python
script_dir = os.path.dirname(os.path.abspath(__file__))
os.environ['HERMES_WEBUI_PYTHON'] = sys.executable

# Add agent dir to sys.path so run_agent is importable
agent_dir = os.environ['HERMES_WEBUI_AGENT_DIR']
if agent_dir not in sys.path:
    sys.path.append(agent_dir)

# Now import and run the server
if __name__ == '__main__':
    from server import main
    main()
