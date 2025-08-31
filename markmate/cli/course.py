import typer
from pathlib import Path

from markmate.load import load_courses


app = typer.Typer()


@app.command("list")
def list_courses(directory: Path):
    """List all courses from data in DIRECTORY."""
    if not directory.exists():
        typer.echo(f"Error: Directory {directory} does not exist.")
        raise typer.Exit(code=1)

    typer.echo(f"Listing marks from {directory}...")

    courses = load_courses(directory)

    for c in courses:
        print(f"{c.id}")
