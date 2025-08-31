from enum import Enum


class Shape(str, Enum):
    CONICAL = "Conical"
    IALA = "IALA"
    CHERRY = "Cherry"


class Color(str, Enum):
    BLACK = "Black"
    ORANGE = "Orange"
    YELLOW = "Yellow"
    GREEN = "Green"


class Rounding(str, Enum):
    PORT = "Port"
    STARBOARD = "Starboard"
