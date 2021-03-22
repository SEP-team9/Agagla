import unittest
import pygame
from agagla import game_state_manager
from agagla.game_state_manager import GameState
import time


class GSMTestCase(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.gsm = game_state_manager.GameStateManager.get_instance()

    def test_state_changes(self):
        # tests that state changes when conditions for change are met
        self.assertEqual(self.gsm.get_state(), GameState.menu)
        self.gsm.start_game()
        self.gsm._force_tick()
        self.assertEqual(self.gsm.get_state(), GameState.running)
        self.gsm.lives = 0
        self.gsm._force_tick()
        self.assertEqual(self.gsm.get_state(), GameState.game_over)

    def test_kill_player(self):
        # tests that player dies and lives go down
        self.gsm.start_game()
        self.gsm._force_tick()
        old_lives = self.gsm.lives
        self.gsm.get_player_ship().set_health(0)
        self.gsm._force_tick()
        self.assertEqual(old_lives - 1, self.gsm.lives)

    def test_score_increase(self):
        # tests that score goes up when an enemy dies
        self.gsm.start_game()
        self.gsm._force_tick()
        old_score = self.gsm.game_score
        self.gsm.get_enemies()[0].set_health(0)
        self.gsm._force_tick()
        self.assertGreater(self.gsm.game_score, old_score)

    def test_tick_timing(self):
        # tests that ticking is locked to the tick rate

        successful_ticks = 0
        start_time = time.time()
        while successful_ticks < 10:
            if self.gsm._tick():
                successful_ticks += 1

        self.assertEqual((time.time() - start_time) // (1 / self.gsm.tick_rate), successful_ticks)

    def tearDown(self):
        self.gsm = None
        game_state_manager.GameStateManager._instance = None
        pygame.quit()

    if __name__ == '__main__':
        unittest.main()
