import unittest
from octopus import Octopus
from main import (
    build_octopus_matrix,
    step_matrix
)

class TestsMain(unittest.TestCase):
    def test_flashes_numbers_10_steps(self):
        expected_result = 204
        result = 0
        filename = "test_input_11.txt"
        with open(filename) as f:
            input_data = f.readlines()
        
        octopus_matrix = build_octopus_matrix(input_data)        
        
        for i in range(10):
            result += step_matrix(octopus_matrix)

        self.assertEqual(result, expected_result)

    def test_flashes_numbers_100_steps(self):
        expected_result = 1656
        result = 0
        filename = "test_input_11.txt"
        with open(filename) as f:
            input_data = f.readlines()
        
        octopus_matrix = build_octopus_matrix(input_data)        
        
        for i in range(100):
            result += step_matrix(octopus_matrix)

        self.assertEqual(result, expected_result)        
        
    def test_find_first_step_all_resets(self):
        expected_result = 195
        result = 0
        filename = "test_input_11.txt"
        with open(filename) as f:
            input_data = f.readlines()
        
        octopus_matrix = build_octopus_matrix(input_data)        
        matrix_size = len(octopus_matrix) * len(octopus_matrix[0])
        
        while True:
            result += 1
            count = step_matrix(octopus_matrix)
            if(count == matrix_size):
                break

        self.assertEqual(result, expected_result)                

if __name__ == "__main__":
    unittest.main()
