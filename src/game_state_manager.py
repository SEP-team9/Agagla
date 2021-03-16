import enum
import time

class GameState(enum.Enum):
    menu = 1
    running = 2
    game_over = 3

class GameStateManager:
    def __init__(self):
        self.tick_rate = 60
        self._last_game_state = None
        self._current_game_state = GameState.menu
        self.game_score = 0
        self.lives = 0
        self.entities = []
        self._last_tick_time = time.time()
        self.states_switch = {GameState.menu: self._menu_fn,
                              GameState.running: self._running_fn,
                              GameState.game_over: self._game_over_fn}

    def _set_state(self, state):
        self._current_game_state = state

    def get_state(self):
        return self._current_game_state

    def get_enemies(self):
        enemies = []

        for i in self.entities:
            if type(i).__name__ == 'Enemy':
                enemies.append(i)

        return enemies

    def get_projectiles(self):
        projectiles = []

        for i in self.entities:
            if type(i).__name__ == 'Projectile':
                projectiles.append(i)

            return projectiles

    def get_player_ship(self):
        for i in self.entities:
            if type(i).__name__ == 'Player_Ship':
                return i

        return None

    def get_ships(self):
        return self.get_enemies().append(self.get_player_ship())

    def get_entities(self):
        return self.entities

    def add_entity(self, e):
        self.entities.append(e)

    def get_score(self):
        return self.game_score

    def start_game(self):
        self._set_state(GameState.running)

    def _menu_fn(self, initial_run):
        return None

    def _running_fn(self, initial_run):
        if self.lives <= 0:
            self._set_state(GameState.game_over)

        self._tick()
        self._render_game()

    def _game_over_fn(self, initial_run):
        return None

    def _game_loop(self):
        self.states_switch[self._current_game_state](not self._current_game_state == self._last_game_state)
        self._last_game_state = self._current_game_state

    def _tick(self):
        if time.time() >= self._last_tick_time+(1 / self.tick_rate):
            for i in self.entities:
                i.tick()

            time_off = (self._last_tick_time + (1/self.tick_rate)) - time.time()
            self._last_tick_time = time.time() - time_off

            return True

        return False


    def _render_game(self):
        for i in self.entities:
            i.render()
