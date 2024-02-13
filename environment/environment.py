from environment.wave import Wave
from environment.ship import Ship


class Environment:
    def __init__(self, width, height):
        self._width = width
        self._height = height

        self._running = True
        self._game_over = False

        self._ship = Ship()
        self._waves = [Wave(5, self._width)]

        self._iteration = 0

    def do(self):
        self._iteration += 1
        self.waves[0].step()

    @property
    def waves(self):
        return self._waves

    @property
    def ship(self):
        return self._ship

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def running(self):
        return self._running
