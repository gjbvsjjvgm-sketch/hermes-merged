---
name: web-search
version: 1.0.0
description: Multi-provider web search integration - Brave Search, Tavily, Serper, Google Custom Search
category: search
tools: [web_search, web_extract]
---

# Web Search Plugin

Real-time web search integration with multiple search providers for up-to-date information retrieval.

## Supported Providers

| Provider | Type | Quality | Rate Limit |
|----------|------|---------|------------|
| Brave Search API | API Key | Excellent | 2000/month free |
| Tavily | API Key | AI-optimized | 1000/month free |
| Serper | API Key | Google results | 2500/month free |
| Google Custom Search | API Key | Google quality | 100/day free |

## Configuration

Add to config.yaml:
```yaml
web_search:
  provider: brave  # brave, tavily, serper, google
  api_key: ${WEB_SEARCH_API_KEY}
  max_results: 10
  include_snippets: true
```

## Features
- Multi-provider fallback chain
- Result deduplication
- Snippet extraction
- Freshness filtering (day, week, month)
- Domain filtering (include/exclude)
- Safe search mode
