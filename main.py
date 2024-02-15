import pygame

from matplotlib import pyplot as plt
from agent.Agent import Agent
from environment.environment import Environment
from ui import Ui
from constants import WIDTH, HEIGHT, QTABLE

if __name__ == '__main__':
    pygame.init()

    env = Environment(WIDTH, HEIGHT)
    agent = Agent(env, 0.7, 0.6)
    agent.load(QTABLE)
    # ui = Ui(env)
    try:
        while env.running:
            agent.do()
            # ui.render()
    except KeyboardInterrupt:
        plt.plot(agent.history)
        plt.show()
        agent.save(QTABLE)

    plt.plot(agent.history)
    plt.show()
    agent.save(QTABLE)





