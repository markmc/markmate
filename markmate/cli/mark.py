import typer
from pathlib import Path
from typing import Optional

from markmate.compute import compute_marks
from markmate.load import load_marks
from markmate import csv
from markmate import pdf


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
def compute(directory: Path,
            format: Optional[str] = typer.Option(
                None,
                "--format",
                help="Output format: pdf or csv",
                case_sensitive=False,
                show_choices=True,
                metavar="pdf|csv",
            )):
    """
    Compute distances and bearings between marks from data in DIRECTORY.

    By default, output is to stdout, but --format=pdf or --format=csv
    is also supported.
    """
    if not directory.exists():
        typer.echo(f"Error: Directory {directory} does not exist.")
        raise typer.Exit(code=1)

    typer.echo(f"Computing mark distances and bearings from {directory}...")

    marks = load_marks(directory)

    matrix = compute_marks(marks)

    if format == "pdf":
        pdf.format_marks(marks, matrix)
    elif format == "csv":
        csv.format_marks(marks, matrix)
    else:
        print(table)
