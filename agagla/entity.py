from pygame.math import Vector2


class Entity:

    def __init__(self, x, y):
        self._position = Vector2(x, y)
        self._rotation = 0

    def get_pos(self):
        return self._position

    def set_pos(self, pos):
        self._position = pos

    def get_rot(self):
        return self._rotation

    def set_rot(self, rot):
        self._rotation = rot

    def render(self):
        pass

    def move(self, delta):
        self.set_pos(self.get_pos()+delta)

    def tick(self):
        pass
