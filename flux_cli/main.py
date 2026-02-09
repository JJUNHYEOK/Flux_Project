import sys
import subprocess
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.status import Status

# 모듈 임포트
from .system_scanner import SystemScanner
from .ai_solver import AISolver
from .ai_critic import AICritic

console = Console()
scanner = SystemScanner()
solver = AISolver(local=True, model_name='gemma3:1b')
critic = AICritic(local=True, model_name='gemma3:1b')

def main():
    if len(sys.argv) < 2:
        console.print("[bold red]Usage: python main.py <command>[/]")
        return

    user_cmd = sys.argv[1:]
    
    # 1. Run the system and capture errors
    process = subprocess.run(user_cmd, capture_output=True, text=True)
    
    if process.returncode == 0:
        console.print(process.stdout)
        console.print("[bold green]Success![/]")
        return

    # 2. if error occurs -> call Gemini
    console.print(Panel(process.stderr.strip()[:300] + "...", title="Error Detected", border_style="red"))
    
    context, _ = scanner.get_context()
    
    with console.status("[bold cyan]Gemini 3 is generating solutions...[/]") as status:
        solutions_data = solver.generate_solution(context, process.stderr)

    # 3. Print the solution
    console.print(f"\n[bold]💡 Analysis:[/bold] {solutions_data.get('analysis', 'No analysis')}")
    
    table = Table(title="Suggested Fixes")
    table.add_column("No.", style="cyan")
    table.add_column("Command", style="green")
    table.add_column("Explanation")
    
    for sol in solutions_data.get('solutions', []):
        table.add_row(str(sol['id']), sol['command'], sol['explanation'])
    
    console.print(table)

    # 4. User selects the option
    choice = Prompt.ask("Select Option", choices=["1", "2", "3", "q"], default="1")
    if choice == 'q': return

    selected_sol = next((s for s in solutions_data['solutions'] if str(s['id']) == choice), None)
    command_to_run = selected_sol['command']

    # 5. Claude Critic
    with console.status("[bold magenta]Claude 3.5 is auditing command safety...[/]") as status:
        audit_result = critic.verify_safety(command_to_run)

    # 6. Branch processing based on situations
    if audit_result['risk_level'] == "HIGH":
        console.print(Panel(
            f"[bold red] CRITICAL WARNING[/]\nReason: {audit_result['warning_message']}",
            title="Security Audit Failed", border_style="red"
        ))
        if not Confirm.ask("[bold red]Do you really want to execute this DANGEROUS command?[/]"):
            console.print("Execution cancelled.")
            return
            
    elif audit_result['risk_level'] == "MEDIUM":
        console.print(f"[yellow] Warning: {audit_result['warning_message']}[/]")
        if not Confirm.ask("Proceed?"):
            return
            
    else:
        console.print("[bold green] Security Audit Passed (Safe)[/]")

    # 7. final execution
    console.print(f"\n[dim]Executing: {command_to_run}...[/]")
    os.system(command_to_run)

if __name__ == "__main__":
    main()