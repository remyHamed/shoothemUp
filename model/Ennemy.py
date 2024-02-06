import random
import time
import pygame
from model import Environment
from model.Bullet import Bullet

class Ennemy:
    def __init__(self, env : 'Environment'):
        
        self._height = 50
        self._width = 50
        self._env = env
        self._position = [env._window_width // 2, env._window_hight // 2]
        self._sprite = pygame.image.load('./assset\enemiSprites\ennemy.png')
        self._sprite = pygame.transform.scale(self._sprite, (self._width, self._height))
        
    def shoot(self):
        time.sleep(3);
        bullet = Bullet(self._position[0] + 15, self._position[1], -1, 10, 10, self)
        self._env.addBullet(bullet)
        
    def patern_reader(self, patern):
        if patern == 1:
            self.patern_1()
        elif patern == 2:
            self.patern_2()
        elif patern == 3:
            self.patern_3()
        elif patern == 4:
            self.patern_4()
        elif patern == 5:
            self.patern_5()
        
    
    def trajectory(self):
        self._position[1] = self._position[1] + 0.2
        if self._position[1] > self._env._window_hight:
            self._position[1] = 0
            self._position[0] = self._env._window_width * random.random()
            
    def goDown(self):
        self._position[1] = self._position[1] + 2
        if self._position[1] > self._env._window_hight:
            self._position[1] = 0
            self._position[0] = self._env._window_width * random.random()
            
    def goUp(self):
        self._position[1] = self._position[1] - 2
        if self._position[1] < 0:
            self._position[1] = self._env._window_hight
            self._position[0] = self._env._window_width * random.random()
            
    def goRight(self):
        self._position[0] = self._position[0] + 2
        if self._position[0] > self._env._window_width:
            self._position[0] = 0
            self._position[1] = self._env._window_hight * random.random()
            
    
    def goLeft(self):
        self._position[0] = self._position[0] - 2
        if self._position[0] < 0:
            self._position[0] = self._env._window_width
            self._position[1] = self._env._window_hight * random.random()
            
    def goDownRight(self):
        self._position[0] = self._position[0] + 2
        self._position[1] = self._position[1] + 2
        if self._position[0] > self._env._window_width:
            self._position[0] = 0
        if self._position[1] > self._env._window_hight:
            self._position[1] = 0
    
    def goDownLeft(self):
        self._position[0] = self._position[0] - 2
        self._position[1] = self._position[1] + 2
        if self._position[0] < 0:
            self._position[0] = self._env._window_width
        if self._position[1] > self._env._window_hight:
            self._position[1] = 0
    
    def goUpRight(self):
        self._position[0] = self._position[0] + 2
        self._position[1] = self._position[1] - 2
        if self._position[0] > self._env._window_width:
            self._position[0] = 0
        if self._position[1] < 0:
            self._position[1] = self._env._window_hight
    
    def goUpLeft(self):
        self._position[0] = self._position[0] - 2
        self._position[1] = self._position[1] - 2
        if self._position[0] < 0:
            self._position[0] = self._env._window_width
        if self._position[1] < 0:
            self._position[1] = self._env._window_hight
    
    def leave_secreen(self):
        if self._position[0] > self._env._window_width or self._position[0] < 0 or self._position[1] > self._env._window_hight or self._position[1] < 0:
            return True
        return False

    def patern_1(self):

    # 1. Déplacer vers le bas
        self.goDown()
    # 2. Tirer*
        self.shoot()
    # 3. Répéter 1-2 trois fois
        for i in range(3):
            self.goDown()
            self.shoot()
        self.leave_secreen()
    

        
    def patern_2(self):
        #1. Déplacer vers le bas
        self.goDown()
        #2. Tirer
        self.shoot()
        #3. Déplacer vers la gauche*
        self.goLeft()
        #4. Tirer
        self.shoot()
        #5. Répéter 1-4 deux fois
        self.goDown()
        
            