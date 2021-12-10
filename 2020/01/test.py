import unittest
from main import (
    example,
    get_first_two_numbers,
    get_first_three_numbers
)


class TestsMain(unittest.TestCase):
    def test_example(self):
        assert example(1, 1) == 2

    def test_get_first_two_numbers(self):
        expected_result = [1721, 299]
        input_data = [
            1721,
            979,
            366,
            299,
            675,
            1456,
        ]

        result = get_first_two_numbers(input_data, 2020)
        self.assertListEqual(result, expected_result)

    def test_get_first_three_numbers(self):
        expected_result = [979, 366, 675]
        input_data = [
            1721,
            979,
            366,
            299,
            675,
            1456,
        ]

        result = get_first_three_numbers(input_data, 2020)
        self.assertListEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
