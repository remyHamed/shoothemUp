import pygame

from constants import BACKGROUND_URL, SCREEN_TITLE, SHIP_SPRITE, ENEMY_SPRITE, SPRITE_SIZE, ENEMY_BULLET_SPRITE, \
    BULLET_SPRITE_SIZE, SHIP_BULLET_SPRITE, RADAR_SPRITE


def is_running():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def _enemy_sprite():
    sprite = pygame.image.load(ENEMY_SPRITE)
    sprite = pygame.transform.scale(sprite, (SPRITE_SIZE, SPRITE_SIZE))
    return sprite


def _ship_sprite():
    sprite = pygame.image.load(SHIP_SPRITE)
    sprite = pygame.transform.scale(sprite, (SPRITE_SIZE, SPRITE_SIZE))
    return sprite


def _enemy_bullet_sprite():
    sprite = pygame.image.load(ENEMY_BULLET_SPRITE)
    sprite = pygame.transform.scale(sprite, (BULLET_SPRITE_SIZE, BULLET_SPRITE_SIZE))
    return sprite


def _ship_bullet_sprite():
    sprite = pygame.image.load(SHIP_BULLET_SPRITE)
    sprite = pygame.transform.scale(sprite, (BULLET_SPRITE_SIZE, BULLET_SPRITE_SIZE))
    return sprite


def _radar_sprite():
    sprite = pygame.image.load(RADAR_SPRITE)
    sprite = pygame.transform.scale(sprite, (50, 50))
    return sprite


class Ui:
    def __init__(self, env):
        self._env = env

        self._ship_sprite = _ship_sprite()
        self._enemy_sprite = _enemy_sprite()
        self._enemy_bullet_sprite = _enemy_bullet_sprite()
        self._ship_bullet_sprite = _ship_bullet_sprite()
        self._radar_sprite = _radar_sprite()
        self._window = pygame.display.set_mode((self._env.width, self._env.height))
        pygame.display.set_caption(SCREEN_TITLE)
        self._background = pygame.image.load(BACKGROUND_URL)
        self._background = pygame.transform.scale(self._background, (self._env.width, self._env.height))
        self._background_y = 0

    def render(self):
        self._env._running = is_running()
        clock = pygame.time.Clock()
        self.display_env()
        pygame.display.update()
        clock.tick(30)

    def display_env(self):
        self.scroll_background()
        self._window.blit(self._ship_sprite, self._env.ship.position)
        self.display_radar()
        for enemy in self._env.waves[0].enemies:
            self._window.blit(self._enemy_sprite, enemy.position)
        for bullet in self._env.waves[0].bullets:
            self._window.blit(self._enemy_bullet_sprite, bullet.position)
        for bullet in self._env.ship.bullets:
            self._window.blit(self._ship_bullet_sprite, bullet.position)

    def display_radar(self):
        for position in self._env.radar_positions:
            self._window.blit(self._radar_sprite, position)

    def display_iteration_info(self):
        font = pygame.font.Font('ubuntu', 12)
        text = font.render(self._env.iteration, True, (255, 255, 255))
        rect = text.get_rect()
        rect.center(50, 50)
        self._window.blit(text, rect)

    def _background(self):
        background = pygame.image.load(BACKGROUND_URL)
        background = pygame.transform.scale(background, (self._env.width, self._env.height))
        return background

    def scroll_background(self):
        scrolling_speed = 4
        self._background_y += scrolling_speed
        if self._background_y >= self._env.height:
            self._background_y = 0
        self._window.blit(self._background, (0, self._background_y))
        self._window.blit(self._background, (0, self._background_y - self._env.height))
