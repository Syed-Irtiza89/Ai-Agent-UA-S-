import pytest
from src.core.constitution import ConstitutionEnforcer, TaskStatus
from src.core.state import GlobalState

def test_constitution_reality_lock():
    enforcer = ConstitutionEnforcer()
    issue = enforcer.check_reality_lock("Go buy a coffee for me")
    assert "Reality Lock" in issue

def test_constitution_loop_detection():
    enforcer = ConstitutionEnforcer()
    class MockStep:
        def __init__(self, action, status):
            self.action = action
            self.status = status
            
    history = [
        MockStep("mkdir test", "FAILED"),
        MockStep("mkdir test", "FAILED")
    ]
    assert enforcer.check_loop(history) == True

def test_state_message_addition():
    state = GlobalState(user_instruction="Hello")
    state.add_message("User", "Hi")
    assert len(state.messages) == 1
    assert state.messages[0].content == "Hi"
