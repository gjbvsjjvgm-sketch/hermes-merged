import { NextRequest, NextResponse } from 'next/server';

// The Python backend is managed by a Bun mini-service on port 3030
// which auto-restarts the Python server when it crashes.
const PROXY_URL = 'http://127.0.0.1:3030';

function filterHeaders(headers: Headers): Record<string, string> {
  const out: Record<string, string> = {};
  const skip = new Set(['host', 'connection', 'content-length', 'transfer-encoding']);
  headers.forEach((v, k) => {
    if (!skip.has(k.toLowerCase())) out[k] = v;
  });
  return out;
}

async function proxy(request: NextRequest, method: string): Promise<NextResponse> {
  try {
    const url = new URL(request.url);
    const backendUrl = `${PROXY_URL}${url.pathname}${url.search}`;

    const headers = filterHeaders(request.headers);
    const opts: RequestInit = { method, headers, signal: AbortSignal.timeout(60000) };

    if (method !== 'GET' && method !== 'HEAD') {
      const body = await request.arrayBuffer();
      if (body.byteLength > 0) opts.body = body;
    }

    const resp = await fetch(backendUrl, opts);

    const respHeaders = new Headers();
    resp.headers.forEach((v, k) => {
      const kl = k.toLowerCase();
      if (!['transfer-encoding', 'connection', 'content-encoding'].includes(kl)) {
        respHeaders.set(k, v);
      }
    });

    return new NextResponse(resp.body, {
      status: resp.status,
      statusText: resp.statusText,
      headers: respHeaders,
    });
  } catch (err: unknown) {
    const msg = err instanceof Error ? err.message : 'Unknown error';
    console.error('[hermes-proxy] Error:', msg);
    return NextResponse.json({ error: `Backend error: ${msg}` }, { status: 502 });
  }
}

export async function GET(request: NextRequest) { return proxy(request, 'GET'); }
export async function POST(request: NextRequest) { return proxy(request, 'POST'); }
export async function PUT(request: NextRequest) { return proxy(request, 'PUT'); }
export async function DELETE(request: NextRequest) { return proxy(request, 'DELETE'); }
export async function PATCH(request: NextRequest) { return proxy(request, 'PATCH'); }
export async function OPTIONS(request: NextRequest) { return proxy(request, 'OPTIONS'); }
