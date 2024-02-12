import keyboard

from model import Agent

class Pad:
    def __init__(self, agent : 'Agent'):
        self._agent = agent
    
    def detectInput(self):
       if keyboard.is_pressed('x'):
           self._agent.noise = 1
           self._agent.reset()
        # if keyboard.is_pressed('left'):
        #     self._agent.move('left')
        # elif keyboard.is_pressed('right'):
        #     self._agent.move('right')
        # elif keyboard.is_pressed('up'):
        #     self._agent.move('up')
        # elif keyboard.is_pressed('down'):
        #     self._agent.move('down')
        # elif keyboard.is_pressed('space'):
        #     self._agent.shoot()
    
    def menu_input(self):
        if keyboard.is_pressed('q'):
            self._agent._env._running = False
        elif keyboard.is_pressed('y'):
            self._agent._env._game_over = False
            self._agent._env._running = True
            self._agent._env.reset()