from agagla import game_state_manager
import pygame
from agagla import shared_objects

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080


def init():
    shared_objects.init_gsm()
    shared_objects.init_im()
    shared_objects.init_hsdb()
    shared_objects.init_bg()

    global gsm, im, hsdb
    gsm = shared_objects.get_gsm()
    im = shared_objects.get_im()
    hsdb = shared_objects.get_hsdb()

    pygame.init()

    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


if __name__ == '__main__':

    init()

    while gsm.get_state() != game_state_manager.GameState.exit:
        gsm.game_loop()
        im.handle_events()
        pygame.display.update()

    pygame.quit()
