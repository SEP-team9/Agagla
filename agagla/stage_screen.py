import pygame
import time
from agagla import shared_objects

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
        self.font_large = shared_objects.get_large_font()
        self.font_small = shared_objects.get_small_font()
        self.last_time = 0
        self.blink = False
        self.gsm = shared_objects.get_gsm()
        self.im = shared_objects.get_im()
        self.hsdb = shared_objects.get_hsdb()

    def render(self):
        text_surface = self.font_large.render('Stage ' + str(self.gsm.stage), False, (255, 255, 255))
        self.screen.blit(text_surface, ((WINDOW_WIDTH / 2) - (text_surface.get_width() / 2), (WINDOW_HEIGHT / 2) - 100))
