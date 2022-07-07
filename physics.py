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

    def update_planet(self, planet: Body, look: pygame.Vector2, sun: Body) -> Body:
        look = look.normalize().xy + planet.velocity.xy
        print(f'{planet.velocity}, {look}')
        planet.position.xy = pygame.Vector2(planet.position.xy + planet.velocity.xy + look.xy)









        return planet
