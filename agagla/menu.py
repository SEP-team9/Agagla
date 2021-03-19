import pygame

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080


class Menu:

    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.font_large = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 40)
        self.font_small = pygame.font.Font("../data/fonts/arcadeclassic.regular.ttf", 30)

    def render(self):
        textsurface = self.font_large.render('Agagla', False, (255, 255, 255))
        self.screen.blit(textsurface, ((WINDOW_WIDTH / 2) - (textsurface.get_width() / 2), (WINDOW_HEIGHT / 2) - 200))

        textsurface = self.font_small.render('Press    fire    to    start', False, (255, 255, 255))
        self.screen.blit(textsurface, ((WINDOW_WIDTH / 2) - (textsurface.get_width() / 2), (WINDOW_HEIGHT / 2) - 100))

        from game_state_manager import GameStateManager
        if GameStateManager.get_instance().get_input_manager().get_fire():
            GameStateManager.get_instance().start_game()

        return None
