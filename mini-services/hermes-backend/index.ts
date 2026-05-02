import { serve } from "bun";

const BACKEND_PORT = 8787;
const WEBUI_DIR = "/home/z/my-project/hermes-merged";
const AGENT_DIR = "/home/z/my-project/hermes-merged/hermes-agent";
const PROXY_PORT = 3030;

const HOME_DIR = process.env.HOME || "/root";
const VENV_PYTHON = HOME_DIR + "/.venv/bin/python3";

const env = {
  ...process.env,
  HERMES_WEBUI_AGENT_DIR: AGENT_DIR,
  HERMES_WEBUI_HOST: "0.0.0.0",
  HERMES_WEBUI_PORT: String(BACKEND_PORT),
  HERMES_WEBUI_STATE_DIR: HOME_DIR + "/.hermes/webui",
  HERMES_WEBUI_DEFAULT_WORKSPACE: HOME_DIR + "/workspace",
  HERMES_HOME: HOME_DIR + "/.hermes",
  PYTHONPATH: AGENT_DIR + ":" + (process.env.PYTHONPATH || ""),
  PATH: HOME_DIR + "/.venv/bin:" + (process.env.PATH || ""),
};

let pythonProcess: ReturnType<typeof Bun.spawn> | null = null;
let isServerReady = false;
let restartCount = 0;

function startPythonServer() {
  console.log(`[hermes-backend] Starting Python server (attempt ${++restartCount})...`);

  try {
    pythonProcess = Bun.spawn([VENV_PYTHON, "-u", "server.py"], {
      cwd: WEBUI_DIR,
      env,
      stdout: "pipe",
      stderr: "pipe",
    });
  } catch (e) {
    console.error("[hermes-backend] Failed to start Python:", e);
    setTimeout(startPythonServer, 5000);
    return;
  }

  const reader = pythonProcess.stdout.getReader();
  const errReader = pythonProcess.stderr.getReader();

  async function readOutput() {
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      const text = new TextDecoder().decode(value);
      console.log("[python]", text.trim());
    }
  }

  async function readErrors() {
    while (true) {
      const { done, value } = await errReader.read();
      if (done) break;
      const text = new TextDecoder().decode(value);
      console.error("[python-err]", text.trim());
    }
  }

  readOutput();
  readErrors();

  pythonProcess.exited.then((code) => {
    console.error(`[hermes-backend] Python server exited with code ${code}`);
    isServerReady = false;
    pythonProcess = null;
    // Auto-restart after delay
    setTimeout(startPythonServer, 3000);
  });

  // Wait for server to be ready, then verify with health check
  setTimeout(async () => {
    for (let i = 0; i < 5; i++) {
      try {
        const resp = await fetch(`http://127.0.0.1:${BACKEND_PORT}/health`);
        if (resp.ok) {
          isServerReady = true;
          console.log("[hermes-backend] Python server is ready!");
          return;
        }
      } catch {}
      await new Promise(r => setTimeout(r, 1000));
    }
    console.error("[hermes-backend] Python server health check failed");
  }, 3000);
}

startPythonServer();

// Health check endpoint for the proxy itself
serve({
  port: PROXY_PORT,
  async fetch(req) {
    const url = new URL(req.url);

    // Proxy health check
    if (url.pathname === "/proxy-health") {
      return Response.json({
        proxy: "ok",
        backend_ready: isServerReady,
        restart_count: restartCount,
      });
    }

    if (!isServerReady || !pythonProcess) {
      return Response.json(
        { error: "Backend not ready", ready: isServerReady },
        { status: 503 }
      );
    }

    const backendUrl = `http://127.0.0.1:${BACKEND_PORT}${url.pathname}${url.search}`;

    try {
      const headers: Record<string, string> = {};
      req.headers.forEach((v, k) => {
        const kl = k.toLowerCase();
        if (!["host", "connection", "content-length"].includes(kl)) {
          headers[k] = v;
        }
      });

      const opts: RequestInit = {
        method: req.method,
        headers,
        signal: AbortSignal.timeout(30000), // 30s timeout
      };

      if (req.method !== "GET" && req.method !== "HEAD") {
        opts.body = await req.arrayBuffer();
      }

      const resp = await fetch(backendUrl, opts);

      const respHeaders = new Headers();
      resp.headers.forEach((v, k) => {
        const kl = k.toLowerCase();
        if (!["transfer-encoding", "connection", "content-encoding"].includes(kl)) {
          respHeaders.set(k, v);
        }
      });

      return new Response(resp.body, {
        status: resp.status,
        statusText: resp.statusText,
        headers: respHeaders,
      });
    } catch (err: any) {
      // Mark backend as not ready so it gets restarted
      isServerReady = false;
      return Response.json(
        { error: `Backend error: ${err.message}` },
        { status: 502 }
      );
    }
  },
});

console.log(`[hermes-backend] Proxy server running on port ${PROXY_PORT}`);
