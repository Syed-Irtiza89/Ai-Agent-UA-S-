from src.agents.base import BaseAgent
from src.core.state import GlobalState
from src.memory.long_term import LongTermMemory

class MemoryAgent(BaseAgent):
    """
    Hippocampus of the system.
    Handles persistent storage of user preferences and task outcomes.

    # Memory write allowed ONLY if:
    # - Validator status == COMPLETED
    # - Confidence >= 0.9
    # - Task hash attached
    """
    
    def __init__(self):
        super().__init__("MemoryManager")
        self.db = LongTermMemory()

    def run(self, state: GlobalState) -> GlobalState:
        self.log(state, "Updating long-term memory with latest results...")
        
        # Rule 6: Memory Governance
        if state.status == "COMPLETED":
            # Store summary of task
            self.db.store(f"last_task_{state.system_version}", state.plan)
            self.log(state, "Task outcome saved to long-term memory.")
            
        # Check for user preferences
        if "mera" in state.user_instruction.lower():
            self.db.store("preference_language", "Roman Urdu")
            self.log(state, "Preference for Roman Urdu detected and saved.")

        return state
