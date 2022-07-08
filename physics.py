import math
import random
from typing import NamedTuple
from planets import Body, Color, Pos
import pygame
"""
velosity is what we add to position
direction is where we shift volosity vector
direction calculated baesd on forces from other plants
forces from other plantes
gravity tells how much particular planet pull on curr planet 
also gravity stornger if planet is closer
mass of curr planet also effects to speed acceliration and direction of planet
"""

class Vector(NamedTuple):
    x: float
    y: float


class Engine:
    def __init__(self) -> None:
        pass

    def normalize_verctor(self, vector: pygame.Vector2):
        pass

    def calculate_physics(self, planet: Body, planet2: Body) -> Body:
        pass

    def update_planet(self, planet: Body, sun: Body) -> Body:
        delta:pygame.Vector2 = pygame.Vector2(sun.position - planet.position)
        angle_to_planet = math.atan2(delta.y, delta.x)
        direction_to_planet = pygame.Vector2(math.cos(angle_to_planet), math.cos(angle_to_planet))
        print(direction_to_planet)
        planet.position.xy += direction_to_planet.xy
        



        return planet
