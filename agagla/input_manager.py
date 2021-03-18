import pygame

LEFT_SCANCODE = 4
RIGHT_SCANCODE = 7
FIRE_SCANCODE = 228


class InputManager:

    def __init__(self):
        self._left_state = False
        self._right_state = False
        self._fire_state = False

    def handle_events(self):
        for i in pygame.event.get():

            if i.type == 768:
                if i.dict['scancode'] == LEFT_SCANCODE:
                    self._left_state = True
                if i.dict['scancode'] == RIGHT_SCANCODE:
                    self._right_state = True
                if i.dict['scancode'] == FIRE_SCANCODE:
                    self._fire_state = True

            if i.type == 769:
                if i.dict['scancode'] == LEFT_SCANCODE:
                    self._left_state = False
                if i.dict['scancode'] == RIGHT_SCANCODE:
                    self._right_state = False
                if i.dict['scancode'] == FIRE_SCANCODE:
                    self._fire_state = False

    def get_left(self):
        return self._left_state

    def get_right(self):
        return self._right_state

    def get_fire(self):
        return self._fire_state
