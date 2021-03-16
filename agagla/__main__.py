from game_state_manager import *

gsm = GameStateManager()

if __name__ == '__main__':

    while gsm.get_state() != GameState.exit:
        gsm.game_loop()