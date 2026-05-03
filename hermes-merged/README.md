# Yusuf Mussa — Advanced AI Agent

<div align="center">

![Yusuf Mussa](https://img.shields.io/badge/Yusuf%20Mussa-v2.0-gold?style=for-the-badge&labelColor=1a1a2e&color=F5C542)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Termux-orange?style=flat-square)

**وكيل ذكاء اصطناعي متقدم لبناء التطبيقات والتصاميم وحل الأخطاء وإنشاء مشاريع SaaS**

[English](#features) | [العربية](#المميزات) | [تثبيت Termux](#التثبيت-على-termux)

</div>

---

## ما هو Yusuf Mussa؟

Yusuf Mussa هو وكيل ذكاء اصطناعي متقدم ومتكامل يعمل محلياً على جهازك، قادر على:

- **البرمجة والتطوير** — كتابة كود بأي لغة (Python, JavaScript, TypeScript, Rust, Go, إلخ)، بناء تطبيقات كاملة من الصفر
- **بناء تطبيقات SaaS** — إنشاء مشاريع SaaS كاملة مع المصادقة، الدفع، المتعدد المستخدمين
- **التصميم** — إنشاء تصاميم UI/UX حديثة، واجهات متجاوبة، وتوليد صور
- **حل الأخطاء** — تحليل وإصلاح الباجات، مراجعة الكود، تحسين الأداء
- **إدارة البنية التحتية** — DevOps، Docker، CI/CD، النشر والتشغيل
- **قاعدة بيانات** — تصميم وإدارة قواعد البيانات، SQL و NoSQL
- **أتمتة المتصفح** — تصفح الويب، استخراج البيانات، أتمتة المهام
- **البحث** — بحث ويب، تحليل أوراق علمية، استخراج المعلومات
- **الذاكرة المستمرة** — يتذكر ما يتعلمه عبر الجلسات، يتحسن مع الوقت

## المميزات

### قدرات الوكيل المتقدم

| القدرة | الوصف |
|--------|-------|
| برمجة كاملة | Python, JS, TS, Rust, Go, Java, C++, Ruby, PHP وأكثر |
| بناء تطبيقات ويب | Next.js, React, Vue, Django, Flask, FastAPI |
| بناء SaaS | مصادقة، دفع Stripe/PayPal، multi-tenancy، APIs |
| تطبيقات موبايل | React Native, Flutter, PWA |
| قواعد بيانات | PostgreSQL, MySQL, MongoDB, SQLite, Redis |
| DevOps | Docker, K8s, GitHub Actions, CI/CD |
| تصميم UI/UX | CSS حديث، Tailwind، أنظمة تصميم، responsive |
| حل الأخطاء | تحليل، تصحيح، مراجعة كود، تحسين أداء |
| أتمتة | Shell scripts، cron jobs، web scraping |
| أمان | فحص ثغرات، تصحيح أمني، أفضل الممارسات |

### واجهة الويب

- **بث مباشر** — تظهر الاستجابة حرفاً بحرف فور توليدها
- **20+ مزود ذكاء اصطناعي** — OpenAI, Anthropic, Google, DeepSeek, Qwen, Z.AI وأكثر
- **10 ثيمات** — Default, Ares, Mono, Slate, Poseidon, Sisyphus, Charizard, Sienna, **Aurora**, **Neon**
- **8 لغات** — English, العربية, Русский, Español, Deutsch, 中文, Português, 한국어
- **دعم RTL كامل** — واجهة عربية من اليمين لليسار
- **متصفح ملفات** — تصفح، تعديل، إنشاء ملفات مباشرة
- **طرفية مدمجة** — تنفيذ أوامر shell مباشرة من المتصفح
- **إدخال صوتي** — تحدث بدلاً من الكتابة
- **مهام مجدولة** — cron jobs تعمل حتى وأنت غير متصل
- **مهارات ذاتية التحسين** — يكتب ويحفظ مهاراته تلقائياً
- **PWA** — يعمل كتطبيق على الهاتف

### الأدوات المتاحة (60+ أداة)

```
browser         — أتمتة المتصفح (13 أداة فرعية)
code_execution  — تنفيذ Python/JS/أي لغة
file            — قراءة، كتابة، تعديل، بحث في الملفات
terminal        — تنفيذ أوامر shell
web             — بحث ويب واستخراج محتوى
image_gen       — توليد صور بالذكاء الاصطناعي
delegation      — تفويض مهام لوكيل فرعي
memory          — ذاكرة مستمرة عبر الجلسات
todo            — إدارة قائمة المهام
cronjob         — جدولة مهام دورية
skills          — نظام مهارات قابل للتوسيع
```

---

## التثبيت السريع

### Linux / macOS

```bash
git clone https://github.com/gjbvsjjvgm-sketch/hermes-merged.git
cd hermes-merged
python3 bootstrap.py
```

أو:

```bash
./start.sh
```

### Docker

```bash
docker pull ghcr.io/nesquena/hermes-webui:latest
docker run -d \
  -e WANTED_UID=$(id -u) -e WANTED_GID=$(id -g) \
  -v ~/.hermes:/home/hermeswebui/.hermes \
  -v ~/workspace:/workspace \
  -p 8788:8788 ghcr.io/nesquena/hermes-webui:latest
```

افتح http://localhost:8788 في المتصفح.

---

## التثبيت على Termux

> **Termux** هو محاكي طرفية أندرويد يتيح تشغيل بيئة Linux كاملة على هاتفك. يمكنك تشغيل Yusuf Mussa بالكامل على هاتفك الأندرويد!

### المتطلبات

- هاتف أندرويد 7.0+
- 2GB RAM كحد أدنى (4GB+ مستحسن)
- 1GB مساحة تخزين حرة
- اتصال إنترنت

### الخطوة 1: تثبيت Termux

قم بتحميل Termux من **F-Droid** (النسخة الموصى بها):

```bash
# لا تستخدم نسخة Google Play — قديمة ولا تعمل
# حمّل من F-Droid:
# https://f-droid.org/packages/com.termux/
```

أو من سطر الأوامر:

```bash
# افتح المتصفح على هاتفك وادخل:
# https://f-droid.org/packages/com.termux/
```

### الخطوة 2: تحديث Termux وتثبيت الحزم الأساسية

```bash
# تحديث الحزم
pkg update && pkg upgrade -y

# تثبيت الأدوات الأساسية
pkg install -y git python python-pip nodejs-lts build-essential binutils openssl

# تثبيت أدوات إضافية مفيدة
pkg install -y curl wget nano vim
```

### الخطوة 3: إعداد بيئة Python

```bash
# تحديث pip
pip install --upgrade pip

# تثبيت الحزم الأساسية
pip install pyyaml
```

### الخطوة 4: تحميل Yusuf Mussa

```bash
# استنساخ المشروع
cd ~
git clone https://github.com/gjbvsjjvgm-sketch/hermes-merged.git
cd hermes-merged
```

### الخطوة 5: تشغيل Yusuf Mussa

```bash
# الطريقة الأولى: استخدام سكريبت البدء
chmod +x start.sh
./start.sh

# الطريقة الثانية: تشغيل مباشر بـ Python
python3 start_server.py
```

### الخطوة 6: الوصول من المتصفح

بعد التشغيل، سترى رسالة مثل:

```
Yusuf Mussa Web UI listening on http://0.0.0.0:8788
```

افتح متصفح هاتفك وادخل:

```
http://localhost:8788
```

### إعداد مفتاح API

عند أول تشغيل، سيظهر معالج الإعداد. ستحتاج إلى:

1. **اختيار مزود AI** — مثلاً OpenAI, Anthropic, أو OpenRouter
2. **إدخال مفتاح API** — احصل عليه من موقع المزود
3. **اختيار نموذج** — مثل `gpt-4o-mini` أو `claude-sonnet-4-20250514`
4. **اختيار مساحة عمل** — المجلد الذي سيعمل فيه الوكيل

أو يدوياً:

```bash
# إنشاء ملف الإعدادات
mkdir -p ~/.hermes
cat > ~/.hermes/.env << 'EOF'
OPENAI_API_KEY=sk-your-key-here
# أو أي مزود آخر:
# ANTHROPIC_API_KEY=sk-ant-your-key
# DEEPSEEK_API_KEY=your-key
# OPENROUTER_API_KEY=your-key
EOF

# إنشاء ملف config.yaml
cat > ~/.hermes/config.yaml << 'EOF'
provider: openai
model: gpt-4o-mini
EOF
```

### تثبيت سريع بأمر واحد (Termux)

```bash
pkg update -y && pkg upgrade -y && \
pkg install -y git python python-pip build-essential && \
pip install pyyaml && \
cd ~ && \
git clone https://github.com/gjbvsjjvgm-sketch/hermes-merged.git && \
cd hermes-merged && \
python3 start_server.py
```

### نصائح Termux

```bash
# تشغيل في الخلفية (حتى لا يتوقف عند إغلاق التermux)
nohup python3 start_server.py &

# أو استخدام tmux
pkg install tmux
tmux new -s yusuf
python3 start_server.py
# اضغط Ctrl+B ثم D للفصل
# tmux attach -t yusuf  للعودة

# تشغيل تلقائي عند فتح Termux
echo 'cd ~/hermes-merged && python3 start_server.py' >> ~/.bashrc

# تغيير المنفذ
HERMES_WEBUI_PORT=9000 python3 start_server.py

# تفعيل كلمة المرور
HERMES_WEBUI_PASSWORD=your-secret python3 start_server.py
```

### الوصول من كمبيوتر آخر على نفس الشبكة

```bash
# اعرف عنوان IP لهاتفك
ifconfig | grep inet

# على الكمبيوتر، افتح:
# http://PHONE-IP:8788
```

### حل مشاكل Termux الشائعة

| المشكلة | الحل |
|---------|------|
| `python: command not found` | `pkg install python` |
| `pip: command not found` | `pkg install python-pip` |
| `git: command not found` | `pkg install git` |
| `ModuleNotFoundError` | `pip install pyyaml` |
| `Permission denied` | `chmod +x start.sh` |
| `Address already in use` | غيّر المنفذ: `HERMES_WEBUI_PORT=9000` |
| `No space left` | `pkg clean && pip cache purge` |
| بناء حزم يفشل | `pkg install build-essential binutils` |
| مشاكل OpenSSL | `pkg install openssl && pip install --upgrade certifi` |

---

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `HERMES_WEBUI_HOST` | `0.0.0.0` | Bind address |
| `HERMES_WEBUI_PORT` | `8788` | Port number |
| `HERMES_WEBUI_PASSWORD` | *(unset)* | Set to enable password auth |
| `HERMES_WEBUI_AGENT_DIR` | `./hermes-agent` | Path to agent |
| `HERMES_WEBUI_STATE_DIR` | `./.hermes-state/webui` | State directory |
| `HERMES_WEBUI_DEFAULT_WORKSPACE` | `./workspace` | Default workspace |
| `HERMES_WEBUI_DEFAULT_MODEL` | `openai/gpt-5.4-mini` | Default model |
| `HERMES_HOME` | `~/.hermes` | Base config directory |

### Supported AI Providers (20+)

| Provider | Models | API Key Env |
|----------|--------|-------------|
| OpenAI | GPT-4o, GPT-5, o3 | `OPENAI_API_KEY` |
| Anthropic | Claude Sonnet, Opus, Haiku | `ANTHROPIC_API_KEY` |
| Google | Gemini 2.5 Pro/Flash | `GOOGLE_API_KEY` |
| DeepSeek | V3, R1 | `DEEPSEEK_API_KEY` |
| Qwen | Qwen3, Qwen2.5 | `DASHSCOPE_API_KEY` |
| xAI | Grok 3 | `XAI_API_KEY` |
| Mistral | Mistral Large, Codestral | `MISTRAL_API_KEY` |
| OpenRouter | 200+ models | `OPENROUTER_API_KEY` |
| Z.AI | GLM-4 | `ZAI_API_KEY` |
| Ollama | Local models | *(no key needed)* |
| GitHub Copilot | Copilot models | `GITHUB_TOKEN` |
| NVIDIA | NIM models | `NVIDIA_API_KEY` |

---

## Themes & Skins (10 skins)

| Skin | Style |
|------|-------|
| **Default** | Gold accents, warm tones |
| **Ares** | Red, aggressive, powerful |
| **Mono** | Monochrome, minimalist |
| **Slate** | Blue-gray, professional |
| **Poseidon** | Ocean blue, calming |
| **Sisyphus** | Purple, deep |
| **Charizard** | Orange, fiery |
| **Sienna** | Warm clay, earthy |
| **Aurora** ✨ | Gradient glassmorphism, aurora borealis |
| **Neon** ✨ | Cyberpunk, neon glow, dark |

Switch with `/theme` command or Settings → Appearance.

---

## Skills System

Yusuf Mussa automatically creates and saves skills as it works. Built-in skills include:

- **Full-Stack Development** — Complete web application building
- **Software Development** — General programming and debugging
- **Research** — Web research, paper analysis
- **Email** — Email drafting and management
- **Social Media** — Content creation
- **Smart Home** — IoT automation
- **MLOps** — Machine learning operations
- **Red Teaming** — Security testing

---

## Architecture

```
Yusuf Mussa Merged Application
├── server.py               — HTTP server (Python stdlib)
├── start_server.py         — Environment setup + launcher
├── start.sh                — Shell startup script
├── api/                    — Backend Python modules
│   ├── config.py           — Discovery, model catalog
│   ├── routes.py           — All API routes
│   ├── streaming.py        — SSE engine, agent runner
│   ├── auth.py             — Password authentication
│   ├── workspace.py        — File operations
│   ├── terminal.py         — Terminal support
│   └── ...                 — 20+ more modules
├── static/                 — Frontend (vanilla JS, no build step)
│   ├── index.html          — Full HTML app
│   ├── style.css           — CSS with 10 skins + RTL
│   ├── ui.js               — DOM helpers, markdown
│   ├── messages.js         — Chat + SSE streaming
│   ├── i18n.js             — 8 languages
│   ├── terminal.js         — xterm.js terminal
│   └── ...                 — 10+ more modules
├── hermes-agent/           — AI Agent engine
│   ├── run_agent.py        — Core agent loop
│   ├── model_tools.py      — 60+ tool definitions
│   ├── toolsets.py         — Toolset organization
│   ├── agent/              — Agent internals
│   │   ├── prompt_builder.py — System prompt assembly
│   │   ├── memory_manager.py — Persistent memory
│   │   └── ...             — More internals
│   ├── plugins/            — Plugin system
│   ├── skills/             — Skill definitions
│   └── environments/       — Execution environments
└── tests/                  — 130+ test files
```

---

## Accessing Remotely

### SSH Tunnel

```bash
ssh -N -L 8788:127.0.0.1:8788 user@your.server.com
```

Then open `http://localhost:8788` on your local machine.

### Tailscale (Phone Access)

```bash
HERMES_WEBUI_HOST=0.0.0.0 HERMES_WEBUI_PASSWORD=your-secret ./start.sh
```

Open `http://<tailscale-ip>:8788` from your phone.

---

## Docker Compose

### Single Container

```bash
docker compose up -d
```

### Two Containers (Agent + WebUI)

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
pytest tests/ -v --timeout=60
```

---

## License

MIT License — Free to use, modify, and distribute.

---

<div align="center">

**Yusuf Mussa** — وكيل الذكاء الاصطناعي المتقدم

*البرمجة • التصميم • حل الأخطاء • بناء SaaS • DevOps*

</div>
