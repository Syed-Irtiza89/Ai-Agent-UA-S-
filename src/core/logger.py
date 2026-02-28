import json
import os
from datetime import datetime
from typing import Any, Optional

LOG_DIR = "logs"

class ExecutionLogger:
    """
    Structured JSON logger for agent execution traces.
    Every step, decision, and result is recorded for explainability.
    """

    def __init__(self, session_id: Optional[str] = None):
        self.session_id = session_id or datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs(LOG_DIR, exist_ok=True)
        self.log_path = os.path.join(LOG_DIR, f"session_{self.session_id}.json")
        self.entries = []

    def log(self, agent: str, step: int, input_text: str, output: str, status: str):
        """Record one agent execution step."""
        entry = {
            "step": step,
            "agent": agent,
            "input": input_text,
            "output": output,
            "status": status,
            "timestamp": datetime.now().isoformat()
        }
        self.entries.append(entry)
        self._flush()

    def _flush(self):
        """Write all entries to disk after each step."""
        with open(self.log_path, "w", encoding="utf-8") as f:
            json.dump({
                "session_id": self.session_id,
                "total_steps": len(self.entries),
                "trace": self.entries
            }, f, indent=2)

    def get_trace(self) -> list:
        return self.entries
