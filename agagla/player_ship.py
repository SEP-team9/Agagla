import pygame
from agagla import game_state_manager as gsm
from agagla.ship import Ship

VELOCITY = 5
INITHEALTH = 2
INITX = (1920 / 2)
INITY = (1080 - 30)

class PlayerShip(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_health(INITHEALTH)
        self.velocity = VELOCITY
        self.set_pos(INITX, INITY)
        self.rect = pygame.Rect(self.get_pos()[0], self.get_pos()[1], 10, 10)

    def render(self):
        pygame.Surface.blit(self.rect)

    def tick(self):
        im = gsm.GameStateManager.get_input_manager()
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
