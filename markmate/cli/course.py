import typer
from pathlib import Path
from typing import Optional

from markmate.compute import compute_courses
from markmate.load import load_courses, load_marks
from markmate import csv
from markmate import pdf


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
    Compute course lengths from data in DIRECTORY.

    By default, output is to stdout, but --format=pdf or --format=csv
    is also supported.
    """
    if not directory.exists():
        typer.echo(f"Error: Directory {directory} does not exist.")
        raise typer.Exit(code=1)

    typer.echo(f"Computing course lengths from {directory}...")

    courses = load_courses(directory)
    marks = load_marks(directory)

    table = compute_courses(courses, marks)

    if format == "pdf":
        pdf.format_courses(table, directory)
    elif format == "csv":
        csv.format_courses(table, directory)
    else:
        print(table)
