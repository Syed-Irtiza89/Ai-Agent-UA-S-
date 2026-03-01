# 🧠 UA²S — Universal Autonomous AI Agent System

UA²S is a **constitutionally-governed, multi-agent autonomous AI framework** designed to behave like a **digital human assistant**.
It combines planning, research, execution, validation, and memory — all enforced by a strict safety constitution.

> ⚠️ UA²S is **not a chatbot**.
> It is a **stateful agentic system** with governance, explainability, and control.

---

## ✨ Key Features

* 🧩 **Multi-Agent Architecture**
  * Planner Agent
  * Researcher Agent
  * Executor Agent
  * Validator Agent
  * Memory Agent

* 📜 **Agent Constitution (16 Rules)**
  * Reality Lock (blocks physical / credential-based tasks)
  * No infinite loops
  * Output discipline (explicit status labels)
  * Workspace Jail (filesystem safety)

* 🧠 **Graph-Based Orchestration**
  * State-machine execution
  * Retry limits (max 3)
  * Deterministic flow

* 💾 **Long-Term Memory**
  * SQLite-based persistence
  * Memory writes gated by Validator approval

* 🌍 **Multi-Language Friendly**
  * English + Roman Urdu tested

---

## 🏗️ Architecture Overview

```
User
 ↓
Planner Agent ──► Task Graph
 ↓
Researcher Agent ──► Context
 ↓
Executor Agent ──► Tools / Actions
 ↓
Validator Agent ──► Safety + Coverage Check
 ↓
Memory Agent ──► Persistent Knowledge
```

All steps are enforced by the **Agent Constitution**.

---

## 📁 Project Structure

```
src/
  agents/
    planner.py
    researcher.py
    executor.py
    validator.py
    memory_agent.py
  core/
    graph.py
    state.py
    constitution.py
    prompts.py
  tools/
    filesystem.py
    shell.py
    browser.py
    gates.py
  memory/
    short_term.py
    long_term.py

tests/
logs/
main.py
CONSTITUTION.md
CHANGELOG.md
requirements.txt
.env.example
```

---

## 🚀 Installation

```bash
git clone https://github.com/Syed-Irtiza89/Ai-Agent-UA-S-
cd Ai-Agent-UA-S-
pip install -r requirements.txt
```

Create environment file:
```bash
cp .env.example .env
```
Add your API keys inside `.env`.

---

## ▶️ Usage

### Basic Run
```bash
python main.py "I want an idea to earn money"
```

### Roman Urdu Example
```bash
python main.py "Mera yeh kaam samajh ke improve karo"
```

---

## 🔍 Example Output

```json
{
  "status": "COMPLETED",
  "summary": "Validated online income idea generated",
  "constitution_violations": []
}
```

---

## 🏷️ Status Labels

* **COMPLETED** ✅
  All requirements satisfied, constitution compliant, validated.

* **PARTIAL** 🟡
  Some subtasks blocked, but useful output produced.

* **BLOCKED** ❌
  Task violates constitution (e.g. physical action, credentials).

* **WAITING** ⏸️
  Explicit user confirmation required.

---

## 🔐 Security Model

* 🔒 Filesystem access restricted to project root
* ⚠️ Dangerous shell commands require user confirmation
* 🚫 Physical-world actions blocked by Reality Lock
* 🔁 Infinite loops automatically terminated

---

## 🧪 Testing

```bash
python -m pytest tests/
```

Includes:
* Agent unit tests
* Plan → Act → Verify integration tests
* Constitution compliance checks

---

## 📜 Agent Constitution

All agents operate under a strict constitution defined in:
```
CONSTITUTION.md
```
This document is **runtime-enforced**, not just documentation.

---

## 🛣️ Roadmap

- [x] Plugin system for custom agents
- [ ] Vector memory support
- [x] Web dashboard (Streamlit)
- [ ] Multi-user isolation
- [ ] On-prem / enterprise mode

---

## 🤝 Contributing

Contributions are welcome!
1. Fork the repo
2. Create a feature branch
3. Add tests for new logic
4. Ensure Validator passes
5. Open a PR with explanation

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🧠 Final Note

UA²S is built for developers who want:
* **control over autonomy**
* **explainable AI behavior**
* **safety by design**

If you’re tired of uncontrolled agent loops — UA²S is for you.
