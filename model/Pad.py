import keyboard

class Pad:
    def __init__(self, player : 'Player'):
        self._player = player
    
    def detectInput(self):
       
        if keyboard.is_pressed('left'):
            print('left')
            self._player.move('left')
        elif keyboard.is_pressed('right'):
            print('right')
            self._player.move('right')
        elif keyboard.is_pressed('up'):
            print('up')
            self._player.move('up')
        elif keyboard.is_pressed('down'):
            print('down')
            self._player.move('down')
        elif keyboard.is_pressed('space'):
            print('space')
            self._player.shoot()