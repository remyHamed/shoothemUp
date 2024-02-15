import pygame

from matplotlib import pyplot as plt
from agent.agent import Agent
from environment.environment import Environment
from ui import Ui
from constants import WIDTH, HEIGHT, QTABLE

if __name__ == '__main__':
    pygame.init()

    env = Environment(WIDTH, HEIGHT)
    agent = Agent(env, learning_rate=0.4, discount_factor=0.8)
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





