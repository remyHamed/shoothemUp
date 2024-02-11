from os.path import exists
import pickle
from random import random, choice
import pygame
from Global.Constants import ACTIONS, BULLET, EMPTY, ENNEMY, MOVES
from model import Environment
from model.Bullet import Bullet

class Agent:
    def __init__(self, env : 'Environment', learning_rate = 0.9, discount_factor = 0.5):
        
        self._height = 50
        self._width = 50
        self._env = env
        self._sprite = pygame.image.load('./assset/player/ship44.png')
        self._sprite = pygame.transform.scale(self._sprite, (self._width, self._height))
        self._radar_sprite = pygame.image.load('./assset/radar/radar_bg.png').convert_alpha()
        self.last_shot_time = pygame.time.get_ticks()
        self._life = 3
        self._score = 0
        self._speed = 2
        self.reset()

        self.qtable = {}
        self.history = []
        self.add_state(self.state)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.noise = 0

    def reset(self):
        self.position = [self._env._window_width // 2, self._env._window_hight // 2]
        self.learning_score = 0
        self.state = self.get_radar()

        
    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= 500:
            bullet = Bullet(self.position[0] + 15, self.position[1], -1, 10, 10, self)
            self._env.addBullet(bullet)
            self.last_shot_time = current_time
        
    def move(self, direction):
        if direction == 'left':
            self.position[0] = max(0, self.position[0] - self._speed)
        elif direction == 'right':
            self.position[0] = min(self._env._window_width - self._width, self.position[0] + self._speed)
        elif direction == 'up':
            self.position[1] = max(0, self.position[1] - self._speed)
        elif direction == 'down':
            self.position[1] = min(self._env._window_hight - self._height, self.position[1] + self._speed)
        elif direction == '':
            self.position = self.position
        else:
            print('Error: unknown direction')

    def does_agent_survives(self):
        self._life -= 1
        return self._life > -1
            
    def do(self):
        action = self.best_action()
        if action == 'F':
            self.shoot()
        else:
            self.move(MOVES[action])
        
        new_state = self.get_radar()

        self.add_state(new_state)
        maxQ = max(self.qtable[new_state].values())
        delta = self.learning_rate * (self.learning_score + self.discount_factor * maxQ - self.qtable[self.state][action])
        self.qtable[self.state][action] += delta
        self.state = new_state
        
    def best_action(self):
        if (random() < self.noise):
            return choice(ACTIONS)
        else:
            return self.arg_max(self.qtable[self.state])

    def add_state(self, state):
        if state not in self.qtable:
            self.qtable[state] = {}
            for action in ACTIONS:
                self.qtable[state][action] = 0.0

    def arg_max(self, table):
        return max(table, key=table.get)

    def get_radar(self):
        _radar = []
        radar_positions = [self.get_radar_unitary_position(0, -100),
                  self.get_radar_unitary_position(-50, -50),
                  self.get_radar_unitary_position(50, -50),
                  self.get_radar_unitary_position(-100, 0),
                  self.get_radar_unitary_position(100, 0),

                  self.get_radar_unitary_position(0, 100),
                  self.get_radar_unitary_position(-50, 50),
                  self.get_radar_unitary_position(50, 50),

                  self.get_radar_unitary_position(-150, -150),
                  self.get_radar_unitary_position(-200, -200),
                  self.get_radar_unitary_position(-250, -250),

                  self.get_radar_unitary_position(150, -150),
                  self.get_radar_unitary_position(200, -200),
                  self.get_radar_unitary_position(250, -250),

                  self.get_radar_unitary_position(0, -400)]
        # for r in radar_positions:
        #     self._env._window.blit(self._radar_sprite, r)
    
        for radar in radar_positions:
            _radar.append(EMPTY)
            for ennemy in self._env.current_ennemies:
                if (self.is_object_in_radar(ennemy, radar)):
                    _radar.append(ENNEMY)
            for bullet in self._env._ennemis_bullets:
                if (self.is_object_in_radar(bullet, radar)):
                    _radar.append(BULLET)
        return tuple(_radar)
    
    def get_radar_unitary_position(self, x, y):
        return (self.position[0] + x, self.position[1] + y)
    
    def is_object_in_radar(self, object, radar, x_detection=50, y_detection=50):
        if (object.position[0] > radar[0] - x_detection 
            & object.position[0] < radar[0] + x_detection
            & object.position[1] > radar[1] - y_detection
            & object.position[1] < radar[1] + y_detection):
            return True
        return False
    
    def load(self, filename):
        if exists(filename):
            with open(filename, 'rb') as file:
                self.qtable = pickle.load(file)
            self.reset()
        
    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.qtable, file)
