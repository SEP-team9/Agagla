import pygame
from agagla import shared_objects
from agagla.ship import Ship
from pygame.math import Vector2
from agagla import __main__ as main

VELOCITY = 5
INIT_HEALTH = 2
INIT_X = (1920 / 2)
INIT_Y = (1080 - 30)

class PlayerShip(Ship):
    def __init__(self, position):
        super().__init__(position)
        self.set_health(INIT_HEALTH)
        self.velocity = VELOCITY
        self.set_pos(Vector2(INIT_X, INIT_Y))
        self.rect = pygame.Rect(self.get_pos()[0], self.get_pos()[1], 10, 10)

    def render(self):
        self.rect = pygame.Rect(self.get_pos()[0], self.get_pos()[1], 10, 10)
        pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), self.rect)

    def tick(self):
        im = shared_objects.get_im()
        left = im.get_left()
        right = im.get_right()
        fire = im.get_fire()
        self._calculate_movement(left, right, fire)

    def _calculate_movement(self, left, right, fire):
        if left:
            self.move(Vector2(-self.velocity, 0))
        elif right:
            self.move(Vector2(self.velocity, 0))
        elif fire:
            self.spawn_projectile((0, -10), 0)
