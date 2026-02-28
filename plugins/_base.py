from abc import ABC, abstractmethod

class PluginBase(ABC):
    """Base class for all UA²S plugins."""
    
    name: str = ""
    description: str = ""

    @abstractmethod
    def run(self, input: str) -> str:
        """Execute the plugin logic and return a result string."""
        pass
