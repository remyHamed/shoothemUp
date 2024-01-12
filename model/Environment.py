import pygame
from model.Player import Player
import sys

class Environment:
    def __init__(self, window_hight, window_width):
        self._window_hight = window_hight
        self._window_width = window_width
        self._window = pygame.display.set_mode((self._window_hight, self._window_width))
        pygame.display.set_caption('Shoot Them Up')
        self._background = pygame.image.load('./assset/background/background.png')
        self._background = pygame.transform.scale(self._background, (window_width, window_hight))
    
    def setPlayer(self, player : 'Player'):
        self._player = player
        
    def run(self):
        y_fond = 0
        Scrolling_speed = 1
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            y_fond += Scrolling_speed
            if y_fond >= self._window_hight:
                y_fond = 0

        
            self._window.blit(self._background, (0, y_fond))
            self._window.blit(self._background, (0, y_fond - self._window_hight))
            
            self._window.blit(self._player._sprite, self._player._position)



    
            pygame.display.update()
    
        pygame.quit()
        sys.exit()