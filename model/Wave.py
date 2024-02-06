


from Enumerator.Status import Status
from Enumerator.ennemy_patern import Patern
from model import Ennemy, Environment


class Wave:
    def __init__(self, env : 'Environment', ennemyQuantity : int, paterne : Patern ):
        
        self._env = env
        self._ennemy = [Ennemy(env) for i in range(ennemyQuantity)]
        for ennemy in self._ennemy:
            ennemy._patern = paterne
            
    def activate(self):
        for ennemy in self._ennemy:
            ennemy.status = Status.A_live
        
        