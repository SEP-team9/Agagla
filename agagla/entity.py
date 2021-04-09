from pygame.math import Vector2
from agagla import shared_objects


class Entity:

    def __init__(self, position, size, window_lock):
        self._position = position
        self._rotation = 0
        self._size = size
        self.window_lock = window_lock

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
        newX = self.get_pos()[0]+vec.x
        newY = self.get_pos()[1]+vec.y

        if self.window_lock:
            if newX < self._size[0]: newX = self._size[0]
            elif newX > shared_objects.get_window_width() - self._size[0]: newX = shared_objects.get_window_width() - self._size[0]

            if newY < self._size[1]: newY = self._size[1]
            elif newY > shared_objects.get_window_height() - self._size[1]: newY = shared_objects.get_window_height() - self._size[1]

        self.set_pos(Vector2(newX, newY))

        if self._position[1] > shared_objects.get_window_height()+self._size[1]: self._position[1] = -self._size[1]
        if self._position[1] > shared_objects.get_window_height()+self._size[1]: self._position[1] = -self._size[1]

    def tick(self):
        pass
