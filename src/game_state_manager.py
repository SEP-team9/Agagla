import enum

class GameState(enum.Enum):
    menu = 1
    running = 2
    game_over = 3

class GameStateManager:
    def __init__(self):
        self.state = GameState.menu

    def _game_loop(self):

