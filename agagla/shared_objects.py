from agagla import game_state_manager
from agagla import input_manager
from agagla import high_score_database
from agagla import background


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

def get_im():
    return im

def get_gsm():
    return gsm

def get_hsdb():
    return hsdb

def get_bg():
    return bg
