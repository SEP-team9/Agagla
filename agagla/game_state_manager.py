import enum
import time
from agagla.menu import Menu
from agagla.player_ship import PlayerShip
from agagla.enemy import Enemy
from agagla.input_manager import InputManager


class GameState(enum.Enum):
    menu = 1
    running = 2
    game_over = 3
    exit = 4


class GameStateManager:
    _instance = None

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

    def get_instance(self):
        if GameStateManager._instance is None:
            GameStateManager._instance = GameStateManager()
        else: GameStateManager

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

    def get_score(self):
        return self.game_score

    def start_game(self):
        self.lives = 3
        self.add_entity(PlayerShip())

        for i in range(0, 10):
            self.add_entity(Enemy())

        self._set_state(GameState.running)

    def _menu_fn(self, initial_run):
        if initial_run:
            self._menu = Menu()

        self._menu.render()

    def _running_fn(self, initial_run):
        self._tick()
        self._render_game()

    def _game_over_fn(self, initial_run):
        self._set_state(GameState.menu)

    def game_loop(self):
        self.states_switch[self._current_game_state](not self._current_game_state == self._last_game_state)
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
            self._last_tick_time = time.time() - time_off

            return True

        return False

    def _render_game(self):
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
            self.add_entity(PlayerShip())

        if self.lives <= 0:
            self._set_state(GameState.game_over)
