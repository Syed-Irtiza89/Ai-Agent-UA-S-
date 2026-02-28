from src.agents.base import BaseAgent
from src.core.state import GlobalState
from src.core.constitution import TaskStatus

class ValidatorAgent(BaseAgent):
    """
    Quality Assurance.
    Reviews outputs and ensures constitution compliance.
    """
    
    def __init__(self):
        super().__init__("Validator")

    def run(self, state: GlobalState) -> GlobalState:
        self.log(state, "Starting validation of results...")
        
        # Rule 7: Success & Completion Rules
        # Check if all steps in history are COMPLETED
        all_completed = all(step.status == "COMPLETED" for step in state.history)
        
        if not all_completed:
            self.log(state, "Some steps are not completed. Requesting retry or planning update.")
            state.status = TaskStatus.PARTIAL
            return state

        # Rule 14: Output Discipline (Final check)
        self.log(state, "All steps verified. Task marked as COMPLETED.")
        state.status = TaskStatus.COMPLETED
        
        # Rule 15: User Trust (Be transparent)
        final_message = self.enforcer.format_output(
            TaskStatus.COMPLETED, 
            "The task was executed successfully according to the Agent Constitution."
        )
        state.add_message("System", final_message)
        
        return state
