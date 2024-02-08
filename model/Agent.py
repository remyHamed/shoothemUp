from random import choice
import pygame
from Global.Constants import MOVES, ACTIONS, REWARD_TAKE_DOWN
from model import Environment
from model.Bullet import Bullet

class Agent:
    def __init__(self, env : 'Environment', learning_rate = 1, discount_factor = 0.5):
        
        self._height = 50
        self._width = 50
        self._env = env
        self._position = [env._window_width // 2, env._window_hight // 2]
        self._sprite = pygame.image.load('./assset/player/ship44.png')
        self._sprite = pygame.transform.scale(self._sprite, (self._width, self._height))
        self.last_shot_time = pygame.time.get_ticks()
        self._life = 3
        self._score = 0

        self.qtable = {}
        self.add_state(self.state)
        self._learning_score = 0
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= 500:
            bullet = Bullet(self._position[0] + 15, self._position[1], -1, 10, 10, self)
            self._env.addBullet(bullet)
            self.last_shot_time = current_time
        
    def move(self, direction):
        if direction == 'left':
            self._position[0] = max(0, self._position[0] - 1)
        elif direction == 'right':
            self._position[0] = min(self._env._window_width - self._width, self._position[0] + 1)
        elif direction == 'up':
            self._position[1] = max(0, self._position[1] - 1)
        elif direction == 'down':
            self._position[1] = min(self._env._window_hight - self._height, self._position[1] + 1)
        else:
            print('Error: unknown direction')

    def does_agent_survives(self):
        self._life -= 1
        return self._life > -1
            
    def menu_input(self):
        pass

    def do(self):
        action = self.best_action()
        
        if action == 'shoot':
            self.shoot()
        else:
            self.move(action)
        
        new_state, reward = self._env.do(self._position, action)
        self._learning_score += reward

        self.add_state(new_state)
        maxQ = max(self.qtable[new_state].values())
        delta = self._learning_rate * (reward + self.discount_factor * maxQ - self.qtable[self.state][action])
        self.qtable[self.state][action] += delta
        self.state = new_state

        
    def best_action(self):
        return self.arg_max(self.qtable[self.state])

    def add_state(self, state):
        if state not in self.qtable:
            self.qtable[state] = {}
            for action in ACTIONS:
                self.qtable[state][action] = 0.0

    def arg_max(table):
        return max(table, key=table.get)

