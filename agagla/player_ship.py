import os

import pygame
from agagla import shared_objects
from agagla.ship import Ship
from pygame.math import Vector2

VELOCITY = 5
INIT_HEALTH = 1
MAX_PROJECTILES = 3
INIT_X = (1920 / 2)
INIT_Y = (1080 - 75)


class PlayerShip(Ship):
    def __init__(self, position):
        super().__init__(position, Vector2(35, 35))
        self.set_health(INIT_HEALTH)
        self.velocity = VELOCITY
        self.set_pos(Vector2(INIT_X, INIT_Y))
        path = os.path.join('../data/player.png')
        player = pygame.image.load(path)
        player = pygame.transform.scale(player, (50, 50))
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.x = self.get_pos()[0]
        self.rect.y = self.get_pos()[1]
        self.firing = False

    def render(self):
        pygame.Surface.blit(pygame.display.get_surface(), self.image, (self.get_pos().x - 17, self.get_pos().y - 17))

    def tick(self):
        im = shared_objects.get_im()
        left = im.get_left()
        right = im.get_right()
        fire = im.get_fire()
        self._calculate_movement(left, right, fire)

    def _calculate_movement(self, left, right, fire):
        if left:
            self.move(Vector2(-self.velocity, 0))
        if right:
            self.move(Vector2(self.velocity, 0))

        if fire and not self.firing:
            self.firing = True

            num = 0

            for i in shared_objects.get_gsm().get_projectiles():
                if i.parent is self:
                    num += 1

            if num < MAX_PROJECTILES:
                self.spawn_projectile((0, -10), 180)

        elif not fire:
            self.firing = False