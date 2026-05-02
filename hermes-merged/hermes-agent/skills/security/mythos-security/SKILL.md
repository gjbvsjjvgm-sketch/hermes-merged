---
name: mythos-security
version: 1.0.0
description: AI-powered code security scanning using Mythos Agent - hypothesis-driven vulnerability detection, variant analysis, and automated patching
category: security
tags: [security, code-review, vulnerability, scanning, mythos]
tools: [terminal, file]
---

# Mythos Security Scanner

AI-powered security scanning using Mythos Agent - the open-source code security scanner with hypothesis-driven vulnerability detection.

## Capabilities

- **Full Security Scan**: Run comprehensive security scans on codebases
- **Variant Analysis**: Find variants of known CVEs in your code
- **AI-Powered Fix**: Generate and apply security patches
- **Taint Analysis**: Trace data flow for security issues
- **Continuous Monitoring**: Watch for security issues on file changes
- **Trust Score**: Assess codebase security trustworthiness

## Usage

When the user asks to scan code for security issues:

1. First check if mythos-agent is installed: `npx mythos-agent --version`
2. If not installed, install it: `npm install -g mythos-agent`
3. Run the appropriate scan command based on the user's request

### Scan Commands

| Command | Purpose |
|---------|---------|
| `mythos-agent scan [path]` | Standard scan (patterns + secrets + deps + IaC + AI) |
| `mythos-agent hunt [path]` | Full autonomous multi-agent scan |
| `mythos-agent variants [cve-id]` | Find variants of known CVEs |
| `mythos-agent fix [path]` | Generate AI-powered patches |
| `mythos-agent taint [path]` | Data flow / taint analysis |
| `mythos-agent ask [question]` | Natural language security queries |
| `mythos-agent watch` | Continuous monitoring |
| `mythos-agent report [path]` | Export findings as JSON/HTML/SARIF |

### Example Interactions

User: "Scan my code for security vulnerabilities"
→ Run `mythos-agent scan .` in the workspace directory and present findings

User: "Check if my code has any CVEs similar to CVE-2024-1234"
→ Run `mythos-agent variants CVE-2024-1234`

User: "Fix the security issues in src/auth.py"
→ Run `mythos-agent fix src/auth.py --apply` (with user confirmation)

User: "How secure is my codebase?"
→ Run `mythos-agent scan .` and summarize the trust score and findings

## Supported Languages
TypeScript, JavaScript, Python, Go, Rust, Java, C/C++, Ruby

## Scanner Categories
43 scanner categories with 329+ rules covering:
- Injection vulnerabilities (SQL, NoSQL, Command, LDAP)
- Authentication & authorization flaws
- Cryptographic weaknesses
- Race conditions & concurrency issues
- Path traversal & file operations
- Deserialization attacks
- SSRF & CSRF vulnerabilities
- Secrets & credential exposure
- Dependency vulnerabilities
- Infrastructure as Code (IaC) misconfigurations

## Notes
- Always ask for confirmation before applying patches with `--apply`
- For large codebases, suggest starting with `scan` before `hunt`
- The `hunt` command is more thorough but takes longer
- Results can be exported for CI/CD integration using `report`
