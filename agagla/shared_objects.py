from agagla import game_state_manager
from agagla import input_manager


def init_im():
    global im
    im = input_manager.InputManager()


def init_gsm():
    global gsm
    gsm = game_state_manager.GameStateManager()


def get_im():
    return im


def get_gsm():
    return gsm
