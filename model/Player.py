import pygame
from model.Bullet import Bullet
class Player:
    def __init__(self, env : 'Environment'):
        
        self._height = 50
        self._width = 50
        self._env = env
        self._position = [env._window_width // 2, env._window_hight // 2]
        self._sprite = pygame.image.load('./assset/player/ship44.png')
        self._sprite = pygame.transform.scale(self._sprite, (self._width, self._height))
        
    def shoot(self):
        bullet = Bullet(self._position[0] + 15, self._position[1], -1, 10, 10, self)
        self._env.addBullet(bullet)
        
    def move(self, direction):
        if direction == 'left':
            self._position[0] = max(0, self._position[0] - 1)
        elif direction == 'right':
            self._position[0] = min(self._env._window_width - self._width, self._position[0] + 1)
        elif direction == 'up':
            self._position[1] = max(0, self._position[1] - 1)
        elif direction == 'down':
            self._position[1] = min(self._env._window_hight - self._height, self._position[1] + 1)
        else:
            print('Error: unknown direction')