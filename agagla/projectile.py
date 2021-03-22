from agagla import entity
from agagla import game_state_manager
from pygame.math import Vector2

PROJECTILE_SPEED = 10


class Projectile(entity.Entity):
    def __init__(self, position, rotation, parent = None):
        super(Projectile, self).__init__(position)
        self.set_rot(rotation)
        self.move_vector = Vector2(0, PROJECTILE_SPEED)
        self.move_vector.rotate(self.get_rot())
        self.parent = parent

    def tick(self):
        super(Projectile, self).tick()

        self.move(self.move_vector)
