from constants import HEIGHT


class Bullet:
    def __init__(self, x, y, speed):
        self._position = [x, y]
        self._speed = speed
        #self._direction = direction

    def move(self):
        self._position[1] += self._speed

    @property
    def position(self):
        return self._position
