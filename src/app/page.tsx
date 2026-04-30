import { NextResponse } from 'next/server'
import { readFileSync, existsSync } from 'fs'
import { join } from 'path'

const WEBUI_DIR = '/home/z/my-project/repos/hermes-webui'

export default function Home() {
  return null // This is a server component that redirects
}

// Serve the hermes-webui index.html directly
export async function GET() {
  try {
    const indexPath = join(WEBUI_DIR, 'static', 'index.html')
    if (existsSync(indexPath)) {
      const html = readFileSync(indexPath, 'utf-8')
      return new NextResponse(html, {
        headers: {
          'Content-Type': 'text/html; charset=utf-8',
          'Cache-Control': 'no-store',
        },
      })
    }
  } catch (error) {
    console.error('Failed to load webui index.html:', error)
  }

  // Fallback: loading page
  return new NextResponse(`<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hermes - Agent + WebUI</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #1a1a2e; color: #e8e8f0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  height: 100vh; display: flex; align-items: center; justify-content: center; }
.card { background: #16213e; border: 1px solid rgba(255,255,255,.08); border-radius: 16px; padding: 36px 32px;
  width: 420px; text-align: center; box-shadow: 0 8px 32px rgba(0,0,0,.3); }
.logo { width: 48px; height: 48px; border-radius: 12px; background: linear-gradient(145deg, #e8a030, #e94560);
  display: inline-flex; align-items: center; justify-content: center; font-weight: 800; font-size: 20px; color: #fff;
  box-shadow: 0 2px 12px rgba(233,69,96,.3); margin-bottom: 16px; }
h1 { font-size: 18px; font-weight: 600; margin-bottom: 4px; }
.sub { font-size: 12px; color: #8888aa; margin-bottom: 20px; }
.info { font-size: 11px; color: #666688; margin-top: 16px; line-height: 1.5; }
.info code { background: rgba(255,255,255,.05); padding: 2px 6px; border-radius: 4px; font-size: 10px; }
.features { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin-top: 16px; }
.tag { background: rgba(124,185,255,.1); border: 1px solid rgba(124,185,255,.2); color: #7cb9ff;
  padding: 4px 10px; border-radius: 20px; font-size: 11px; }
</style>
</head>
<body>
<div class="card">
  <div class="logo">H</div>
  <h1>Hermes Agent + WebUI</h1>
  <p class="sub">Self-improving AI agent with web interface</p>
  <div class="features">
    <span class="tag">Multi-LLM</span>
    <span class="tag">80+ Tools</span>
    <span class="tag">SSE Streaming</span>
    <span class="tag">Skills System</span>
    <span class="tag">Memory</span>
    <span class="tag">Cron Jobs</span>
  </div>
  <p class="info">
    Powered by <code>hermes-agent</code> + <code>hermes-webui</code><br>
    Merged into a single application with Next.js
  </p>
</div>
</body>
</html>`, {
    headers: { 'Content-Type': 'text/html; charset=utf-8' },
  })
}
