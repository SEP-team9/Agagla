import random
import pygame
from agagla import ship
from pygame.math import Vector2
import os


class Enemy(ship.Ship):
    def __init__(self, position):
        super().__init__(position, Vector2(50, 50))
        path = os.path.join('../data/enemy1.png')
        enemy1 = pygame.image.load(path)
        enemy1 = pygame.transform.scale(enemy1, (50, 50))
        self.image = enemy1
        self.health = 1
        self.velocity = 1
        self.type = 1
        self.rect = self.image.get_rect()
        self.rect.x = self.get_pos().x
        self.rect.y = self.get_pos().y

    def path(self):
        self._position.y = self._position.y + self.velocity
        self.rect = pygame.Rect(self.get_pos().x, self.get_pos().y, 10, 10)
        return None

    def fire(self):
        if random.randint(1, 180) == 45:
            self.spawn_projectile(Vector2(0, 10), 0)
        return None

    def get_type(self):
        return self.type

    def render(self):
        pygame.Surface.blit(pygame.display.get_surface(), pygame.transform.rotate(self.image, 180), (self.get_pos().x - 20, self.get_pos().y))
        return None

    def tick(self):
        self.path()
        self.fire()
        return None
