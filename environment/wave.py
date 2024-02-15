import random
from enum import Enum

from environment.enemy import Enemy


class EnemyAction(Enum):
    SHOOT = 0
    MOVE = 1


class Wave:
    def __init__(self, quantity, width):
        self.enemy_spacing = width // (quantity + 1)
        self._enemies = []
        self._bullets = []
        self._wave_step = 0
        for i in range(quantity):
            enemy = Enemy(self.enemy_spacing * (i + 1), 10)
            self._enemies.append(enemy)

    @property
    def enemies(self):
        return self._enemies

    @property
    def bullets(self,):
        return self._bullets

    def _shoot_all(self):
        for i in self._enemies:
            bullet = i.shoot()
            self._bullets.append(bullet)

    def _move_all_enemies(self):
        for i in self._enemies:
            i.move()

    def step(self):
        my_list = [EnemyAction.SHOOT] * 10 + [EnemyAction.MOVE] * 90
        choice = random.choice(my_list)
        if choice == EnemyAction.MOVE:
            self._move_all_enemies()
        else:
            self._move_all_enemies()
            self._shoot_all()
