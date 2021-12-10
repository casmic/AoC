import unittest
from policy import Policy
from password import Password

from main import example


class TestsMain(unittest.TestCase):
    def test_example(self):
        assert example(1, 1) == 2

    def test_policy_init(self):
        input_str = "1-3 a"
        expected_result = Policy()
        expected_result._max = 3 
        expected_result._min = 1
        expected_result._character = "a"

        result = Policy(input_str)
        self.assertEqual(result==expected_result, True)

    def test_password_init(self):
        input_data_str = "1-3 a: abcde"
        expected_result = Password()
        expected_result._policy = Policy("1-3 a")
        expected_result._password = "abcde"

        result = Password(input_data_str)
        self.assertEqual(result==expected_result, True)

    def test_password_valid_true(self):
        input_data_str = "1-3 a: abcde"
        passwd = Password(input_data_str) 
        expected_result = True
        valida, validb = passwd.IsValid()
        self.assertEqual(valida, expected_result)

    def test_password_valid_false(self):
        input_data_str = "1-3 b: cdefg"
        passwd = Password(input_data_str) 
        expected_result = False
        valida, validb = passwd.IsValid()
        self.assertEqual(valida, expected_result)

if __name__ == "__main__":
    unittest.main()
