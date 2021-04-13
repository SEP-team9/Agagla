from agagla import entity
from pygame.math import Vector2
from agagla import shared_objects
import pygame
import os

PROJECTILE_SPEED = 10


class Projectile(entity.Entity):
    def __init__(self, position, rotation, parent=None):
        super(Projectile, self).__init__(position, Vector2(10, 10), False)
        path = os.path.join('../data/projectile.png')
        projectile = pygame.image.load(path)
        projectile = pygame.transform.scale(projectile, (9, 15))
        self.image = projectile
        self.set_rot(rotation)
        self.move_vector = Vector2(0, PROJECTILE_SPEED)
        self.move_vector = self.move_vector.rotate(rotation)
        self.parent = parent
        self.rect = pygame.Rect(self.get_pos()[0], self.get_pos()[1], 10, 10)

    def die(self):
        shared_objects.get_gsm().remove_entity(self)

    def tick(self):
        super(Projectile, self).tick()

        for i in shared_objects.get_gsm().get_ships():
            distance = self.get_pos() - i.get_pos()
            if abs(distance.x) < i.get_size().x \
                    and abs(distance.y) < i.get_size().y \
                    and not isinstance(i, type(self.parent)):
                i.damage()
                self.die()
                return

        self.move(self.move_vector)

        if self.get_pos().y > shared_objects.get_window_height() or self.get_pos().y < 0:
            self.die()
            return

    def render(self):
        pygame.Surface.blit(pygame.display.get_surface(), self.image, (self.get_pos()[0], self.get_pos()[1]))
