# https://docs.python.org/3/library/unittest.html

import unittest
#from main import sum
from main import count_increases
from main import aggregate_measurements

class TestsMain(unittest.TestCase):
#    def test_sum(self):
#        assert sum(1, 1) == 2

    def test_increases_calculation_with_1_measurement(self):
        measurements = [199]
        nr_increases = count_increases(measurements)
        self.assertEqual(nr_increases, 0)

    def test_if_measurements_is_empty(self):
        measurements = []
        nr_increases = count_increases(measurements)
        self.assertEqual(nr_increases, 0)

    def test_with_example_measurements(self):
        measurements = [
            199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263
        ]
        nr_increases = count_increases(measurements)
        self.assertEqual(nr_increases, 7)

    def test_measurements_conversion_to_sliding_windows(self):
        measurements = [
            199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263            
        ]
        expected_measuremet = [
            607,
            618,
            618,
            617,
            647,
            716,
            769,
            792
        ]

        aggregated_measurements = aggregate_measurements(measurements)
        self.assertListEqual(aggregated_measurements,expected_measuremet)

if __name__ == "__main__":
    unittest.main()
