from agagla import entity
from agagla import shared_objects
from agagla import projectile


class Ship(entity.Entity):

    def __init__(self, position, size):
        super().__init__(position, size)
        self._health = 1

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def damage(self):
        self._health -= 1

    def spawn_projectile(self, offset, rotation):
        shared_objects.get_gsm().add_entity(projectile.Projectile(self.get_pos() + offset, rotation, self))
