import typer

app = typer.Typer()


@app.command("generate")
def generate_pdf():
    """
    Generate a PDF showing courses and marks.
    """
    typer.echo("Generating PDF...")
