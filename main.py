import time
import math
import cmath
import numpy as np
import sys, os
import random
from string import ascii_lowercase
import pygame
from planets import Body, Color, Pos
from physics import Engine


pygame.init()
pygame.display.set_caption('Sumilation')

SIZE = HEIGHT, WIDTH = 1000, 1000
FPS = 40
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
black = 0, 0, 0
fps_stat = pygame.font.SysFont('Arial', 50)

"""
TODO: change color and size of a planed depnding on its mass
"""

def create_new_planets(n: int) -> list[Body]:
    surficies: list[Body] = []
    for _ in range(n):
        name = ''.join([random.choice(ascii_lowercase) for _ in range(10)])
        radius = 20.0
        color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        mass = random.random()
        #velocity = pygame.Vector2(random.random(), random.random())
        velocity = pygame.Vector2(0, -0.1)
        #position = pygame.Vector2(random.randrange(100, 600), random.randrange(100, 600))
        position = pygame.Vector2(200, 200)
        gravity = random.uniform(0, 1)
        acceliration=pygame.Vector2(-0.01, 0.01)
        planet = Body(
            name=name, 
            radius=radius,
            color=color, 
            mass=mass, 
            velocity=velocity, 
            position=position,
            gravity=gravity,
            acceliration=acceliration
        )
        surficies.append(planet)
    return surficies 

SUN = Body(
    name='SUN', 
    radius=33.0,
    color=Color(255,255,0), 
    mass=10, 
    velocity=pygame.Vector2(0, 0), 
    position=pygame.Vector2(HEIGHT / 2, WIDTH / 2),
    gravity=0.01,
    acceliration=pygame.Vector2(0, 0)
)

def main():
    planets = create_new_planets(1)
    engine = Engine()
    point = pygame.Surface((50, 50))
    point.fill((255,255,255))
    while True:
        screen.fill(black)
        mouse_pos = pygame.mouse.get_pos()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #center = pygame.Vector2(HEIGHT / 2, WIDTH / 2) 
        pygame.draw.circle(screen, SUN.color, SUN.position, SUN.radius)
        for p in planets:
            delta:pygame.Vector2 = pygame.Vector2(SUN.position - p.position)
            angle_to_cursor = math.atan2(delta.y, delta.x)
            angle = pygame.Vector2(10*math.cos(angle_to_cursor), 10*math.sin(angle_to_cursor))
            engine.update_planet(p, SUN)
            pygame.draw.circle(screen, p.color, p.position, p.radius)
            pygame.draw.line(screen, (255,0,0),p.position, p.velocity + angle * 5, 2)
            #pygame.draw.line(screen, (255,255,0),p.position, p.position + p.velocity + angle.xy * 2, 2)














        #atangent = math.atan2(mouse_pos[1] - p[1], mouse_pos[0] - mouse_pos[0])
        #print(atangent.real)
        #print(cmath.atan(angle_to_cursor))

        #print(p[0] + WIDTH / 2 - mouse_pos[0], p[1] + HEIGHT / 2 - mouse_pos[1])
        #screen.blit(point, (WIDTH / 2, p[1] + HEIGHT / 2))
        #for p in path:
        #    pygame.draw.circle(screen, (255,255,255), (p[0] + WIDTH / 2, p[1] + HEIGHT / 2), 2)
        #for planet in planets:
        #    pygame.draw.circle(screen, planet.color, planet.position, planet.radius)
        #engine.update_planets(planets)
        clock.tick(FPS)
        pygame.display.flip()



if __name__ == '__main__':
    #surficies: list[Body] = create_new_planets(8)
    #engine = Engine()
    #engine.update_planets(surficies)
    main()