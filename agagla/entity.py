class Entity:

    def __init__(self, type, x, y, health):
        self.health = health
        self.type = type
        self.x = x
        self.y = y

    def get_pos(self):
        return self.x, self.y

    def get_type(self):
        return self.type

    def get_health(self):
        return self.health

    def render(self):
        self.render()