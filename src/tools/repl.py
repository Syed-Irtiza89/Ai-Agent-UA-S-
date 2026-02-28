import sys
import io
import contextlib
import traceback

class PythonREPL:
    """Safe (simulated jail) execution of Python code for calculations and data logic."""
    
    def __init__(self):
        self.globals = {}
        self.locals = {}

    def execute(self, code: str) -> str:
        """Executes a string of Python code and returns the output or error."""
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            try:
                # Basic safety check: simple keyword filtering (Not a substitute for containerization)
                forbidden = ["os.", "sys.", "subprocess", "eval", "exec", "__import__", "open("]
                if any(f in code for f in forbidden):
                    return "Error: Use of restricted libraries or functions detected."

                exec(code, self.globals, self.locals)
            except Exception:
                return traceback.format_exc()
        
        return output.getvalue() or "Code executed successfully (no output)."
