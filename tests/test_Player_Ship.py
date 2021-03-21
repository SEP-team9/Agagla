import unittest
import pygame
from agagla.player_ship import PlayerShip
from agagla.projectile import Projectile

class test_player_ship(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.ps = PlayerShip(500, 500)

    def test_move_right(self):
        # Tests that the player ship moves right
        oldx = self.ps.get_pos()[0]
        oldy = self.ps.get_pos()[1]
        self.ps.move(5)
        self.assertEqual(self.ps.get_pos()[0], (oldx + 5))
        self.assertEqual(self.ps.get_pos()[1], oldy)

        # Tests that the player ship moves left
        oldx = self.ps.get_pos()[0]
        oldy = self.ps.get_pos()[1]
        self.ps.move(-5)
        self.assertEqual(self.ps.get_pos()[0], oldx - 5)
        self.assertEqual(self.ps.get_pos()[1], oldy)

    def test_fire_projectile(self):
        # Tests that a new projectile appears
        newproj = self.ps.fire_projectile()
        self.assertIsInstance(newproj, Projectile)

    def tearDown(self):
        self.ps = None
        pygame.quit()

    if __name__ == '__main__':
        unittest.main()

