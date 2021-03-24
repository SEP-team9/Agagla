import unittest
from pygame import event
import pygame
from agagla.input_manager import InputManager


class InputManagerTestCase(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.im = InputManager()

    def test_buttons(self):
        self.assertEqual(self.im.get_left(), False)
        self.assertEqual(self.im.get_right(), False)
        self.assertEqual(self.im.get_fire(), False)

        event.post(event.Event(768, {'scancode': 4}))
        self.im.handle_events()

        self.assertEqual(self.im.get_left(), True)
        self.assertEqual(self.im.get_right(), False)
        self.assertEqual(self.im.get_fire(), False)

        event.post(event.Event(768, {'scancode': 7}))
        self.im.handle_events()

        self.assertEqual(self.im.get_right(), True)
        self.assertEqual(self.im.get_left(), True)
        self.assertEqual(self.im.get_fire(), False)

        event.post(event.Event(768, {'scancode': 228}))
        self.im.handle_events()

        self.assertEqual(self.im.get_fire(), True)
        self.assertEqual(self.im.get_left(), True)
        self.assertEqual(self.im.get_right(), True)

        event.post(event.Event(769, {'scancode': 228}))
        self.im.handle_events()

        self.assertEqual(self.im.get_fire(), False)
        self.assertEqual(self.im.get_left(), True)
        self.assertEqual(self.im.get_right(), True)

        event.post(event.Event(769, {'scancode': 4}))
        self.im.handle_events()

        self.assertEqual(self.im.get_fire(), False)
        self.assertEqual(self.im.get_left(), False)
        self.assertEqual(self.im.get_right(), True)

        event.post(event.Event(769, {'scancode': 7}))
        self.im.handle_events()

        self.assertEqual(self.im.get_fire(), False)
        self.assertEqual(self.im.get_left(), False)
        self.assertEqual(self.im.get_right(), False)

    def tearDown(self):
        self.im = None
        pygame.quit()

    if __name__ == '__main__':
        unittest.main()
