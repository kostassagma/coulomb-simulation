from vector import Vector
from constants import K, dt
from state import particles


class ElectricalField:
    def __init__(self, E: Vector) -> None:
        self.E = E
        particles.append(self)
