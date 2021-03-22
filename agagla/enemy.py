import random
import pygame
from agagla import ship
from pygame.math import Vector2
import os

class Enemy(ship.Ship):
    def __init__(self, position):
        super().__init__(position)
        enemy1 = os.path.join('../data/enemy1.png')
        self.image = pygame.image.load(enemy1)
        self.health = 1
        self.velocity = 5
        self.type = 1
        self.rect = pygame.Rect(self.xPos(), 0, 10, 10)

    def xPos(self):
        position = random.randint(10, 1910)
        return position

    def path(self):
        self.rect.y = self.rect.y - self.velocity
        return None

    def fire(self):
        if random.randint(1, 90) == 45:
            self.spawn_projectile(Vector2(0, 10), 0)
        return None

    def get_type(self):
        return self.type

    def render(self):
        pygame.Surface.blit(self.rect)
        return None

    def tick(self):
        self.path()
        self.fire()
        return None
