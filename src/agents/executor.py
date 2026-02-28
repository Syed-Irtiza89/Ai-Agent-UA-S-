from src.agents.base import BaseAgent
from src.core.state import GlobalState
from src.core.constitution import TaskStatus

class ExecutorAgent(BaseAgent):
    """
    Hands of the system.
    Translates plans into tool calls and execution steps.
    """
    
    def __init__(self):
        super().__init__("Executor")

    def run(self, state: GlobalState) -> GlobalState:
        if state.status == TaskStatus.BLOCKED:
            return state

        current_step = None
        for step in state.history:
            if step.status == "PENDING":
                current_step = step
                break
        
        if not current_step:
            self.log(state, "No more pending steps to execute.")
            return state

        self.log(state, f"Executing step: {current_step.action}")
        
        # Rule 5: Tool Usage
        # In a real scenario, this would choose a tool from src/tools/
        # For now, we simulate execution.
        
        # Rule 3.2: Loop Detection (checked via Graph or here)
        if current_step.retries >= self.enforcer.MAX_RETRIES:
            self.log(state, f"Max retries reached for step: {current_step.id}")
            current_step.status = "FAILED"
            state.status = TaskStatus.BLOCKED
            state.add_message("System", f"❌ Aborting due to repeated failure on: {current_step.action}")
            return state

        # Simulate success
        current_step.result = f"Successfully performed: {current_step.action}"
        current_step.status = "COMPLETED"
        
        self.log(state, f"Step {current_step.id} completed.")
        return state
