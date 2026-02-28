from typing import Dict, List, Callable, Any
from src.core.state import GlobalState
from src.core.constitution import ConstitutionEnforcer, TaskStatus
from src.agents.planner import PlannerAgent
from src.agents.executor import ExecutorAgent
from src.agents.researcher import ResearcherAgent
from src.agents.validator import ValidatorAgent
from src.agents.memory_agent import MemoryAgent

class GraphEngine:
    """Manages the execution flow between agents (nodes)."""
    
    def __init__(self):
        self.enforcer = ConstitutionEnforcer()
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.researcher = ResearcherAgent()
        self.validator = ValidatorAgent()
        self.memory_manager = MemoryAgent()

    def execute(self, state: GlobalState) -> GlobalState:
        """Main execution loop for the task graph cycle with robust error handling."""
        try:
            print(f"--- UA²S Execution v{state.system_version} ---")
            
            # 1. Planning Phase
            if not state.plan:
                state = self.planner.run(state)
                if state.status == TaskStatus.BLOCKED:
                    return state

            # 2. Execution Loop
            max_iterations = 10 
            iteration = 0
            
            while iteration < max_iterations:
                iteration += 1
                
                pending_steps = [s for s in state.history if s.status == "PENDING"]
                if not pending_steps:
                    break
                    
                # Rule 5: Tool Usage / Research
                state = self.researcher.run(state)
                state = self.executor.run(state)
                
                # Rule 3.2: Loop Detection
                if self.enforcer.check_loop(state.history):
                    print("[Graph] Infinite loop detected.")
                    state.status = TaskStatus.BLOCKED
                    state.add_message("System", "❌ Infinite loop detected. Escalating to user.")
                    return state

            # 3. Validation Phase
            state = self.validator.run(state)
            
            # 4. Persistence Phase
            state = self.memory_manager.run(state)
            
            print(f"--- Cycle Finished: {state.status} ---")
            return state
        except Exception as e:
            print(f"[Graph Critical Error] {str(e)}")
            state.status = TaskStatus.BLOCKED
            state.add_message("System", f"❌ Execution failed due to a system error: {str(e)}")
            return state
