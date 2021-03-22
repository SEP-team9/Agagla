from agagla import entity
from agagla import game_state_manager
from agagla import projectile


class Ship(entity.Entity):

    def __init__(self, position):
        super().__init__(position)
        self._health = 1

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def damage(self):
        self._health -= 1

    def spawn_projectile(self, offset, rotation):
        game_state_manager.GameStateManager.get_instance().add_entity(projectile.Projectile(self.get_pos() + offset,
                                                                                            rotation, self))
