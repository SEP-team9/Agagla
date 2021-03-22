import pygame
from agagla import game_state_manager as gsm
from agagla.ship import Ship
from pygame.math import Vector2

VELOCITY = 5
INIT_HEALTH = 2
INIT_X = (1920 / 2)
INIT_Y = (1080 - 30)

class PlayerShip(Ship):
    def __init__(self, position):
        super().__init__(position)
        self.set_health(INIT_HEALTH)
        self.velocity = VELOCITY
        self.set_pos(INIT_X, INIT_Y)
        self.rect = pygame.Rect(self.get_pos()[0], self.get_pos()[1], 10, 10)

    def render(self):
        pygame.Surface.blit(self.rect)

    def tick(self):
        im = gsm.GameStateManager.get_instance().get_input_manager()
        left = im.get_left()
        right = im.get_right()
        fire = im.get_fire()
        self._calculateMovement(left, right, fire)

    def _calculateMovement(self, left, right, fire):
        if left:
            self.move(-self.velocity, 0)
        elif right:
            self.move(self.velocity, 0)
        elif fire:
            self.spawn_projectile((0, -10), 0)
