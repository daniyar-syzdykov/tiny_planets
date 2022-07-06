import random
from typing import NamedTuple
from planets import Body, Color, Pos


class Vector(NamedTuple):
    x: float
    y: float


class Engine:
    def __init__(self) -> None:
        pass

    def normalize_verctor(self, vector: Vector):
        pass

    def calculate_physics(self, planet: Body, planet2: Body) -> Body:
        pass

    def update_planets(self, planets: list[Body]) -> list[Body]:
        for planet in planets:
            for forces in planets:
                self.calculate_physics(planet, forces)
        return planets
