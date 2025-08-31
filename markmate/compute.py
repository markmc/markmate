
import math

from markmate.enums import Rounding
from markmate.models import LatLong


# Magnetic variation (negative = west)
MAG_VARIATION = -2.0


def to_radians(deg):
    return deg * math.pi / 180.0


# Haversine distance in NM
def haversine_distance(a: LatLong, b: LatLong):
    (a_lat, a_long) = a.to_decimal()
    (b_lat, b_long) = b.to_decimal()
    R = 3440.065  # Nautical miles
    dlat = to_radians(b_lat - a_lat)
    dlon = to_radians(b_long - a_long)
    a = math.sin(dlat / 2)**2 + math.cos(to_radians(a_lat)) * math.cos(to_radians(b_lat)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


# Bearing (true) between two positions
def bearing(a: LatLong, b: LatLong):
    (a_lat, a_long) = a.to_decimal()
    (b_lat, b_long) = b.to_decimal()
    a_lat_rad = to_radians(a_lat)
    b_lat_rad = to_radians(b_lat)
    dlon_rad = to_radians(b_long - a_long)
    x = math.sin(dlon_rad) * math.cos(b_lat_rad)
    y = math.cos(a_lat_rad) * math.sin(b_lat_rad) - math.sin(a_lat_rad) * math.cos(b_lat_rad) * math.cos(dlon_rad)
    bearing = math.degrees(math.atan2(x, y))
    return (bearing + 360) % 360


# Apply magnetic variation
def magnetic_bearing(true_bearing):
    mag_brng = true_bearing + MAG_VARIATION
    if mag_brng < 0:
        mag_brng += 360
    elif mag_brng >= 360:
        mag_brng -= 360
    return mag_brng



def compute_marks(marks):
    """Compute the distance and bearing between every pair of marks."""

    ids = [m.id for m in marks]
    table = []

    for m1 in marks:
        row = []
        for m2 in marks:
            if m1 == m2:
                row.append("—")
                continue
            dist = haversine_distance(m1.latlong, m2.latlong)
            true_brng = bearing(m1.latlong, m2.latlong)
            mag_brng = magnetic_bearing(true_brng)
            row.append(f"{mag_brng:.0f}° / {dist:.2f}")
        table.append(row)

    return table


def compute_courses(courses, marks):
    """Compute course lengths."""
    table = []

    mark_dict = {}
    for m in marks:
        mark_dict[m.id] = m

    for course in courses:
        # course ID encodes TWA - e.g. 032 means TWA=40
        wind_angle = (int(course.id[:2]) * 10) + 10

        mark_seq = []
        for m in course.marks:
            if m.id == "Z":
                continue # Ignore Z mark, all courses include it
            if m.id not in mark_dict:
                raise Exception(f"Unknown mark {m.id}")
            mark_seq.append((mark_dict[m.id], m.rounding))

        mark_seq_str = "Z"

        total_distance = 0.0
        for i in range(len(mark_seq) - 1):
            m1, m2 = mark_seq[i][0], mark_seq[i+1][0]

            dist = haversine_distance(m1.latlong, m2.latlong)
            brng = bearing(m1.latlong, m2.latlong)

            suffix = prefix = ""

            # Starboard rounding
            if mark_seq[i][1] == Rounding.STARBOARD:
                prefix += "↫"

            # Add 50% for upwind legs
            angle_diff = abs((wind_angle - brng + 180) % 360 - 180)
            if angle_diff <= 37:
                dist *= 1.5
                suffix += "↑"

            mark_seq_str += f" {prefix}{m1.id}{suffix}"

            total_distance += dist

        # Final mark
        prefix = ""
        if mark_seq[i+1][1] == Rounding.STARBOARD:
            prefix += "↫"
        mark_seq_str += f" {prefix}{mark_seq[i+1][0].id}"

        # Add extra legs - first beat, second leg, and final beat
        total_distance += (0.5*1.5) + 0.3 + (0.3*1.5)
        total_distance = round(total_distance, 2)

        table.append([
            course.id,
            mark_seq_str,
            total_distance,
        ])

    return table
