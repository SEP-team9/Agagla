import pygame
import time
from agagla import shared_objects

#WINDOW_WIDTH = 1920
#WINDOW_HEIGHT = 1080
#WAIT_TIME_TO_END = 10

WINDOW_HEIGHT = shared_objects.get_window_height()
WINDOW_WIDTH = shared_objects.get_window_width()

WAIT_TIME_TO_END = 10
TOP_LINE = (WINDOW_HEIGHT / 2) - (WINDOW_HEIGHT * 0.3)
LEFT_COLUMN = (WINDOW_WIDTH / 2) - (WINDOW_WIDTH * 0.2)
RIGHT_COLUMN = (WINDOW_WIDTH / 2) + (WINDOW_WIDTH * 0.2)
MAX_NAME_LENGTH = 10

class StageScreen:

    def __init__(self):
        self.screen = pygame.display.get_surface()
        #self.font_large = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 40)
        #self.font_small = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 30)
        self.font_large = shared_objects.get_large_font()
        self.font_small = shared_objects.get_small_font()
        self.last_time = 0
        self.blink = False
        self.gsm = shared_objects.get_gsm()
        self.im = shared_objects.get_im()
        self.hsdb = shared_objects.get_hsdb()
        self.btn_pressed = False
        self.time_of_last_key = time.time()
        self.time = 1100
        self.screneExit = False

    def render(self):

        while not self.screneExit:
            self.screen.fill((0, 0, 0))
            shared_objects.get_bg().render()
            text_surface = self.font_large.render('Stage ' + str(self.gsm.stage - 1), False, (255, 255, 255))
            self.screen.blit(text_surface, ((WINDOW_WIDTH / 2) - (text_surface.get_width() / 2), (WINDOW_HEIGHT / 2) - 100))

            passed_time = pygame.time.Clock().tick(60)
            self.time -= passed_time
            if self.time <= 0:
                self.screneExit = True

            pygame.display.update()
