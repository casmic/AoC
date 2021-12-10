import unittest
from delimiter import Delimiter

from main import (
    example,
    process_input_line,
    process_input_data,
    calc_completion_score,
    calc_middle_completion_score
)

class TestsMain(unittest.TestCase):
    def test_example(self):
        assert example(1, 1) == 2

    def test_recognize_opening_char_true(self):
        chunk = Delimiter("<")
        self.assertEqual(chunk.is_opening_char(), False)

    def test_recognize_opening_char_true(self):
        chunk = Delimiter("{")
        self.assertEqual(chunk.is_opening_char(), True)

    def test_corruption_score_single_line(self):
        input_data = "{([(<{}[<>[]}>{[]{[(<()>"
        expected_result = 1197

        chunk_list, corruption = process_input_line(input_data)
        self.assertEqual(corruption, expected_result)

    def test_corruption_score_multiple(self):
        with open("test_input_10.txt") as f:
            input_data = f.readlines()

        expected_result = 26397
        chunk_list, corruption = process_input_data(input_data)
        self.assertEqual(corruption, expected_result)

    def test_completion_score_single(self):
        input_data_str = "<{([{{}}[<[[[<>{}]]]>[]]"
        expected_result = 294

        delimiters_list, corruption = process_input_line(input_data_str)
        completion_score = calc_completion_score(delimiters_list, 0)
        self.assertEqual(completion_score, expected_result)

    def test_completion_score_middle(self):
        expected_result = 288957
        with open("test_input_10.txt") as f:
            input_data = f.readlines()        

        chunk_list, corruption = process_input_data(input_data)
        result = calc_middle_completion_score(chunk_list)
        self.assertEqual(result, expected_result)
        
if __name__ == "__main__":
    unittest.main()
