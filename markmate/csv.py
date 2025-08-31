
import pandas as pd


def format_marks(marks, matrix):
    """Format the output of compute_marks() in CSV."""
    ids = [m.id for m in marks]
    df = pd.DataFrame(matrix, index=ids, columns=ids)

    output_filename = "marks_distances_bearings.csv"
    print(f"Generating {output_filename}")
    df.to_csv(output_filename)


def format_courses(table):
    """Format the output of compute_courses in CSV."""
    columns = ["Sequence", "Length"]
    ids = [r[0] for r in table]
    df = pd.DataFrame([r[1:] for r in table], columns=columns, index=ids)

    output_filename = "course_lengths.csv"
    print(f"Generating {output_filename}")
    df.to_csv(output_filename)
