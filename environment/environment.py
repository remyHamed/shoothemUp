from constants import SPRITE_SIZE
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

    def reset(self):
        self._ship = Ship()
        self._waves = [Wave(5, self._width)]
        self._iteration += 1
        self._game_over = False

    def do(self):
        self._iteration += 1
        self.waves[0].step()
        self.ship.random()
        self.update_bullets()
        if self.is_ship_and_enemy_bullet_impact():
            self._game_over = True
            self.reset()
        if self.is_ship_bullet_and_enemy_impact():
            print("enemy touched")

        if self.is_win_iteration():
            self._game_over = True
            self.reset()

    def is_win_iteration(self):
        if len(self._waves[0].enemies) > 0 and self._game_over is False:
            return False
        return True

    def is_ship_and_enemy_bullet_impact(self):
        for enemy in self.waves[0].enemies:
            for bullet in enemy.bullets:
                if self.is_impact(bullet, self._ship):
                    return True
        return False

    def is_ship_bullet_and_enemy_impact(self):
        for bullet in self._ship.bullets:
            for enemy in self._waves[0].enemies:
                if self.is_impact(bullet, enemy):
                    self._waves[0].enemies.remove(enemy)
                    return True
        return False

    @property
    def waves(self):
        return self._waves

    def update_bullets(self):
        for enemy in self._waves[0].enemies:
            for bullet in enemy.bullets:
                bullet.move()
                if self.is_bullet_out_of_screen(bullet.position):
                    enemy.bullets.remove(bullet)
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

    def is_impact(self, element_1, element_2):
        if element_2.position[0] < element_1.position[0] < element_2.position[0] + SPRITE_SIZE:
            if element_2.position[1] < element_1.position[1] < element_2.position[1] + SPRITE_SIZE:
                return True
        return False

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
