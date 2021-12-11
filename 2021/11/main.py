#!/usr/bin/python3
from logging import Manager
from typing import List
from octopus import Octopus

def build_octopus_line(octopus_line, line_index):
    result = []
    for i in range(len(octopus_line)):
        result.append(Octopus(int(octopus_line[i]), i, line_index))

    return result

def build_octopus_matrix(input_data):
    result_matrix = []
    for i in range(len(input_data)):
        result_matrix.append(build_octopus_line(input_data[i].strip(), i))

    return result_matrix

def print_matrix(matrix):

    for line in matrix:
        string = "".join([str(oct._energy) for oct in line])
        print(string)
    
def flash_adjacents(octopus:Octopus, matrix:List, flashing_list: List):
    min_x = min_y = max_x = max_y = 0
    x = octopus._x
    y = octopus._y

    min_x = x - 1
    if(min_x < 0):
        min_x = 0

    max_x = x + 1
    if(max_x >= len(matrix[0])):
        max_x = x

    min_y = y - 1 
    if(min_y < 0):
        min_y = 0

    max_y = y + 1
    if(max_y >= len(matrix)):
        max_y = y

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y+1):
            if(matrix[y][x].Step()):
                flashing_list.append(matrix[y][x])

    return flashing_list

def flash_octopuses(flashing_octopuses:List, matrix:List, number:int):
    if(flashing_octopuses is None or len(flashing_octopuses) == 0):
        return number

    octopus = flashing_octopuses.pop(0)
    number += 1
    flashing_octopuses = flash_adjacents(octopus, matrix, flashing_octopuses)
    return flash_octopuses(flashing_octopuses, matrix, number)


def step_matrix(matrix):
    flashing_octopuses = []
    count_flashes = 0
    for line in matrix:
        for octopus in line:
            if(octopus.Step()):
                flashing_octopuses.append(octopus)

    count_flashes = flash_octopuses(flashing_octopuses, matrix, 0)
    reset_matrix(matrix)   

    return count_flashes

def reset_matrix(matrix):
    resets_count = 0
    for line in matrix:
        for octopus in line:
            octopus.Reset()

if __name__ == "__main__":
    filename = "input_11.txt"
    result = 0

    with open(filename) as f:
        input_data = f.readlines()

    octopus_matrix = build_octopus_matrix(input_data)
    matrix_size = len(octopus_matrix) * len(octopus_matrix[0])

    for i in range(100):
        result += step_matrix(octopus_matrix)
    print("11A total flashes:", result)

    octopus_matrix = build_octopus_matrix(input_data)
    result = 0
    while True:
        result += 1
        count = step_matrix(octopus_matrix)
        if(count == matrix_size):
            break 
    print("11B first step total flash:", result)