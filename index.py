import pygame
from Global.Constants import AGENT_FILE
from model.Agent import Agent
from model.Pad import Pad
from Enumerator.ennemy_patern import ennemy_patern
from model.Environment import Environment
from model.Wave import Wave
from model.Combo import Combo
pygame.init()

height = 960  
width = 1080

env = Environment(height, width)
agent = Agent(env)
Combo_instance = Combo()

wave = Wave(env, 5, ennemy_patern.p_1)
wave_2 = Wave(env, 5, ennemy_patern.p_2)
wave_3 = Wave(env, 5, ennemy_patern.p_3)

waves = [wave, wave_2, wave_3]

pad = Pad(agent)
env.setagent(agent)
agent.load(AGENT_FILE) 
env.setPad(pad)
env.setWave(waves)
env.setCombo(Combo_instance)
env.run()







