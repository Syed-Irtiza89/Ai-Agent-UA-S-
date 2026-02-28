import subprocess
from src.core.constitution import ConstitutionEnforcer

class ShellToolSet:
    """Safe shell command execution."""
    
    def __init__(self):
        self.enforcer = ConstitutionEnforcer()

    def execute_command(self, command: str) -> str:
        # Rule 4.2 / 5.1: Whitelist and Security check
        cmd_base = command.split()[0] if command else ""
        if cmd_base not in self.enforcer.SECURITY_WHITELIST:
            return f"Error: Command '{cmd_base}' is not whitelisted or requires user confirmation."

        if self.enforcer.is_destructive(command):
            return "Error: Destructive command blocked. Waiting for manual approval."

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                return result.stdout
            else:
                return f"Execution Error: {result.stderr}"
        except Exception as e:
            return f"System Error: {str(e)}"
