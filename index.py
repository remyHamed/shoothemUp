import pygame
from model.Player import Player
from model.Pad import Pad
from Enumerator.ennemy_patern import ennemy_patern
from model.Environment import Environment
from model.Wave import Wave
from model.Combo import Combo
pygame.init()

height = 960  
width = 1080

env = Environment(height, width)
player = Player(env)
Combo_instance = Combo()

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
env.setCombo(Combo_instance)
env.run()







