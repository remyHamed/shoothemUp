from environment.enemy import Enemy


class Wave:
    def __init__(self, quantity, width):
        self.enemy_spacing = width // (quantity + 1)
        self._enemies = []
        self._waze_step = 1
        for i in range(quantity):
            enemy = Enemy(self.enemy_spacing * (i + 1), 10)
            self._enemies.append(enemy)
        print(len(self._enemies))

    @property
    def enemies(self):
        return self._enemies

    def _shoot_all(self):
        for i in self._enemies:
            i.shoot()

    def _move_all(self):
        for i in self._enemies:
            i.move()

    def step(self):
        match self._waze_step:
            case 0:
                self._shoot_all()
            case 1:
                self._move_all()


