import { NextRequest, NextResponse } from 'next/server';

const HERMES_BACKEND = 'http://localhost:8787';

// Headers that should NOT be forwarded between client and backend
const HOP_BY_HOP = new Set([
  'host',
  'connection',
  'content-length',
  'transfer-encoding',
  'content-encoding',
  'upgrade',
]);

function filterRequestHeaders(headers: Headers): Record<string, string> {
  const out: Record<string, string> = {};
  headers.forEach((v, k) => {
    if (!HOP_BY_HOP.has(k.toLowerCase())) out[k] = v;
  });
  return out;
}

function filterResponseHeaders(headers: Headers): Headers {
  const out = new Headers();
  headers.forEach((v, k) => {
    if (!HOP_BY_HOP.has(k.toLowerCase())) out.set(k, v);
  });
  return out;
}

async function proxy(request: NextRequest, method: string): Promise<NextResponse> {
  try {
    const url = new URL(request.url);
    // Strip the /hermes prefix so /hermes/api/sessions → /api/sessions
    const backendPath = url.pathname.replace(/^\/hermes/, '') || '/';
    const backendUrl = `${HERMES_BACKEND}${backendPath}${url.search}`;

    const headers = filterRequestHeaders(request.headers);
    const opts: RequestInit = { method, headers, signal: AbortSignal.timeout(60000) };

    // Forward body for non-GET/HEAD requests
    if (method !== 'GET' && method !== 'HEAD') {
      const body = await request.arrayBuffer();
      if (body.byteLength > 0) opts.body = body;
    }

    const resp = await fetch(backendUrl, opts);
    const respHeaders = filterResponseHeaders(resp.headers);

    return new NextResponse(resp.body, {
      status: resp.status,
      statusText: resp.statusText,
      headers: respHeaders,
    });
  } catch (err: unknown) {
    const msg = err instanceof Error ? err.message : 'Unknown error';
    console.error('[hermes-proxy] Error:', msg);
    return NextResponse.json({ error: `Hermes backend error: ${msg}` }, { status: 502 });
  }
}

export async function GET(request: NextRequest) { return proxy(request, 'GET'); }
export async function POST(request: NextRequest) { return proxy(request, 'POST'); }
export async function PUT(request: NextRequest) { return proxy(request, 'PUT'); }
export async function DELETE(request: NextRequest) { return proxy(request, 'DELETE'); }
export async function PATCH(request: NextRequest) { return proxy(request, 'PATCH'); }
export async function OPTIONS(request: NextRequest) { return proxy(request, 'OPTIONS'); }
