import random
import pygame
from agagla import ship
from pygame.math import Vector2
import os
from enum import Enum


class Type(Enum):
    STANDARD = 1
    ASSAULT = 2
    REINFORCED = 3
    ELITE = 4


class Enemy(ship.Ship):
    #    def __init__(self, position):
    #        super().__init__(position, Vector2(50, 50))
    #        path = os.path.join('../data/enemy1.png')
    #        enemy1 = pygame.image.load(path)
    #        enemy1 = pygame.transform.scale(enemy1, (50, 50))
    #        self.image = enemy1
    #        self.health = 1
    #        self.velocity = 1
    #        self.type = 1
    #        self.rect = self.image.get_rect()
    #        self.rect.x = self.get_pos().x
    #        self.rect.y = self.get_pos().y
    #
    #    def path(self):
    #        self._position.y = self._position.y + self.velocity
    #        self.rect = pygame.Rect(self.get_pos().x, self.get_pos().y, 10, 10)
    #        return None
    #
    #    def fire(self):
    #        if random.randint(1, 180) == 45:
    #            self.spawn_projectile(Vector2(0, 10), 0)
    #        return None
    #
    #    def get_type(self):
    #        return self.type
    #
    #    def render(self):
    #        pygame.Surface.blit(pygame.display.get_surface(), pygame.transform.rotate(self.image, 180),
    #                            (self.get_pos().x - 20, self.get_pos().y))
    #        return None
    #
    #    def tick(self):
    #        self.path()
    #        self.fire()
    #        return None
    #
    def __init__(self, position):
        if Type == 1:
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
        elif Type == 2:
            super().__init__(position, Vector2(50, 50))
            path = os.path.join('../data/enemy2.png')
            enemy2 = pygame.image.load(path)
            enemy2 = pygame.transform.scale(enemy2, (50, 50))
            self.image = enemy2
            self.health = 1
            self.velocity = 2
            self.type = 2
            self.rect = self.image.get_rect()
            self.rect.x = self.get_pos().x
            self.rect.y = self.get_pos().y
        elif Type == 3:
            super().__init__(position, Vector2(50, 50))
            path = os.path.join('../data/enemy3.png')
            enemy3 = pygame.image.load(path)
            enemy3 = pygame.transform.scale(enemy3, (50, 50))
            self.image = enemy3
            self.health = 2
            self.velocity = 1
            self.type = 3
            self.rect = self.image.get_rect()
            self.rect.x = self.get_pos().x
            self.rect.y = self.get_pos().y
        else:
            super().__init__(position, Vector2(50, 50))
            path = os.path.join('../data/enemy4.png')
            enemy4 = pygame.image.load(path)
            enemy4 = pygame.transform.scale(enemy4, (50, 50))
            self.image = enemy4
            self.health = 3
            self.velocity = 3
            self.type = 4
            self.rect = self.image.get_rect()
            self.rect.x = self.get_pos().x
            self.rect.y = self.get_pos().y

    def path(self):
        self._position.y = self._position.y + self.velocity
        self.rect = pygame.Rect(self.get_pos().x, self.get_pos().y, 10, 10)
        return None

    def fire(self):
        if Type == 1:
            if random.randint(1, 100) == 25:
                self.spawn_projectile(Vector2(0, 10), 0)
        if Type == 2:
            if random.randint(1, 50) == 25:
                for x in range(3):
                    self.spawn_projectile(Vector2(0, 10), 0)
        if Type == 3:
            if random.randint(1, 200) == 25:
                self.spawn_projectile(Vector2(0, 10), 0)
                self.spawn_projectile(Vector2(0, 10), 45)
                self.spawn_projectile(Vector2(0, 10), -45)
        if Type == 4:
            if random.randint(1, 25) == 25:
                for x in range(5):
                    self.spawn_projectile(Vector2(0, 10), 0)
                    self.spawn_projectile(Vector2(0, 10), 45)
                    self.spawn_projectile(Vector2(0, 10), -45)
                    self.spawn_projectile(Vector2(0, 10), 22)
                    self.spawn_projectile(Vector2(0, 10), -22)
        return None

    def get_type(self):
        return self.type

    def render(self):
        pygame.Surface.blit(pygame.display.get_surface(), pygame.transform.rotate(self.image, 180),
                            (self.get_pos().x - 20, self.get_pos().y))
        return None

    def tick(self):
        self.path()
        self.fire()
        return None
