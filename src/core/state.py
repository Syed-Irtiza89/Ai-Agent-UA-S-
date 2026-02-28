from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class AgentMessage(BaseModel):
    role: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)

class TaskStep(BaseModel):
    id: str
    agent_name: str
    action: str
    result: Optional[str] = None
    status: str = "PENDING"
    retries: int = 0
    timestamp: datetime = Field(default_factory=datetime.now)

class GlobalState(BaseModel):
    """The global state for the task graph execution."""
    user_instruction: str
    plan: List[str] = []
    current_step_index: int = 0
    history: List[TaskStep] = []
    messages: List[AgentMessage] = []
    memory_context: Dict[str, Any] = {}
    system_version: str = "0.1.0"
    status: str = "WAITING FOR USER"
    
    def add_message(self, role: str, content: str):
        self.messages.append(AgentMessage(role=role, content=content))

    def update_step(self, step_id: str, **kwargs):
        for step in self.history:
            if step.id == step_id:
                for key, value in kwargs.items():
                    setattr(step, key, value)
                break
