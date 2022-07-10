import math
from planets import Body
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


class Engine:
    def __init__(self) -> None:
        pass

    def update_planet(self, planets: list[Body]) -> list[Body]:
        for a in range(len(planets)):
            position_angle = math.atan2(planets[a].position.y, planets[a].position.x)
            for b in range(len(planets)):
                if b == a:
                    continue
                angle_to = math.atan2(planets[b].position.y - planets[a].position.y, planets[b].position.x - planets[a].position.x)
                gravity_vector = pygame.Vector2(
                                math.cos(position_angle) * planets[b].mass / planets[a].position.distance_squared_to(planets[b].position),
                                math.sin(position_angle) * planets[b].mass / planets[a].position.distance_squared_to(planets[b].position))
                gravity_vector.xy = pygame.Vector2(
                                    math.cos(angle_to) * gravity_vector.magnitude(),
                                    math.sin(angle_to) * gravity_vector.magnitude()).xy
                planets[a].velocity.xy += gravity_vector.xy
            planets[a].position.xy += planets[a].velocity.xy        
        return planets
