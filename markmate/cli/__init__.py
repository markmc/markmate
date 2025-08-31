import typer
from markmate.cli import course, mark, pdf


app = typer.Typer()
app.add_typer(course.app, name="course")
app.add_typer(mark.app, name="mark")
app.add_typer(pdf.app, name="pdf")


def main():
    app()


if __name__ == "__main__":
    main()
