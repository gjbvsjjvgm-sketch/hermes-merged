#!/usr/bin/env python3
"""Start the Yusuf Mussa Web UI server with correct Python environment."""
import os
import sys

# Set environment variables
os.environ['YM_WEBUI_AGENT_DIR'] = os.environ.get(
    'YM_WEBUI_AGENT_DIR', 
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ym-agent')
)
os.environ.setdefault('YM_WEBUI_HOST', '0.0.0.0')
os.environ.setdefault('YM_WEBUI_PORT', '8788')
os.environ.setdefault('YM_WEBUI_STATE_DIR', 
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '.ym-state', 'webui'))
os.environ.setdefault('YM_WEBUI_DEFAULT_WORKSPACE',
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'workspace'))
os.environ.setdefault('YM_HOME',
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '.ym-state'))

# Make sure we're using the right Python
script_dir = os.path.dirname(os.path.abspath(__file__))
os.environ['YM_WEBUI_PYTHON'] = sys.executable

# Add agent dir to sys.path so run_agent is importable
agent_dir = os.environ['YM_WEBUI_AGENT_DIR']
if agent_dir not in sys.path:
    sys.path.append(agent_dir)

# Now import and run the server
if __name__ == '__main__':
    from server import main
    main()
