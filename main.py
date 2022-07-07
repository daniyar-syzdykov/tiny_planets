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

SIZE = HEIGHT, WIDTH = 800, 800
FPS = 60
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
    radius = 100
    for i in np.arange(0, 2 * cmath.pi, 0.05):
        #s_y = cmath.sin(i).real * 300
        #c_y = cmath.cos(i).real * 300
        #t_y = cmath.tan(i).real * 300
        #path.append((x, s_y, c_y))
        x = radius * cmath.cos(i).real * 1
        y = radius * cmath.sin(i).real * 1.5
        path.append((x, y)) 
    return path


def main():
    planets = create_new_planets(8)
    engine = Engine()
    point = pygame.Surface((50, 50))
    point.fill((255,255,255))
    path = create_path()
    while True:
        screen.fill(black)
        mouse_pos = pygame.mouse.get_pos()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        p = (HEIGHT / 2, WIDTH / 2) 
        angle_to_cursor = 1 / cmath.sqrt(mouse_pos[0] - p[0] / mouse_pos[1] - p[1])
        print(angle_to_cursor.real)
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