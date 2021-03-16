import unittest
import time
from src.game_state_manager import *

class GSMTestCase(unittest.TestCase):
    def setUp(self):
        self.gsm = GameStateManager()

    def test_state_changes(self):
        # tests that state changes when conditions for change are met
        self.assertEqual(self.gsm.get_state(), GameState.menu)
        self.gsm.start_game()
        self.gsm._tick()
        self.assertEqual(self.gsm.get_state(), GameState.running)
        self.gsm.lives = 0
        self.gsm._tick()
        self.assertEqual(self.gsm.get_state(), GameState.game_over)

    def test_kill_player(self):
        # tests that player dies and lives go down
        self.gsm.start_game()
        self.gsm._tick()
        old_lives = self.gsm.lives
        self.gsm.get_player_ship().setHealth(0)
        self.gsm._tick()
        self.assertEqual(self.gsm.lives, old_lives-1)

    def test_score_increase(self):
        # tests that score goes up when an enemy dies
        self.gsm.start_game()
        self.gsm._tick()
        old_score = self.gsm.game_score
        self.gsm.get_enemies()[0].setHealth(0)
        self.gsm.tick()
        self.assertGreater(old_score, self.gsm.game_score)

    def test_tick_timing(self):
        # tests that ticking is locked to the tick rate

        successful_ticks = 0
        start_time = time.time()
        while successful_ticks < 10:
            if self.gsm._tick():
                successful_ticks += 1

        self.assertEqual((time.time()-start_time)//(1/self.gsm.tick_rate), successful_ticks)

    def tearDown(self):
        self.gsm = None
