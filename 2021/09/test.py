import unittest
from main import (
    calc_basin_size,
    example,
    read_input,
    calc_risk_level,
    get_low_points,
    calc_total_three_largest_basins_size
)


class TestsMain(unittest.TestCase):
    def test_example(self):
        assert example(1, 1) == 2

 #   def test_read_input(self):
 #       input_file="test_input_09.txt"
 #       expected_result = [
 #           [99,99,99,99,99,99,99,99,99,99,99,99],
 #           [99,2,1,9,9,9,4,3,2,1,0,99],
 #           [99,3,9,8,7,8,9,4,9,2,1,99],
 #           [99,9,8,5,6,7,8,9,8,9,2,99],
 #           [99,8,7,6,7,8,9,6,7,8,9,99],
 #           [99,9,8,9,9,9,6,5,6,7,8,99],
 #           [99,99,99,99,99,99,99,99,99,99,99,99]
 #       ]

 #       result = read_input(input_file)
 #       self.assertListEqual(result, expected_result)

    def test_calc_risk_level(self):
        input_file="test_input_09.txt"
        expected_result = 15
        low_points = []

        input_data = read_input(input_file)
        low_points = get_low_points(input_data, low_points)
        sum_low_points=calc_risk_level(low_points)

        self.assertEqual(sum_low_points, expected_result)

    def test_calc_basin_size_0(self):
        input_file="test_input_09.txt"
        expected_result = 3
        low_points = []

        input_data = read_input(input_file)
        low_points = get_low_points(input_data, low_points)
        result = calc_basin_size(low_points[0],0)
        self.assertEqual(result,expected_result)

    def test_calc_basin_size_1(self):
        input_file="test_input_09.txt"
        expected_result = 9
        low_points = []

        input_data = read_input(input_file)
        low_points = get_low_points(input_data, low_points)
        result = calc_basin_size(low_points[1],0)
        self.assertEqual(result,expected_result)

    def test_calc_basin_size_2(self):
        input_file="test_input_09.txt"
        expected_result = 14
        low_points = []

        input_data = read_input(input_file)
        low_points = get_low_points(input_data, low_points)
        result = calc_basin_size(low_points[2],0)
        self.assertEqual(result,expected_result)        

    def test_calc_basin_size_3(self):
        input_file="test_input_09.txt"
        expected_result = 9
        low_points = []

        input_data = read_input(input_file)
        low_points = get_low_points(input_data, low_points)
        result = calc_basin_size(low_points[3],0)
        self.assertEqual(result,expected_result)

    def test_calc_mult_largest_basins(self):
        input_file="test_input_09.txt"
        expected_result = 1134
        low_points = []

        input_data = read_input(input_file)
        low_points = get_low_points(input_data, low_points)
        result = calc_total_three_largest_basins_size(low_points)

        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
