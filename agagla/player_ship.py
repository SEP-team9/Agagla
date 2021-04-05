import os

import pygame
from agagla import shared_objects
from agagla.ship import Ship
from pygame.math import Vector2

VELOCITY = 5
INIT_HEALTH = 2
MAX_PROJECTILES = 3


class PlayerShip(Ship):
    def __init__(self, position):
        super().__init__(position, Vector2(50, 25))
        self.set_health(INIT_HEALTH)
        self.velocity = VELOCITY
        path = os.path.join('../data/player.png')
        player = pygame.image.load(path)
        player = pygame.transform.scale(player, (50, 50))
        self.image = player
        #self.last_velocity = 5
        self.rect = self.image.get_rect()
        self.rect.x = self.get_pos()[0]
        self.rect.y = self.get_pos()[1]
        self.firing = False
        self.fire_sound = pygame.mixer.Sound(os.path.join('../data/player-shoot.wav'))
        self.hit_sound = pygame.mixer.Sound(os.path.join("../data/player-hit.wav"))
        self.die_sound = pygame.mixer.Sound(os.path.join("../data/player-explode.wav"))

    def render(self):
        pygame.Surface.blit(pygame.display.get_surface(), self.image, (self.get_pos().x - 17, self.get_pos().y - 17))

    def tick(self):
        im = shared_objects.get_im()
        left = im.get_left()
        right = im.get_right()
        fire = im.get_fire()
        self._calculate_movement(left, right, fire)

    def spawn_projectile(self, offset, rotation):
        super().spawn_projectile(offset, rotation)
        self.fire_sound.play()

    def damage(self):
        super().damage()
        if self.get_health() > 0:
            self.hit_sound.play()
        else:
            self.die_sound.play()

    def _calculate_movement(self, left, right, fire):
        if left:
            self.move(Vector2(-self.velocity, 0))
        elif right:
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