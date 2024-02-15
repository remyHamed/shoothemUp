import pygame
from matplotlib import pyplot as plt

from agent.agent import Agent
from constants import WIDTH, HEIGHT, QTABLE
from environment.environment import Environment

if __name__ == '__main__':
    pygame.init()

    env = Environment(WIDTH, HEIGHT)
    agent = Agent(env, 0.1, 0.5)
    agent.load(QTABLE)
    # ui = Ui(env)
    try:
        while env.running:
            agent.do()
            # ui.render()
    except KeyboardInterrupt:
        pass

    plt.plot(agent.history)
    plt.show()
    agent.save(QTABLE)
