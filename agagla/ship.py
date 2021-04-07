from pygame import Vector2

from agagla import entity
from agagla import shared_objects
from agagla import projectile


class Ship(entity.Entity):

    def __init__(self, position, size, window_lock):
        super().__init__(position, size, window_lock)
        self._health = 1

        self.LINE_OF_SIGHT_LENGTH = shared_objects.get_window_height()

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def damage(self):
        self._health -= 1

    def spawn_projectile(self, offset, rotation):
        shared_objects.get_gsm().add_entity(projectile.Projectile(self.get_pos() + offset, rotation, self))

    def get_line_of_sight(self):
        vector = Vector2(0, self.LINE_OF_SIGHT_LENGTH)
        vector = self.get_pos() + vector
        vector = vector.rotate(self.get_rot())
        return vector

