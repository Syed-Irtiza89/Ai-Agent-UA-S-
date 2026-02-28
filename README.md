# 🧠 Universal Autonomous AI Agent System (UA²S)

**UA²S** is a general-purpose autonomous AI agent workforce designed to behave like a digital human assistant. It transitions from a simple chatbot to a thinking, planning, and acting system.

---

## 🏗️ System Architecture

UA²S leverages a **Stateful Multi-Agent Graph** architecture:
- **Planner Agent**: The "Brain" that decomposes vague instructions into actionable plans.
- **Executor Agent**: The "Hands" that interact with the OS, Shell, and Filesystem.
- **Researcher Agent**: The "Eyes" that gather external intelligence.
- **Validator Agent**: The "Critic" that ensures quality and protocol compliance.
- **Memory Agent**: The "Hippocampus" that manages long-term persistence and user preferences.

---

## 🛡️ Agent Constitution (Safety & Honesty)

Every action is governed by a **16-clause Constitution** (see `CONSTITUTION.md`):
- **Reality Lock**: Prevents agents from assuming physical or unauthorized superpowers.
- **No-Loop Enforcement**: Hard limit of 3 retries per step to prevent infinite reasoning loops.
- **Output Discipline**: Clear status labeling (`✅ COMPLETED`, `❌ BLOCKED`, etc.).
- **Workspace Jail**: Strict file system and shell boundaries.

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- LLM API Keys (OpenAI, Anthropic, or Google Gemini)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/Syed-Irtiza89/Ai-Agent-UA-S-.git
cd Ai-Agent-UA-S-

# Install dependencies
pip install -r requirements.txt
```

### 3. Setup Environment
Rename `.env.example` to `.env` and add your API keys:
```bash
cp .env.example .env
```

### 4. Run the Agent
```bash
python main.py
```

---

## 🛠️ Modularity & Tools
The project is structured for high maintainability:
- `src/agents/`: Specialized agent logic.
- `src/core/`: Orchestration, State, and Constitution.
- `src/tools/`: Filesystem, Shell, and Browser integrations.
- `src/memory/`: SQLite-based persistent storage.

---

## 🧪 Testing
Run the test suite to ensure stability:
```bash
pytest tests/
```

## 📜 License
This project is part of a foundation for a real AI product. Built with ❤️ for autonomy.
