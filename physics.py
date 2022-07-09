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
        #angle = math.atan2(planet.position.y, planet.position.x)
        angle_to = math.atan2(sun.position.y - planet.position.y, sun.position.x - planet.position.x)
        #gravity_vector = pygame.Vector2(
        #                math.cos(angle) * sun.mass / math.sqrt(delta.x ** 2 + delta.y ** 2) ** 2,
        #                math.sin(angle) * sun.mass / math.sqrt(delta.x ** 2 + delta.y ** 2) ** 2)
        #gravity_vector.xy = (
        #                    math.cos(angle_to) * math.sqrt(gravity_vector.x ** 2 + gravity_vector.y ** 2),
        #                    math.sin(angle_to) * math.sqrt(gravity_vector.x ** 2 + gravity_vector.y ** 2))
        #print(gravity_vector)
        #planet.velocity.xy += gravity_vector.xy
        planet.position.xy += planet.velocity.xy        
        #for a in range(len(planets)):
        #    position_angle = math.atan2(planets[a].position.y, planets[a].position.x)
        #    for b in range(len(planets)):
        #        if b == a:
        #            continue
        #        delta = pygame.Vector2(planets[a].position - planets[b].position)
        #        #angle_to = math.atan2(sun.position.y - planet.position.y, sun.position.x - planet.position.x)
                





        return planet
