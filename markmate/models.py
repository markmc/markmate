from dataclasses import dataclass
from typing import List
from .enums import Shape, Color, Rounding


@dataclass
class LatLong:
    latitude: float
    longitude: float


@dataclass
class Mark:
    id: str
    name: str
    shape: Shape
    color: Color
    latlong: LatLong


@dataclass
class CourseMark:
    mark_id: str
    rounding: Rounding


@dataclass
class Course:
    id: str
    marks: List[CourseMark]
    length: float
