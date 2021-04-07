from agagla import game_state_manager
from agagla import input_manager
from agagla import high_score_database
from agagla import background
import pygame

def init_im():
    global im
    im = input_manager.InputManager()


def init_gsm():
    global gsm
    gsm = game_state_manager.GameStateManager()

def init_hsdb():
    global hsdb
    hsdb = high_score_database.HighScoreDatabase()
    

def init_bg():
    global bg
    bg = background.Background()

def init_fonts():
    global large_font
    large_font = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 40)

    global small_font
    small_font = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 30)

    global tiny_font
    tiny_font = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 20)

def get_im():
    return im

def get_gsm():
    return gsm

def get_hsdb():
    return hsdb

def get_bg():
    return bg

def get_large_font():
    return large_font

def get_small_font():
    return small_font

def get_tiny_font():
    return tiny_font

def get_window_width():
    return 600

def get_window_height():
    return 700
