from abc import ABC, abstractmethod
from src.core.state import GlobalState
from src.core.constitution import ConstitutionEnforcer

class BaseAgent(ABC):
    """Abstract base class for all specialized agents."""
    
    def __init__(self, name: str):
        self.name = name
        self.enforcer = ConstitutionEnforcer()

    @abstractmethod
    def run(self, state: GlobalState) -> GlobalState:
        """Execute the agent's logic on the state."""
        pass

    def log(self, state: GlobalState, message: str):
        """Standardized logging for agents."""
        state.add_message(self.name, message)
        print(f"[{self.name}] {message}")
