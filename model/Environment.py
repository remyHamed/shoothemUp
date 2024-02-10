
from typing import List
import pygame
from Enumerator.Status import Status
from Enumerator.ennemy_patern import ennemy_patern
from devtool.Logger import Logger
from model import Ennemy, Player
from model.Wave import Wave
from model.Bullet import Bullet
from model.Combo import Combo
import sys
from model.Pad import Pad

class Environment:
    def __init__(self, window_hight, window_width):
        self._window_hight = window_hight
        self._window_width = window_width
        self._window = pygame.display.set_mode((self._window_width, self._window_hight))
        pygame.display.set_caption('Shoot Them Up')
        self._background = pygame.image.load('./assset/background/background.png')
        self._background = pygame.transform.scale(self._background, (window_width, window_hight))
        self._running = True
        
        self.combo_bonus = 0
        
        self.game_over = False
        
        self._bullets = []
        self._ennemis_bullets = []
        self._current_wave_index = 0
        self.current_enemi = []
        
    
    def setPlayer(self, player : 'Player'):
        self._player = player
        
    def setEnnemis(self, ennemis : 'Ennemy'):
        self._ennemis = ennemis
    
    def setPad(self, pad : 'Pad'):
        self._pad = pad
    
    def setCombo(self, combo_bonus : 'Combo'):
        self.combo_bonus = combo_bonus
        
        
    
    def setWave(self, waves: List[Wave]):
        self._waves = waves
        self._current_wave = self._waves[self._current_wave_index]
        self._current_wave.activate()
        
    def activateWave(self):
        self._current_wave.activate()
        
    def checkWave(self):
        for ennemi in self._current_wave._ennemy:
            if ennemi.status == Status.A_live:
                return
        self._current_wave_index += 1
        self.nextWave()
    
    def nextWave(self):
        if(self._current_wave_index >= len(self._waves)):
            self.game_over = True
            return
        else:

            self._current_wave = self._waves[self._current_wave_index]
            self._current_wave.activate()
            return
        
        


    def addBullet(self, bullet : 'Bullet'):
        self._bullets.append(bullet)
    
    def removeBullet(self, bullet : 'Bullet'):
        self._bullets.remove(bullet)
    
    def moveBullets(self):
        for bullet in self._bullets:
            bullet.move()
            if bullet._y < 0 or bullet._y > self._window_hight:
                self.removeBullet(bullet)
                
                
    def add_ennemy_bullet(self, bullet : 'Bullet'):
        self._ennemis_bullets.append(bullet)
    
    def remove_ennemy_bullet(self, bullet : 'Bullet'):
        self._ennemis_bullets.remove(bullet)
    
    
    def move_ennemy_bullets(self):
        for bullet in self._ennemis_bullets:
            bullet.move()
            if bullet._y < 0 or bullet._y > self._window_hight:
                self.remove_ennemy_bullet(bullet)
    
    def drawBullets(self):
        for bullet in self._bullets:
            self._window.blit(bullet._sprite, (bullet._x, bullet._y))
    
    def draw_ennemy_bullets(self):
        for bullet in self._ennemis_bullets:
            self._window.blit(bullet._sprite, (bullet._x, bullet._y))
    
    def collision(self, bullet, ennemi):
        if bullet._x > ennemi._position[0] and bullet._x < ennemi._position[0] + ennemi._sprite.get_width():
            if bullet._y > ennemi._position[1] and bullet._y < ennemi._position[1] + ennemi._sprite.get_height():
                return True
        return False

    def collisionPlayer(self, bullet, player):
        if bullet._x > player._position[0] and bullet._x < player._position[0] + player._sprite.get_width():
            if bullet._y > player._position[1] and bullet._y < player._position[1] + player._sprite.get_height():
                return True
        return False
       
    def collisionDetection(self):
        for bullet in self._bullets:
            for ennemi in self._waves[self._current_wave_index]._ennemy:
                if self.collision(bullet, ennemi):
                    self.removeBullet(bullet)
                    ennemi.status = Status.Dead
                    self._player._score += 10 + self.combo_bonus.kill_update()
                    self._waves[self._current_wave_index]._ennemy.remove(ennemi)
                    
                    
        for bullet in self._ennemis_bullets:
            if self.collisionPlayer(bullet, self._player):
                self.remove_ennemy_bullet(bullet)
                self.game_over = True
                print("Game Over")
                return
            
    def reset(self):
        
        self.game_over = False
        self._bullets = []
        self._ennemis_bullets = []
        self._current_wave_index = 0
        self.current_enemi = []
        self._player._score = 0
        self._player._life = 3
        self._player._position = [self._window_width // 2, self._window_hight // 2]
        self.combo_bonus._index = 0 
        
        wave = Wave(self, 5, ennemy_patern.p_1)
        wave_2 = Wave(self, 5, ennemy_patern.p_2)
        wave_3 = Wave(self, 5, ennemy_patern.p_3)
        waves = [wave, wave_2, wave_3]
        
        self.setWave(waves)
        
        for wave in self._waves:
            for ennemi in wave._ennemy:
                ennemi.status = Status.Stand_by
                
        
        self._player._position = [self._window_width // 2, self._window_hight // 2]
        self._current_wave.activate()
        
        
            
        
    
    def run(self):
        y_fond = 0
        Scrolling_speed = 1
        clock = pygame.time.Clock()
        target_fps = 200 

        while self._running:
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            y_fond += Scrolling_speed
            if y_fond >= self._window_hight:
                y_fond = 0
            
            self._window.blit(self._background, (0, y_fond))
            self._window.blit(self._background, (0, y_fond - self._window_hight))
                
            if self.game_over == True:
                
                sprite_game_over = pygame.image.load('./assset/game_over/g_m.png')
                sprite_game_over = pygame.transform.scale(sprite_game_over, (300, 300))
                self._window.blit(sprite_game_over, (340, 280))
                
                sprit_continue_or_quit = pygame.image.load('./assset/game_over/continue_or_quit.png')
                self._window.blit(sprit_continue_or_quit, (340, 480))
                
                print("Game Over")
                print(self._player._score)
                
                self._pad.menu_input()
                
            else:

                self.moveBullets()
                self.move_ennemy_bullets()
                self.collisionDetection()

                for ennemi in self._waves[self._current_wave_index]._ennemy:
                    if ennemi.status == Status.A_live:
                        ennemi.patern_reader(ennemi._patern)
                        self._window.blit(ennemi._sprite, ennemi._position)

                self._window.blit(self._player._sprite, self._player._position)
                self.drawBullets()
                self.draw_ennemy_bullets()

                self._pad.detectInput()

            pygame.display.update()
            clock.tick(target_fps)
            self.checkWave()
            
            

    
        pygame.quit()
        sys.exit()