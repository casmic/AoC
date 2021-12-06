# https://docs.python.org/3/library/unittest.html

import unittest
from Vent import *
from Map import *
from main import (
    draw_vents_on_map,
    example,
    count_overlaps,
    init_map_vents
)


class TestsMain(unittest.TestCase):
    def test_example(self):
        assert example(1, 1) == 2

    def _test_count_overlaps(self,expected_overlaps, only_ortogonals):
        
        input_file = 'test_input_05.txt'
        vents, map = init_map_vents(input_file, only_ortogonals)
        draw_vents_on_map(vents, map, only_ortogonals)
        print(map)
        overlaps = count_overlaps(map)
        return overlaps

    def test_count_overlapsA(self):
        expected_overlaps = 5
        overlaps = self._test_count_overlaps(expected_overlaps, True)
        self.assertEqual(overlaps,expected_overlaps)

    def test_count_overlapsB(self):
        expected_overlaps = 12
        overlaps = self._test_count_overlaps(expected_overlaps, False)
  
        self.assertEqual(overlaps,expected_overlaps)
    

    def test_vent_init_horizontal(self):
        input_vent = '0,9 -> 5,9'

        test_vent = Vent(input_vent)
        expected_vent = Vent()

        expected_vent._x1 = 0
        expected_vent._x2 = 5
        expected_vent._y1 = 9
        expected_vent._y2 = 9
        expected_vent._max_x = 5
        expected_vent._max_y = 9
        expected_vent._is_ortogonal = True

        self.assertEqual(expected_vent,test_vent)

    def test_vent_init_vertical(self):
        input_vent = '7,0 -> 7,4'

        test_vent = Vent(input_vent)
        expected_vent = Vent()

        expected_vent._x1 = 7
        expected_vent._x2 = 7
        expected_vent._y1 = 0
        expected_vent._y2 = 4
        expected_vent._max_x = 7
        expected_vent._max_y = 4
        expected_vent._is_ortogonal = True

        self.assertEqual(expected_vent,test_vent)

    def test_read_vents(self):
        input_file = 'test_input_05.txt'

        result_vents, result_map = init_map_vents(input_file, False)
        pass

    def test_draw_map(self):
        input_file = 'test_input_05.txt'
        vents, map = init_map_vents(input_file, False)

        draw_vents_on_map(vents, map, True)

if __name__ == "__main__":
    unittest.main()
