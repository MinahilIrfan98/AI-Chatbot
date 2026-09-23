# 🤖 Pixel AI

A Python-based AI chatbot with multiple interfaces — a Streamlit UI (local or cloud-powered) and a simple script for quick testing.

🔗 **Live demo:** [pixel-aii.streamlit.app](https://pixel-aii.streamlit.app/)

## Architecture

* `main.py` — One-shot prompt script. Sends a single message to the local Ollama model and prints the reply. Good for quick backend testing.
* `app.py` — Local chat UI (Streamlit). Runs fully offline using [Ollama](https://ollama.com/), requesting completions from the local Ollama runtime.
* `app_cloud.py` — Cloud chat UI (Streamlit). Reads the API key from environment variables and requests completions from the [Groq API](https://groq.com/) — used for deployment so anyone can try it online.
* `src/openchat/__init__.py` — Package entry point with a greeting.

User → Cloud chat UI (app_cloud.py) → reads API key from Environment variables → requests completion → Groq API → shows reply → User

User → Local chat UI (app.py) → requests completion → Ollama runtime → shows reply → User

User → One-shot prompt (main.py) → requests completion → Ollama runtime

## Features

* Clean chat interface with persistent message history
* Two backend modes: fully offline (Ollama) or cloud-based (Groq)
* Simple script mode for quick single-prompt testing

## Tech Stack

* Python
* Streamlit
* Ollama (local LLMs — gemma3:1b, llama3.2:1b)
* Groq API (cloud LLM)

## Setup

### Local mode (offline)

1. Install [Ollama](https://ollama.com/) and pull a model: `ollama pull gemma3:1b`
2. Install dependencies: `uv sync`
3. Run: `streamlit run app.py`

### Cloud mode (deployed)

1. Get a free API key from [console.groq.com](https://console.groq.com/)
2. Add it to a `.env` file: `GROQ_API_KEY=your_key_here`
3. Install dependencies: `uv sync`
4. Run: `streamlit run app_cloud.py`

### Quick test (script only)

python main.py

## About

Pixel AI — a local & cloud-powered AI chatbot built with Streamlit and Python. Offline mode runs on Ollama with local LLMs (gemma3, llama3.2) for privacy; cloud mode uses Groq API for fast, deployable responses. Features a clean chat interface with persistent session history. Built as part of an AI/coding learning project.