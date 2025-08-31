import typer
from pathlib import Path


app = typer.Typer()


@app.command("generate")
def generate_pdf(directory: Path):
    """
    Generate a PDF representation of courses and marks from data in DIRECTORY.
    """
    if not directory.exists():
        typer.echo(f"Error: Directory {directory} does not exist.")
        raise typer.Exit(code=1)

    typer.echo(f"Generating PDF using data from {directory}...")
