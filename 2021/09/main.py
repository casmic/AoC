#!/usr/bin/python3

from typing import List
from point import Point

def example(value1, value2):
    return value1 + value2

def get_low_points(input_data:Point, low_points:List):
    if(input_data is None):
        return low_points

    if(input_data.isLowPoint()):
        low_points.append(input_data)

    low_points = get_low_points(input_data._right, low_points)

    if(input_data._left is None):
        low_points = get_low_points(input_data._down, low_points)

    return low_points


def calc_risk_level(low_points):
    result = 0
    for point in low_points:
        result += point._risk

    return result
    
def calc_basin_size(point:Point, size):
    if(point is None or point._visited or point._value==9):
        return size

    point._visited = True
    size += 1

    size = calc_basin_size(point._down, size)
    size = calc_basin_size(point._left, size)
    size = calc_basin_size(point._up, size)
    size = calc_basin_size(point._right, size)

    return size        

def calc_total_three_largest_basins_size(low_points):
    sizes = []
    return_val=0
    for point in low_points:
        sizes.append(calc_basin_size(point, 0))

    sizes.sort(reverse=True)
    if(len(sizes)>2):
        return_val=1
        for x in sizes[:3]:
            return_val *= x

    return return_val

def ProcessInputLine(line, head:Point , left_point:Point, up_point:Point):
    point = Point(int(line[0]))
    next_up_point = None

    if(head is None):
        head = point

    if(left_point is not None):
        point._left = left_point
        left_point._right = point
    else:
        left_point = point

    if(up_point is not None):
        point._up = up_point
        up_point._down = point
        next_up_point = up_point._right

    if(len(line)==1):
        return point
    else:
        head._right=ProcessInputLine(line[1:], head._right, point, next_up_point)
        return head

def read_input(filename):
    input_data=[]
    cursor_point = top_left_point = None
    with open(filename) as f:
        lines = f.readlines()
        cursor_point = None
        up = None
        for i in range(len(lines)):
            cursor_point=ProcessInputLine(lines[i].strip(), cursor_point, None, up)
            if (i == 0):
                top_left_point = cursor_point
            up = cursor_point
            cursor_point = None

    return top_left_point

if __name__ == "__main__":

    low_points = []
    input_data = read_input("input_09.txt")
    low_points = get_low_points(input_data, low_points)

    risk_level = calc_risk_level(low_points)

    print("09A - risk level:", risk_level)

    total_basins_size = calc_total_three_largest_basins_size(low_points)
    print("09B - total basins size:", total_basins_size)
    pass
