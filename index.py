import pygame
from model.Ennemy import Ennemy
from model.Environment import Environment
from model.Player import Player
from model.Pad import Pad

pygame.init()

width = 800
height = 600  

env = Environment(height, width)
player = Player(env)
ennemis = [Ennemy(env) for i in range(10)]
pad = Pad(player)
env.setPlayer(player) 
env.setEnnemis(ennemis)
env.setPad(pad)
env.run()







