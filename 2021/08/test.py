import unittest
from main import (
    example,
    count_obvious_result_patterns,
    process_input_data,
    get_result_number
)

class TestsMain(unittest.TestCase):
    def test_example(self):
        assert example(1, 1) == 2

    def test_count_easy_cyphers_none_input(self):
        expected_result = 0
        input_result_patterns = None
        result = count_obvious_result_patterns(input_result_patterns)

        self.assertEqual(result,expected_result)

    def test_count_easy_cyphers_empty_input(self):
        expected_result = 0
        input_result_patterns = []
        result = count_obvious_result_patterns(input_result_patterns)

        self.assertEqual(result,expected_result)

    def test_count_easy_cyphers(self):
        expected_result = 26
        input_result_patterns = [
            ["fdgacbe", "cefdb", "cefbgd", "gcbe"],
            ["fcgedb", "cgb", "dgebacf", "gc"],
            ["cg", "cg", "fdcagb", "cbg"],
            ["efabcd", "cedba", "gadfec", "cb"],
            ["gecf", "egdcabf", "bgf", "bfgea"],
            ["gebdcfa", "ecba", "ca", "fadegcb"],
            ["cefg", "dcbef", "fcge", "gbcadfe"],
            ["ed", "bcgafe", "cdgba", "cbgef"],
            ["gbdfcae", "bgc", "cg", "cgb"],
            ["fgae", "cfgab", "fg", "bagce"],
        ]
        result = count_obvious_result_patterns(input_result_patterns)

        self.assertEqual(result,expected_result)

    def test_process_input_data_only_results(self):
        input_data=['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf\n']
        expected_output = [
            ["cdfeb", "fcadb", "cdfeb", "cdbaf"]
        ]
        inputs, results=process_input_data(input_data)

        self.assertListEqual(results, expected_output)

    def test_get_result_number_single(self):
        input_data=['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf\n']
        expected_output = "5353"
        inputs, outputs = process_input_data(input_data)
        number = get_result_number(inputs[0], outputs[0])
        self.assertEqual(number, expected_output)

    def test_calc_sum(self):
        expected_output = 61229
        with open("test_input_08.txt") as f:
            data = f.readlines()
        inputs, outputs = process_input_data(data)
        result = 0
        for i in range(len(inputs)):
            number = get_result_number(inputs[i], outputs[i])
            result += int(number)

        self.assertEqual(result, expected_output)        

if __name__ == "__main__":
    unittest.main()
