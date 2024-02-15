from enum import Enum

from constants import SPRITE_SIZE, SHIP_HIT_REWARD, ENEMY_HIT_REWARD
from environment.wave import Wave
from environment.ship import Ship


class RadarState(Enum):
    EMPTY = 0
    ENEMY = 1
    BULLET = 2


def is_in_radar(element, radar, x_detection=50, y_detection=50):
    if (radar[0] - x_detection < element.position[0] < radar[0] + x_detection
            and radar[1] - y_detection < element.position[1] < radar[1] + y_detection):
        return True
    return False


def is_impact(element_1, element_2):
    if element_2.position[0] < element_1.position[0] < element_2.position[0] + SPRITE_SIZE:
        if element_2.position[1] < element_1.position[1] < element_2.position[1] + SPRITE_SIZE:
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
        # self._survive_turn = 0

    def reset(self):
        self._ship = Ship()
        self._waves = [Wave(5, self._width)]
        self._iteration += 1
        self._game_over = False

    def do(self, action):
        _reward = 0
        self._iteration += 1
        self.waves[0].step()
        self.ship.do(action)
        self.update_bullets()
        if self.is_ship_and_enemy_bullet_impact():
            _reward += SHIP_HIT_REWARD
            self._game_over = True
        if self.is_ship_bullet_and_enemy_impact():
            #print("reward hit ,",ENEMY_HIT_REWARD // len(self._waves[0].enemies) )
            _reward += (ENEMY_HIT_REWARD // len(self._waves[0].enemies))

        if self.is_win_iteration():
            self._game_over = True
        return self.get_radar(), _reward

    def is_win_iteration(self):
        if len(self._waves[0].enemies) > 0 and self._game_over is False:
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

        for index, radar in enumerate(self._get_radar_positions()):
            _radar.append(RadarState.EMPTY.value)
            for enemy in self._waves[0].enemies:
                if is_in_radar(enemy, radar):
                    _radar[index] = RadarState.ENEMY.value
            for bullet in self._waves[0].bullets:
                if is_in_radar(bullet, radar):
                    _radar[index] = RadarState.BULLET.value
        return tuple(_radar)

    def _get_radar_positions(self):
        return [
            self.get_radar_unitary_position(0, -100),
            self.get_radar_unitary_position(-50, -50),
            self.get_radar_unitary_position(50, -50),
            self.get_radar_unitary_position(-100, 0),
            self.get_radar_unitary_position(100, 0),

            self.get_radar_unitary_position(0, 100),
            self.get_radar_unitary_position(-50, 50),
            self.get_radar_unitary_position(50, 50),

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
