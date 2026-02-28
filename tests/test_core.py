import pytest
from src.core.constitution import ConstitutionEnforcer, TaskStatus
from src.core.state import GlobalState, TaskStep
from src.agents.planner import PlannerAgent
from src.agents.executor import ExecutorAgent
from src.agents.validator import ValidatorAgent
from src.core.logger import ExecutionLogger

# ─── Constitution Tests ────────────────────────────────────────
class TestConstitution:
    def test_reality_lock_triggers_on_buy(self):
        e = ConstitutionEnforcer()
        assert "Reality Lock" in e.check_reality_lock("Go buy a coffee")

    def test_reality_lock_passes_on_safe_step(self):
        e = ConstitutionEnforcer()
        assert e.check_reality_lock("Analyze GitHub repo") is None

    def test_loop_detection_with_two_failed_same_actions(self):
        e = ConstitutionEnforcer()
        history = [
            TaskStep(id="s0", agent_name="Executor", action="mkdir test", status="FAILED"),
            TaskStep(id="s1", agent_name="Executor", action="mkdir test", status="FAILED"),
        ]
        assert e.check_loop(history) is True

    def test_no_loop_on_distinct_actions(self):
        e = ConstitutionEnforcer()
        history = [
            TaskStep(id="s0", agent_name="Executor", action="mkdir test", status="FAILED"),
            TaskStep(id="s1", agent_name="Executor", action="git status", status="FAILED"),
        ]
        assert e.check_loop(history) is False

    def test_destructive_command_detected(self):
        e = ConstitutionEnforcer()
        assert e.is_destructive("rm -rf /") is True

    def test_safe_command_not_destructive(self):
        e = ConstitutionEnforcer()
        assert e.is_destructive("git status") is False

    def test_format_output_completed(self):
        e = ConstitutionEnforcer()
        output = e.format_output(TaskStatus.COMPLETED, "All done.")
        assert "✅" in output

    def test_format_output_blocked(self):
        e = ConstitutionEnforcer()
        output = e.format_output(TaskStatus.BLOCKED, "Physical action required.")
        assert "❌" in output


# ─── State Tests ────────────────────────────────────────────────
class TestGlobalState:
    def test_message_addition(self):
        state = GlobalState(user_instruction="Hello")
        state.add_message("User", "Test msg")
        assert len(state.messages) == 1
        assert state.messages[0].role == "User"

    def test_step_update(self):
        state = GlobalState(user_instruction="Test")
        step = TaskStep(id="s0", agent_name="Executor", action="do something", status="PENDING")
        state.history.append(step)
        state.update_step("s0", status="COMPLETED")
        assert state.history[0].status == "COMPLETED"


# ─── Planner Agent Tests ────────────────────────────────────────
class TestPlannerAgent:
    def test_plan_created_for_generic_instruction(self):
        planner = PlannerAgent()
        state = GlobalState(user_instruction="Analyze this report")
        result = planner.run(state)
        assert len(result.plan) > 0

    def test_plan_blocked_on_physical_task(self):
        planner = PlannerAgent()
        state = GlobalState(user_instruction="Buy me groceries from the store")
        result = planner.run(state)
        # Buy triggers reality lock in plan steps
        assert result.status in [TaskStatus.BLOCKED, TaskStatus.IN_PROGRESS]


# ─── Executor Agent Tests ────────────────────────────────────────
class TestExecutorAgent:
    def test_executor_completes_a_step(self):
        from src.core.state import TaskStep
        executor = ExecutorAgent()
        state = GlobalState(user_instruction="Do task", plan=["Step 1"], status=TaskStatus.IN_PROGRESS)
        state.history.append(TaskStep(id="s0", agent_name="Executor", action="Do Step 1", status="PENDING"))
        result = executor.run(state)
        assert result.history[0].status == "COMPLETED"

    def test_executor_skips_on_blocked_state(self):
        executor = ExecutorAgent()
        state = GlobalState(user_instruction="Blocked task", status=TaskStatus.BLOCKED)
        result = executor.run(state)
        assert result.status == TaskStatus.BLOCKED


# ─── Validator Agent Tests ────────────────────────────────────────
class TestValidatorAgent:
    def test_validator_marks_all_steps_completed(self):
        from src.core.state import TaskStep
        validator = ValidatorAgent()
        state = GlobalState(user_instruction="Test", status=TaskStatus.IN_PROGRESS)
        state.history.append(TaskStep(id="s0", agent_name="Executor", action="Task A", status="COMPLETED"))
        result = validator.run(state)
        assert result.status == TaskStatus.COMPLETED

    def test_validator_marks_partial_if_pending(self):
        from src.core.state import TaskStep
        validator = ValidatorAgent()
        state = GlobalState(user_instruction="Test", status=TaskStatus.IN_PROGRESS)
        state.history.append(TaskStep(id="s0", agent_name="Executor", action="Task A", status="PENDING"))
        result = validator.run(state)
        assert result.status == TaskStatus.PARTIAL


# ─── Logger Tests ────────────────────────────────────────────────
class TestExecutionLogger:
    def test_log_creates_entry(self, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        logger = ExecutionLogger(session_id="test_session")
        logger.log("Planner", 1, "Research AI", "Plan created.", "OK")
        trace = logger.get_trace()
        assert len(trace) == 1
        assert trace[0]["agent"] == "Planner"
