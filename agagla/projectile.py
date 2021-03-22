from agagla import entity
from agagla import game_state_manager

PROJECTILE_SPEED = 10


class Projectile(entity.Entity):
    def __init__(self, position, rotation, parent = None):
        super(Projectile, self).__init__(position)
        self.set_rot(rotation)
        self.parent = parent

    def tick(self):
        super(Projectile, self).tick()
        self.move()
