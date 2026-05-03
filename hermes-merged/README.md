# Yusuf Mussa — Advanced AI Agent

<div align="center">

![Yusuf Mussa](https://img.shields.io/badge/Yusuf%20Mussa-v2.0-gold?style=for-the-badge&labelColor=1a1a2e&color=F5C542)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Termux-orange?style=flat-square)

**وكيل ذكاء اصطناعي متقدم لبناء التطبيقات والتصاميم وحل الأخطاء وإنشاء مشاريع SaaS**

[English](#english) | [العربية](#العربية) | [التثبيت السريع](#التثبيت-السريع-1)

</div>

---

<a id="english"></a>

## What is Yusuf Mussa?

Yusuf Mussa is a fully self-hosted, privacy-first AI agent that runs entirely on your machine. It combines a powerful web-based chat interface with a sophisticated backend agent engine capable of programming, design, debugging, application building, SaaS creation, and complex program development. Unlike cloud-only AI tools, all your data, conversations, and code stay on your device.

### Core Capabilities

| Capability | Description |
|------------|-------------|
| **Full-Stack Programming** | Write code in any language (Python, JS, TS, Rust, Go, Java, C++, Ruby, PHP) — build complete applications from scratch |
| **SaaS Building** | Create multi-tenant SaaS projects with authentication, payments (Stripe/Paymob/PayPal), and APIs |
| **UI/UX Design** | Generate modern, responsive designs with CSS frameworks, design systems, and component libraries |
| **Bug Fixing & Debugging** | Analyze errors, trace bugs, review code, optimize performance across any codebase |
| **Infrastructure & DevOps** | Docker, Kubernetes, CI/CD pipelines, deployment automation, monitoring setup |
| **Database Design** | PostgreSQL, MySQL, MongoDB, SQLite, Redis — schema design, migrations, optimization |
| **Browser Automation** | Web scraping, data extraction, task automation using headless browser control |
| **Research & Analysis** | Web search, academic paper analysis, data synthesis, report generation |
| **Persistent Memory** | Learns and remembers across sessions, improves over time |
| **Image Generation** | Create AI-generated images, logos, icons, and visual assets |

### Web Interface Features

- **Live Streaming** — Responses appear character-by-character as they are generated via Server-Sent Events (SSE)
- **20+ AI Providers** — OpenAI, Anthropic, Google, DeepSeek, Qwen, Z.AI, xAI, Mistral, OpenRouter, and more
- **10 Themes & Skins** — Default, Ares, Mono, Slate, Poseidon, Sisyphus, Charizard, Sienna, Aurora (glassmorphism), Neon (cyberpunk)
- **8 Languages** — English, العربية (full RTL), Русский, Español, Deutsch, 中文, Português, 한국어
- **File Browser** — Browse, edit, and create files directly in the workspace panel
- **Built-in Terminal** — Execute shell commands from the browser using xterm.js
- **Voice Input** — Speak instead of typing using Web Speech API or MediaRecorder
- **Scheduled Tasks** — Cron jobs that run even when you are offline
- **Self-improving Skills** — Automatically writes and saves new skills as it works
- **PWA Support** — Install as a native-like app on your phone
- **Multi-profile Support** — Switch between different agent configurations and workspaces
- **Workspace Panel** — Side-by-side file browsing and code preview while chatting

### 60+ Built-in Tools

```
browser         — Browser automation (13 sub-tools)
code_execution  — Execute Python/JS/any language
file            — Read, write, edit, search files
terminal        — Execute shell commands
web             — Web search and content extraction
image_gen       — AI image generation
delegation      — Delegate tasks to sub-agents
memory          — Persistent memory across sessions
todo            — Task list management
cronjob         — Schedule recurring tasks
skills          — Extensible skill system
clarify         — Ask clarifying questions
webhook         — Send/receive webhook notifications
```

---

<a id="العربية"></a>

## ما هو Yusuf Mussa؟

Yusuf Mussa هو وكيل ذكاء اصطناعي متقدم ومتكامل يعمل محلياً على جهازك بالكامل، مما يضمن خصوصية بياناتك. يجمع بين واجهة ويب متطورة ومحرك وكيل خلفي قادر على البرمجة والتصميم وحل الأخطاء وبناء التطبيقات وإنشاء مشاريع SaaS وتطوير برامج معقدة. على عكس أدوات الذكاء الاصطناعي السحابية، جميع بياناتك ومحادثاتك وشيفراتك تبقى على جهازك.

### القدرات الأساسية

| القدرة | الوصف |
|--------|-------|
| برمجة كاملة | Python, JS, TS, Rust, Go, Java, C++, Ruby, PHP وأكثر |
| بناء تطبيقات ويب | Next.js, React, Vue, Django, Flask, FastAPI |
| بناء SaaS | مصادقة، دفع Stripe/Paymob/PayPal، multi-tenancy، APIs |
| تطبيقات موبايل | React Native, Flutter, PWA |
| قواعد بيانات | PostgreSQL, MySQL, MongoDB, SQLite, Redis |
| DevOps | Docker, K8s, GitHub Actions, CI/CD |
| تصميم UI/UX | CSS حديث، Tailwind، أنظمة تصميم، responsive |
| حل الأخطاء | تحليل، تصحيح، مراجعة كود، تحسين أداء |
| أتمتة | Shell scripts، cron jobs، web scraping |
| أمان | فحص ثغرات، تصحيح أمني، أفضل الممارسات |
| توليد صور | إنشاء صور ورموز وأصول بصرية بالذكاء الاصطناعي |
| بحث وتحليل | بحث ويب، تحليل أوراق علمية، استخراج معلومات |

---

<a id="التثبيت-السريع-1"></a>

## التثبيت السريع

### Linux / macOS (أمر واحد)

```bash
git clone https://github.com/gjbvsjjvgm-sketch/hermes-merged.git && cd hermes-merged && python3 start_server.py
```

### أو بالتفصيل

```bash
git clone https://github.com/gjbvsjjvgm-sketch/hermes-merged.git
cd hermes-merged
python3 start_server.py
```

ثم افتح **http://localhost:8788** في المتصفح.

### Docker

```bash
docker compose up -d
```

أو بناء يدوي:

```bash
docker build -t yusuf-mussa .
docker run -d -p 8788:8788 -v ~/.yusuf-mussa:/home/yusufmussa/.yusuf-mussa yusuf-mussa
```

---

## التثبيت على Termux (أندرويد)

> **Termux** هو محاكي طرفية أندرويد يتيح تشغيل Yusuf Mussa بالكامل على هاتفك!

### تثبيت سريع بأمر واحد (Termux)

```bash
pkg update -y && pkg upgrade -y && pkg install -y git python python-pip build-essential && pip install pyyaml && cd ~ && git clone https://github.com/gjbvsjjvgm-sketch/hermes-merged.git && cd hermes-merged && python3 start_server.py
```

### تثبيت مفصل خطوة بخطوة

**الخطوة 1:** ثبّت Termux من [F-Droid](https://f-droid.org/packages/com.termux/) (لا تستخدم نسخة Google Play)

**الخطوة 2:** حدّث الحزم وثبّت الأدوات:

```bash
pkg update && pkg upgrade -y
pkg install -y git python python-pip nodejs-lts build-essential binutils openssl
pip install --upgrade pip pyyaml
```

**الخطوة 3:** حمّل المشروع وشغّله:

```bash
cd ~
git clone https://github.com/gjbvsjjvgm-sketch/hermes-merged.git
cd hermes-merged
python3 start_server.py
```

**الخطوة 4:** افتح **http://localhost:8788** في متصفح هاتفك.

### نصائح Termux

```bash
# تشغيل في الخلفية
nohup python3 start_server.py &

# أو باستخدام tmux
pkg install tmux
tmux new -s yusuf
python3 start_server.py
# Ctrl+B ثم D للفصل | tmux attach -t yusuf للعودة

# تشغيل تلقائي عند فتح Termux
echo 'cd ~/hermes-merged && python3 start_server.py' >> ~/.bashrc

# تغيير المنفذ
YM_WEBUI_PORT=9000 python3 start_server.py

# تفعيل كلمة المرور
YM_WEBUI_PASSWORD=your-secret python3 start_server.py

# الوصول من كمبيوتر آخر على نفس الشبكة
ifconfig | grep inet    # اعرف IP الهاتف
# ثم من الكمبيوتر: http://PHONE-IP:8788
```

### حل مشاكل Termux الشائعة

| المشكلة | الحل |
|---------|------|
| `python: command not found` | `pkg install python` |
| `pip: command not found` | `pkg install python-pip` |
| `ModuleNotFoundError` | `pip install pyyaml` |
| `Permission denied` | `chmod +x start.sh` |
| `Address already in use` | `YM_WEBUI_PORT=9000 python3 start_server.py` |
| `No space left` | `pkg clean && pip cache purge` |
| بناء حزم يفشل | `pkg install build-essential binutils` |
| مشاكل OpenSSL | `pkg install openssl && pip install --upgrade certifi` |

---

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `YM_WEBUI_HOST` | `0.0.0.0` | Bind address |
| `YM_WEBUI_PORT` | `8788` | Port number |
| `YM_WEBUI_PASSWORD` | *(unset)* | Set to enable password authentication |
| `YM_WEBUI_AGENT_DIR` | `./hermes-agent` | Path to agent engine |
| `YM_WEBUI_STATE_DIR` | `./.ym-state/webui` | State storage directory |
| `YM_WEBUI_DEFAULT_WORKSPACE` | `./workspace` | Default workspace path |
| `YM_WEBUI_DEFAULT_MODEL` | *(provider default)* | Default model to use |
| `YM_WEBUI_TLS_CERT` | *(unset)* | TLS certificate path (HTTPS) |
| `YM_WEBUI_TLS_KEY` | *(unset)* | TLS key path (HTTPS) |
| `YM_HOME` | `~/.yusuf-mussa` | Base configuration directory |

### Quick Configuration

```bash
# Set up API key
mkdir -p ~/.yusuf-mussa
cat > ~/.yusuf-mussa/.env << 'EOF'
OPENAI_API_KEY=sk-your-key-here
# Or any other provider:
# ANTHROPIC_API_KEY=sk-ant-your-key
# DEEPSEEK_API_KEY=your-key
# OPENROUTER_API_KEY=your-key
# GOOGLE_API_KEY=your-key
EOF

# Set default model
cat > ~/.yusuf-mussa/config.yaml << 'EOF'
provider: openai
model: gpt-4o-mini
EOF
```

### Supported AI Providers (20+)

| Provider | Models | API Key Env |
|----------|--------|-------------|
| OpenAI | GPT-4o, GPT-5.4, o3 | `OPENAI_API_KEY` |
| Anthropic | Claude Opus 4.7, Sonnet 4.6, Haiku 4.5 | `ANTHROPIC_API_KEY` |
| Google | Gemini 3.1 Pro, 2.5 Flash | `GOOGLE_API_KEY` |
| DeepSeek | V4 Pro, V4 Flash, R1 | `DEEPSEEK_API_KEY` |
| Qwen | Qwen3 Coder, Qwen3.6 Plus | `DASHSCOPE_API_KEY` |
| xAI | Grok 4.20 | `XAI_API_KEY` |
| Mistral | Mistral Large, Codestral | `MISTRAL_API_KEY` |
| OpenRouter | 200+ models from all providers | `OPENROUTER_API_KEY` |
| Z.AI / GLM | GLM-5.1, GLM-5, GLM-5 Turbo | `ZAI_API_KEY` |
| Ollama | Local models (Llama, Mistral, etc.) | *(no key needed)* |
| GitHub Copilot | Copilot models | `GITHUB_TOKEN` |
| NVIDIA NIM | Nemotron, Llama models | `NVIDIA_API_KEY` |
| MiniMax | M2.7, M2.5 | `MINIMAX_API_KEY` |
| MiniMax (China) | M2.7, M2.5, M2 | `MINIMAX_API_KEY` |

---

## Themes & Skins (10 skins)

| Skin | Style |
|------|-------|
| **Default** | Gold accents, warm tones |
| **Ares** | Red, aggressive, powerful |
| **Mono** | Monochrome, minimalist |
| **Slate** | Blue-gray, professional |
| **Poseidon** | Ocean blue, calming |
| **Sisyphus** | Purple, deep and rich |
| **Charizard** | Orange, fiery energy |
| **Sienna** | Warm clay, earthy tones |
| **Aurora** | Gradient glassmorphism, aurora borealis effect |
| **Neon** | Cyberpunk, neon glow on dark background |

Switch themes with the Appearance settings or use `/theme dark` and `/skin neon` commands.

---

## Architecture

```
Yusuf Mussa
├── server.py               — HTTP server (Python stdlib, no external deps)
├── start_server.py         — Environment setup + launcher
├── start.sh / run.sh       — Shell startup scripts
├── .env                    — Environment configuration
├── api/                    — Backend Python modules
│   ├── config.py           — Discovery, model catalog, provider resolution
│   ├── routes.py           — All API route handlers
│   ├── streaming.py        — SSE streaming engine, agent runner
│   ├── auth.py             — Password authentication
│   ├── workspace.py        — File operations API
│   ├── terminal.py         — Terminal support (xterm.js backend)
│   ├── models.py           — Model discovery and caching
│   ├── providers.py        — Provider management and credential pooling
│   ├── profiles.py         — Multi-profile support
│   ├── paymob.py           — Paymob payment integration
│   ├── background.py       — Background task execution
│   └── ...                 — 15+ more modules
├── static/                 — Frontend (vanilla JS, zero build step)
│   ├── index.html          — Full single-page application
│   ├── style.css           — CSS with 10 skins + full RTL support
│   ├── boot.js             — App initialization and event handlers
│   ├── ui.js               — DOM helpers, markdown rendering
│   ├── messages.js         — Chat messages + SSE streaming display
│   ├── i18n.js             — Internationalization (8 languages)
│   ├── sessions.js         — Session management and persistence
│   ├── panels.js           — Settings and configuration panels
│   ├── commands.js         — Slash command system
│   ├── terminal.js         — xterm.js terminal integration
│   ├── workspace.js        — File browser and preview
│   ├── onboarding.js       — First-run setup wizard
│   └── ...                 — More modules
├── hermes-agent/           — AI Agent engine
│   ├── run_agent.py        — Core agent loop
│   ├── model_tools.py      — 60+ tool definitions
│   ├── toolsets.py         — Toolset organization
│   ├── agent/              — Agent internals
│   │   ├── prompt_builder.py — System prompt assembly
│   │   ├── memory_manager.py — Persistent memory system
│   │   └── ...             — More internals
│   ├── gateway/            — Messaging gateway (Telegram, Discord, Slack)
│   ├── plugins/            — Plugin system (achievements, disk-cleanup)
│   ├── skills/             — 50+ skill definitions
│   └── environments/       — Execution environments
├── skills/                 — Bundled WebUI skills
│   ├── data-analyst/       — Data analysis skill
│   ├── code-assistant/     — Code assistance skill
│   ├── image-creator/      — Image generation skill
│   ├── web-research/       — Web research skill
│   └── arabic-assistant/   — Arabic language assistant
└── tests/                  — 130+ test files
```

---

## Skills System

Yusuf Mussa features a powerful skill system that allows the agent to learn and improve. Skills are automatically created and saved as the agent works, making it smarter over time.

### Built-in Skills

- **Full-Stack Development** — Complete web application building with modern frameworks
- **Software Development** — General programming, debugging, and code review
- **Research** — Web research, academic paper analysis, information synthesis
- **Email** — Email drafting, scheduling, and management
- **Social Media** — Content creation and scheduling across platforms
- **Smart Home** — IoT device automation and control
- **MLOps** — Machine learning model training, deployment, and monitoring
- **Red Teaming** — Security testing and vulnerability assessment
- **Data Analyst** — Data analysis, visualization, and reporting
- **Code Assistant** — Pair programming and code generation
- **Image Creator** — AI image generation and editing
- **Web Research** — Automated web research and summarization
- **Arabic Assistant** — Specialized Arabic language support

### Creating Custom Skills

Skills are defined in YAML and can be created through the Web UI or manually:

```yaml
name: my-custom-skill
description: A custom skill for specific tasks
instructions: |
  When this skill is active, follow these specific instructions...
tools:
  - file
  - terminal
  - web
```

---

## Accessing Remotely

### SSH Tunnel (Secure)

```bash
ssh -N -L 8788:127.0.0.1:8788 user@your.server.com
```

Then open `http://localhost:8788` on your local machine.

### Tailscale / ZeroTier

```bash
YM_WEBUI_HOST=0.0.0.0 YM_WEBUI_PASSWORD=your-secret ./start.sh
```

Open `http://<tailscale-ip>:8788` from any device on your tailnet.

### HTTPS with TLS

```bash
YM_WEBUI_TLS_CERT=/path/to/cert.pem YM_WEBUI_TLS_KEY=/path/to/key.pem ./start.sh
```

---

## Docker Compose

### Single Container (Simplest)

```bash
docker compose up -d
```

### Two Containers (Agent + WebUI separated)

```bash
docker compose -f docker-compose.two-container.yml up -d
```

### Three Containers (Agent + Dashboard + WebUI)

```bash
docker compose -f docker-compose.three-container.yml up -d
```

---

## Running Tests

```bash
# Run all tests
pytest tests/ -v --timeout=60

# Run specific test file
pytest tests/test_auth_sessions.py -v

# Run with coverage
pytest tests/ --cov=api --cov-report=html
```

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Cmd/Ctrl + K` | New conversation |
| `Enter` | Send message (configurable) |
| `Shift + Enter` | New line |
| `Escape` | Close panels / cancel edit |
| `Tab` | Accept autocomplete suggestion |

---

## License

MIT License — Free to use, modify, and distribute.

---

<div align="center">

**Yusuf Mussa** — وكيل الذكاء الاصطناعي المتقدم

*البرمجة • التصميم • حل الأخطاء • بناء SaaS • DevOps*

</div>
