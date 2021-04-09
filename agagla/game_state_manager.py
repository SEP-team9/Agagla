import enum
import time
import random
from agagla import menu
from agagla import player_ship
from agagla import shared_objects
from agagla import enemy
from agagla import death_screen as ds
from pygame.math import Vector2

import pygame

PLAYER_SPAWN = Vector2(shared_objects.get_window_width() / 2, shared_objects.get_window_height() - 50)
MAX_ENEMIES = 15

ENEMY_IDLE_BOUNDS = 75


class GameState(enum.Enum):
    menu = 1
    running = 2
    game_over = 3
    exit = 4


class GameStateManager:

    def __init__(self):

        self.tick_rate = 60
        self._last_game_state = None
        self._current_game_state = GameState.menu
        self.game_score = 0
        self.stage = 0
        self.lives = 3
        self.enemy_idle_left = False
        self._entities = []
        self._last_tick_time = time.time()
        self.states_switch = {GameState.menu: self._menu_fn,
                              GameState.running: self._running_fn,
                              GameState.game_over: self._game_over_fn}

        self._menu = None
        self._death_screen = None

    def _set_state(self, state):
        self._current_game_state = state

    def get_state(self):
        return self._current_game_state

    def get_enemies(self):
        enemies = []

        for i in self._entities:
            if type(i).__name__ == 'Enemy':
                enemies.append(i)

        return enemies

    def get_projectiles(self):
        projectiles = []

        for i in self._entities:
            if type(i).__name__ == 'Projectile':
                projectiles.append(i)

        return projectiles

    def get_player_ship(self):
        for i in self._entities:
            if type(i).__name__ == 'PlayerShip':
                return i

    def get_ships(self):
        enemies = self.get_enemies()
        if self.get_player_ship() is not None:
            ships = [self.get_player_ship()]
        else:
            ships = []

        ships += enemies
        return ships

    def get_entities(self):
        return self._entities

    def add_entity(self, e):
        self._entities.append(e)

    def remove_entity(self, e):
        self._entities.remove(e)

    def get_score(self):
        return self.game_score

    def start_game(self):
        self.add_entity(player_ship.PlayerShip(PLAYER_SPAWN))

        self._set_state(GameState.running)

    def spawn_wave(self, wave):
        new_enemies = []

        def add_enemies(enemy_type, number):
            for i in range(0, int(number)):
                new_enemies.append(enemy_type)

        if self.stage % 5 == 0:
            stage_num = int(self.stage / 5) - 1
            num_elite = int(stage_num % 20) + 1
            num_standard = stage_num - num_elite
            if num_standard < 0: num_standard = 0

            add_enemies(enemy.EnemyType.ELITE, num_elite)
            add_enemies(enemy.EnemyType.STANDARD, num_standard)
        elif self.stage % 4 == 0:
            stage_num = int(self.stage / 4) - 1
            if stage_num <= 0: stage_num = 2
            num_reinforced = stage_num / 2
            num_standard = stage_num - num_reinforced

            add_enemies(enemy.EnemyType.REINFORCED, num_reinforced)
            add_enemies(enemy.EnemyType.STANDARD, num_standard)
        elif self.stage % 3 == 0:
            stage_num = int(self.stage / 4) - 1
            if stage_num <= 0: stage_num = 2
            num_assault = stage_num / 2
            num_standard = stage_num - num_assault

            add_enemies(enemy.EnemyType.ASSAULT, num_assault)
            add_enemies(enemy.EnemyType.STANDARD, num_standard)
        else:
            add_enemies(enemy.EnemyType.STANDARD, self.stage)

        num_new_enemies = min(self.stage, MAX_ENEMIES)

        num_per_row = 5

        for i in range(0, min(len(new_enemies), num_new_enemies)):
            row_index = int(i / num_per_row)
            spawn_y = (row_index * 75) + 100
            spawn_x = ((i % num_per_row) * 100) + 200
            self.add_entity(enemy.Enemy(Vector2(spawn_x, spawn_y), new_enemies[i]))

    def submitted_hs(self):
        self.__init__()

    def _menu_fn(self, initial_run):
        if initial_run:
            self._menu = menu.Menu()

        self._menu.render()

    def _running_fn(self, initial_run):
        self._tick()
        self._render_game()

    def _game_over_fn(self, initial_run):
        if initial_run:
            self._death_screen = ds.DeathScreen()
        # self._set_state(GameState.menu)
        self._death_screen.render()

    def game_loop(self):
        if self._last_game_state == self._current_game_state:
            self.states_switch[self._current_game_state](False)
        else:
            self.states_switch[self._current_game_state](True)
            self._last_game_state = self._current_game_state

    def _force_tick(self):
        while not self._tick():
            continue

    def _tick(self):
        if time.time() >= self._last_tick_time + (1 / self.tick_rate):

            self.manage_game()

            for i in self._entities:
                i.tick()

            time_off = (self._last_tick_time + (1 / self.tick_rate)) - time.time()

            if time_off < 0:
                time_off = 0

            self._last_tick_time = time.time() - time_off

            return True

        return False

    def render_game_ui(self):
        screen = pygame.display.get_surface()
        font_small = shared_objects.get_tiny_font()
        score_surface = font_small.render("Score   " + str(self.game_score), False, (255, 255, 255))
        screen.blit(score_surface, (30, 10))

        round_surface = font_small.render("Stage   " + str(self.stage), False, (255, 255, 255))
        screen.blit(round_surface, ((shared_objects.get_window_width() / 2) - (round_surface.get_width() / 2), 10))

        life_surface = font_small.render("Lives   " + str(self.lives), False, (255, 255, 255))
        screen.blit(life_surface, (shared_objects.get_window_width() - life_surface.get_width() - 30, 10))

        return None

    def _render_game(self):
        pygame.display.get_surface().fill((0, 0, 0))
        shared_objects.get_bg().render()

        for i in self._entities:
            i.render()

        self.render_game_ui()

    def are_enemy_idle_left(self):
        return self.enemy_idle_left

    def manage_game(self):

        num_dropping = 0

        for i in self.get_enemies():
            if i.is_idle():
                # print(i.get_pos().x)
                if i.get_pos().x < ENEMY_IDLE_BOUNDS: self.enemy_idle_left = False

                elif i.get_pos().x > shared_objects.get_window_width() - ENEMY_IDLE_BOUNDS: self.enemy_idle_left = True

            if i.is_dropping():
                num_dropping += 1

            if i.get_health() <= 0:
                self.game_score += i.get_score()

        if num_dropping < 2:
            if len(self.get_enemies()) > 0:
                self.get_enemies()[random.randint(0, len(self.get_enemies())-1)].drop()

        for i in self.get_ships():
            if i.get_health() <= 0:
                self._entities.remove(i)

        ps = self.get_player_ship()

        if ps is None:
            self.lives -= 1
            self.add_entity(player_ship.PlayerShip(Vector2(PLAYER_SPAWN.x, PLAYER_SPAWN.y)))

        if self.lives <= 0:
            self._set_state(GameState.game_over)
        elif len(self.get_enemies()) <= 0:
            self.stage += 1
            self.spawn_wave(self.stage)

