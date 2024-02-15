import pickle
from os.path import exists
from random import random, choice, uniform

from environment.ship import ShipAction


def arg_max(table):
    return max(table, key=table.get)


class Agent:
    def __init__(self, environment, learning_rate=0.5, discount_factor=0.5):
        self._score = None
        self.state = None
        self._environment = environment
        self._learning_rate = learning_rate
        self._discount_factor = discount_factor
        self._actions = [a.value for a in ShipAction]
        self.qtable = {}
        self.reset()
        self.add_state(self.state)
        self.history = []
        self.noise = 0

    def reset(self):
        self._score = 0
        self.state = self._environment.get_radar()

    def best_action(self):
        if random() < self.noise:
            return choice(self._actions)
        else:
            return arg_max(self.qtable[self.state])

    def add_state(self, state):
        if state not in self.qtable:
            self.qtable[state] = {}
            for action in self._actions :
                self.qtable[state][action] = uniform(-1.0, 1.0)

    def do(self):
        action = self.best_action()
        new_state, reward = self._environment.do(action)
        self._score += reward
        self.add_state(new_state)
        maxQ = max(self.qtable[new_state].values())
        delta = self._learning_rate * (
                    reward + self._discount_factor * maxQ - self.qtable[self.state][action])
        self.qtable[self.state][action] += delta
        self.state = new_state
        if self._environment.game_over:
            self._environment.increment_iteration()
            self.history.append(self._score)
            self.reset()
            self._environment.reset()

    def load(self, filename):
        if exists(filename):
            with open(filename, 'rb') as file:
                self.qtable = pickle.load(file)
            self.reset()

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.qtable, file)
