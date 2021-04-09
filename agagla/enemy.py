import random
import time
import pygame
from agagla import ship
from pygame.math import Vector2
import os
import math
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
        self.offset = Vector2(0, 45)
        self._dropping = False
        self._drop_velocity = 2
        self._drop_time = 0
        self._min_drop_time = 2
        self._max_drop_time = 5
        self._max_path_width_mult = 50
        self._min_path_width_mult = 30
        self._path_width_mult = random.randint(self._max_path_width_mult, self._max_path_width_mult)

        self.fire_sound = pygame.mixer.Sound(os.path.join("../data/enemy-shoot.wav"))
        self.explode_sound = pygame.mixer.Sound(os.path.join("../data/enemy-explode.wav"))

        if self.type == EnemyType.STANDARD:
            super().__init__(position, Vector2(40, 50), True)

            path = os.path.join('../data/enemy1.png')
            enemy1 = pygame.image.load(path)
            enemy1 = pygame.transform.scale(enemy1, (50, 50))
            self.image = enemy1
            self.health = 1
            self.score = 5
            self.fire_cooldown = 50
            self.velocity = 1
            self.rect = self.image.get_rect()
            self.rect.x = self.get_pos().x
            self.rect.y = self.get_pos().y
        elif self.type == EnemyType.ASSAULT:
            super().__init__(position, Vector2(40, 50), True)
            path = os.path.join('../data/enemy2.png')
            enemy2 = pygame.image.load(path)
            enemy2 = pygame.transform.scale(enemy2, (50, 50))
            self.image = enemy2
            self.health = 1
            self.score = 10
            self.velocity = 2
            self.fire_cooldown = 50
            self.rect = self.image.get_rect()
            self.rect.x = self.get_pos().x
            self.rect.y = self.get_pos().y
        elif self.type == EnemyType.REINFORCED:

            super().__init__(position, Vector2(40, 50), True)

            path = os.path.join('../data/enemy3.png')
            enemy3 = pygame.image.load(path)
            enemy3 = pygame.transform.scale(enemy3, (50, 50))
            self.image = enemy3
            self.health = 2

            self.score = 20

            self.velocity = 1
            self.fire_cooldown = 30
            self.rect = self.image.get_rect()
            self.rect.x = self.get_pos().x
            self.rect.y = self.get_pos().y
        else:
            super().__init__(position, Vector2(40, 50), True)

            path = os.path.join('../data/enemy4.png')
            enemy4 = pygame.image.load(path)
            enemy4 = pygame.transform.scale(enemy4, (50, 50))
            self.image = enemy4
            self.health = 3

            self.score = 30
            self.fire_cooldown = 40
            self.velocity = 3
            self.rect = self.image.get_rect()
            self.rect.x = self.get_pos().x
            self.rect.y = self.get_pos().y

    def path(self):
        gsm = shared_objects.get_gsm()
        if not (self._dropping and time.time() > self._drop_time):
            self.move(Vector2(-self.velocity if gsm.enemy_idle_left else self.velocity,
                          self.velocity*math.sin(self.get_pos()[0]/10)))
        self.rect = pygame.Rect(self.get_pos().x, self.get_pos().y, 10, 10)
        return None

    def is_dropping(self):
        return self._dropping

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

            self.spawn_projectile(self.offset, 0)
        if self.type == EnemyType.ASSAULT:
            for x in range(3):
                self.spawn_projectile(self.offset, 0)
        if self.type == EnemyType.REINFORCED:
            self.spawn_projectile(self.offset, 0)

            self.spawn_projectile(self.offset, 45)
            self.spawn_projectile(self.offset, -45)
        if self.type == EnemyType.ELITE:
            for x in range(5):
                self.spawn_projectile(self.offset, 0)
                self.spawn_projectile(self.offset, 45)
                self.spawn_projectile(self.offset, -45)
                self.spawn_projectile(self.offset, 22)
                self.spawn_projectile(self.offset, -22)
        return None

    def get_type(self):
        return self.type

    def drop(self):
        if not self._dropping:
            self._dropping = True
            self._drop_time = time.time()+random.randint(self._min_drop_time, self._max_drop_time)

    def drop_move(self):
        # TODO: add paths
        if time.time() > self._drop_time:
            self.move(Vector2(math.sin(self.get_pos().y/self._path_width_mult)*self.velocity, self._drop_velocity))

    def render(self):
        pygame.Surface.blit(pygame.display.get_surface(), pygame.transform.rotate(self.image, 180),
                            (self.get_pos().x - 20, self.get_pos().y))
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
        if self.is_dropping(): self.drop_move()
        return None

    def is_idle(self):
        return self.idle

    def spawn_projectile(self, offset, rotation):
        super().spawn_projectile(offset, rotation)
        self.fire_sound.play()

    def damage(self):
        super().damage()
        if self.get_health() <= 0:
            self.explode_sound.play()
            
    def get_score(self):
        return self.score

