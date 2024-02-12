from Enumerator.Bullet_direction import Bullet_direction

IDLE, UP, DOWN, LEFT, RIGHT, FIRE = 'I', 'U', 'D', 'L', 'R', 'F'
ACTIONS = [IDLE, UP, DOWN, LEFT, RIGHT, FIRE]
MOVES = {IDLE: '',
         UP : 'up',
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

FIRE_REWARD = 1
REWARD_TAKE_DOWN = 30
REWRAD_HIT = -300
REWARD_COMBO = 1
REWARD_NO_COMBO = -3
REWARD_CLEAR_WAVE = 300
REWARD_LOOSE = -300
REWARD_GOOD_POSITIONING = 1
REWARD_SELF_BLINDING = -30
EMPTY = "EMPTY"
ENNEMY = "ENNEMY"
BULLET = "BULLET"

AGENT_FILE = './agent.qtable'