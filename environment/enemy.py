import random

from constants import HEIGHT
from environment.bullet import Bullet, BULLET_DIRECTIONS


class Enemy:
    def __init__(self, x, y):
        self._position = [x, y]
        self._is_alive = True
        self._bullets = []

    def move(self):
        self.down()

    def down(self):
        self.position[1] += 4
        if self.position[1] > HEIGHT:
            self.position[1] = 0

    def shoot(self):
        bullet = Bullet(self._position[0] + 15, self._position[1], 16, random.choice(BULLET_DIRECTIONS))
        self._bullets.append(bullet)

    @property
    def position(self):
        return self._position

    @property
    def is_alive(self):
        return self._is_alive

    @property
    def bullets(self):
        return self._bullets
