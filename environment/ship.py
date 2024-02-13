import random
from enum import Enum

from constants import WIDTH, HEIGHT, SPRITE_SIZE
from environment.bullet import BulletDirection, Bullet


class ShipDirection(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Ship:
    def __init__(self):
        self._speed = 2
        self._position = [WIDTH // 2, HEIGHT // 2]
        self._bullets = []

    # def random(self):
    #     directions = [ShipDirection.UP, ShipDirection.DOWN, ShipDirection.LEFT, ShipDirection.RIGHT]
    #     self.move(random.choice(directions))
    #     self.shoot()

    def move(self, direction):
        match direction:
            case ShipDirection.UP:
                self._position[1] = max(0, self._position[1] - self._speed)
            case ShipDirection.DOWN:
                self._position[1] = min(HEIGHT - SPRITE_SIZE, self._position[1] + self._speed)
            case ShipDirection.LEFT:
                self._position[0] = max(0, self._position[0] - self._speed)
            case ShipDirection.RIGHT:
                self._position[0] = min(WIDTH - SPRITE_SIZE, self._position[0] + self._speed)
            case _:
                print('Error: unknown direction')

    def shoot(self):
        bullet = Bullet(self._position[0] + 15, self._position[1], 16, BulletDirection.UP)
        self._bullets.append(bullet)

    @property
    def position(self):
        return self._position

    @property
    def bullets(self):
        return self._bullets
