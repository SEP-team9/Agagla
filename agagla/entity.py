from pygame.math import Vector2


class Entity:

    def __init__(self, position, size):
        self._position = position
        self._rotation = 0
        self._size = size

    def get_pos(self):
        return self._position

    def set_pos(self, vec):
        self._position = vec

    def get_rot(self):
        return self._rotation

    def set_rot(self, rot):
        self._rotation = rot

    def get_size(self):
        return self._size

    def render(self):
        pass

    def move(self, vec):
        self.set_pos(Vector2(self.get_pos()[0]+vec.x, self.get_pos()[1]+vec.y))

    def tick(self):
        pass
