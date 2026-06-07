---
title: Luis Santiago — Career AI
emoji: 🧑‍💻
colorFrom: blue
colorTo: slate
sdk: gradio
sdk_version: 5.37.0
app_file: app.py
pinned: false
---

# Personal Career Agent AI

[![Live Demo](https://img.shields.io/badge/Live-Demo-blue)](https://lasc1026-career-ai.hf.space)

A custom AI chatbot that represents **me** in a professional context. It is designed to answer recruiter questions based on my real experience, resume, and past interviews using a structured set of markdown files and a streamlined chat interface.

## 🔗 Live App

👉 [Try it here](https://lasc1026-career-ai.hf.space/) (Might take a while for Hugging Space to load the instance if inactive. Email me at lasc1026@gmail.com if you need me to start the gradio space manually.)

## 💡 Features

- Simulates me during recruiter interactions
- Pulls from resume, LinkedIn, interview, and prompt files
- Guardrails against prompt injection and jailbreak attempts
- Input rate limiting and validation
- Polished portfolio-ready UI

## 🛠️ Tech Stack

- **Python**
- **Gradio** – for building the web interface
- **OpenAI Python SDK** (`openai`) – to interact with LLMs
- **dotenv** – for environment variable management
- **Markdown** – stores resume, prompt, and context data

## 📁 Context Files Used

Located in the `./career-data/` folder:

- `master_prompt.md`
- `refined_resume.md`
- `linkedin.md`
- `simulated_interview.md`
- `refined_simulated_interview.md`

These files are loaded and injected into the system prompt.
