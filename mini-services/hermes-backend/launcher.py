"""Robust launcher for Hermes WebUI server that auto-restarts on crashes."""
import os, sys, time, signal, subprocess

# Set up environment
os.environ['HERMES_WEBUI_AGENT_DIR'] = '/home/z/my-project/repos/hermes-agent'
os.environ['HERMES_WEBUI_HOST'] = '0.0.0.0'
os.environ['HERMES_WEBUI_PORT'] = '8787'
os.environ['HERMES_WEBUI_STATE_DIR'] = os.path.expanduser('~/.hermes/webui')
os.environ['HERMES_WEBUI_DEFAULT_WORKSPACE'] = os.path.expanduser('~/workspace')
os.environ['HERMES_HOME'] = os.path.expanduser('~/.hermes')
os.environ['PYTHONPATH'] = '/home/z/my-project/repos/hermes-agent:' + os.environ.get('PYTHONPATH', '')

os.chdir('/home/z/my-project/repos/hermes-webui')

# Ignore signals that might kill us
signal.signal(signal.SIGHUP, signal.SIG_IGN)
signal.signal(signal.SIGTERM, signal.SIG_IGN)

print("[launcher] Starting Hermes WebUI with auto-restart...", flush=True)

while True:
    try:
        proc = subprocess.Popen(
            [sys.executable, '-u', 'server.py'],
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
        print(f"[launcher] Server started with PID {proc.pid}", flush=True)
        proc.wait()
        print(f"[launcher] Server exited with code {proc.returncode}", flush=True)
    except Exception as e:
        print(f"[launcher] Error: {e}", flush=True)
    
    print("[launcher] Restarting in 2 seconds...", flush=True)
    time.sleep(2)
