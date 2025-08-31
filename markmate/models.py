from dataclasses import dataclass
from typing import Optional
from .enums import Shape, Color, Rounding


@dataclass
class Coordinate:
    deg: float
    min: float

    def to_decimal(self) -> float:
        """Convert degrees and minutes to decimal degrees."""
        sign = -1 if self.deg < 0 else 1
        return sign * (abs(self.deg) + self.min / 60.0)


@dataclass
class LatLong:
    lat: Coordinate
    long: Coordinate

    def to_decimal(self) -> tuple[float, float]:
        """Return (latitude, longitude) in decimal degrees."""
        return (self.lat.to_decimal(), self.long.to_decimal())


@dataclass
class Mark:
    id: str
    name: str
    shape: Shape
    color: Color
    latlong: LatLong


@dataclass
class CourseMark:
    id: str
    rounding: Rounding


@dataclass
class Course:
    id: str
    marks: list[CourseMark]
    length: Optional[float] = None
