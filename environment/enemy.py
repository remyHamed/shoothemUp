from random import randint

from constants import HEIGHT
from environment.bullet import Bullet


class Enemy:
    def __init__(self, x, y):
        self._position = [x, y]
        self._is_alive = True
        self._bullets = []

    def move(self):
        self.down()

    def down(self):
        self.position[1] += 2
        if self.position[1] > HEIGHT:
            self.position[1] = 0

    def shoot(self):
        bullet = Bullet(self._position[0] + 25, self._position[1], 2.5, randint(1, 8))
        self._bullets.append(bullet)

    @property
    def position(self):
        return self._position

    @property
    def is_alive(self):
        return self._is_alive
