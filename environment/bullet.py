class Bullet:
    def __init__(self, x, y, speed, direction):
        self._position = [x, y]
        self._speed = speed
        self._direction = direction

    def move(self):
        self._position[1] += self._speed * self._direction


