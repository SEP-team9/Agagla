from agagla.entity import Entity


class Ship(Entity):

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_type(self, type):
        self.type = type

    def render(self):
        self.render()


