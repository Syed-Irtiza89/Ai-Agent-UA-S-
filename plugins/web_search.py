"""
Example Plugin — searches for a query using DuckDuckGo.
Copy this file as a template for your own tool plugins.
"""
from plugins._base import PluginBase

class WebSearchPlugin(PluginBase):
    name = "web_search"
    description = "Searches the web for a given query and returns a summary."

    def run(self, input: str) -> str:
        # In production: use duckduckgo_search or Tavily API here
        return f"[Simulated] Search results for '{input}': Found 5 relevant articles on autonomous AI agents."
