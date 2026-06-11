---
title: Luis Santiago — Career AI
emoji: 🧑‍💻
colorFrom: blue
colorTo: gray
sdk: gradio
sdk_version: 5.37.0
app_file: app.py
pinned: false
---

# Career AI — Personal Career Agent Chatbot

[![Live Demo](https://img.shields.io/badge/Live-Demo-blue)](https://lasc1026-career-ai.hf.space)

A portfolio-ready AI chatbot that represents **Luis Santiago** in a professional context. Designed to answer recruiter and hiring manager questions based on real experience, a detailed resume, and structured career data — with enterprise-grade guardrails, rate limiting, and a polished UI.

## 🔗 Live App

👉 [Try it here](https://lasc1026-career-ai.hf.space/) (May take a moment to wake up if the HF Space is cold. Email lasc1026@gmail.com if needed.)

## 💡 Features

- **Accurate persona simulation** — responds as Luis Santiago using structured career data
- **Multi-layer guardrails** — jailbreak detection (15 patterns), input length cap (2000 chars), hardened system preamble preventing persona override
- **Rate limiting** — TokenBucket algorithm (30 msg/min per session) prevents abuse
- **Polished portfolio UI** — custom Gradio Soft theme (Inter font, blue/slate palette), branded header/footer, custom CSS for iframe embedding
- **Three CI/CD pipelines** — auto-sync to Hugging Face Spaces, keep-alive pings (every 40 min), GitHub Pages deployment

## 🛠️ Tech Stack

- **Python 3** — core application logic
- **Gradio** — web interface (Blocks API, custom theme, HTML components)
- **OpenAI Python SDK** — LLM interaction via Gemini API
- **Python-dotenv** — environment variable management
- **Markdown** — structured career data files
- **GitHub Actions** — CI/CD, keep-alive, Pages deployment

## 📁 Career Data Files

Located in `./career-data/`:

| File | Purpose |
|------|---------|
| `resume.md` | Canonical resume with full role descriptions, projects, and certifications |
| `master_prompt.md` | System prompt defining persona, tone, constraints, and context |

## 🧱 Architecture

```
app.py           → Gradio Blocks UI + chat orchestration + error handling
guardrails.py    → Jailbreak detection, input validation, TokenBucket rate limiter
career-data/     → Structured markdown files loaded into the system prompt
.github/workflows → sync-to-hub.yml, keep-alive.yml, deploy-gh-pages.yml
docs/            → index.html for GitHub Pages iframe embedding
```

The system loads all markdown files at startup, concatenates them with a hardened preamble, and injects them as the system prompt for every conversation turn.
