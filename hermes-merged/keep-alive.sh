#!/bin/bash
# Keep-alive wrapper for Yusuf Mussa server
while true; do
    cd /home/z/my-project/hermes-merged
    HERMES_WEBUI_HOST=0.0.0.0 /home/z/.venv/bin/python3 -u server.py 2>&1
    echo "Server exited, restarting in 3 seconds..." >&2
    sleep 3
done
