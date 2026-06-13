from rich.console import Console

console = Console()

def banner():

    console.print(
        "\n[bold green]LifeBot - Agentic Wearable Intelligence OS[/bold green]\n"
    )

def print_response(response):
    console.print(
        f"\n[bold cyan]LifeBot:[/bold cyan] {response}\n")