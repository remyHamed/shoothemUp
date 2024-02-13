import pygame

from environment.environment import Environment
from ui import Ui
from constants import WIDTH, HEIGHT

if __name__ == '__main__':
    pygame.init()

    env = Environment(WIDTH, HEIGHT)
    ui = Ui(env)

    while env.running:
        env.do()
        ui.render()





