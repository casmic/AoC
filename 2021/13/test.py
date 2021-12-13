import unittest
from main import (
    count_visible_dots,
    fill_paper_folds
)



class TestsMain(unittest.TestCase):

    def test_fill_paper_folds(self):
        filename = 'test_input_13.txt'
        expected_result = 17
        paper= []
        folds = []

        paper, folds = fill_paper_folds(filename)
        pass

    def test_count_visible_dots_single_fold(self):
        filename = 'test_input_13.txt'
        folds_number = 1
        expected_result = 17
        folds = []
        paper, folds = fill_paper_folds(filename)
        result = count_visible_dots(paper, folds, folds_number)
        self.assertEqual(result, expected_result)

    def test_count_visible_dots_double_fold(self):
        filename = 'test_input_13.txt'
        folds_number = 2
        expected_result = 16
        folds = []
        paper, folds = fill_paper_folds(filename)
        result = count_visible_dots(paper, folds, folds_number)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
