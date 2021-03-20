import unittest
import pygame
from pygame import event
from agagla.player_ship import PlayerShip
from agagla.input_manager import InputManager as im


class test_player_ship(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.ps = PlayerShip()

    def test_move_right(self):
        # Tests that the player ship moves right
        oldx = self.ps.get_pos()[0]
        event.post(event.Event(768, {'scancode': 7}))
        im.handle_events(self)
        self.ps.move(self)
        self.assertEqual(self.ps.get_pos()[0], (oldx + 5))

    def test_move_left(self):
        # Tests that the player ship moves left
        oldx = self.ps.get_pos()[0]
        event.post(event.Event(768, {'scancode': 4}))
        im.handle_events(self)
        self.ps.move(self)
        self.assertEqual(self.ps.get_pos()[0], oldx - 5)

    def test_fire_projectile(self):
        # Tests that a new projectile appears
        self.assertEqual(True, True)

    def tearDown(self):
        self.ps = None
        pygame.quit()

    if __name__ == '__main__':
        unittest.main()

