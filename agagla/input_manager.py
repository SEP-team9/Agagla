import pygame



class InputManager:
    def __init__(self):
        self.left = False
        self.right = False
        self.fire = False

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_fire(self):
        return self.fire