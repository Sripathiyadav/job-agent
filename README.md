
# 🚀 Job-Agent

An AI-powered job search assistant built with **Python**, **Telegram**, **Ollama**, **SQLite**, and future **OpenClaw browser automation**.

---

## 📌 Overview

Job-Agent is designed to help users search, organize, and manage job opportunities directly through Telegram.

The project combines:

- 🤖 AI-powered conversations using Ollama
- 📱 Telegram Bot interface
- 💾 Local SQLite database
- 🔍 Multi-source job search architecture
- 🌐 Browser automation (OpenClaw - upcoming)

The long-term vision is to create a personal AI job-hunting assistant capable of finding, ranking, tracking, and recommending jobs automatically.

---

## ✨ Features

### ✅ Currently Working

- 🤖 Telegram Bot
- 🧠 Ollama AI Integration
- 💾 SQLite Job Database
- 🔎 Job Search Framework
- 📄 Job Details Lookup
- 📌 Save Jobs Feature
- 🗂 Multi-source Search Architecture
- ☁️ GitHub Repository Integration

### 🔜 Planned Features

- 🕷 OpenClaw Browser Automation
- 💼 Stepstone Integration
- 💼 Indeed Integration
- 💼 LinkedIn Integration
- 🎯 AI Job Ranking
- 📄 Resume Matching
- 🔔 Job Alerts
- 📈 Career Recommendations
- 🤖 Autonomous Job Search Agent

---

## 🏗 Project Structure

```text
job-agent/

├── agents/
│   └── openclaw_agent.py

├── docs/

├── sources/
│   ├── indeed.py
│   ├── linkedin.py
│   └── stepstone.py

├── tests/

├── main.py
├── job_search.py
├── database.py
├── config.py
├── requirements.txt
├── jobs.db
└── README.md
```

---

## 🛠 Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python 3.13 |
| AI Model | Ollama |
| Bot Framework | Telegram Bot API |
| Database | SQLite |
| Job Sources | Apify / OpenClaw |
| Version Control | Git & GitHub |

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Sripathiyadav/job-agent.git

cd job-agent
```

### 2️⃣ Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 3️⃣ Install Ollama

MacOS:

```bash
brew install ollama
```

Start Ollama:

```bash
ollama serve
```

Download the model:

```bash
ollama pull llama3.2:latest
```

Verify:

```bash
ollama list
```

---

## 🔑 Configuration

Create a file named:

```text
config.py
```

Add your credentials:

```python
APIFY_TOKEN = "YOUR_APIFY_TOKEN"
TELEGRAM_TOKEN = "YOUR_TELEGRAM_TOKEN"
```

---

## ▶️ Running the Project

Start the bot:

```bash
python3.13 main.py
```

Expected output:

```text
AgentClaw AI Started...
```

---

## 📱 Telegram Commands

### 🔍 Search Jobs

```text
/jobs flutter
```

Example:

```text
/jobs python
/jobs flutter
/jobs data analyst
```

### 📄 View Job Details

```text
/details 1
```

### 📌 Save a Job

```text
/save 1
```

### 📂 View Saved Jobs

```text
/saved
```

---

## 🗺 Development Roadmap

### ✅ Phase 1 — Foundation

- Telegram Bot
- Ollama Integration
- SQLite Database
- GitHub Repository

### 🚧 Phase 2 — Automation

- OpenClaw Integration
- Browser Automation
- Real Job Sources

### 🎯 Phase 3 — Intelligence

- AI Job Ranking
- Resume Matching
- Personalized Recommendations

### 🤖 Phase 4 — Autonomous Agent

- Automated Job Discovery
- Daily Job Monitoring
- Career Guidance
- Smart Notifications

---

## 👨‍💻 Author

### Sripathi Vangapandla

GitHub:
https://github.com/Sripathiyadav

LinkedIn:
https://www.linkedin.com/in/sripathi-yadav/

Portfolio:
https://sripathiyadavportfolio.netlify.app/

---

## ⭐ Future Goal

Build a fully autonomous AI career assistant capable of:

- Finding jobs automatically
- Evaluating job relevance
- Matching resumes
- Tracking applications
- Recommending career opportunities

All from a simple Telegram chat interface.

---

## 📜 License

This project is currently under active development and intended for educational and personal use.