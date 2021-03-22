from game_state_manager import *
import pygame

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

if __name__ == '__main__':

    gsm = GameStateManager.get_instance()

    pygame.init()

    while gsm.get_state() != GameState.exit:
        gsm.game_loop()
        pygame.display.update()

    pygame.quit()
