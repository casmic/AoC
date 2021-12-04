# https://docs.python.org/3/library/unittest.html

import unittest
from main import (
    example,
    get_winner_score,
    read_input_data
)


class TestsMain(unittest.TestCase):
    def test_example(self):
        assert example(1, 1) == 2

    def test_calculate_final_scoreA(self):

        draws = []
        boards = []


        draws, boards = read_input_data("test_input_04.txt")
        results=get_winner_score(boards, draws)
        self.assertEqual(results[0], 4512)

    def test_calculate_final_scoreA(self):

        draws = []
        boards = []


        draws, boards = read_input_data("test_input_04.txt")
        results=get_winner_score(boards, draws)
        result=results[len(results)-1]
        self.assertEqual(result, 1924)        

    def test_reading_input_draws(self):
        expected_drawns = [
            7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
        ]

        draws = []
        boards = []

        draws, boards = read_input_data("test_input_04.txt")
        self.assertListEqual(expected_drawns,draws)

if __name__ == "__main__":
    unittest.main()
