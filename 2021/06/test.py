# https://docs.python.org/3/library/unittest.html

import unittest
from main import (
    example,
    get_lanternfish_number,
    init_fishes,
    grow_fishes
)


class TestsMain(unittest.TestCase):
    def test_example(self):
        assert example(1, 1) == 2

    def test_input_fishes(self):
        expected_result = [0, 1, 1 , 2, 1, 0, 0, 0, 0] # [3, 4, 3, 1 ,2]
        input_fishes_str = "3,4,3,1,2"
        fishes = init_fishes(input_fishes_str)
        self.assertListEqual(expected_result, fishes)

    def test_grow_fishes_18_days(self):
        input_fishes = [0, 1, 1 , 2, 1, 0, 0, 0, 0]
        days_of_test = 18
        expected_fishes = 26

        fishes = grow_fishes(input_fishes, days_of_test)
        self.assertEqual(expected_fishes, sum(fishes))

    def test_grow_fishes_80_days(self):
        days_of_test = 80
        expected_fishes = 5934
        input_fishes = [0, 1, 1 , 2, 1, 0, 0, 0, 0]
        fishes = grow_fishes(input_fishes, days_of_test)
        self.assertEqual(expected_fishes, sum(fishes))

    def test_grow_fishes_256_days(self):
        days_of_test = 256
        expected_fishes = 26984457539
        input_fishes = [0, 1, 1 , 2, 1, 0, 0, 0, 0]
        fishes = grow_fishes(input_fishes, days_of_test)
        self.assertEqual(expected_fishes, sum(fishes))



if __name__ == "__main__":
    unittest.main()
