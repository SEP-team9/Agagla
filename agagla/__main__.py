from agagla import game_state_manager
import pygame
from agagla import shared_objects
import os
import time

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080


def init():
    shared_objects.init_gsm()
    shared_objects.init_im()
    shared_objects.init_hsdb()

    global gsm, im, hsdb
    gsm = shared_objects.get_gsm()
    im = shared_objects.get_im()
    hsdb = shared_objects.get_hsdb()

    pygame.init()

    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

if __name__ == '__main__':

    init()

    winners = pygame.image.load(os.path.join("../data/winners.png"))
    pygame.Surface.blit(pygame.display.get_surface(), winners, ((WINDOW_WIDTH-winners.get_width())/2, (WINDOW_HEIGHT-winners.get_height())/2))
    pygame.display.update()
    time.sleep(5)

    while gsm.get_state() != game_state_manager.GameState.exit:
        gsm.game_loop()
        im.handle_events()
        pygame.display.update()

    pygame.quit()
