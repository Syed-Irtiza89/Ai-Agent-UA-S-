import sys
from rich.console import Console
from rich.panel import Panel
from src.core.state import GlobalState
from src.core.graph import GraphEngine
from src.core.constitution import TaskStatus

console = Console()

class UA2SCLI:
    """CLI for the Universal Autonomous AI Agent System."""
    
    def __init__(self):
        self.graph = GraphEngine()

    def start(self):
        console.print(Panel.fit(
            "🧠 [bold blue]Universal Autonomous AI Agent System (UA²S)[/bold blue]\n"
            "System Status: [green]Ready[/green] | Mode: [cyan]Autonomous[/cyan]",
            title="UA²S v0.1.0"
        ))
        
        while True:
            try:
                user_input = console.input("[bold yellow]Query (or 'exit'): [/bold yellow]")
                if user_input.lower() in ["exit", "quit", "stop"]:
                    break
                
                if not user_input.strip():
                    continue
                    
                state = GlobalState(user_instruction=user_input)
                final_state = self.graph.execute(state)
                
                # Rule 14: Output Discipline (Rich display)
                color = "green" if final_state.status == TaskStatus.COMPLETED else "yellow"
                if final_state.status == TaskStatus.BLOCKED: color = "red"
                
                console.print(f"\n[bold {color}]RESULT: {final_state.status}[/bold {color}]")
                for msg in final_state.messages:
                    if msg.role == "System":
                        console.print(f"[bold white]{msg.content}[/bold white]")
                    else:
                        console.print(f"[dim][{msg.role}][/dim] {msg.content}")
                
            except KeyboardInterrupt:
                console.print("\n[red]Session Aborted by User.[/red]")
                break
            except Exception as e:
                console.print(f"[bold red]CLI Error: {str(e)}[/bold red]")

if __name__ == "__main__":
    cli = UA2SCLI()
    cli.start()
