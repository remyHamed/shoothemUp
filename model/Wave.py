from Enumerator.Status import Status
from Enumerator.ennemy_patern import ennemy_patern
from model import Environment
from model.Ennemy import Ennemy



class Wave:
    def __init__(self, env : 'Environment', ennemyQuantity : int, paterne : ennemy_patern ):
        
        self._env = env
        self._ennemy = [Ennemy(env) for i in range(ennemyQuantity)]
        for ennemy in self._ennemy:
            ennemy._patern = paterne
        
        self.position_ennemies()
            
    def activate(self):
        for ennemy in self._ennemy:
            ennemy.status = Status.A_live
            
    
    def position_ennemies(self):
        spacing = self._env._window_width // (len(self._ennemy) + 1)
        for index, ennemy in enumerate(self._ennemy):
            x_pos = spacing * (index + 1)
            y_pos = 10 
            ennemy.set_position(x_pos, y_pos)
        
        