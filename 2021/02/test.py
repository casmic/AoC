# https://docs.python.org/3/library/unittest.html

import unittest
from main import process_command
from main import process_inputA
from main import process_inputB
#from main import sum


class TestsMain(unittest.TestCase):
#    def test_sum(self):
#        assert sum(1, 1) == 2


    def test_process_empty_command(self):
        command=[]
        expected_result=[0 , 0]
        result = process_command(command)
        self.assertListEqual(result,expected_result)

    def test_process_command_forward(self):
        command=['forward', 5]
        expected_result=[5 , 0]
        result = process_command(command)
        self.assertListEqual(result,expected_result)

    def test_process_command_up(self):
        command=['up',3]
        expected_result=[0 , -3]
        result = process_command(command)
        self.assertListEqual(result,expected_result)

    def test_process_command_down(self):
        command=['down',5]
        expected_result=[0 , 5]
        result = process_command(command)
        self.assertListEqual(result,expected_result)

    def test_process_command_wrong_command(self):
        command=['does_not_exist',5]
        expected_result=[0 , 0]
        result = process_command(command)
        self.assertListEqual(result,expected_result)

    def test_calculation_final_result(self):
        infile='test_input_02.txt'
        expected_result=150
        result=process_inputA(infile)
        self.assertEqual(result,expected_result)

    def test_calculation_final_resultB(self):
        infile='test_input_02.txt'
        expected_result=900
        result=process_inputB(infile)
        self.assertEqual(result,expected_result)

if __name__ == "__main__":
    unittest.main()
