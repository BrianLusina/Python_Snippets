import unittest

def square_odds(num_list):


class SquareOddTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual("1,3,5,7,9", square_odds("1,2,3,4,5,6,7,8,9"))