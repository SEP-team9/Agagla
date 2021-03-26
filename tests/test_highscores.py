import unittest
from agagla import high_score_database
import pymysql
from pymysql import Error

from agagla.high_score_database import HighScoreDatabase


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.hsdb = HighScoreDatabase()

    def test_get_scores(self):
        scores = self.hsdb.get_high_score()
        self.assertIsNot(scores,0)

    def test_add_score(self):
        scores = self.hsdb.get_high_score()
        didit= self.hsdb.add_high_score('test2', 500)
        self.assertEqual(didit, True)

if __name__ == '__main__':
    unittest.main()
