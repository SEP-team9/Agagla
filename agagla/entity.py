from pygame.math import Vector2


class Entity:

    def __init__(self, position):
        self._position = position
        self._rotation = 0

    def get_pos(self):
        return self._position

    def set_pos(self, x, y):
        self._position = (x, y)

    def get_rot(self):
        return self._rotation

    def set_rot(self, rot):
        self._rotation = rot

    def render(self):
        pass

    def move(self, x, y):
        self.set_pos(self.get_pos()[0]+x, self.get_pos()[1]+y)

    def tick(self):
        pass
