import unittest
from main import (
    fill_map_graph,
    get_path_number
)


class TestsMain(unittest.TestCase):
    def test_fill_map_graph(self):
        filename = "test_1_input_12.txt"

        data_graph = {}
        with open(filename) as f:
            input_data = f.readlines()

        data_graph = fill_map_graph(input_data)
        print(data_graph)
        self.assertEqual(1,1)

    def test_get_pahts_number(self):
        filename = "test_1_input_12.txt"
        expected_result = 10
        data_graph = {}

        with open(filename) as f:
            input_data = f.readlines()

        data_graph = fill_map_graph(input_data)
        result = get_path_number(data_graph, False)

        self.assertEqual(result, expected_result)        

if __name__ == "__main__":
    unittest.main()
