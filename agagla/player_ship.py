import pygame
# from agagla.game_state_manager import GameStateManager
from agagla.projectile import Projectile
from agagla.ship import Ship

VELOCITY = 5

class PlayerShip(Ship):
    def __init__(self, x, y):
        self.health = 2
        self.rect = Rect(x, y, 10, 10)

    def move(self):
        im = GameStateManager.get_input_manager()
        l= im.get_left()
        r = im.get_right()
        if (l):
            self.x -= VELOCITY
        elif (r):
            self.x += VELOCITY
        return self.x

    def fire_projectile(self):
        im = GameStateManager.get_input_manager()
        f = im.get_fire()
        if (f):
            proj = Projectile(self)
            proj.position = (self.x, self.y-10)
            return proj
        else:
            return None

    def render(self):
        pygame.Surface.blit(self.rect)
        return None

