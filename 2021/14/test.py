import unittest
from main import (
    read_template_rules,
    subratct_more_common_less_common,
    polymer_insert
)

class TestsMain(unittest.TestCase):

    def test_read_template_rules(self):
        filename = "test_input_14.txt"
        expected_template = "NNCB"
        expected_rules_length = 16

        template, rules = read_template_rules(filename)

        self.assertEqual(template, expected_template)
        self.assertEqual(len(rules), expected_rules_length)

    def test_template_insert_1(self):
        filename = "test_input_14.txt"
        expected_elems_count = {'B': 2, 'N': 2, 'H': 1, 'C': 2}

        template, rules = read_template_rules(filename)
        elems_count = polymer_insert(template, rules, 1)

        self.assertDictEqual(elems_count, expected_elems_count)

    def test_template_insert_2(self):
        filename = "test_input_14.txt"
        expected_elems_count = {'B': 6, 'C': 4, 'H': 1, 'N': 2}

        template, rules = read_template_rules(filename)
        elems_count = polymer_insert(template, rules, 2)

        self.assertDictEqual(elems_count, expected_elems_count)

    def test_elems_difference(self):
        filename = "test_input_14.txt"
        expected_result = 1588

        template, rules = read_template_rules(filename)
        elems_count = polymer_insert(template, rules, 10)
        result = subratct_more_common_less_common(elems_count)

        self.assertEqual(result, expected_result)

    def test_elems_difference_40_steps(self):
        filename = "test_input_14.txt"
        expected_result = 2188189693529

        template, rules = read_template_rules(filename)
        elems_count = polymer_insert(template, rules, 40)
        result = subratct_more_common_less_common(elems_count)

        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()