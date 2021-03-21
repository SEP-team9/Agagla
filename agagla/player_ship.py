import pygame
from pygame.math import Vector2
from agagla import game_state_manager
# from agagla.game_state_manager import GameStateManager
from agagla.projectile import Projectile
from agagla.ship import Ship

VELOCITY = 5
INITHEALTH = 2

class PlayerShip(Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.set_health(INITHEALTH)
        self.set_pos((x, y))
        self.rect = pygame.Rect(self.get_pos()[0], self.get_pos()[1], 10, 10)

    def move(self, offset):
        self.set_pos((self.get_pos()[0] + offset, self.get_pos()[1]))

    def fire_projectile(self):
        proj = Projectile(self.get_pos()[0], self.get_pos()[1] - 10)
        return proj

    def render(self):
        pygame.Surface.blit(self.rect)

    def tick(self):
        im = game_state_manager.GameStateManager.get_input_manager()
        left = im.get_left()
        right = im.get_right()
        fire = im.get_fire()
        if left:
            self.move(-VELOCITY)
        elif right:
            self.move(VELOCITY)
        elif fire:
            self.fire_projectile()
