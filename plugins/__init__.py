"""
Plugin System for UA²S.

HOW TO ADD A PLUGIN:
1. Create a new .py file in this plugins/ directory.
2. Your file must define a class that inherits from PluginBase.
3. Implement the required `name`, `description`, and `run()` method.
4. The plugin will be auto-discovered by the PluginLoader.

Example:
    from plugins._base import PluginBase
    
    class MyCustomTool(PluginBase):
        name = "my_tool"
        description = "Does something useful."
        
        def run(self, input: str) -> str:
            return f"Processed: {input}"
"""
