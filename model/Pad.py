import keyboard

from model import Player

class Pad:
    def __init__(self, player : 'Player'):
        self._player = player
    
    def detectInput(self):
       
        if keyboard.is_pressed('left'):
            self._player.move('left')
        elif keyboard.is_pressed('right'):
            self._player.move('right')
        elif keyboard.is_pressed('up'):
            self._player.move('up')
        elif keyboard.is_pressed('down'):
            self._player.move('down')
        elif keyboard.is_pressed('space'):
            self._player.shoot()
    
    def menu_input(self):
        if keyboard.is_pressed('q'):
            self._player._env._running = False
        elif keyboard.is_pressed('y'):
            self._player._env._game_over = False
            self._player._env._running = True
            self._player._env.reset()