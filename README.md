<div align="center">

# Yusuf Mussa

**وكيل ذكاء اصطناعي متقدم — Advanced AI Agent**

![Yusuf Mussa](https://img.shields.io/badge/Yusuf%20Mussa-v2.0-gold?style=for-the-badge&labelColor=1a1a2e&color=F5C542)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Node.js](https://img.shields.io/badge/Node.js-18+-green?style=flat-square&logo=node.js)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Termux-orange?style=flat-square)

[English](#features) | [العربية](#المميزات) | [Termux Install](#termux-installation)

</div>

---

## ما هو Yusuf Mussa؟

Yusuf Mussa هو وكيل ذكاء اصطناعي متقدم ومتكامل يعمل محلياً على جهازك، يجمع بين واجهة ويب حديثة ومحرك وكيل ذكي قوي. يقدر على:

- **البرمجة والتطوير** — كتابة كود بأي لغة (Python, JavaScript, TypeScript, Rust, Go, Java, C++ وأكثر)
- **بناء تطبيقات SaaS** — إنشاء مشاريع SaaS كاملة مع المصادقة، الدفع، المتعدد المستخدمين
- **التصميم** — إنشاء تصاميم UI/UX حديثة، واجهات متجاوبة، وتوليد صور
- **حل الأخطاء** — تحليل وإصلاح الباجات، مراجعة الكود، تحسين الأداء
- **بناء تطبيقات كاملة** — من الصفر حتى النشر (frontend + backend + database)
- **إدارة البنية التحتية** — DevOps، Docker، CI/CD، النشر والتشغيل
- **قاعدة بيانات** — تصميم وإدارة قواعد البيانات، SQL و NoSQL
- **أتمتة المتصفح** — تصفح الويب، استخراج البيانات، أتمتة المهام
- **البحث** — بحث ويب، تحليل أوراق علمية، استخراج المعلومات
- **الذاكرة المستمرة** — يتذكر ما يتعلمه عبر الجلسات، يتحسن مع الوقت

---

## المميزات | Features

### قدرات الوكيل المتقدم | Advanced Agent Capabilities

| القدرة | الوصف | Capability | Description |
|--------|-------|-----------|-------------|
| برمجة كاملة | Python, JS, TS, Rust, Go, Java, C++, Ruby, PHP | Full Programming | Any language, any framework |
| بناء تطبيقات ويب | Next.js, React, Vue, Django, Flask, FastAPI | Web Apps | Modern frameworks & APIs |
| بناء SaaS | مصادقة، دفع Stripe/PayPal، multi-tenancy | SaaS Building | Auth, payments, multi-tenant |
| تطبيقات موبايل | React Native, Flutter, PWA | Mobile Apps | Cross-platform |
| قواعد بيانات | PostgreSQL, MySQL, MongoDB, SQLite, Redis | Databases | SQL & NoSQL |
| DevOps | Docker, K8s, GitHub Actions, CI/CD | DevOps | Deploy & automate |
| تصميم UI/UX | CSS حديث، Tailwind، أنظمة تصميم | UI/UX Design | Modern, responsive |
| حل الأخطاء | تحليل، تصحيح، مراجعة كود، تحسين أداء | Bug Fixing | Debug & optimize |
| أتمتة | Shell scripts، cron jobs، web scraping | Automation | Scripts & tasks |
| أمان | فحص ثغرات، تصحيح أمني، أفضل الممارسات | Security | Audit & harden |

### واجهة الويب | Web UI

- **بث مباشر** — تظهر الاستجابة حرفاً بحرف فور توليدها (SSE streaming)
- **20+ مزود ذكاء اصطناعي** — OpenAI, Anthropic, Google, DeepSeek, Qwen, Z.AI وأكثر
- **10 ثيمات** — Default, Ares, Mono, Slate, Poseidon, Sisyphus, Charizard, Sienna, Aurora, Neon
- **8 لغات** — English, العربية, Русский, Español, Deutsch, 中文, Português, 한국어
- **دعم RTL كامل** — واجهة عربية من اليمين لليسار
- **متصفح ملفات** — تصفح، تعديل، إنشاء ملفات مباشرة
- **طرفية مدمجة** — تنفيذ أوامر shell مباشرة من المتصفح
- **إدخال صوتي** — تحدث بدلاً من الكتابة
- **مهام مجدولة** — cron jobs تعمل حتى وأنت غير متصل
- **مهارات ذاتية التحسين** — يكتب ويحفظ مهاراته تلقائياً
- **PWA** — يعمل كتطبيق على الهاتف

### الأدوات المتاحة (60+ أداة) | Available Tools

```
browser         — أتمتة المتصفح (13 أداة فرعية) | Browser automation (13 sub-tools)
code_execution  — تنفيذ Python/JS/أي لغة | Execute Python/JS/any language
file            — قراءة، كتابة، تعديل، بحث في الملفات | File read/write/edit/search
terminal        — تنفيذ أوامر shell | Execute shell commands
web             — بحث ويب واستخراج محتوى | Web search & content extraction
image_gen       — توليد صور بالذكاء الاصطناعي | AI image generation
delegation      — تفويض مهام لوكيل فرعي | Delegate tasks to sub-agents
memory          — ذاكرة مستمرة عبر الجلسات | Persistent memory across sessions
todo            — إدارة قائمة المهام | Task list management
cronjob         — جدولة مهام دورية | Schedule recurring tasks
skills          — نظام مهارات قابل للتوسيع | Extensible skills system
```

---

## هيكل المشروع | Project Structure

```
Yusuf Mussa
├── hermes-merged/          — الوكيل + واجهة الويب المدمجة | Agent + WebUI merged
│   ├── server.py           — خادم HTTP (Python) | HTTP server
│   ├── start_server.py     — إعداد البيئة + المشغل | Env setup + launcher
│   ├── start.sh            — سكريبت بدء التشغيل | Startup shell script
│   ├── install-termux.sh   — تثبيت على Termux | Termux installer
│   ├── README.md           — توثيق مفصل | Detailed docs
│   ├── api/                — وحدات Python الخلفية | Backend modules
│   │   ├── config.py       — اكتشاف، كتالوج النماذج | Discovery, model catalog
│   │   ├── routes.py       — مسارات API | API routes
│   │   ├── streaming.py    — محرك SSE | SSE engine
│   │   ├── auth.py         — مصادقة بكلمة مرور | Password auth
│   │   ├── workspace.py    — عمليات الملفات | File operations
│   │   └── ...             — 20+ وحدة أخرى | 20+ more modules
│   ├── static/             — الواجهة الأمامية (vanilla JS) | Frontend
│   │   ├── index.html      — تطبيق HTML كامل | Full HTML app
│   │   ├── style.css       — CSS مع 10 ثيمات + RTL | CSS with 10 skins + RTL
│   │   ├── ui.js           — مساعدات DOM، Markdown | DOM helpers, markdown
│   │   ├── messages.js     — دردشة + بث SSE | Chat + SSE streaming
│   │   ├── i18n.js         — 8 لغات | 8 languages
│   │   └── ...             — 10+ وحدات أخرى | 10+ more modules
│   └── hermes-agent/       — محرك وكيل الذكاء الاصطناعي | AI Agent engine
│       ├── run_agent.py    — حلقة الوكيل الأساسية | Core agent loop
│       ├── model_tools.py  — 60+ تعريف أداة | 60+ tool definitions
│       ├── agent/          — دواخل الوكيل | Agent internals
│       └── skills/         — تعريفات المهارات | Skill definitions
├── hermes-agent/           — كود الوكيل الأصلي | Original agent code
├── hermes-webui/           — كود واجهة الويب الأصلية | Original WebUI code
├── src/                    — تطبيق Next.js (لوحة تحكم) | Next.js dashboard app
├── skills/                 — مهارات إضافية | Additional skills
└── mini-services/          — خدمات مصغرة | Mini services
```

---

## التثبيت السريع | Quick Install

### Linux / macOS

```bash
git clone https://github.com/gjbvsjjvgm-sketch/hermes-merged.git
cd hermes-merged/hermes-merged
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
  -p 8787:8787 ghcr.io/nesquena/hermes-webui:latest
```

افتح http://localhost:8787 في المتصفح.

---

## التثبيت على Termux | Termux Installation

> **Termux** هو محاكي طرفية أندرويد يتيح تشغيل بيئة Linux كاملة على هاتفك. يمكنك تشغيل Yusuf Mussa بالكامل على هاتفك الأندرويد!

### المتطلبات | Requirements

- هاتف أندرويد 7.0+ | Android 7.0+ phone
- 2GB RAM كحد أدنى (4GB+ مستحسن) | 2GB min (4GB+ recommended)
- 1GB مساحة تخزين حرة | 1GB free storage
- اتصال إنترنت | Internet connection

### الخطوة 1: تثبيت Termux | Step 1: Install Termux

قم بتحميل Termux من **F-Droid** (النسخة الموصى بها):

```
https://f-droid.org/packages/com.termux/
```

> **تحذير**: لا تستخدم نسخة Google Play — قديمة ولا تعمل!

### الخطوة 2: تحديث وتثبيت الحزم | Step 2: Update & Install Packages

```bash
pkg update && pkg upgrade -y
pkg install -y git python python-pip nodejs-lts build-essential binutils openssl
pkg install -y curl wget nano vim
```

### الخطوة 3: إعداد Python | Step 3: Setup Python

```bash
pip install --upgrade pip
pip install pyyaml
```

### الخطوة 4: تحميل المشروع | Step 4: Clone Project

```bash
cd ~
git clone https://github.com/gjbvsjjvgm-sketch/hermes-merged.git
cd hermes-merged/hermes-merged
```

### الخطوة 5: التشغيل | Step 5: Run

```bash
chmod +x start.sh
./start.sh

# أو مباشرة:
python3 start_server.py
```

### الخطوة 6: الوصول من المتصفح | Step 6: Open Browser

افتح متصفح هاتفك وادخل:

```
http://localhost:8787
```

### إعداد مفتاح API | Setup API Key

عند أول تشغيل، سيظهر معالج الإعداد. ستحتاج إلى:

1. **اختيار مزود AI** — مثلاً OpenAI, Anthropic, أو OpenRouter
2. **إدخال مفتاح API** — احصل عليه من موقع المزود
3. **اختيار نموذج** — مثل `gpt-4o-mini` أو `claude-sonnet-4-20250514`
4. **اختيار مساحة عمل** — المجلد الذي سيعمل فيه الوكيل

أو يدوياً:

```bash
mkdir -p ~/.hermes
cat > ~/.hermes/.env << 'EOF'
OPENAI_API_KEY=sk-your-key-here
# أو أي مزود آخر:
# ANTHROPIC_API_KEY=sk-ant-your-key
# DEEPSEEK_API_KEY=your-key
# OPENROUTER_API_KEY=your-key
EOF
```

### تثبيت سريع بأمر واحد | One-line Install

```bash
pkg update -y && pkg upgrade -y && \
pkg install -y git python python-pip build-essential && \
pip install pyyaml && \
cd ~ && \
git clone https://github.com/gjbvsjjvgm-sketch/hermes-merged.git && \
cd hermes-merged/hermes-merged && \
python3 start_server.py
```

### نصائح Termux | Termux Tips

```bash
# تشغيل في الخلفية
nohup python3 start_server.py &

# أو استخدام tmux
pkg install tmux
tmux new -s yusuf
python3 start_server.py
# Ctrl+B ثم D للفصل | Ctrl+B then D to detach
# tmux attach -t yusuf  للعودة | to reattach

# تشغيل تلقائي عند فتح Termux
echo 'cd ~/hermes-merged/hermes-merged && python3 start_server.py' >> ~/.bashrc

# تغيير المنفذ | Change port
HERMES_WEBUI_PORT=9000 python3 start_server.py

# تفعيل كلمة المرور | Enable password
HERMES_WEBUI_PASSWORD=your-secret python3 start_server.py
```

### الوصول من كمبيوتر آخر | Access from Another Device

```bash
# اعرف عنوان IP لهاتفك | Find phone IP
ifconfig | grep inet

# على الكمبيوتر، افتح | On computer, open:
# http://PHONE-IP:8787
```

### حل مشاكل Termux الشائعة | Troubleshooting

| المشكلة | الحل | Problem | Solution |
|---------|------|---------|----------|
| `python: command not found` | `pkg install python` | python not found | `pkg install python` |
| `pip: command not found` | `pkg install python-pip` | pip not found | `pkg install python-pip` |
| `git: command not found` | `pkg install git` | git not found | `pkg install git` |
| `ModuleNotFoundError` | `pip install pyyaml` | Module error | `pip install pyyaml` |
| `Permission denied` | `chmod +x start.sh` | Permission error | `chmod +x start.sh` |
| `Address already in use` | `HERMES_WEBUI_PORT=9000 python3 start_server.py` | Port in use | Change port |
| `No space left` | `pkg clean && pip cache purge` | No space | Clean caches |
| بناء يفشل | `pkg install build-essential binutils` | Build fails | Install build tools |
| مشاكل OpenSSL | `pkg install openssl && pip install --upgrade certifi` | SSL errors | Install openssl |

---

## الإعدادات | Configuration

### متغيرات البيئة | Environment Variables

| المتغير | الافتراضي | الوصف |
|---------|-----------|-------|
| `HERMES_WEBUI_HOST` | `0.0.0.0` | عنوان الربط | Bind address |
| `HERMES_WEBUI_PORT` | `8787` | رقم المنفذ | Port number |
| `HERMES_WEBUI_PASSWORD` | *(غير محدد)* | كلمة المرور | Password auth |
| `HERMES_WEBUI_AGENT_DIR` | `./hermes-agent` | مسار الوكيل | Agent path |
| `HERMES_WEBUI_DEFAULT_WORKSPACE` | `./workspace` | مساحة العمل | Workspace |
| `HERMES_WEBUI_DEFAULT_MODEL` | `openai/gpt-5.4-mini` | النموذج الافتراضي | Default model |
| `HERMES_HOME` | `~/.hermes` | مجلد الإعدادات | Config dir |

### مزودو AI المدعومون (20+) | Supported AI Providers

| المزود | النماذج | مفتاح API |
|--------|---------|-----------|
| OpenAI | GPT-4o, GPT-5, o3 | `OPENAI_API_KEY` |
| Anthropic | Claude Sonnet, Opus, Haiku | `ANTHROPIC_API_KEY` |
| Google | Gemini 2.5 Pro/Flash | `GOOGLE_API_KEY` |
| DeepSeek | V3, R1 | `DEEPSEEK_API_KEY` |
| Qwen | Qwen3, Qwen2.5 | `DASHSCOPE_API_KEY` |
| xAI | Grok 3 | `XAI_API_KEY` |
| Mistral | Mistral Large, Codestral | `MISTRAL_API_KEY` |
| OpenRouter | 200+ models | `OPENROUTER_API_KEY` |
| Z.AI | GLM-4 | `ZAI_API_KEY` |
| Ollama | Local models | *(لا يحتاج مفتاح)* |
| GitHub Copilot | Copilot models | `GITHUB_TOKEN` |

---

## الثيمات (10 ثيمات) | Themes

| الثيم | النمط | Theme | Style |
|-------|-------|-------|-------|
| Default | ذهبي، دافئ | Default | Gold, warm |
| Ares | أحمر، قوي | Ares | Red, aggressive |
| Mono | أحادي اللون | Mono | Monochrome |
| Slate | أزرق رمادي | Slate | Blue-gray |
| Poseidon | أزرق محيطي | Poseidon | Ocean blue |
| Sisyphus | بنفسجي عميق | Sisyphus | Deep purple |
| Charizard | برتقالي ناري | Charizard | Fiery orange |
| Sienna | طيني دافئ | Sienna | Warm clay |
| **Aurora** | تدرج زجاجي، شفق قطبي | **Aurora** | Glassmorphism gradient |
| **Neon** | سايبربانك، توهج نيون | **Neon** | Cyberpunk neon glow |

غيّر الثيم بأمر `/theme` أو الإعدادات → المظهر.

---

## الوصول عن بعد | Remote Access

### SSH Tunnel

```bash
ssh -N -L 8787:127.0.0.1:8787 user@your.server.com
```

ثم افتح `http://localhost:8787` على جهازك.

### Tailscale

```bash
HERMES_WEBUI_HOST=0.0.0.0 HERMES_WEBUI_PASSWORD=your-secret ./start.sh
```

افتح `http://<tailscale-ip>:8787` من هاتفك.

---

## Docker Compose

```bash
# حاوية واحدة | Single container
docker compose up -d

# حاويتين (Agent + WebUI)
docker compose -f docker-compose.two-container.yml up -d

# ثلاث حاويات (Agent + Dashboard + WebUI)
docker compose -f docker-compose.three-container.yml up -d
```

---

## الاختبارات | Running Tests

```bash
cd hermes-merged
pytest tests/ -v --timeout=60
```

---

## الترخيص | License

MIT License — حر في الاستخدام والتعديل والتوزيع.

---

<div align="center">

**Yusuf Mussa** — وكيل الذكاء الاصطناعي المتقدم

البرمجة • التصميم • حل الأخطاء • بناء SaaS • DevOps

*Built with ❤️ for developers everywhere*

</div>
