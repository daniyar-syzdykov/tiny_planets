import random
from string import ascii_lowercase
from typing import NamedTuple, Union
from dataclasses import dataclass
import pygame

class Pos(NamedTuple):
    x: Union[int, float]
    y: Union[int, float]


class Color(NamedTuple):
    r: int
    g: int
    b: int

@dataclass
class Body:
    GRAVITY_CONST: float = 9.8
    def __init__(self, *, name: str,
                radius: float,
                color: Color,
                mass: float,
                velocity: pygame.Vector2,
                position: pygame.Vector2,
                gravity: float,
                acceliration: pygame.Vector2
    ) -> None:
        self.name: str = name
        self.radius: float = radius
        self.color: Color = color
        self.mass: float = mass
        self.velocity: pygame.Vector2 = velocity
        self.position: pygame.Vector2 = position
        self.gravity: float = gravity
        self.acceliration: pygame.Vector2 = acceliration 

    #def create_new_planets(self, n: int) -> list:
    #    surficies: list[Body] = []
    #    for i in range(n):
    #        name = ''.join([random.choice(ascii_lowercase) for _ in range(10)])
    #        radius = 30.0
    #        #color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    #        color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    #        mass = random.random()
    #        speed = random.random()
    #        position = Pos(random.randrange(100, 900), random.randrange(100, 900))
    #        planet = Body(
    #            name=name, 
    #            radius=radius,
    #            color=color, 
    #            mass=mass, 
    #            speed=speed, 
    #            position=position
    #        )
    #        surficies.append(planet)
    #        # planet = Planet(Pos(i * 100, i * 100), Pos(1,1))
    #        # surficies.append(planet)
    #    return surficies

    # def __str__(self) -> str:
    #     return self.name
    
    # def __repr__(self) -> str:
    #     return f'{self.name}'#, {self.radius}, {self.mass}, {self.speed}'

if __name__ == '__main__':
    body = Body(
        name='earth',
        radius=3,
        color=Color(255,255,255),
        mass=1,
        velocity=pygame.Vector2(1, 1),
        position=pygame.Vector2(1, 1),
        gravity=3,
        acceliration=pygame.Vector2(1, 1)
        )
    print(body.__repr__())


