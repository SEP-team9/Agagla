from agagla import entity
from pygame.math import Vector2
from agagla import shared_objects
import pygame

PROJECTILE_SPEED = 10


class Projectile(entity.Entity):
    def __init__(self, position, rotation, parent = None):
        super(Projectile, self).__init__(position, Vector2(10, 10))
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
            distance = self.get_pos()-i.get_pos()
            if abs(distance.x) < i.get_size().x and abs(distance.y) < i.get_size().y and i is not self.parent:
                i.damage()
                self.die()
                return

        self.move(self.move_vector)

        if self.get_pos().y > 1080 or self.get_pos().y < 0:
            self.die()
            return

    def render(self):
        self.rect = pygame.Rect(self.get_pos()[0], self.get_pos()[1], 10, 10)
        pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), self.rect)
