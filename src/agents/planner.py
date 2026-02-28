from typing import List
from src.agents.base import BaseAgent
from src.core.state import GlobalState, TaskStep
from src.core.constitution import TaskStatus

class PlannerAgent(BaseAgent):
    """
    Brain of the system.
    Responsible for interpreting intent and decomposing goals.
    """
    
    def __init__(self):
        super().__init__("Planner")

    def run(self, state: GlobalState) -> GlobalState:
        self.log(state, "Interpreting user intent...")
        
        # In a real scenario, this would call an LLM.
        # For now, we simulate the decomposition based on the instruction.
        if "idea" in state.user_instruction.lower() and "paisa" in state.user_instruction.lower():
            state.plan = [
                "Research profitable AI SaaS ideas for 2026",
                "Analyze competition and market gap",
                "Generate a finalized business proposal"
            ]
        elif "repo" in state.user_instruction.lower():
            state.plan = [
                "Read repository file structure",
                "Analyze core modules",
                "Suggest specific improvements"
            ]
        else:
            state.plan = [f"Complete the task: {state.user_instruction}"]

        # Initialize the history with the plan steps
        for i, step_desc in enumerate(state.plan):
            # Check for reality lock
            reality_issue = self.enforcer.check_reality_lock(step_desc)
            if reality_issue:
                self.log(state, f"Reality Check failed for step: {step_desc}")
                state.status = TaskStatus.BLOCKED
                state.add_message("System", f"❌ {reality_issue}")
                return state

            state.history.append(TaskStep(
                id=f"step_{i}",
                agent_name="Executor", # Default executor
                action=step_desc,
                status="PENDING"
            ))

        self.log(state, f"Plan created with {len(state.plan)} steps.")
        state.status = TaskStatus.IN_PROGRESS
        return state
