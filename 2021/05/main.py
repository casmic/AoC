from contextlib import contextmanager
from Vent import *
from Map import *

def example(value1, value2):
    return value1 + value2

def count_overlaps(map):

    return(map._intersections_count)

def draw_vents_on_map(vents, map, only_ortogonals):
    for vent in vents:
        map.DrawVent(vent, only_ortogonals)

def init_map_vents(filename, only_ortogonals=True):
    return_vents = []
    return_map = []
    max_x = 0
    max_y = 0

    with open(filename) as f:
        file_content = f.readlines()
        
        for line in file_content:
            new_vent = Vent(line.strip())
            if(new_vent._is_ortogonal or only_ortogonals == False):
                if(new_vent._max_x > max_x):
                    max_x = new_vent._max_x
                if(new_vent._max_y > max_y):
                    max_y = new_vent._max_y
                return_vents.append(new_vent)
    
    return_map = Map(max_x+1, max_y+1)
    return return_vents, return_map


if __name__ == "__main__":
    input_file = 'input_05.txt'
    vents, map = init_map_vents(input_file, True)

    draw_vents_on_map(vents, map, True)
    overlaps = count_overlaps(map)
    print("05A - overlaps:", overlaps)

    vents, map = init_map_vents(input_file, False)
    draw_vents_on_map(vents, map, False)
    overlaps = count_overlaps(map)
    print("05B - overlaps:", overlaps)
