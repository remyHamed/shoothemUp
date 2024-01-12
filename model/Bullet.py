import pygame

class Bullet:
    def __init__(self, x, y, direction, speed, damage, owner):
        self._x = x
        self._y = y
        self._direction = direction
        self._speed = speed
        self._damage = damage
        self._owner = owner
        self._sprite = pygame.image.load('./assset/bullet/bullet2.png')
    
    def move(self):
        self._y += self._speed * self._direction
    