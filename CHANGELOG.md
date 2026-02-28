# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.1] - 2026-03-01

### Added
- **Plugin System**: Structured plugin architecture in `plugins/` with auto-loader and example web search plugin.
- **Structured Logging**: JSON-based execution traces in `logs/` for full agent explainability.
- **Open Source Readiness**: Added `CONTRIBUTING.md` and GitHub Issue Templates (Bug/Feature).
- **Expanded Test Suite**: Comprehensive tests in `tests/test_core.py` covering all agents, constitution, and state logic.
- **Packaging**: Added `pyproject.toml` for pip-installability.
- **Sample Trace**: Provided `docs/sample_trace.json` for onboarding.

### Improved
- **Robustness**: Added top-level try-except blocks to `GraphEngine` and `CLI` to handle API failures gracefully.

---

## [0.1.0] - 2026-02-28

### Added
- **Core Orchestration**: Graph-based state machine for agent execution.
- **Specialized Agents**: Planner, Executor, Researcher, Validator, and Memory agents.
- **Agent Constitution**: 16-clause safety and honesty framework.
- **Memory System**: SQLite-based long-term persistence.
- **Streamlit Interface**: Premium web dashboard for agent interaction.
- **Tools**: Filesystem, Shell, and Python REPL integrations.
- **CLI**: Rich-based command line interface.
- **Initial Setup**: Project structure, requirements, and basic README.

---
[0.1.1]: https://github.com/Syed-Irtiza89/Ai-Agent-UA-S-/commits/main
[0.1.0]: https://github.com/Syed-Irtiza89/Ai-Agent-UA-S-/commit/initial
