---
Task ID: 1
Agent: main
Task: Merge hermes-webui and hermes-agent into one working application

Work Log:
- Verified existing hermes-merged directory from previous session
- Checked all files present: hermes-webui (326 files) + hermes-agent (2829 files) all preserved
- Compared file lists: ZERO missing files from either repository
- Verified Python venv with pyyaml dependency installed
- Tested server startup: all endpoints responding correctly
  - GET / → 200 (main HTML page)
  - GET /api/sessions → 200 (JSON response)
  - GET /api/models → 200 (JSON response)
  - GET /api/workspaces → 200 (JSON response)
  - GET /static/style.css → 200
  - GET /static/ui.js → 200
- Created start.sh startup script (executable by z user)
- Removed stray =6.0 file
- Server starts on http://0.0.0.0:8788

Stage Summary:
- Application is fully functional at /home/z/my-project/hermes-merged/
- All 326 files from hermes-webui preserved exactly
- All 2829 files from hermes-agent preserved exactly
- Integration glue: .env, start_server.py, start.sh, run.sh
- To run: cd /home/z/my-project/hermes-merged && bash start.sh
