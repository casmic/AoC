#!/usr/bin/python3
from typing import Dict, List
from unittest import result


def example(value1, value2):
    return value1 + value2

def cut_dead_leaves(graph):
    keys_to_delete=[]
    for key in graph.keys():
        if(len(graph[key])== 1 and graph[key][0] == graph[key][0].casefold()):
            keys_to_delete.append((key, graph[key][0]))

    for key, val in keys_to_delete:
        value = graph[key][0]
        del(graph[key])
        graph[val].remove(key)

    return graph

def fill_map_graph(data):
    result_dict = {}

    for line in data:
        elems = line.strip().split('-')
        for elem in elems:
            if elem not in result_dict.keys():
                result_dict[elem] = []
        result_dict[elems[0]].append(elems[1])
        result_dict[elems[1]].append(elems[0])

    result_dict = cut_dead_leaves(result_dict)
    return result_dict

def get_path_number(graph:Dict, can_duplicate):    
    paths_list = [(('start',), not can_duplicate)]
    paths_count = 0

    while len(paths_list) > 0:
        print("paths_list:", paths_list)
        path, duplicate = paths_list.pop()
        print("path, duplicate:", path, duplicate)
        if path[-1] == 'end':
            paths_count += 1
        else:
            print(f"neighbours of {path[-1]}:", graph[path[-1]])
            for neighbour in graph[path[-1]]:
                if neighbour.isupper() or neighbour not in path:
                    paths_list.append((path + (neighbour,), duplicate))
                    print("work in loop1:", paths_list)
                elif not duplicate and neighbour != 'start':
                    paths_list.append((path + (neighbour,), True))
                    print("work in loop2:", paths_list)
    
    return paths_count


if __name__ == "__main__":
    filename = "input_12.txt"
    data_dict = {}
    data_graph = {}

    with open(filename) as f:
        input_data = f.readlines()

    data_graph = fill_map_graph(input_data)
    paths_number = get_path_number(data_graph, False)

    print("12A paths number:", paths_number)
    
    paths_number = get_path_number(data_graph, True)
    print("12B paths number:", paths_number)
