import pygame
from model.Bullet import Bullet
import sys

class Environment:
    def __init__(self, window_hight, window_width):
        self._window_hight = window_hight
        self._window_width = window_width
        self._window = pygame.display.set_mode((self._window_hight, self._window_width))
        pygame.display.set_caption('Shoot Them Up')
        self._background = pygame.image.load('./assset/background/background.png')
        self._background = pygame.transform.scale(self._background, (window_width, window_hight))
        self._bullets = []
    
    def setPlayer(self, player : 'Player'):
        self._player = player
        

    def addBullet(self, bullet : 'Bullet'):
        self._bullets.append(bullet)
    
    def removeBullet(self, bullet : 'Bullet'):
        self._bullets.remove(bullet)
    
    def moveBullets(self):
        for bullet in self._bullets:
            bullet.move()
            if bullet._y < 0 or bullet._y > self._window_hight:
                self.removeBullet(bullet)
    
    def drawBullets(self):
        for bullet in self._bullets:
            self._window.blit(bullet._sprite, (bullet._x, bullet._y))
        
    def run(self):
        y_fond = 0
        Scrolling_speed = 1
        
        a = 0
        
        running = True
        while running:
            if(a % 50 == 0):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                y_fond += Scrolling_speed
                if y_fond >= self._window_hight:
                    y_fond = 0
                
                if(a % 30 == 0):
                    self._player.shoot()
                    
                
                self.moveBullets()
            
                self._window.blit(self._background, (0, y_fond))
                self._window.blit(self._background, (0, y_fond - self._window_hight))
                
                self._window.blit(self._player._sprite, self._player._position)
                self.drawBullets()   


           
                pygame.display.update()
            a += 1
    
        pygame.quit()
        sys.exit()