import unittest
from agagla.high_score_database import HighScoreDatabase


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.hsdb = HighScoreDatabase()

    def test_get_scores(self):
        scores = self.hsdb.get_high_score()
        self.assertEqual(len(scores), 10)

    def test_add_score(self):
        did_it = self.hsdb.add_high_score('test_no_add', 1)
        self.assertEqual(did_it, False)
        did_it = self.hsdb.add_high_score('test_add', 500)
        self.assertEqual(did_it, True)

    def tearDown(self):
        self.hsdb = None

if __name__ == '__main__':
    unittest.main()
