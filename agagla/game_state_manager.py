import enum
import time
from agagla import menu
from agagla import player_ship
from agagla import enemy
from agagla import death_screen as ds
from pygame.math import Vector2
from agagla import __main__ as main

import pygame

PLAYER_SPAWN = Vector2(100, 100)


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
        self.lives = 0
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
        self.lives = 1
        self.add_entity(player_ship.PlayerShip(PLAYER_SPAWN))

        for i in range(0, 15):
            self.add_entity(enemy.Enemy(Vector2(i*100 + 200, 10)))

        self._set_state(GameState.running)

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

    def _render_game(self):
        pygame.display.get_surface().fill((0, 0, 0))

        for i in self._entities:
            i.render()

    def manage_game(self):

        for i in self.get_enemies():
            if i.get_health() <= 0:
                self.game_score += 10

        for i in self.get_ships():
            if i.get_health() <= 0:
                self._entities.remove(i)

        ps = self.get_player_ship()

        if ps is None:
            self.lives -= 1
            self.add_entity(player_ship.PlayerShip(Vector2(PLAYER_SPAWN.x, PLAYER_SPAWN.y)))

        if self.lives <= 0:
            self._set_state(GameState.game_over)
