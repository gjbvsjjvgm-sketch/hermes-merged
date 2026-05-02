---
name: mythos-governance
version: 1.0.0
description: AI Agent Identity & Governance via MythOS MCP - persistent identity, governance boundaries, quality eval, and cross-session memory
category: ai-agents
tags: [mcp, governance, identity, memory, mythos]
tools: [terminal]
---

# MythOS Governance - Agent Identity & Memory

Provides AI agents with persistent identity context, governance boundaries, quality evaluation, and cross-session memory via the MythOS MCP server.

## Capabilities

- **Identity Context**: Load creator's voice, values, and venture context
- **Governance Guard**: Get constraints, execution limits, and narrative boundaries
- **Quality Evaluation**: Check pass rates, coherence scores, and diagnostics
- **Memory Search**: Search creator memory for facts, preferences, decisions
- **Session Recap**: Get recent session history for continuity
- **12 Archetypal Governance**: Run 12 governance perspectives against intent
- **Approval Gate**: Creator approves/rejects governed plans before execution

## MCP Tools Provided

| Tool | Purpose |
|------|---------|
| `mythos_getContext` | Load creator identity, voice, values, venture context |
| `mythos_guard` | Get constraints, execution limits, narrative boundaries |
| `mythos_evaluate` | Check quality health — pass rates, scores, diagnostics |
| `mythos_search` | Search creator memory — facts, preferences, decisions |
| `mythos_recap` | Get recent session history for cross-session continuity |
| `mythos_consult` | Run 12 archetypal governance seats against intent |
| `mythos_approve` | Approve or reject a consultation plan before execution |

## Setup

1. Install the MythOS MCP server: `npm install -g @myth-os/mcp`
2. Configure in your MCP settings with your MythOS backend URL
3. The tools will be available automatically when the MCP server is connected

## Usage

When the user asks about identity, governance, or memory:

- "What are my core values?" → Use `mythos_getContext`
- "Is this action within my boundaries?" → Use `mythos_guard`
- "How am I performing?" → Use `mythos_evaluate`
- "What did I decide about X?" → Use `mythos_search`
- "What happened last session?" → Use `mythos_recap`
- "Should I proceed with this plan?" → Use `mythos_consult` then `mythos_approve`
