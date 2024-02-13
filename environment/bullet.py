from enum import Enum


class BulletDirection(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    UP_LEFT = 5
    UP_RIGHT = 6
    DOWN_LEFT = 7
    DOWN_RIGHT = 8


BULLET_DIRECTIONS = [
    BulletDirection.UP,
    BulletDirection.DOWN,
    BulletDirection.LEFT,
    BulletDirection.RIGHT,
    BulletDirection.UP_LEFT,
    BulletDirection.UP_RIGHT,
    BulletDirection.DOWN_LEFT,
    BulletDirection.DOWN_RIGHT,
]


class Bullet:
    def __init__(self, x, y, speed, direction):
        self._position = [x, y]
        self._speed = speed
        self._direction = direction

    def move(self):
        match self._direction:
            case BulletDirection.UP:
                self._position[1] -= self._speed
            case BulletDirection.DOWN:
                self._position[1] += self._speed
            case BulletDirection.LEFT:
                self._position[0] -= self._speed
            case BulletDirection.RIGHT:
                self._position[0] += self._speed
            case BulletDirection.UP_LEFT:
                self._position[0] -= self._speed
                self._position[1] -= self._speed
            case BulletDirection.UP_RIGHT:
                self._position[0] += self._speed
                self._position[1] -= self._speed
            case BulletDirection.DOWN_LEFT:
                self._position[0] -= self._speed
                self._position[1] += self._speed
            case BulletDirection.DOWN_RIGHT:
                self._position[0] += self._speed
                self._position[1] += self._speed
            case _:
                pass

    @property
    def position(self):
        return self._position
