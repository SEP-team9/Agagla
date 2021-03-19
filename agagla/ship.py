from agagla.entity import Entity
from agagla.game_state_manager import GameStateManager
from agagla.projectile import Projectile


class Ship(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._health = 1

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def damage(self):
        self._health -= 1

    def spawn_projectile(self, offset, rotation):
        GameStateManager.get_instance().add_entity(Projectile(self.get_pos() + offset, rotation))
