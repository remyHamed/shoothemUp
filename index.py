import pygame
from model.Player import Player
from model.Pad import Pad
from Enumerator.ennemy_patern import ennemy_patern
from model.Environment import Environment
from model.Wave import Wave
pygame.init()

width = 800
height = 1200  

env = Environment(height, width)
player = Player(env)

wave = Wave(env, 5, ennemy_patern.p_1)
wave_2 = Wave(env, 5, ennemy_patern.p_2)
wave_3 = Wave(env, 5, ennemy_patern.p_2)
#wave_4 = Wave(env, 5, Patern(4))
#wave_5 = Wave(env, 5, Patern(5))

waves = [wave, wave_2]

pad = Pad(player)
env.setPlayer(player) 
env.setPad(pad)
env.setWave(waves)
env.run()







