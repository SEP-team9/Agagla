
class Enemy(Ship):
    def __init__(self, type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy1.png
        self.health = 1
        self.type = type
        self.rect = self.image.get_rect()
        #self.rect = Rect(x, y, 10, 10)

    def get_type(self):
        return self.type

    def render(self):
        screen.blit(self.image, self.rect)
        return None
