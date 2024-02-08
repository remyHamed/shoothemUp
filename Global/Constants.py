UP, DOWN, LEFT, RIGHT, FIRE = 'U', 'D', 'L', 'R', 'F'
ACTIONS = [UP, DOWN, LEFT, RIGHT, FIRE]
MOVES = {UP : 'up',
                DOWN : 'down',
                LEFT : 'left',
                RIGHT : 'right',
                FIRE : 'shoot'}

REWARD_TAKE_DOWN = 100
REWARD_LOOSE = -1000
REWRAD_HIT = -300