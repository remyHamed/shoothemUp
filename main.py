import pygame
from matplotlib import pyplot as plt

from agent.agent import Agent
from constants import WIDTH, HEIGHT, QTABLE
from environment.environment import Environment
from ui import Ui

if __name__ == '__main__':
    pygame.init()

    env = Environment(WIDTH, HEIGHT)
    agent = Agent(env, 0.7, 0.7)
    agent.load(QTABLE)
    ui = Ui(env)
    try:
        while env.running:
            agent.do()
            ui.render()
    except KeyboardInterrupt:
        pass

    plt.plot(agent.history)
    plt.show()
    agent.save(QTABLE)
