import unittest
import pygame
from agagla.player_ship import PlayerShip
from agagla.game_state_manager import GameStateManager

class test_player_ship(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.ps = PlayerShip(self, 100, 0)

    def test_move_right(self):
        # Tests that the player ship moves right
        im = GameStateManager.get_input_manager()
        oldx = self.x
        l = True
        self.assertEqual(self.x, oldx - 10)
        self.assertEqual(True, False)

    def test_move_left(self):
        # Tests that the player ship moves left
        oldx = self.x
        r = True
        self.assertEqual(self.x, oldx + 10)

    def test_fire_projectile(self):
        # Tests that a new projectile appears
        self.assertEqual(True, False)

    def tearDown(self):
        self.ps = None
        pygame.quit()

    if __name__ == '__main__':
        unittest.main()

