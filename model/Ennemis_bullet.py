import pygame
from Enumerator.Bullet_direction import Bullet_direction

class Ennemis_bullet:
    def __init__(self, x, y, direction, speed, damage, owner):
        self._x = x
        self._y = y
        self._position = (x, y)
        self._direction = direction
        self._speed = speed
        self._damage = damage
        self._owner = owner
        self._sprite = pygame.image.load('./assset/bullet/v_e.png')
        self._sprite = pygame.transform.scale(self._sprite, (25, 25))
    
    def move(self):
        
        match self._direction:
            case Bullet_direction.UP:
                self._y -= self._speed
            case Bullet_direction.DOWN:
                self._y += self._speed
            case Bullet_direction.LEFT:
                self._x -= self._speed
            case Bullet_direction.RIGHT:
                self._x += self._speed
            case Bullet_direction.UP_LEFT:
                self._x -= self._speed
                self._y -= self._speed
            case Bullet_direction.UP_RIGHT:
                self._x += self._speed
                self._y -= self._speed
            case Bullet_direction.DOWN_LEFT:
                self._x -= self._speed
                self._y += self._speed
            case Bullet_direction.DOWN_RIGHT:
                self._x += self._speed
                self._y += self._speed
            case _: 
                pass
    