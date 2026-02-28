import importlib
import os
from plugins._base import PluginBase

class PluginLoader:
    """Auto-discovers and loads plugins from the plugins/ directory."""
    
    def __init__(self, plugin_dir: str = "plugins"):
        self.plugin_dir = plugin_dir
        self.plugins: dict[str, PluginBase] = {}
        self._discover()

    def _discover(self):
        for filename in os.listdir(self.plugin_dir):
            if filename.startswith("_") or not filename.endswith(".py"):
                continue
            module_name = f"plugins.{filename[:-3]}"
            try:
                module = importlib.import_module(module_name)
                for attr_name in dir(module):
                    cls = getattr(module, attr_name)
                    if isinstance(cls, type) and issubclass(cls, PluginBase) and cls is not PluginBase:
                        instance = cls()
                        self.plugins[instance.name] = instance
                        print(f"[PluginLoader] Loaded plugin: {instance.name}")
            except Exception as e:
                print(f"[PluginLoader] Failed to load {filename}: {e}")

    def get(self, name: str) -> PluginBase:
        return self.plugins.get(name)

    def list_plugins(self) -> list:
        return list(self.plugins.keys())
