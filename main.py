import time
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

SIZE = HEIGHT, WIDTH = 800, 800
FPS = 60
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
black = 0, 0, 0

"""
TODO: change color and size of a planed depnding on its mass
"""

def create_new_planets(n: int) -> list[Body]:
    surficies: list[Body] = []
    for _ in range(n):
        name = ''.join([random.choice(ascii_lowercase) for _ in range(10)])
        radius = 30.0
        color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        mass = random.random()
        velocity = random.random()
        position = Pos(random.randrange(100, 900), random.randrange(100, 900))
        planet = Body(
            name=name, 
            radius=radius,
            color=color, 
            mass=mass, 
            velocity=velocity, 
            position=position
        )
        surficies.append(planet)
    return surficies 

def create_path():
    path = []
    for i in np.arange(0, 4 * cmath.pi, 0.001):
        x = i * 100
        s_y = cmath.sin(i).real * 100
        c_y = cmath.cos(i).real * 100
        t_y = cmath.tan(i).real * 100
        path.append((x, s_y))
    return path


def main():
    planets = create_new_planets(8)
    engine = Engine()
    ptr = pygame.Surface((10, 10))
    ptr.fill((255,255,255))
    while True:
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(FPS)
        screen.fill(black)
        path = create_path()
        #for p in path:
        #    screen.blit(ptr, (p[0],p[1] + HEIGHT / 2))
            #pygame.draw.circle(screen, (255,255,255), (s_x - i, t_y + HEIGHT / 2), 1)
        for planet in planets:
            pygame.draw.circle(screen, planet.color, planet.position, planet.radius)
        engine.update_planets(planets)
        pygame.display.flip()



if __name__ == '__main__':
    #surficies: list[Body] = create_new_planets(8)
    #engine = Engine()
    #engine.update_planets(surficies)
    main()