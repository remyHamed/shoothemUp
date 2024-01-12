import pygame
import sys
import model.Environment

class Player:
    def __init__(self, env : 'Environment'):
        
        self._height = 50
        self._width = 50
        self._env = env
        self._position = [env._window_width // 2, env._window_hight // 2]
        self._sprite = pygame.image.load('./assset/player/ship.png')
        self._sprite = pygame.transform.scale(self._sprite, (self._width, self._height))