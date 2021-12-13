import unittest
from main import (
    example,
    count_trees_on_track,
    calc_trees_multiple_slopes
)

class TestsMain(unittest.TestCase):
    def test_example(self):
        assert example(1, 1) == 2

    def test_count_trees_3_1(self):
        input_file = "test_03.in"
        expected_result = 7
        with open(input_file) as f:
            slopes = f.readlines()

        result = count_trees_on_track(slopes, 3, 1)
        self.assertEqual(result, expected_result)
        
    def test_count_trees_1_2(self):
        input_file = "test_03.in"
        expected_result = 2
        with open(input_file) as f:
            slopes = f.readlines()

        result = count_trees_on_track(slopes, 1, 2)
        self.assertEqual(result, expected_result)

    def test_count_trees_on_track(self):
        input_file = "test_03.in"
        expected_result = 336
        with open(input_file) as f:
            slopes = f.readlines()

        result = calc_trees_multiple_slopes(slopes)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
