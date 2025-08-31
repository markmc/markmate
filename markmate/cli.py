import typer
from markmate import pdf


app = typer.Typer()
app.add_typer(pdf.app, name="pdf")


def main():
    app()


if __name__ == "__main__":
    main()
