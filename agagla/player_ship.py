import pygame
from pygame.math import Vector2
from agagla import game_state_manager
# from agagla.game_state_manager import GameStateManager
from agagla.projectile import Projectile
from agagla.ship import Ship

init_position = Vector2(500, 500)
VELOCITY = 5
y = 500
class PlayerShip(Ship):
    def __init__(self):
        self.health = 2
        self.set_pos(init_position)
        self.rect = pygame.Rect(self.get_pos()[0], self.get_pos()[1], 10, 10)

    def move(self):
        im = game_state_manager.GameStateManager.get_input_manager()
        l = im.get_left()
        r = im.get_right()
        x = self.get_pos()[0]
        if (l):
            x -= VELOCITY
        elif (r):
            x += VELOCITY
        self.set_pos((x, y))
        return None

    def fire_projectile(self):
        im = game_state_manager.GameStateManager.get_input_manager()
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

