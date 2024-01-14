import pygame
from model.Environment import Environment
from model.Player import Player
from model.Pad import Pad

pygame.init()

width = 800
height = 600  

env = Environment(height, width)
player = Player(env)
pad = Pad(player)
env.setPlayer(player)
env.setPad(pad)
env.run()







