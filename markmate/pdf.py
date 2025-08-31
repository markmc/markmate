from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Image
from reportlab.lib.units import inch


def format_marks(marks, matrix, directory: Path):
    """Format the output of compute_marks() in PDF."""
    mark_ids = [m.id for m in marks]

    doc = SimpleDocTemplate(str(directory / "marks.pdf"), pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    title = Paragraph("Mark Information", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Add map image
    img = Image(str(directory / "map.png"), width=5*inch, height=3*inch)
    elements.append(img)
    elements.append(Spacer(1, 12))

    # Table 1: Coordinates
    coord_data = [["ID", "Name", "Description", "Latitude", "Longitude"]]
    for m in marks:
        coord_data.append([m.id,
                           m.name,
                           f"{m.color.value} {m.shape.value}",
                           f"{m.latlong.lat.deg} {m.latlong.lat.min}",
                           f"{m.latlong.long.deg} {m.latlong.long.min}"])

    coord_table = Table(coord_data, colWidths=[40, 120, 100, 100])
    coord_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    elements.append(Paragraph("Coordinates:", styles['Heading2']))
    elements.append(coord_table)
    elements.append(Spacer(1, 12))

    # Table 2: Distance/Bearing Matrix
    matrix_data = [ [""] + mark_ids ]
    for mark_id, row in zip(mark_ids, matrix):
        matrix_data.append([mark_id] + list(row))

    matrix_table = Table(matrix_data, colWidths=[40] + [50]*len(mark_ids))
    matrix_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),  # Small font for big table
        ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
    ]))
    elements.append(Paragraph("Bearing & Distance Matrix:", styles['Heading2']))
    elements.append(matrix_table)

    doc.build(elements)


def format_courses(table, directory: Path):
    """Format the output of compute_courses in CSV."""
    doc = SimpleDocTemplate(str(directory / "courses.pdf"), pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    title = Paragraph("Race Courses", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Create 18 rows and 4 columns for courses
    rows = 18
    cols = 4
    table_idx = 0

    # Header row
    data = [["", "1", "2", "3", "4"]]

    # Fill rows
    for r in range(rows):
        row_label = f"{r:02}"
        row_data = [row_label]
        for c in range(cols):
            row_data.append(f"{table[table_idx][1]} {table[table_idx][2]}")
            table_idx += 1
        data.append(row_data)

    # Create table
    table = Table(data) #, colWidths=[70, 300, 80])

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    elements.append(table)

    doc.build(elements)
