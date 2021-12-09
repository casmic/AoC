import unittest
from main import (
    example,
    calc_fuel_spent,
    init_crabs,
    calc_cheaper_position
)


class TestsMain(unittest.TestCase):
    def test_example(self):
        assert example(1, 1) == 2

    def test_calc_fuel_spent_position_0(self):
        test_position = 0
        expected_fuel_spent = 49
        crabs_positions = [1, 2, 3, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]

        fuel_spent = calc_fuel_spent(crabs_positions, test_position)
        self.assertEqual(fuel_spent, expected_fuel_spent)

    def test_calc_fuel_spent_position_2(self):
        test_position = 2
        expected_fuel_spent = 37
        crabs_positions = [1, 2, 3, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]

        fuel_spent = calc_fuel_spent(crabs_positions, test_position)
        self.assertEqual(fuel_spent, expected_fuel_spent)

    def test_calc_fuel_spent_position_3(self):
        test_position = 3
        expected_fuel_spent = 39
        crabs_positions = [1, 2, 3, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]

        fuel_spent = calc_fuel_spent(crabs_positions, test_position)
        self.assertEqual(fuel_spent, expected_fuel_spent)

    def test_calc_fuel_spent_position_10(self):
        test_position = 10
        expected_fuel_spent = 71
        crabs_positions = [1, 2, 3, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]

        fuel_spent = calc_fuel_spent(crabs_positions, test_position)
        self.assertEqual(fuel_spent, expected_fuel_spent)

    def test_init_crabs(self):
        crabs_str = "16,1,2,0,4,2,7,1,2,14"
        expected_crabs = [1, 2, 3, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]

        crabs = init_crabs(crabs_str)
        self.assertListEqual(crabs, expected_crabs)

    def test_calc_cheaper_positionA(self):
        crabs = [1, 2, 3, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]
        expected_position = 2
        expected_consumption = 37

        position, consumption = calc_cheaper_position(crabs)
        self.assertEqual(position, expected_position)
        self.assertEqual(consumption, expected_consumption)

    def test_calc_cheaper_positionB(self):
        crabs = [1, 2, 3, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1]
        expected_position = 5
        expected_consumption = 168

        position, consumption = calc_cheaper_position(crabs, 1)
        self.assertEqual(position, expected_position)
        self.assertEqual(consumption, expected_consumption)        

if __name__ == "__main__":
    unittest.main()
