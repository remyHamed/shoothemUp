from constants import WIDTH, HEIGHT, SPRITE_SIZE


class Ship:
    def __init__(self):
        self._speed = 2
        self._position = [WIDTH // 2, HEIGHT // 2]

    def move(self, direction):
        if direction == 'left':
            self._position[0] = max(0, self._position[0] - self._speed)
        elif direction == 'right':
            self._position[0] = min(WIDTH - SPRITE_SIZE, self._position[0] + self._speed)
        elif direction == 'up':
            self._position[1] = max(0, self._position[1] - self._speed)
        elif direction == 'down':
            self._position[1] = min(HEIGHT - SPRITE_SIZE, self._position[1] + self._speed)
        elif direction == '':
            self._position = self._position
        else:
            print('Error: unknown direction')

    @property
    def position(self):
        return self._position

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
