from enum import Enum

from constants import SPRITE_SIZE, SHIP_HIT_REWARD, ENEMY_HIT_REWARD, DEFAULT_REWARD, BULLET_SPRITE_SIZE, WIN_REWARD
from environment.ship import Ship
from environment.wave import Wave


class RadarState(Enum):
    EMPTY = 0
    ENEMY = 1
    BULLET = 2


def is_in_radar(element, radar, x_detection=50, y_detection=50):
    if (radar[0] - x_detection < element.position[0] < radar[0] + x_detection
            and radar[1] - y_detection < element.position[1] < radar[1] + y_detection):
        return True
    return False


def is_in_bullet_radar(bullet, position, radius=200):
    if (bullet.position[0] - position[0]) ** 2 + (bullet.position[1] - position[1]) ** 2 > radius ** 2:
        return -1, False

    if bullet.position[0] > position[0] and bullet.position[1] >= position[1]:
        return 0, True
    if bullet.position[0] <= position[0] and bullet.position[1] > position[1]:
        return 1, True
    if bullet.position[0] < position[0] and bullet.position[1] <= position[1]:
        return 2, True
    if bullet.position[0] >= position[0] and bullet.position[1] < position[1]:
        return 3, True

    return -1, True


def is_impact(element_1, element_2):
    if ((element_2.position[0] < element_1.position[0] < element_2.position[0] + SPRITE_SIZE
         or element_1.position[0] < element_2.position[0] < element_1.position[0] + BULLET_SPRITE_SIZE) and
            (element_2.position[1] < element_1.position[1] < element_2.position[1] + SPRITE_SIZE
             or element_1.position[1] < element_2.position[1] < element_1.position[1] + BULLET_SPRITE_SIZE)):
        return True
    return False


class Environment:
    def __init__(self, width, height):
        self._width = width
        self._height = height

        self._running = True
        self._game_over = False

        self._ship = Ship()
        self._waves = [Wave(5, self._width)]

        self._iteration = 0

    def reset(self):
        self._ship = Ship()
        self._waves = [Wave(5, self._width)]
        self._iteration += 1
        self._game_over = False

    def do(self, action):
        _reward = DEFAULT_REWARD
        self.waves[0].step()
        self.ship.do(action)
        self.update_bullets()
        if self.is_ship_and_enemy_bullet_impact():
            _reward += SHIP_HIT_REWARD
            self._game_over = True
        if self.is_ship_bullet_and_enemy_impact():
            _reward += ENEMY_HIT_REWARD

        if self.is_win_iteration():
            self._game_over = True
            _reward += WIN_REWARD
        return self.get_radar(), _reward

    def is_win_iteration(self):
        if len(self._waves[0].enemies) > 0:
            return False
        return True

    def is_ship_and_enemy_bullet_impact(self):
        for bullet in self.waves[0].bullets:
            if is_impact(bullet, self._ship):
                return True
        return False

    def is_ship_bullet_and_enemy_impact(self):
        for bullet in self._ship.bullets:
            for enemy in self._waves[0].enemies:
                if is_impact(bullet, enemy):
                    self._waves[0].enemies.remove(enemy)
                    self._ship.remove_bullet_on_hit(bullet)
                    return True
        return False

    def increment_iteration(self):
        self._iteration += 1

    @property
    def waves(self):
        return self._waves

    def update_bullets(self):
        for bullet in self._waves[0].bullets:
            bullet.move()
            if self.is_bullet_out_of_screen(bullet.position):
                self._waves[0].bullets.remove(bullet)
        for bullet in self._ship.bullets:
            bullet.move()
            if self.is_bullet_out_of_screen(bullet.position):
                self._ship.bullets.remove(bullet)

    def is_bullet_out_of_screen(self, bullet_position):
        if bullet_position[0] > self._width \
                or bullet_position[0] < 0 \
                or bullet_position[1] > self._height \
                or bullet_position[1] < 0:
            return True
        return False

    def get_radar(self):
        _radar = []
        _bullet_radar = [RadarState.EMPTY.value, RadarState.EMPTY.value, RadarState.EMPTY.value, RadarState.EMPTY.value]

        for index, radar in enumerate(self._get_radar_positions()):
            _radar.append(RadarState.EMPTY.value)
            for enemy in self._waves[0].enemies:
                if is_in_radar(enemy, radar):
                    _radar[index] = RadarState.ENEMY.value
        for bullet in self._waves[0].bullets:
            _bullet_radar_index, is_in = is_in_bullet_radar(bullet, self._ship.position)
            if is_in and _bullet_radar_index >= 0:
                _bullet_radar[_bullet_radar_index] = RadarState.BULLET.value
        return tuple(_radar + _bullet_radar)

    def _get_radar_positions(self):
        return [
            self.get_radar_unitary_position(-175, -175),
            self.get_radar_unitary_position(-250, -250),
            self.get_radar_unitary_position(-325, -325),
            self.get_radar_unitary_position(-400, -400),

            self.get_radar_unitary_position(175, -175),
            self.get_radar_unitary_position(250, -250),
            self.get_radar_unitary_position(325, -325),
            self.get_radar_unitary_position(400, -400),

            self.get_radar_unitary_position(0, -400)
        ]

    def get_radar_unitary_position(self, x, y):
        return self._ship.position[0] + x, self._ship.position[1] + y

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

    @property
    def game_over(self):
        return self._game_over

    @property
    def iteration(self):
        return self._iteration

    @property
    def radar_positions(self):
        return self._get_radar_positions()
