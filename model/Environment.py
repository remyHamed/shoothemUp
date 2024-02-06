from typing import List
import pygame
from Enumerator.Status import Status
from model import Ennemy, Player
from model.Wave import Wave
from model.Bullet import Bullet
import sys
from model.Pad import Pad

class Environment:
    def __init__(self, window_hight, window_width):
        self._window_hight = window_hight
        self._window_width = window_width
        self._window = pygame.display.set_mode((self._window_hight, self._window_width))
        pygame.display.set_caption('Shoot Them Up')
        self._background = pygame.image.load('./assset/background/background.png')
        self._background = pygame.transform.scale(self._background, (window_width, window_hight))
        self._bullets = []
        self._current_wave_index = 0
        self.current_enemi = []
    
    def setPlayer(self, player : 'Player'):
        self._player = player
        
    def setEnnemis(self, ennemis : 'Ennemy'):
        self._ennemis = ennemis
    
    def setPad(self, pad : 'Pad'):
        self._pad = pad
        
        
        
        
        
    
    def setWave(self, waves: List[Wave]):
        self._waves = waves
        self._current_wave = self._waves[self.current_wave_index]
        
    def activateWave(self):
        self._current_wave.activate()
        
    def checkWave(self):
        for ennemi in self._current_wave._ennemy:
            if ennemi.status == Status.A_live:
                return
        self.nextWave()
    
    def nextWave(self):
        self._current_wave_index += 1
        self._current_wave = self._waves[self._current_wave_index]
        
        
        


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
    
    def collision(self, bullet, ennemi):
        return bullet._x < ennemi._position[0] + ennemi._sprite.get_width() and bullet._x + bullet._sprite.get_width() > ennemi._position[0] and bullet._y < ennemi._position[1] + ennemi._sprite.get_height() and bullet._y + bullet._sprite.get_height() > ennemi._position[1]
    
    def collisionDetection(self):
        for bullet in self._bullets:
            for ennemi in self._ennemis:
                if self.collision(bullet, ennemi):
                    self.removeBullet(bullet)
                    
                    self._ennemis.remove(ennemi)
                    break
    
    def run(self):
        y_fond = 0
        Scrolling_speed = 1
        clock = pygame.time.Clock()
        target_fps = 200 
        
        running = True
        while running:
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            y_fond += Scrolling_speed
            if y_fond >= self._window_hight:
                y_fond = 0

            self.moveBullets()

            self._window.blit(self._background, (0, y_fond))
            self._window.blit(self._background, (0, y_fond - self._window_hight))
            self.collisionDetection()

            for ennemi in self._waves[self._current_wave_index]._ennemy:
                if ennemi.status == Status.A_live:
                    ennemi.patern_reader(ennemi._patern)
                self._window.blit(ennemi._sprite, ennemi._position)

            self._window.blit(self._player._sprite, self._player._position)
            self.drawBullets()

            self._pad.detectInput()

            pygame.display.update()
            clock.tick(target_fps)
            self.checkWave()
            
            

    
        pygame.quit()
        sys.exit()