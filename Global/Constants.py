from Enumerator.Bullet_direction import Bullet_direction

UP, DOWN, LEFT, RIGHT, FIRE = 'U', 'D', 'L', 'R', 'F'
ACTIONS = [UP, DOWN, LEFT, RIGHT, FIRE]
MOVES = {UP : 'up',
         DOWN : 'down',
         LEFT : 'left',
         RIGHT : 'right',
         FIRE : 'shoot'}

ENNEMY_BULLET_DIRECTION = [Bullet_direction.UP, 
                           Bullet_direction.DOWN, 
                           Bullet_direction.LEFT, 
                           Bullet_direction.RIGHT, 
                           Bullet_direction.UP_LEFT, 
                           Bullet_direction.UP_RIGHT, 
                           Bullet_direction.DOWN_LEFT, 
                           Bullet_direction.DOWN_RIGHT]

REWARD_TAKE_DOWN = 10000
REWARD_LOOSE = -10000
REWRAD_HIT = -3000
REWARD_NO_COMBO = -3000
REWARD_EMPTY_MOVE = -5
EMPTY = "EMPTY"
ENNEMY = "ENNEMY"
BULLET = "BULLET"