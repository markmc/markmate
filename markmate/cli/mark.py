import typer
from pathlib import Path

from markmate.compute import compute_marks
from markmate.load import load_marks


app = typer.Typer()


@app.command("list")
def list(directory: Path):
    """
    List all marks from data in DIRECTORY.
    """
    if not directory.exists():
        typer.echo(f"Error: Directory {directory} does not exist.")
        raise typer.Exit(code=1)

    typer.echo(f"Listing marks from {directory}...")

    marks = load_marks(directory)

    for m in marks:
        print(f"{m.id}")


@app.command("compute")
def compute(directory: Path):
    """
    List all marks from data in DIRECTORY.
    """
    if not directory.exists():
        typer.echo(f"Error: Directory {directory} does not exist.")
        raise typer.Exit(code=1)

    typer.echo(f"Computing mark distances and bearings from {directory}...")

    marks = load_marks(directory)

    table = compute_marks(marks)

    print(table)
