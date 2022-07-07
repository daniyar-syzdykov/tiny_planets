import math
import random
from typing import NamedTuple
from planets import Body, Color, Pos
import pygame


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

    def update_planets(self, planets: list[Body], look: pygame.Vector2) -> list[Body]:
        for planet in planets:
            planet.position.xy = pygame.Vector2(planet.position.xy + look.xy)
        return planets
