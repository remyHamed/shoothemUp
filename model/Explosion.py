from model import Environment


class Explosion:
    def __init__(self, env : 'Environment', sprites_path : list):
        
        self._height = 50
        self._width = 50
        self._env = env
        self._position = [env._window_width // 2, env._window_hight // 2]
        self._sprites_path = sprites_path
        self._sprite = pygame.image.load(self._sprites_path[0])
        self._sprite = pygame.transform.scale(self._sprite, (self._width, self._height))
        self._index = 0
    
    def change_Sprite(self, index):
        self._sprite = pygame.image.load(self._sprites_path[index])
        self._sprite = pygame.transform.scale(self._sprite, (self._width, self._height))
        self._index = index