import os
from src.core.constitution import ConstitutionEnforcer

class FilesystemToolSet:
    """Provides safe file system operations."""
    
    def __init__(self, root_dir: str):
        self.root_dir = os.path.abspath(root_dir)

    def _is_safe_path(self, path: str) -> bool:
        """Ensures path is within root_dir (Workspace Jail)."""
        abs_path = os.path.abspath(os.path.join(self.root_dir, path))
        return abs_path.startswith(self.root_dir)

    def write_file(self, filename: str, content: str) -> str:
        if not self._is_safe_path(filename):
            return "Error: Access denied (path outside workspace)."
        
        with open(os.path.join(self.root_dir, filename), "w") as f:
            f.write(content)
        return f"File '{filename}' written successfully."

    def read_file(self, filename: str) -> str:
        if not self._is_safe_path(filename):
            return "Error: Access denied."
            
        if not os.path.exists(os.path.join(self.root_dir, filename)):
            return f"Error: File '{filename}' not found."
            
        with open(os.path.join(self.root_dir, filename), "r") as f:
            return f.read()
