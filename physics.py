import math
import random
from typing import NamedTuple

from numpy import angle
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

#class Vector:
#    def __init__(self, *, x: float, y: float) -> None:
#        self.x = x
#        self.y = y
#    
#
#    def sqrt_distance_to(self, p2: Vector):
#        return self.x + p2.x, self.y, p2.y




class Engine:
    def __init__(self) -> None:
        pass

    def normalize_verctor(self, vector: pygame.Vector2):
        pass

    def calculate_physics(self, planet: Body, planet2: Body) -> Body:
        pass

    def update_planet(self, planet: Body, sun: Body) -> Body:
        delta = pygame.Vector2(sun.position - planet.position)
        angle_to_planet = math.atan2(delta.y, delta.x)
        angle_vector = pygame.Vector2(math.cos(angle_to_planet), math.sin(angle_to_planet))
        # calculating gravity vector
        gravity_vector = pygame.Vector2(math.cos(planet.position.x) * sun.mass / dist, sun.mass / delta.y ** 2)

        print(gravity_vector)
        
        # fianl update to planets position
        planet.position.xy += planet.velocity.xy        



        return planet
