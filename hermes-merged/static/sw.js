/**
 * Yusuf Mussa WebUI Service Worker
 * Enhanced PWA service worker with modern features:
 *   - Network-first for API calls with stale-while-revalidate option
 *   - Cache-first for static assets with runtime caching
 *   - Background sync for offline form/message submissions
 *   - Push notification handling
 *   - Rich offline page
 *   - Improved cache versioning with precache manifest
 *
 * Cache version is injected by the server at request time (routes.py /sw.js handler).
 * Bumps automatically whenever the git commit changes — no manual edits needed.
 */

// ---------------------------------------------------------------------------
// Cache versioning
// ---------------------------------------------------------------------------
const CACHE_VERSION = '__CACHE_VERSION__';
const CACHE_NAMES = {
  precache:  `ym-precache-${CACHE_VERSION}`,
  runtime:   `ym-runtime-${CACHE_VERSION}`,
  api:       `ym-api-${CACHE_VERSION}`,
  images:    `ym-images-${CACHE_VERSION}`,
};

// Convenience: all cache name prefixes for cleanup
const ALL_CACHE_PREFIXES = Object.values(CACHE_NAMES);

// ---------------------------------------------------------------------------
// Static assets that form the app shell (precache)
// ---------------------------------------------------------------------------
const SHELL_ASSETS = [
  './',
  './static/style.css',
  './static/boot.js',
  './static/ui.js',
  './static/messages.js',
  './static/sessions.js',
  './static/panels.js',
  './static/commands.js',
  './static/icons.js',
  './static/i18n.js',
  './static/workspace.js',
  './static/terminal.js',
  './static/onboarding.js',
  './static/favicon.svg',
  './static/favicon-32.png',
  './static/manifest.json',
];

// ---------------------------------------------------------------------------
// API / streaming route detection
// ---------------------------------------------------------------------------
function isApiRequest(url) {
  const p = url.pathname;
  return (
    p.startsWith('/api/') ||
    p.includes('/api/') ||
    p.includes('/stream') ||
    p.startsWith('/health') ||
    p.includes('/health')
  );
}

function isNavigationRequest(request) {
  return request.mode === 'navigate';
}

function isStaticAsset(url) {
  return SHELL_ASSETS.some((asset) => {
    const assetUrl = new URL(asset, self.location.origin);
    return url.pathname === assetUrl.pathname;
  });
}

function isImageRequest(url, request) {
  return (
    request.destination === 'image' ||
    /\.(png|jpg|jpeg|gif|webp|svg|ico)$/i.test(url.pathname)
  );
}

// ---------------------------------------------------------------------------
// Offline page HTML
// ---------------------------------------------------------------------------
const OFFLINE_PAGE_HTML = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Offline — Yusuf Mussa</title>
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{
    font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
    background:#1a1a1a;color:#e0e0e0;display:flex;align-items:center;
    justify-content:center;min-height:100vh;padding:2rem;
  }
  .container{text-align:center;max-width:480px}
  .icon{
    width:80px;height:80px;margin:0 auto 1.5rem;opacity:.5;
  }
  .icon svg{width:100%;height:100%}
  h1{font-size:1.5rem;margin-bottom:.75rem;color:#fff}
  p{font-size:1rem;line-height:1.6;margin-bottom:1.25rem;color:#aaa}
  .status{
    display:inline-flex;align-items:center;gap:.5rem;
    padding:.5rem 1rem;border-radius:9999px;font-size:.875rem;
    background:#2a2a2a;color:#ff6b6b;margin-bottom:1.5rem;
  }
  .status-dot{
    width:8px;height:8px;border-radius:50%;background:#ff6b6b;
    animation:pulse 2s infinite;
  }
  @keyframes pulse{
    0%,100%{opacity:1}50%{opacity:.4}
  }
  button{
    padding:.65rem 1.5rem;border:1px solid #444;border-radius:8px;
    background:#2a2a2a;color:#e0e0e0;font-size:1rem;cursor:pointer;
    transition:background .2s;
  }
  button:hover{background:#333}
  .queued-count{margin-top:1rem;font-size:.85rem;color:#888}
</style>
</head>
<body>
<div class="container">
  <div class="icon">
    <svg viewBox="0 0 24 24" fill="none" stroke="#888" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <line x1="1" y1="1" x2="23" y2="23"/>
      <path d="M16.72 11.06A10.94 10.94 0 0 1 19 12.55"/>
      <path d="M5 12.55a10.94 10.94 0 0 1 5.17-2.39"/>
      <path d="M10.71 5.05A16 16 0 0 1 22.56 9"/>
      <path d="M1.42 9a15.91 15.91 0 0 1 4.7-2.88"/>
      <path d="M8.53 16.11a6 6 0 0 1 6.95 0"/>
      <line x1="12" y1="20" x2="12.01" y2="20"/>
    </svg>
  </div>
  <h1>You're Offline</h1>
  <div class="status"><span class="status-dot"></span> No connection</div>
  <p>Yusuf Mussa requires a server connection. Your messages will be queued and sent automatically when you're back online.</p>
  <button onclick="window.location.reload()">Try Again</button>
  <div class="queued-count" id="queued-count"></div>
</div>
<script>
  if('serviceWorker' in navigator){
    navigator.serviceWorker.ready.then(function(reg){
      return reg.sync.getTags();
    }).then(function(tags){
      var el=document.getElementById('queued-count');
      var pending=tags.filter(function(t){return t.startsWith('ym-outbox-')}).length;
      if(pending>0) el.textContent=pending+' message'+(pending>1?'s':'')+' queued for delivery';
    }).catch(function(){});
  }
</script>
</body>
</html>`;

// ---------------------------------------------------------------------------
// Install: pre-cache the app shell
// ---------------------------------------------------------------------------
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAMES.precache).then((cache) => {
      return cache.addAll(SHELL_ASSETS).catch((err) => {
        console.warn('[sw] Shell pre-cache partial failure:', err);
      });
    })
  );
  self.skipWaiting();
});

// ---------------------------------------------------------------------------
// Activate: clean up old caches + claim clients
// ---------------------------------------------------------------------------
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((k) => !ALL_CACHE_PREFIXES.includes(k))
          .map((k) => {
            console.log('[sw] Removing old cache:', k);
            return caches.delete(k);
          })
      )
    )
  );
  self.clients.claim();
});

// ---------------------------------------------------------------------------
// Fetch handling — routing
// ---------------------------------------------------------------------------
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);

  // Never intercept cross-origin requests
  if (url.origin !== self.location.origin) return;

  // Non-GET requests: try network, queue for background sync on failure
  if (event.request.method !== 'GET') {
    event.respondWith(handleNonGetRequest(event));
    return;
  }

  // API and streaming endpoints — network-first with stale cache fallback
  if (isApiRequest(url)) {
    event.respondWith(networkFirstWithCache(event, CACHE_NAMES.api));
    return;
  }

  // Image requests — cache-first with network fallback, stored in image cache
  if (isImageRequest(url, event.request)) {
    event.respondWith(cacheFirstWithNetwork(event, CACHE_NAMES.images));
    return;
  }

  // Shell / static assets — cache-first
  if (isStaticAsset(url)) {
    event.respondWith(cacheFirstWithNetwork(event, CACHE_NAMES.precache));
    return;
  }

  // Navigation requests — network-first, fall back to offline page
  if (isNavigationRequest(event.request)) {
    event.respondWith(navigationNetworkFirst(event));
    return;
  }

  // Everything else — stale-while-revalidate
  event.respondWith(staleWhileRevalidate(event, CACHE_NAMES.runtime));
});

// ---------------------------------------------------------------------------
// Caching strategies
// ---------------------------------------------------------------------------

/**
 * Cache-first: return cached version if available, otherwise fetch & cache.
 * Used for static assets that rarely change (they're bust-binned by the
 * CACHE_VERSION in the cache name).
 */
async function cacheFirstWithNetwork(event, cacheName) {
  const cached = await caches.match(event.request);
  if (cached) return cached;

  try {
    const response = await fetch(event.request);
    if (response.ok) {
      const clone = response.clone();
      caches.open(cacheName).then((cache) => cache.put(event.request, clone));
    }
    return response;
  } catch (err) {
    // Final fallback for navigation
    if (isNavigationRequest(event.request)) {
      return offlineResponse();
    }
    return new Response('Network error', { status: 503, statusText: 'Service Unavailable' });
  }
}

/**
 * Network-first for API calls: try the network, fall back to stale cache.
 * Keeps API data fresh while still working offline from cached responses.
 */
async function networkFirstWithCache(event, cacheName) {
  try {
    const response = await fetch(event.request);
    if (response.ok) {
      const clone = response.clone();
      caches.open(cacheName).then((cache) => cache.put(event.request, clone));
    }
    return response;
  } catch (err) {
    const cached = await caches.match(event.request);
    if (cached) {
      // Inform the page that stale data is being served
      const headers = new Headers(cached.headers);
      headers.set('X-SW-Cache-Status', 'stale');
      return new Response(cached.body, {
        status: cached.status,
        statusText: cached.statusText,
        headers,
      });
    }
    return new Response(JSON.stringify({ error: 'offline', message: 'No cached data available' }), {
      status: 503,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}

/**
 * Stale-while-revalidate: return cache immediately, update cache in background.
 * Great for non-critical resources where freshness is nice but not required.
 */
async function staleWhileRevalidate(event, cacheName) {
  const cached = await caches.match(event.request);
  const fetchPromise = fetch(event.request)
    .then((response) => {
      if (response.ok) {
        const clone = response.clone();
        caches.open(cacheName).then((cache) => cache.put(event.request, clone));
      }
      return response;
    })
    .catch(() => cached);

  return cached || fetchPromise;
}

/**
 * Navigation requests: network-first with rich offline fallback.
 */
async function navigationNetworkFirst(event) {
  try {
    const response = await fetch(event.request);
    if (response.ok) {
      const clone = response.clone();
      caches.open(CACHE_NAMES.runtime).then((cache) => cache.put(event.request, clone));
    }
    return response;
  } catch (err) {
    // Try cached version of the page first
    const cached = await caches.match(event.request);
    if (cached) return cached;

    // Fall back to the app shell (cached './' route)
    const shellCached = await caches.match('./');
    if (shellCached) return shellCached;

    // Last resort: the rich offline page
    return offlineResponse();
  }
}

/**
 * Handle non-GET requests (POST/PUT/DELETE): try network, queue for
 * background sync on failure.
 */
async function handleNonGetRequest(event) {
  try {
    return await fetch(event.request);
  } catch (err) {
    // Queue for background sync if supported
    if ('sync' in self.registration) {
      try {
        await storeOutboxItem(event.request);
        const tag = 'ym-outbox-' + Date.now();
        await self.registration.sync.register(tag);
        return new Response(
          JSON.stringify({ queued: true, message: 'Request queued for background sync' }),
          { status: 202, headers: { 'Content-Type': 'application/json' } }
        );
      } catch (syncErr) {
        console.warn('[sw] Background sync registration failed:', syncErr);
      }
    }
    return new Response(
      JSON.stringify({ error: 'offline', message: 'You are offline and background sync is not available' }),
      { status: 503, headers: { 'Content-Type': 'application/json' } }
    );
  }
}

/**
 * Return the rich offline page response.
 */
function offlineResponse() {
  return new Response(OFFLINE_PAGE_HTML, {
    status: 503,
    headers: { 'Content-Type': 'text/html; charset=utf-8' },
  });
}

// ---------------------------------------------------------------------------
// Outbox (IndexedDB) for background sync
// ---------------------------------------------------------------------------
const OUTBOX_DB = 'ym-outbox';
const OUTBOX_STORE = 'requests';

function openOutboxDB() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(OUTBOX_DB, 1);
    request.onupgradeneeded = (event) => {
      const db = event.target.result;
      if (!db.objectStoreNames.contains(OUTBOX_STORE)) {
        const store = db.createObjectStore(OUTBOX_STORE, { keyPath: 'id', autoIncrement: true });
        store.createIndex('timestamp', 'timestamp', { unique: false });
      }
    };
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

async function storeOutboxItem(request) {
  const db = await openOutboxDB();
  const body = await request.text();
  const item = {
    url: request.url,
    method: request.method,
    headers: Object.fromEntries(request.headers.entries()),
    body: body,
    timestamp: Date.now(),
  };
  return new Promise((resolve, reject) => {
    const tx = db.transaction(OUTBOX_STORE, 'readwrite');
    tx.objectStore(OUTBOX_STORE).add(item);
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
  });
}

async function getAllOutboxItems() {
  const db = await openOutboxDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(OUTBOX_STORE, 'readonly');
    const request = tx.objectStore(OUTBOX_STORE).getAll();
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

async function removeOutboxItem(id) {
  const db = await openOutboxDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(OUTBOX_STORE, 'readwrite');
    tx.objectStore(OUTBOX_STORE).delete(id);
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
  });
}

async function clearOutbox() {
  const db = await openOutboxDB();
  return new Promise((resolve, reject) => {
    const tx = db.transaction(OUTBOX_STORE, 'readwrite');
    tx.objectStore(OUTBOX_STORE).clear();
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
  });
}

// ---------------------------------------------------------------------------
// Background Sync
// ---------------------------------------------------------------------------
self.addEventListener('sync', (event) => {
  if (event.tag.startsWith('ym-outbox-')) {
    event.waitUntil(replayOutbox());
  }
});

async function replayOutbox() {
  const items = await getAllOutboxItems();
  if (items.length === 0) return;

  console.log('[sw] Replaying', items.length, 'outbox item(s)');

  for (const item of items) {
    try {
      const response = await fetch(item.url, {
        method: item.method,
        headers: item.headers,
        body: item.method !== 'GET' && item.method !== 'HEAD' ? item.body : undefined,
      });

      if (response.ok) {
        await removeOutboxItem(item.id);
        // Notify all clients about the successful replay
        await notifyClients({
          type: 'SYNC_SUCCESS',
          url: item.url,
          method: item.method,
          status: response.status,
        });
      } else {
        console.warn('[sw] Replay failed for', item.url, '- status:', response.status);
        // Keep in outbox for next sync attempt
      }
    } catch (err) {
      console.warn('[sw] Replay network error for', item.url, ':', err);
      // Keep in outbox; sync will be retried by the browser
      return; // Stop replaying — we're offline again
    }
  }
}

/**
 * Send a message to all controlled client windows.
 */
async function notifyClients(message) {
  const clientList = await self.clients.matchAll({ type: 'window' });
  clientList.forEach((client) => client.postMessage(message));
}

// ---------------------------------------------------------------------------
// Push Notifications
// ---------------------------------------------------------------------------
self.addEventListener('push', (event) => {
  let data = {};

  if (event.data) {
    try {
      data = event.data.json();
    } catch {
      data = { title: 'Yusuf Mussa', body: event.data.text() };
    }
  }

  const title = data.title || 'Yusuf Mussa';
  const options = {
    body: data.body || 'You have a new notification',
    icon: data.icon || './static/favicon-32.png',
    badge: data.badge || './static/favicon-32.png',
    tag: data.tag || 'ym-notification',
    data: {
      url: data.url || './',
      timestamp: Date.now(),
    },
    vibrate: data.vibrate || [100, 50, 100],
    // Allow the app to handle the notification itself if it's in the foreground
    silent: data.silent || false,
    actions: data.actions || [],
  };

  event.waitUntil(
    self.registration.showNotification(title, options)
  );
});

// Handle notification click — focus or open the app
self.addEventListener('notificationclick', (event) => {
  event.notification.close();

  const targetUrl = (event.notification.data && event.notification.data.url) || './';
  const actionUrl = event.action
    ? (event.notification.actions.find((a) => a.action === event.action) || {}).url
    : null;
  const finalUrl = actionUrl || targetUrl;

  event.waitUntil(
    self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then((clientList) => {
      // If there's already a window open, focus it and navigate
      for (const client of clientList) {
        if (client.url.includes(self.location.origin) && 'focus' in client) {
          client.navigate(finalUrl);
          return client.focus();
        }
      }
      // Otherwise open a new window
      return self.clients.openWindow(finalUrl);
    })
  );
});

// ---------------------------------------------------------------------------
// Push subscription change (e.g., key rotation)
// ---------------------------------------------------------------------------
self.addEventListener('pushsubscriptionchange', (event) => {
  const oldSubscription = event.oldSubscription;
  const newSubscription = event.newSubscription;

  // Notify the app about the change so it can update the server
  event.waitUntil(
    notifyClients({
      type: 'PUSH_SUBSCRIPTION_CHANGE',
      oldEndpoint: oldSubscription ? oldSubscription.endpoint : null,
      newEndpoint: newSubscription ? newSubscription.endpoint : null,
    })
  );
});

// ---------------------------------------------------------------------------
// Message handling from clients
// ---------------------------------------------------------------------------
self.addEventListener('message', (event) => {
  if (!event.data || !event.data.type) return;

  switch (event.data.type) {
    case 'GET_CACHE_SIZES':
      getCacheSizes().then((sizes) => {
        event.ports[0].postMessage({ type: 'CACHE_SIZES', sizes });
      });
      break;

    case 'CLEAR_CACHES':
      clearAllCaches().then(() => {
        event.ports[0].postMessage({ type: 'CACHES_CLEARED' });
      });
      break;

    case 'GET_OUTBOX_COUNT':
      getAllOutboxItems().then((items) => {
        event.ports[0].postMessage({ type: 'OUTBOX_COUNT', count: items.length });
      });
      break;

    case 'SKIP_WAITING':
      self.skipWaiting();
      break;

    case 'GET_VERSION':
      event.ports[0].postMessage({ type: 'VERSION', version: CACHE_VERSION });
      break;

    default:
      break;
  }
});

async function getCacheSizes() {
  const sizes = {};
  for (const [name, cacheName] of Object.entries(CACHE_NAMES)) {
    const cache = await caches.open(cacheName);
    const keys = await cache.keys();
    sizes[name] = keys.length;
  }
  return sizes;
}

async function clearAllCaches() {
  const keys = await caches.keys();
  await Promise.all(keys.map((k) => caches.delete(k)));
  await clearOutbox();
}
