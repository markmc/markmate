import typer
from pathlib import Path

from markmate.compute import compute_courses
from markmate.load import load_courses, load_marks


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


@app.command("compute")
def compute(directory: Path):
    """
    Compute course lengths from data in DIRECTORY.
    """
    if not directory.exists():
        typer.echo(f"Error: Directory {directory} does not exist.")
        raise typer.Exit(code=1)

    typer.echo(f"Computing course lengths from {directory}...")

    courses = load_courses(directory)
    marks = load_marks(directory)

    table = compute_courses(courses, marks)

    print(table)
