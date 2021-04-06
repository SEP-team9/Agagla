import pygame
import time
from agagla import shared_objects

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
WAIT_TIME_TO_END = 10
TOP_LINE = (WINDOW_HEIGHT / 2) - 300

class DeathScreen:

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
        text_surface = self.font_large.render('Game Over', False, (255, 255, 255))
        self.screen.blit(text_surface, ((WINDOW_WIDTH / 2) - (text_surface.get_width() / 2), (WINDOW_HEIGHT ) - 300))

        time_ms = time.time() * 1000.0

        if time_ms - self.last_time > 500.0:
            self.blink = ~self.blink
            self.last_time = time_ms
        self.display_scores()
        if self.hs_rank < 10:
            text_surface = self.font_small.render("HIGH SCORE!", False, (255, 255, 255))
            self.screen.blit(text_surface, (((WINDOW_WIDTH - text_surface.get_width()) / 2), (WINDOW_HEIGHT / 2) - 450))

            text_surface = self.font_small.render("{:<20} {:^25} {:>20}".format(self.name, (self.ch if self.blink else '    '),''),
                                                  False,
                                                  (255, 255, 255))
            self.screen.blit(text_surface, ((((WINDOW_WIDTH-text_surface.get_width()) / 2)), TOP_LINE + 50 * (self.hs_rank)))

            self.char_selection()

        if time.time() - self.time_of_last_key > WAIT_TIME_TO_END:
            # print(self.name)
            if self.hs_rank <= 10:
                self.hsdb.add_high_score(self.name, self.score)
            self.gsm.submitted_hs()

    def display_scores(self):
        gutter = " "
        for i in range(0, self.hs_rank):
            hs_formatted = "{:<20} {:^25} {:>20}".format(self.h_scores[i][1], gutter, str(self.h_scores[i][2]))
            text_surface = self.font_small.render(hs_formatted, False, (255, 255, 255))
            self.screen.blit(text_surface, (((WINDOW_WIDTH - text_surface.get_width()) / 2), TOP_LINE + 50*i))
        if self.hs_rank <10:
            hs_formatted = "{:<20} {:^25} {:>20}".format('',gutter, str(self.score))
            text_surface = self.font_small.render(hs_formatted, False, (255, 255, 255))
            self.screen.blit(text_surface, (((WINDOW_WIDTH - text_surface.get_width()) / 2), TOP_LINE + 50 * self.hs_rank))
        for i in range(self.hs_rank+1, len(self.h_scores)):
            hs_formatted = "{:<20} {:^25} {:>20}".format(self.h_scores[i-1][1], gutter, str(self.h_scores[i-1][2]))
            text_surface = self.font_small.render(hs_formatted, False, (255, 255, 255))
            self.screen.blit(text_surface, (((WINDOW_WIDTH - text_surface.get_width()) / 2), TOP_LINE + 50*(i)))

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


