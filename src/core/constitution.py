from typing import List, Any, Optional
import enum

class TaskStatus(str, enum.Enum):
    COMPLETED = "COMPLETED"
    PARTIAL = "PARTIALLY COMPLETED"
    BLOCKED = "BLOCKED"
    WAITING = "WAITING FOR USER"
    IN_PROGRESS = "IN PROGRESS"

class ConstitutionEnforcer:
    """Enforces the 16 clauses of the Agent Constitution."""
    
    VERSION = "0.1.0"
    MAX_RETRIES = 3
    SECURITY_WHITELIST = ["ls", "dir", "cat", "type", "mkdir", "git status"]
    DESTRUCTIVE_COMMANDS = ["rm", "del", "kill", "format", "drop"]

    @staticmethod
    def check_loop(history: List[Any]) -> bool:
        """Rule 3.2: Detect if the same action produces the same failure twice."""
        if len(history) < 2:
            return False
            
        last_two = history[-2:]
        if last_two[0].action == last_two[1].action and last_two[1].status == "FAILED" and last_two[0].status == "FAILED":
            return True
        return False

    @staticmethod
    def check_reality_lock(plan_step: str) -> Optional[str]:
        """Rule 11: Real world/physical limitations check."""
        physical_keywords = ["buy", "purchase", "physical", "secret", "private credential", "human action"]
        for kw in physical_keywords:
            if kw in plan_step.lower():
                return f"Reality Lock: Task '{plan_step}' requires {kw} which is a physical/private limitation."
        return None

    @staticmethod
    def is_destructive(command: str) -> bool:
        """Rule 4.2: Check if command is destructive."""
        return any(cmd in command.lower() for cmd in ConstitutionEnforcer.DESTRUCTIVE_COMMANDS)

    @staticmethod
    def format_output(status: TaskStatus, message: str) -> str:
        """Rule 14: Output Discipline Rule."""
        label_map = {
            TaskStatus.COMPLETED: "✅ COMPLETED",
            TaskStatus.PARTIAL: "🟡 PARTIALLY COMPLETED",
            TaskStatus.BLOCKED: "❌ BLOCKED",
            TaskStatus.WAITING: "⏸️ WAITING FOR USER",
            TaskStatus.IN_PROGRESS: "⏳ IN PROGRESS"
        }
        return f"{label_map.get(status, 'Status Unknown')} - {message}"
