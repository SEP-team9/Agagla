from agagla import game_state_manager
import pygame
import os
import time
from agagla import shared_objects
import os
import time


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
    pygame.mixer.init()

    pygame.display.set_caption("Agagla")
    path = os.path.join('../data/window-icon.png')
    icon = pygame.image.load(path)
    pygame.display.set_icon(icon)

    pygame.display.set_mode((shared_objects.get_window_width(), shared_objects.get_window_height()))
    pygame.display.update()

    shared_objects.init_fonts()

if __name__ == '__main__':

    init()

    winners = pygame.image.load(os.path.join("../data/winners.png"))
    pygame.Surface.blit(pygame.display.get_surface(),
                        winners,
                        ((shared_objects.get_window_width()-winners.get_width())/2,
                         (shared_objects.get_window_height()-winners.get_height())/2))

    pygame.display.update()
    time.sleep(5)

    enemies = pygame.image.load(os.path.join("../data/enemies.png"))
    pygame.Surface.blit(pygame.display.get_surface(),
                        enemies,
                        ((shared_objects.get_window_width()-enemies.get_width())/2,
                         (shared_objects.get_window_height()-enemies.get_height())/2))

    pygame.display.update()
    time.sleep(5)

    controls = pygame.image.load(os.path.join("../data/controls.png"))
    pygame.Surface.blit(pygame.display.get_surface(),
                        controls,
                        ((shared_objects.get_window_width()-controls.get_width())/2,
                         (shared_objects.get_window_height()-controls.get_height())/2))

    pygame.display.update()
    time.sleep(5)

    while gsm.get_state() != game_state_manager.GameState.exit:
        gsm.game_loop()
        im.handle_events()
        pygame.display.update()

    pygame.quit()
