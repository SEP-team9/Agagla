import pygame
import time
from agagla import shared_objects

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080


class DeathScreen:

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.font_large = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 40)
        self.font_small = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 30)
        self.last_time = 0
        self.blink = False
        self.gsm = shared_objects.get_gsm()
        self.im = shared_objects.get_im()

    def render(self):
        self.screen.fill((0, 0, 0))
        text_surface = self.font_large.render('Game Over', False, (255, 255, 255))
        self.screen.blit(text_surface, ((WINDOW_WIDTH / 2) - (text_surface.get_width() / 2), (WINDOW_HEIGHT / 2) - 100))

        time_ms = time.time() * 1000.0

        if time_ms - self.last_time > 500.0:
            self.blink = ~self.blink
            self.last_time = time_ms

        if self.blink:

            text_surface = self.font_small.render(self.char_selection(self, 'A'), False, (255, 255, 255))
            self.screen.blit(text_surface, ((WINDOW_WIDTH / 2) - 50, (WINDOW_HEIGHT / 2) - 300))

            text_surface = self.font_small.render(self.char_selection(self, 'A'), False, (255, 255, 255))
            self.screen.blit(text_surface, ((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) - 300))

            text_surface = self.font_small.render(self.char_selection(self, 'A'), False, (255, 255, 255))
            self.screen.blit(text_surface, ((WINDOW_WIDTH / 2) + 50, (WINDOW_HEIGHT / 2) - 300))


        return self.gsm.game_score

    def char_selection(self, ch):
        if self.im.get_right():
            ch = chr(ord(ch) + 1)
            if ord(ch) == 91:
                ch = chr(97)
            if ord(ch) == 123:
                ch = chr(65)
        self.char_selection(self, ch)
        if self.im.get_left():
            ch = chr(ord(ch) - 1)
            if ord(ch) == 64:
                ch = chr(122)
            if ord(ch) == 96:
                ch = chr(90)
        self.char_selection(self, ch)
        if self.im.get_fire():
            return ch