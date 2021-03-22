import unittest
import pygame
from agagla.player_ship import PlayerShip
from pygame.math import Vector2

class test_player_ship(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.ps = PlayerShip(Vector2(0,0))

    def test_move(self):
        # Test initial position
        self.assertEqual(self.ps.get_pos(), (960, 1050))

        # Tests that the player ship moves right
        oldx = self.ps.get_pos()[0]
        oldy = self.ps.get_pos()[1]
        self.ps.move(self.ps.velocity, 0)
        self.assertEqual(self.ps.get_pos()[0], (oldx+self.ps.velocity))
        self.assertEqual(self.ps.get_pos()[1], oldy)

        # Tests that the player ship moves left
        oldx = self.ps.get_pos()[0]
        oldy = self.ps.get_pos()[1]
        self.ps.move(-self.ps.velocity, 0)
        self.assertEqual(self.ps.get_pos()[0], oldx-self.ps.velocity)
        self.assertEqual(self.ps.get_pos()[1], oldy)

    def tearDown(self):
        self.ps = None
        pygame.quit()

    if __name__ == '__main__':
        unittest.main()

