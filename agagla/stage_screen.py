import pygame
import time
from agagla import shared_objects

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WAIT_TIME_TO_END = 10


class StageScreen:

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.font_large = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 40)
        self.font_small = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 30)
        self.last_time = 0
        self.blink = False
        self.gsm = shared_objects.get_gsm()
        self.im = shared_objects.get_im()
        self.hsdb = shared_objects.get_hsdb()
        self.btn_pressed = False
        self.time_of_last_key = time.time()
        self.time = 1000
        self.screneExit = False

    def render(self):

        while not self.screneExit:

                self.screen.fill((0, 0, 0))
                text_surface = self.font_large.render('Level ' + str(self.gsm.stage - 10), False, (255, 255, 255))
                self.screen.blit(text_surface, ((WINDOW_WIDTH / 2) - (text_surface.get_width() / 2), (WINDOW_HEIGHT / 2) - 100))

                pygame.display.update()

                passed_time = pygame.time.Clock().tick(60)
                self.time -= passed_time
                if self.time <= 0:
                    self.screneExit = True

        pygame.display.update()
