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
    def __init__(self, *, name: str,
                radius: float,
                color: Color,
                mass: float,
                velocity: pygame.Vector2,
                position: pygame.Vector2,
                acceliration: pygame.Vector2
    ) -> None:
        self.name: str = name
        self.radius: float = radius
        self.color: Color = color
        self.mass: float = mass
        self.velocity: pygame.Vector2 = velocity
        self.position: pygame.Vector2 = position
        self.acceliration: pygame.Vector2 = acceliration 

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


if __name__ == '__main__':
    body = Body(
        name='earth',
        radius=3,
        color=Color(255,255,255),
        mass=1,
        velocity=pygame.Vector2(1, 1),
        position=pygame.Vector2(1, 1),
        acceliration=pygame.Vector2(1, 1)
        )
    print(body.__repr__())


