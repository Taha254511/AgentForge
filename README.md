# 🤖 AgentForge

**AgentForge** is a collection of AI-powered agents and experiments built using Python, Agno, Groq, and other tools. The project explores AI agents, multi-agent systems, persistent memory, financial research, and interactive applications.

## ✨ Features

### 📺 YouTube Analyzer

* Analyze YouTube videos using AI.
* Extract and process video information with YouTube tools.
* Generate useful insights through an interactive Streamlit interface.

### 🌐 Multi-Agent Translation Team

* Uses specialized AI agents for English, Chinese, and Hindi.
* Explores collaboration between multiple AI agents.
* Powered by Groq-hosted language models.

### 🧠 AI Agent with Persistent Memory

* Stores agent memory using SQLite.
* Explores how AI agents can retain information between interactions.

### 📈 Stock Research Agent

* Retrieves financial information using YFinance tools.
* Uses web search to support financial research.
* Helps organize stock-related information for analysis.

### ✈️ Travel Assistant

* Uses AI and web search tools to assist with travel-related queries.
* Explores tool-using AI agents for practical tasks.

## 🛠️ Tech Stack

* **Language:** Python
* **AI Agent Framework:** Agno
* **LLM Provider:** Groq
* **Models:** `openai/gpt-oss-20b`, `openai/gpt-oss-120b`
* **Frontend:** Streamlit
* **Tools:** YouTubeTools, YFinanceTools, DuckDuckGoTools
* **Database:** SQLite
* **Environment Management:** Python environment variables with `python-dotenv`

## 📁 Project Structure

```text
AGENTIC_AI/
│
├── __pycache__/
├── .env
├── .gitignore
├── agent.py
├── agno.db
├── finance.py
├── memory.py
├── README.md
├── team.py
├── ui.py
└── youtube_analyzer.py
```

**Note:** Runtime-generated files, such as the SQLite database and Python cache, are excluded from version control.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Taha254511/AgentForge.git
cd AgentForge
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows using Git Bash:

```bash
source .venv/Scripts/activate
```

### 3. Install dependencies

Install the libraries required by your project:

```bash
pip install agno streamlit python-dotenv yfinance
```

Install any additional packages required by the individual agents. Depending on your installed Agno version, some integrations may require separate packages.

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your own API key.

**Important:** Never commit your `.env` file or expose your API key in source code.

### 5. Run the YouTube Analyzer

```bash
streamlit run ui.py
```

Streamlit will provide a local URL in the terminal. Open that URL in your browser to use the application.

## 🔐 Security

* Store API keys in environment variables.
* Keep `.env` and other secret files out of Git.
* Do not commit local databases containing personal or runtime data.
* Never publish API keys in source code or screenshots.

## 🎯 Goals

* Explore practical applications of AI agents.
* Experiment with multi-agent collaboration.
* Integrate external tools with large language models.
* Learn about persistent memory and data retrieval.
* Build useful AI-powered applications.

## 👨‍💻 Author

**Taha Hussain**

---

*AgentForge — Experimenting with AI agents, one project at a time.*
