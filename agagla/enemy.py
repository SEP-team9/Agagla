import random

import pygame

from agagla import ship


class Enemy(ship.Ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        enemy1 = 'enemy1.png'
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
        if random.randint(1,90) == 45:
            self.spawn_projectile(0, 10, 0)
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
