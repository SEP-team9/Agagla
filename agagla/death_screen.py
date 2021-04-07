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

class DeathScreen:

    def __init__(self):
        self.screen = pygame.display.get_surface()

        self.font_large = shared_objects.get_large_font()
        self.font_small = shared_objects.get_small_font()

        self.last_time = 0
        self.blink = False
        self.gsm = shared_objects.get_gsm()
        self.im = shared_objects.get_im()
        self.hsdb = shared_objects.get_hsdb()
        self.btn_pressed = False
        self.ch = 'A'
        self.name = ''
        self.score = self.gsm.game_score
        self.time_of_last_key = time.time()
        self.h_scores = self.hsdb.get_high_score()
        self.hs_rank = 10
        for i in range(0, len(self.h_scores)):
            if self.h_scores[i][2] < self.score:
                self.hs_rank = i
                break


    def render(self):
        self.screen.fill((0, 0, 0))
        shared_objects.get_bg().render()
        text_surface = self.font_large.render('Game Over', False, (255, 255, 255))
        self.screen.blit(text_surface, ((WINDOW_WIDTH / 2) - (text_surface.get_width() / 2), 25))

        time_ms = time.time() * 1000.0

        if time_ms - self.last_time > 500.0:
            self.blink = ~self.blink
            self.last_time = time_ms

        self.display_scores()
        if self.hs_rank < 10:

            text_surface = self.font_small.render("HIGH SCORE ACHIEVED!", False, (255, 255, 255))
            self.screen.blit(text_surface, (((WINDOW_WIDTH - text_surface.get_width()) / 2), 75))

            text_surface = self.font_small.render(self.name + (self.ch if self.blink else '_'),
                                                  False,
                                                  (255, 255, 255))

            self.screen.blit(text_surface, (LEFT_COLUMN, TOP_LINE + 50 * self.hs_rank))

            self.char_selection()

        if (time.time() - self.time_of_last_key > WAIT_TIME_TO_END) or len(self.name) == MAX_NAME_LENGTH:

            # print(self.name)
            if self.hs_rank <= 10:
                self.hsdb.add_high_score(self.name, self.score)
            self.gsm.submitted_hs()


    def display_scores(self):
        for i in range(0, self.hs_rank):
            hs_name = self.font_small.render(self.h_scores[i][1], False, (255, 255, 255))
            hs_score = self.font_small.render(str(self.h_scores[i][2]), False, (255, 255, 255))
            self.screen.blit(hs_name, (LEFT_COLUMN, TOP_LINE + 50 * i))
            self.screen.blit(hs_score, (RIGHT_COLUMN, TOP_LINE + 50 * i))
        if self.hs_rank <10:
            text_surface = self.font_small.render(str(self.score), False, (255, 255, 255))
            self.screen.blit(text_surface, (RIGHT_COLUMN, TOP_LINE + 50 * self.hs_rank))
        for i in range(self.hs_rank, len(self.h_scores)):
            hs_name = self.font_small.render(self.h_scores[i][1], False, (255, 255, 255))
            hs_score = self.font_small.render(str(self.h_scores[i][2]), False, (255, 255, 255))
            self.screen.blit(hs_name, (LEFT_COLUMN, TOP_LINE + 50 * (i + 1)))
            self.screen.blit(hs_score, (RIGHT_COLUMN, TOP_LINE + 50 * (i + 1)))

            
    def char_selection(self):
        if self.im.get_right():
            if not self.btn_pressed:
                self.ch = chr(ord(self.ch) + 1)
                if ord(self.ch) == 91:
                    self.ch = chr(97)
                if ord(self.ch) == 123:
                    self.ch = chr(65)
                self.btn_pressed = True
                self.time_of_last_key = time.time()
        elif self.im.get_left():
            if not self.btn_pressed:
                self.ch = chr(ord(self.ch) - 1)
                if ord(self.ch) == 64:
                    self.ch = chr(122)
                if ord(self.ch) == 96:
                    self.ch = chr(90)
                self.btn_pressed = True
                self.time_of_last_key = time.time()
        elif self.im.get_fire():
            if not self.btn_pressed:
                self.name += self.ch
                self.btn_pressed = True
                self.time_of_last_key = time.time()
        else:
            self.btn_pressed = False


