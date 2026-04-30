import { NextRequest, NextResponse } from 'next/server';

const PROXY_URL = 'http://127.0.0.1:3030';

export async function GET(request: NextRequest) {
  try {
    const url = new URL(request.url);
    const backendUrl = `${PROXY_URL}/static${url.pathname.replace('/static', '')}${url.search}`;

    const resp = await fetch(backendUrl, { signal: AbortSignal.timeout(30000) });
    const contentType = resp.headers.get('content-type') || 'application/octet-stream';

    const headers = new Headers();
    headers.set('Content-Type', contentType);
    headers.set('Cache-Control', 'public, max-age=3600');

    const data = await resp.arrayBuffer();
    return new NextResponse(data, {
      status: resp.status,
      headers,
    });
  } catch (err: unknown) {
    const msg = err instanceof Error ? err.message : 'Unknown error';
    return NextResponse.json({ error: `Static file error: ${msg}` }, { status: 502 });
  }
}
