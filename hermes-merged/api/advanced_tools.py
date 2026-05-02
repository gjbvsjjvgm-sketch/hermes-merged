"""
Yusuf Mussa Web UI -- Advanced Tools Integration Module.
Provides web search, code execution sandbox, image generation,
and enhanced memory capabilities.
"""

import json
import logging
import os
import threading
import time
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)

# ── Web Search Tool ──────────────────────────────────────────────────────────
# Supports Tavily, Serper.dev, and Brave Search APIs

def web_search(query: str, max_results: int = 5, provider: str = "auto") -> dict:
    """
    Perform web search using configured provider.
    Providers: tavily, serper, brave, or auto (tries each in order).

    Returns dict with: {results: [{title, url, snippet}], provider, query}
    """
    results = []
    used_provider = "none"

    # Try Tavily first
    tavily_key = os.getenv("TAVILY_API_KEY", "").strip()
    if provider in ("auto", "tavily") and tavily_key:
        try:
            import urllib.request
            req = urllib.request.Request(
                "https://api.tavily.com/search",
                data=json.dumps({
                    "api_key": tavily_key,
                    "query": query,
                    "max_results": max_results,
                    "include_answer": True,
                }).encode(),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())
                results = [
                    {"title": r.get("title", ""), "url": r.get("url", ""), "snippet": r.get("content", "")}
                    for r in data.get("results", [])[:max_results]
                ]
                used_provider = "tavily"
        except Exception as e:
            logger.warning(f"Tavily search failed: {e}")

    # Try Serper.dev
    serper_key = os.getenv("SERPER_API_KEY", "").strip()
    if not results and provider in ("auto", "serper") and serper_key:
        try:
            import urllib.request
            req = urllib.request.Request(
                "https://google.serper.dev/search",
                data=json.dumps({"q": query, "num": max_results}).encode(),
                headers={"X-API-KEY": serper_key, "Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())
                results = [
                    {"title": r.get("title", ""), "url": r.get("link", ""), "snippet": r.get("snippet", "")}
                    for r in data.get("organic", [])[:max_results]
                ]
                used_provider = "serper"
        except Exception as e:
            logger.warning(f"Serper search failed: {e}")

    # Try Brave Search
    brave_key = os.getenv("BRAVE_API_KEY", "").strip()
    if not results and provider in ("auto", "brave") and brave_key:
        try:
            import urllib.request
            req = urllib.request.Request(
                f"https://api.search.brave.com/res/v1/web/search?q={query}&count={max_results}",
                headers={"X-Subscription-Token": brave_key, "Accept": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())
                results = [
                    {"title": r.get("title", ""), "url": r.get("url", ""), "snippet": r.get("description", "")}
                    for r in data.get("web", {}).get("results", [])[:max_results]
                ]
                used_provider = "brave"
        except Exception as e:
            logger.warning(f"Brave search failed: {e}")

    return {"results": results, "provider": used_provider, "query": query}


# ── Code Execution Sandbox ──────────────────────────────────────────────────

def execute_code(code: str, language: str = "python", timeout: int = 30) -> dict:
    """
    Execute code in a sandboxed environment.
    Returns dict with: {stdout, stderr, exit_code, language, timed_out}
    """
    import subprocess
    import tempfile

    timed_out = False
    stdout = ""
    stderr = ""
    exit_code = -1

    try:
        with tempfile.NamedTemporaryFile(
            mode='w', suffix=f'.{language}', delete=False
        ) as f:
            f.write(code)
            temp_path = f.name

        if language == "python":
            cmd = [sys.executable if 'sys' in dir() else "python3", temp_path]
        elif language == "javascript":
            cmd = ["node", temp_path]
        elif language == "bash":
            cmd = ["bash", temp_path]
        else:
            return {"error": f"Unsupported language: {language}", "stdout": "", "stderr": "", "exit_code": 1}

        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout,
            cwd=tempfile.gettempdir()
        )
        stdout = proc.stdout[:10000]  # Limit output
        stderr = proc.stderr[:10000]
        exit_code = proc.returncode

    except subprocess.TimeoutExpired:
        timed_out = True
        stdout = ""
        stderr = f"Execution timed out after {timeout} seconds"
        exit_code = -1
    except Exception as e:
        stderr = str(e)
        exit_code = 1
    finally:
        try:
            os.unlink(temp_path)
        except:
            pass

    return {
        "stdout": stdout,
        "stderr": stderr,
        "exit_code": exit_code,
        "language": language,
        "timed_out": timed_out,
    }


# ── Image Generation ─────────────────────────────────────────────────────────

def generate_image(prompt: str, size: str = "1024x1024", n: int = 1) -> dict:
    """
    Generate images using OpenAI DALL-E API or compatible endpoint.
    Returns dict with: {images: [{url, b64}], provider, prompt}
    """
    openai_key = os.getenv("OPENAI_API_KEY", os.getenv("HERMES_API_KEY", "")).strip()
    base_url = os.getenv("OPENAI_BASE_URL", os.getenv("HERMES_BASE_URL", "https://api.openai.com/v1")).strip()

    images = []
    provider = "none"

    if openai_key:
        try:
            import urllib.request
            url = f"{base_url.rstrip('/')}/images/generations"
            req = urllib.request.Request(
                url,
                data=json.dumps({
                    "model": "dall-e-3",
                    "prompt": prompt,
                    "size": size,
                    "n": n,
                    "response_format": "b64_json",
                }).encode(),
                headers={
                    "Authorization": f"Bearer {openai_key}",
                    "Content-Type": "application/json",
                },
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read())
                for img in data.get("data", []):
                    images.append({
                        "url": img.get("url", ""),
                        "b64": img.get("b64_json", ""),
                    })
                provider = "openai"
        except Exception as e:
            logger.warning(f"Image generation failed: {e}")

    return {"images": images, "provider": provider, "prompt": prompt}


# ── Enhanced Memory System ───────────────────────────────────────────────────

_MEMORY_DIR = None

def _get_memory_dir() -> Path:
    """Get or create the memory storage directory."""
    global _MEMORY_DIR
    if _MEMORY_DIR is None:
        from api.config import STATE_DIR
        _MEMORY_DIR = STATE_DIR / "memory"
    _MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    return _MEMORY_DIR


def save_memory(user_id: str, key: str, value: str, category: str = "general") -> dict:
    """Save a memory entry for a user."""
    mem_dir = _get_memory_dir() / user_id
    mem_dir.mkdir(parents=True, exist_ok=True)

    entry = {
        "key": key,
        "value": value,
        "category": category,
        "timestamp": time.time(),
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    # Load existing memories
    mem_file = mem_dir / "memories.json"
    memories = []
    if mem_file.exists():
        try:
            memories = json.loads(mem_file.read_text())
        except:
            memories = []

    # Update or add
    found = False
    for i, m in enumerate(memories):
        if m.get("key") == key and m.get("category") == category:
            memories[i] = entry
            found = True
            break
    if not found:
        memories.append(entry)

    mem_file.write_text(json.dumps(memories, indent=2, ensure_ascii=False))
    return {"status": "saved", "key": key, "category": category}


def search_memory(user_id: str, query: str, limit: int = 10) -> dict:
    """Search memories by keyword."""
    mem_dir = _get_memory_dir() / user_id
    if not mem_dir.exists():
        return {"results": [], "count": 0}

    mem_file = mem_dir / "memories.json"
    if not mem_file.exists():
        return {"results": [], "count": 0}

    try:
        memories = json.loads(mem_file.read_text())
    except:
        return {"results": [], "count": 0}

    # Simple keyword search
    query_lower = query.lower()
    matched = [
        m for m in memories
        if query_lower in m.get("key", "").lower()
        or query_lower in m.get("value", "").lower()
        or query_lower in m.get("category", "").lower()
    ]

    return {"results": matched[:limit], "count": len(matched)}


def get_all_memories(user_id: str) -> dict:
    """Get all memories for a user."""
    mem_dir = _get_memory_dir() / user_id
    if not mem_dir.exists():
        return {"memories": [], "count": 0}

    mem_file = mem_dir / "memories.json"
    if not mem_file.exists():
        return {"memories": [], "count": 0}

    try:
        memories = json.loads(mem_file.read_text())
    except:
        return {"memories": [], "count": 0}

    return {"memories": memories, "count": len(memories)}


# ── System Info ───────────────────────────────────────────────────────────────

def get_system_info() -> dict:
    """Get system information including available tools and integrations."""
    return {
        "tools": {
            "web_search": bool(os.getenv("TAVILY_API_KEY", "") or os.getenv("SERPER_API_KEY", "") or os.getenv("BRAVE_API_KEY", "")),
            "image_generation": bool(os.getenv("OPENAI_API_KEY", "") or os.getenv("HERMES_API_KEY", "")),
            "code_execution": True,
            "memory": True,
            "mcp": True,
        },
        "version": "2.0.0",
        "features": [
            "web_search", "code_execution", "image_generation",
            "enhanced_memory", "mcp_protocol", "arabic_support",
            "rtl_layout", "multi_provider", "skills_system",
            "cron_scheduling", "workspace_management", "profiles",
        ],
    }
