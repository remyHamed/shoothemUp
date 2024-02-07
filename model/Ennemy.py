import random
import pygame
from Enumerator.Bullet_direction import Bullet_direction
from Enumerator.Status import Status
from Enumerator.ennemy_patern import ennemy_patern
from devtool.Logger import Logger
from model import Environment
from model.Ennemis_bullet import Ennemis_bullet



class Ennemy:
    def __init__(self, env : 'Environment'):
        
        self._height = 50
        self._width = 50
        self._env = env
        self._position = [env._window_width // 2, env._window_hight // 2]
        self._sprite = pygame.image.load('./assset\enemiSprites\ennemy.png')
        self._sprite = pygame.transform.scale(self._sprite, (self._width, self._height))
        self._patern_index = 0
        self._patern = 1
        self.status = Status.Stand_by
        self.last_shot_time = pygame.time.get_ticks()
        self.logger = Logger("Ennemy.log")

        
    def set_position(self, x, y):
        self._position = [x, y]
        
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= 3000:
            bullet = Ennemis_bullet(self._position[0] + 15, self._position[1], Bullet_direction.DOWN, 3, 10, self)
            self._env.add_ennemy_bullet(bullet)
            self.last_shot_time = current_time
        
    def patern_reader(self, ennemy_patern : ennemy_patern):
        match ennemy_patern:
            case ennemy_patern.p_1:
                self.patern_1()
            case ennemy_patern.p_2:
                self.patern_2()
            case ennemy_patern.p_3:
                self.patern_3()
            case ennemy_patern.p_4:
                self.patern_4()
            case ennemy_patern.p_5:
                self.patern_5()

        
        
    
    def trajectory(self):
        self._position[1] = self._position[1] + 0.2
        if self._position[1] > self._env._window_hight:
            self._position[1] = 0
            self._position[0] = self._env._window_width * random.random()
            
    def go_down(self):
        self._position[1] += 2  
        if self._position[1] > self._env._window_hight:
            self._position[1] = 0

            
    def goUp(self):
        self._position[1] -= 2
        if self._position[1] < 0:
            self._position[1] = self._env._window_hight

    def goRight(self):
        self._position[0] += 2
        if self._position[0] > self._env._window_width:
            self._position[0] = 0
                
    
    def goLeft(self):
        self._position[0] -= 2
        if self._position[0] < 0:
            self._position[0] = self._env._window_width

            
    def goDownRight(self):
        self._position[0] += 2
        self._position[1] += 2
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
        
        self.logger.write_log("ennemy log: patern_1()")
        
        match self._patern_index:
            case 1:
                self.go_down()
                self.logger.write_log("ennemy log: goDown() 1")
            case 2:
                self.shoot()
                self.logger.write_log("ennemy log: shoot() 2")
            case 3:
                self.go_down()
                self.logger.write_log("ennemy log: goDown() 3")
            case 4:
                self.shoot()
            case 5:
                self.go_down()
            case 6:
                self.shoot()
            case 7:
                self.leave_secreen()
        
        self._patern_index += 1
        if self._patern_index == 7:
            self._patern_index = 0

    
    def patern_2(self):
       
        match self._patern_index:
            case 1:
                self.go_down()
            case 2:
                self.shoot()
            case 3:
                self.go_down()
            case 4:
                self.shoot()
            case 5:
                self.go_down()
            case 6:
                self.shoot()
            case 7:
                self.leave_secreen()
        
        self._patern_index += 1
        if self._patern_index == 7:
            self._patern_index = 0
        
        


        
            