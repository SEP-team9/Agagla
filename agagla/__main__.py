from agagla import game_state_manager
import pygame
import os
from agagla import shared_objects


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
    pygame.display.set_caption("Agagla")
    path = os.path.join('../data/window-icon.png')
    icon = pygame.image.load(path)
    pygame.display.set_icon(icon)

    pygame.display.set_mode((shared_objects.get_window_width(), shared_objects.get_window_height()))
    pygame.display.update()


if __name__ == '__main__':

    init()

    while gsm.get_state() != game_state_manager.GameState.exit:
        gsm.game_loop()
        im.handle_events()
        pygame.display.update()

    pygame.quit()
