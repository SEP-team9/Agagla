import random
import pygame
from agagla import ship
from pygame.math import Vector2
import os
from enum import Enum
from agagla import shared_objects


class EnemyType(Enum):
    STANDARD = 1
    ASSAULT = 2
    REINFORCED = 3
    ELITE = 4


class Enemy(ship.Ship):

    def __init__(self, position, type):
        self.type = type
        self.current_fire_cooldown = 5
        self.idle = True
        if self.type == EnemyType.STANDARD:
            super().__init__(position, Vector2(50, 50), False)
            path = os.path.join('../data/enemy1.png')
            enemy1 = pygame.image.load(path)
            enemy1 = pygame.transform.scale(enemy1, (50, 50))
            self.image = enemy1
            self.health = 1
            self.score = 5
            self.fire_cooldown = 10
            self.velocity = 1
            self.rect = self.image.get_rect()
            self.rect.x = self.get_pos().x
            self.rect.y = self.get_pos().y
        elif self.type == EnemyType.ASSAULT:
            super().__init__(position, Vector2(50, 50), False)
            path = os.path.join('../data/enemy2.png')
            enemy2 = pygame.image.load(path)
            enemy2 = pygame.transform.scale(enemy2, (50, 50))
            self.image = enemy2
            self.health = 1
            self.score = 10
            self.velocity = 2
            self.fire_cooldown = 15
            self.rect = self.image.get_rect()
            self.rect.x = self.get_pos().x
            self.rect.y = self.get_pos().y
        elif self.type == EnemyType.REINFORCED:
            super().__init__(position, Vector2(50, 50), False)
            path = os.path.join('../data/enemy3.png')
            enemy3 = pygame.image.load(path)
            enemy3 = pygame.transform.scale(enemy3, (50, 50))
            self.image = enemy3
            self.health = 2
            self.score = 20
            self.velocity = 1
            self.fire_cooldown = 20
            self.rect = self.image.get_rect()
            self.rect.x = self.get_pos().x
            self.rect.y = self.get_pos().y
        else:
            super().__init__(position, Vector2(50, 50), False)
            path = os.path.join('../data/enemy4.png')
            enemy4 = pygame.image.load(path)
            enemy4 = pygame.transform.scale(enemy4, (50, 50))
            self.image = enemy4
            self.health = 3
            self.score = 30
            self.fire_cooldown = 30
            self.velocity = 3
            self.rect = self.image.get_rect()
            self.rect.x = self.get_pos().x
            self.rect.y = self.get_pos().y

    def path(self):
        gsm = shared_objects.get_gsm()
        # self._position.y = self._position.y + self.velocity
        self.move(Vector2(-self.velocity if gsm.enemy_idle_left else self.velocity, 0))
        self.rect = pygame.Rect(self.get_pos().x, self.get_pos().y, 10, 10)
        return None

    def fire(self):
        self.current_fire_cooldown = self.fire_cooldown
        if self.type == EnemyType.STANDARD:
            self.spawn_projectile(Vector2(0, 10), 0)
        if self.type == EnemyType.ASSAULT:
            for x in range(3):
                self.spawn_projectile(Vector2(0, 10), 0)
        if self.type == EnemyType.REINFORCED:
            self.spawn_projectile(Vector2(0, 10), 0)
            self.spawn_projectile(Vector2(0, 10), 45)
            self.spawn_projectile(Vector2(0, 10), -45)
        if self.type == EnemyType.ELITE:
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

        # pygame.draw.line(pygame.display.get_surface(), (255, 0, 0), self.get_pos(), self.get_line_of_sight(), 3)

        return None

    def should_fire(self):
        if self.current_fire_cooldown > 0: return False
        gsm = shared_objects.get_gsm()
        player_ship = gsm.get_player_ship()
        if player_ship is None: return False

        closest_ship = None
        closest_y = 10000000
        for ship in gsm.get_ships():
            if ship is self: continue
            if ship.get_pos().y < self.get_pos().y: continue
            if ship.get_pos().y < closest_y and abs(ship.get_pos().x - self.get_pos().x) <= ship.get_size().x:
                closest_y = ship.get_pos().y
                closest_ship = ship

        return closest_ship is player_ship

    def tick(self):
        self.path()
        if self.current_fire_cooldown > 0: self.current_fire_cooldown -= 1
        if self.should_fire(): self.fire()
        return None

    def is_idle(self):
        return self.idle

    def get_score(self):
        return self.score
