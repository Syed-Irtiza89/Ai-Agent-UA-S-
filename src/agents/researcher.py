from src.agents.base import BaseAgent
from src.core.state import GlobalState
from src.core.constitution import TaskStatus

class ResearcherAgent(BaseAgent):
    """
    Information gatherer.
    Searches web, reads docs, and provides context.
    """
    
    def __init__(self):
        super().__init__("Researcher")

    def run(self, state: GlobalState) -> GlobalState:
        self.log(state, "Gathering research data...")
        
        # Simulate research finding
        research_context = "Market trends suggest high demand for autonomous AI agents in 2026."
        state.memory_context["last_research"] = research_context
        
        self.log(state, "Research complete.")
        return state
