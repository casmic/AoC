# https://docs.python.org/3/library/unittest.html

import unittest

from main import (
    calculate_gamma_rate,
    calculate_epsilon_rate,
    consumption_of_the_submarine,
    oxygen_rating,
    co2_scrubbing,
    read_input_data,
    _calculate_counter,
    _filter_diagnostic_report,
    calculate_life_support_rating
)


class TestsMain(unittest.TestCase):
    def test_calculate_gamma_rate(self):
        diagnostic_report = read_input_data("test_input_03.txt")
        self.assertEqual(calculate_gamma_rate(diagnostic_report), 22)

    def test_calculate_epsilon_rate(self):
        diagnostic_report = read_input_data("test_input_03.txt")
        self.assertEqual(calculate_epsilon_rate(diagnostic_report), 9)

    def test_calculate_oxygen_rating(self):
        diagnostic_report = read_input_data("test_input_03.txt")
        self.assertEqual(oxygen_rating(diagnostic_report), 23)

    def test_calculate_co2_scrubbing(self):
        diagnostic_report = read_input_data("test_input_03.txt")
        self.assertEqual(co2_scrubbing(diagnostic_report), 10)

    def test_consumption_of_the_submarine(self):
        diagnostic_report = read_input_data("test_input_03.txt")
        self.assertEqual(consumption_of_the_submarine(diagnostic_report), 198)

    def test_filter_diagnostic_report_higher(self):
        diagnostic_report = read_input_data("test_input_03.txt")
        self.assertEqual(_filter_diagnostic_report(diagnostic_report, [0], True), "10111")

    def test_filter_diagnostic_report_lower(self):
        diagnostic_report = read_input_data("test_input_03.txt")
        self.assertEqual(_filter_diagnostic_report(diagnostic_report, [0], False), "01010")

    def test_life_support_rating(self):
        diagnostic_report = read_input_data("test_input_03.txt")
        expected_rating=230
        self.assertEqual(calculate_life_support_rating(diagnostic_report), expected_rating)

    def test_calculate_counter_range_0(self):
        diagnostic_report = [
            "000000"
        ]
        bit_range=[0]
        self.assertEqual(_calculate_counter(diagnostic_report, bit_range), [-1])

    def test_calculate_counter_range_middle(self):
        diagnostic_report = [
            "000000"
        ]
        bit_range=[1,2,3]
        self.assertEqual(_calculate_counter(diagnostic_report, bit_range), [-1, -1, -1])        

    def test_nrt_length_binary_number_is_taken_into_account(self):
        diagnostic_report = [
            "000000",
        ]
        self.assertEqual(consumption_of_the_submarine(diagnostic_report), 0)
    
    def test_nrt_strip_end_of_line(self):
        diagnostic_report = read_input_data("test_input_03.txt")
        self.assertEqual(consumption_of_the_submarine(diagnostic_report), 198)


if __name__ == "__main__":
    unittest.main()
