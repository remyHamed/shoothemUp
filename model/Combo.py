

import pygame


class Combo:
    def __init__(self):
        self._index = 0
        self._last_kill_time = 0
        
    def kill_update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self._last_kill_time >= 1000:
            self._index = 0
            self._last_kill_time = current_time
        else:
            self._index += 1
            self._last_kill_time = current_time
        return self._index

