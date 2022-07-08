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
        angle_to_cursor = math.atan2(delta.y, delta.x)
        angle = pygame.Vector2(10*math.cos(angle_to_cursor), 10*math.sin(angle_to_cursor))
        angle.xy = pygame.Vector2(angle.normalize().xy)
        
        #print(f'Angle: {angle.magnitude()}')
        #print(f'Angle before: {angle}')

        planet.acceliration.xy += pygame.Vector2(angle.x + (sun.gravity + delta.x), angle.y + (sun.gravity + delta.y))
        planet.acceliration = planet.acceliration.normalize()
        print(planet.acceliration.xy)

        #print(f'Acceliration: {planet.acceliration}')
        #planet.acceliration.xy = planet.acceliration.normalize().xy
        planet.velocity.xy += planet.acceliration.xy

        planet.position.xy = pygame.Vector2(planet.position.xy + angle.xy + planet.velocity)









        return planet
