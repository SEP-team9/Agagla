import random
import pygame
from agagla import ship
from pygame.math import Vector2
import os


class Enemy(ship.Ship):
    def __init__(self, position):
        super().__init__(position, Vector2(10, 10))
        enemy1 = os.path.join('../data/enemy1.png')
        self.image = pygame.image.load(enemy1)
        self.health = 1
        self.velocity = 1
        self.type = 1
        self.rect = pygame.Rect(self.get_pos().x, self.get_pos().y, 10, 10)

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
        self.rect = pygame.Rect(self.get_pos().x, self.get_pos().y, 10, 10)
        pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), self.rect)
        return None

    def tick(self):
        self.path()
        self.fire()
        return None
