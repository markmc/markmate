import json
from pathlib import Path
from markmate.models import Coordinate, Course, CourseMark, LatLong, Mark
from markmate.enums import Color, Rounding, Shape


def load_courses(directory: Path) -> list[Course]:
    """Load courses from course.json in the given directory."""

    file_path = directory / "courses.json"
    if not file_path.exists():
        raise FileNotFoundError(f"No courses.json found in {directory}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    courses = []
    for c in data:
        marks = []
        for m in c.get("marks", []):
            marks.append(CourseMark(
                id=m["id"],
                rounding=Rounding(m.get("rounding", "P"))))
        courses.append(Course(
            id=c["id"],
            marks=marks))

    return courses


def load_marks(directory: Path) -> list[Mark]:
    """Load marks from marks.json in the given directory."""

    file_path = directory / "marks.json"
    if not file_path.exists():
        raise FileNotFoundError(f"No marks.json found in {directory}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    marks = []
    for m in data:
        latlong = LatLong(
            lat=Coordinate(deg=m["lat"]["deg"], min=m["lat"]["min"]),
            long=Coordinate(deg=m["long"]["deg"], min=m["long"]["min"])
        )
        marks.append(Mark(
            id=m["id"],
            name=m["name"],
            shape=Shape(m["shape"]),
            color=Color(m["color"]),
            latlong=latlong))

    return marks
