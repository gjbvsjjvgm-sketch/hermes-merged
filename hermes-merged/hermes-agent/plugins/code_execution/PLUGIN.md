---
name: code-execution
version: 1.0.0
description: Secure code execution in sandboxed environments - Python, JavaScript, TypeScript, and more
category: execution
tools: [execute_code, terminal]
---

# Code Execution Plugin

Secure code execution in sandboxed environments for AI-generated code.

## Supported Environments

| Environment | Languages | Security | Speed |
|-------------|-----------|----------|-------|
| Local Shell | All | Low | Fast |
| Docker Container | All | High | Medium |
| E2B Sandbox | Python, JS | Very High | Medium |
| Modal | Python | High | Fast |

## Features
- Multi-language support (Python, JS, TS, Rust, Go, etc.)
- Timeout management
- Output capture (stdout, stderr)
- Package installation within sandbox
- File I/O within sandbox
- Network access control
- Resource limits (memory, CPU)
