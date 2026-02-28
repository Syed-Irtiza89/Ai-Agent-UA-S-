# 🧠 Universal Autonomous AI Agent System (UA²S)

> *"Mera yeh kaam kar do" — and the system handles it, end-to-end.*

**UA²S** is a production-grade, constitutionally-governed multi-agent AI framework that behaves like a digital human assistant.

![Python](https://img.shields.io/badge/python-3.10+-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Status](https://img.shields.io/badge/status-alpha-orange) ![CI](https://github.com/Syed-Irtiza89/Ai-Agent-UA-S-/actions/workflows/ci.yml/badge.svg)

---

## 🏗️ System Architecture

```
User Instruction
      │
      ▼
┌─────────────────┐
│  Planner Agent  │  ← Decomposes intent into steps
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────────────┐
│              Graph Engine                   │
│  Research → Execute → Validate → Persist    │
└────────┬────────────────────────────────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
Executor  Researcher     ← Tools: Shell, Filesystem, REPL, Browser
    │
    ▼
Validator ─► Memory Agent ─► SQLite Storage
```

Every decision is governed by the **16-clause Agent Constitution** (see `CONSTITUTION.md`):
- 🔒 **Reality Lock** — blocks impossible actions
- 🔁 **No-Loop Rule** — max 3 retries per step
- 🏷️ **Output Discipline** — every response is labeled

---

## 🚀 Getting Started

### 1. Clone & Install

```bash
git clone https://github.com/Syed-Irtiza89/Ai-Agent-UA-S-.git
cd Ai-Agent-UA-S-
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env and add your API keys
```

### 3. Run the Agent (CLI)

```bash
python main.py
```

### 4. Run the Dashboard (Streamlit UI)

```bash
streamlit run src/interface/app.py
```

---

## 🎮 Usage Examples

### English Instruction
```
Query: I want ideas to earn money with AI
Agent Status: IN_PROGRESS → COMPLETED
✅ COMPLETED: Analyzed 5 profitable AI SaaS niches. Top recommendation: Document automation.
```

### Roman Urdu Instruction
```
Query: Mera yeh repo samajh ke improve karo
Agent Status: IN_PROGRESS → COMPLETED
✅ COMPLETED: Read repo structure and suggested 3 specific performance improvements.
```

### Blocked by Reality Lock (Clause 11)
```
Query: Go buy a coffee for me
Agent Status: BLOCKED
❌ BLOCKED: Physical action required. Cannot execute without physical presence.
   Next best option: I can order online if given store URL and credentials.
```

---

## 📊 Sample Execution Trace (JSON Log)

Every run generates a structured log at `logs/session_<timestamp>.json`:

```json
{
  "session_id": "20260301_013000",
  "total_steps": 3,
  "trace": [
    {
      "step": 1,
      "agent": "Planner",
      "input": "Research profitable AI ideas",
      "output": "Plan created with 3 steps",
      "status": "✅ OK"
    },
    {
      "step": 2,
      "agent": "Executor",
      "input": "Research profitable AI SaaS ideas for 2026",
      "output": "Successfully performed research step",
      "status": "✅ COMPLETED"
    },
    {
      "step": 3,
      "agent": "Validator",
      "input": "Verify all steps completed",
      "output": "All steps verified. Task marked as COMPLETED.",
      "status": "✅ COMPLETED"
    }
  ]
}
```

---

## 🟢 Status Labels

| Label | Meaning |
|---|---|
| ✅ `COMPLETED` | All steps verified and done |
| 🟡 `PARTIAL` | Some steps incomplete |
| ❌ `BLOCKED` | Physical limit, missing creds, or reality lock |
| ⏳ `WAITING` | User input required |
| 🔄 `IN_PROGRESS` | Currently executing |

---

## 🛠️ Modularity

```
src/
  agents/        ← Planner, Executor, Researcher, Validator, Memory
  core/          ← Graph Engine, Constitution, State, Prompts, Logger
  tools/         ← Filesystem, Shell, Browser, Python REPL
  memory/        ← SQLite Long-Term Storage
  interface/     ← CLI (Rich) + Dashboard (Streamlit)
plugins/         ← Drop-in custom agents/tools
tests/           ← Full test suite (15+ tests)
docs/            ← Sample traces and references
```

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for architecture guidelines, code style, and constitution compliance rules.

---

## 📜 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## 📦 Install as Package

```bash
pip install .
```

---

## 📄 License

MIT — Built with ❤️ for autonomous AI research.
## ?? Example Run

### Input
`ash
python main.py "I want an idea to earn money"
`

### Execution Flow

* Planner ? Task decomposition
* Researcher ? Market trends
* Executor ? Proposal generation
* Validator ? Constitution + coverage check
* Memory Agent ? Store validated outcome

### Output

`json
{
  "status": "COMPLETED",
  "summary": "Generated a validated online income idea",
  "constitution_violations": []
}
`

### Status Labels

* **COMPLETED** ? 100% requirements satisfied
* **PARTIAL** ? Some tasks blocked
* **BLOCKED** ? Reality lock / missing credentials
* **WAITING** ? User confirmation required
