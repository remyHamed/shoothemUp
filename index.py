import pygame
from model.Environment import Environment
from model.Player import Player


pygame.init()

pygame.init()

width = 800
height = 600  

env = Environment(height, width)
player = Player(env)

env.setPlayer(player)
env.run()







