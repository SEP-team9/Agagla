import pygame
import time
from agagla import shared_objects

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080


class Menu:

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.font_large = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 40)
        self.font_small = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 30)
        self.last_time = 0
        self.blink = False
        self.gsm = shared_objects.get_gsm()

    def render(self):
        self.screen.fill((0, 0, 0))
        text_surface = self.font_large.render('agagla', False, (255, 255, 255))
        self.screen.blit(text_surface, ((WINDOW_WIDTH / 2) - (text_surface.get_width() / 2), (WINDOW_HEIGHT / 2) - 200))

        time_ms = time.time()*1000.0

        if time_ms - self.last_time > 500.0:
            self.blink = ~self.blink
            self.last_time = time_ms

        if self.blink:
            text_surface = self.font_small.render('Press    fire    to    start', False, (255, 255, 255))
            self.screen.blit(text_surface, ((WINDOW_WIDTH / 2) - (text_surface.get_width() / 2), (WINDOW_HEIGHT / 2) - 100))

        if shared_objects.get_im().get_fire():
            self.gsm.start_game()

        return None
