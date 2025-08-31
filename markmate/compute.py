
import math

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
