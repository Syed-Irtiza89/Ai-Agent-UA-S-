# Contributing to UA²S

Thank you for your interest in contributing to the **Universal Autonomous AI Agent System (UA²S)**! 🎉

---

## 🛠️ How to Contribute

### 1. Fork & Clone
```bash
git clone https://github.com/<your-username>/Ai-Agent-UA-S-.git
cd Ai-Agent-UA-S-
```

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Set Up Environment
```bash
pip install -r requirements.txt
cp .env.example .env
# Fill in your API keys
```

### 4. Make Changes
- Follow the existing code style.
- All agents must inherit from `BaseAgent`.
- All new tools must pass `ConstitutionEnforcer.check_reality_lock()` before execution.
- New agents must be registered in `GraphEngine`.

### 5. Add Tests
Every new feature requires a corresponding test in `tests/`.

### 6. Submit a Pull Request
- Clear title and description.
- Reference any related issues.
- Ensure all tests pass: `pytest tests/`

---

## 🏗️ Architecture Guide

- **Agents**: `src/agents/` — Inherit `BaseAgent`, implement `run(state) -> state`.
- **Tools**: `src/tools/` — Stateless utilities. Must respect Workspace Jail.
- **Plugins**: `plugins/` — Drop-in `.py` files following the Plugin interface.
- **Core**: `src/core/` — Do not modify `constitution.py` without opening a proposal issue first.

---

## 📌 Code Style

- Python 3.10+
- Type hints required.
- Docstrings for all public classes and methods.
- Max line length: 120 characters.

---

## 🔒 Constitution Compliance

> All contributions must respect the 16-clause [CONSTITUTION.md](CONSTITUTION.md).
> Any PR that bypasses safety rules will be rejected.

---

## 🙏 Thank You

Every contribution — code, docs, tests, or bug reports — makes UA²S better for everyone.
