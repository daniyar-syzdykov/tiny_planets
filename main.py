import math
import sys
import random
import pygame
from string import ascii_letters
from planets import Body, Color
from physics import Engine


pygame.init()
pygame.display.set_caption('Sumilation')

LAPTOP = False

SIZE = HEIGHT, WIDTH = (1000, 1000) if not LAPTOP else (800,800)
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
        name = ''.join([random.choice(ascii_letters) for _ in range(10)])
        radius = 15.0
        color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        #mass = random.uniform(1, 10)
        mass = 0.05
        #velocity = pygame.Vector2(random.uniform(-3, 3), random.uniform(-3, 3))
        velocity = pygame.Vector2(0, 5)
        #position = pygame.Vector2(random.randrange(100, 600), random.randrange(100, 600))
        position = pygame.Vector2(900, HEIGHT / 2)
        acceliration=pygame.Vector2(0, 0)
        planet = Body(
            name=name, 
            radius=radius,
            mass=mass, 
            color=color, 
            velocity=velocity, 
            position=position,
            acceliration=acceliration
        )
        surficies.append(planet)
    return surficies 

SUN = Body(
    name='SUN', 
    radius=33.0,
    color=Color(255,255,0), 
    mass=19890, 
    velocity=pygame.Vector2(0, 0), 
    position=pygame.Vector2(HEIGHT / 2, WIDTH / 2),
    acceliration=pygame.Vector2(0, 0)
)

MOON = Body(
    name='MOON', 
    radius=5.0,
    color=Color(80,80,80), 
    mass=0.00007342, 
    velocity=pygame.Vector2(0, 5), 
    position=pygame.Vector2(900, WIDTH / 2),
    acceliration=pygame.Vector2(0, 0)
)

def main():
    planets = create_new_planets(1)
    planets.append(SUN)
    engine = Engine()
    while True:
        screen.fill(black)
        mouse_pos = pygame.mouse.get_pos()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.circle(screen, SUN.color, SUN.position, SUN.radius)
        for p in planets:
            delta:pygame.Vector2 = pygame.Vector2(SUN.position - p.position)
            angle_to_cursor = math.atan2(delta.y, delta.x)
            angle = pygame.Vector2(math.cos(angle_to_cursor), math.sin(angle_to_cursor))
            pygame.draw.circle(screen, p.color, p.position, p.radius)
            pygame.draw.line(screen, (255,0,0),p.position, p.position + angle * 20, 3)
            pygame.draw.line(screen, (255,255,0),p.position, p.position + p.velocity * 10, 1)
        engine.update_planet(planets)
        clock.tick(FPS)
        pygame.display.flip()



if __name__ == '__main__':
    main()