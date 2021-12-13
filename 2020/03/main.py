#!/usr/bin/python3
def example(value1, value2):
    return value1 + value2

def count_trees_on_track(slopes, horizontal_increment, vertical_increment):
    trees_count = 0
    x = 0
    for line in slopes[::vertical_increment]:
        res = is_hitting_tree(line.strip(), x)
        if(res):
            trees_count += 1
        x += horizontal_increment

    return trees_count

def is_hitting_tree(line, x:int):
    retval = 0
    linelen = len(line)

    if(x > linelen - 1):
        x = x % linelen

    if(line[x] == "#"):
        retval = 1

    return retval
    
def calc_trees_multiple_slopes(slopes):
    result = 1

    for i in [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees_count = count_trees_on_track(slopes, i[0], i[1])
        if(trees_count == 0):
            trees_count = 1
        result *= trees_count
    
    return result

if __name__ == "__main__":
    input_file = "03.in"
    expected_result = 7
    with open(input_file) as f:
        slopes = f.readlines()

    result = count_trees_on_track(slopes ,3, 1)
    print("03A: trees count:", result)

    result = calc_trees_multiple_slopes(slopes)
    print("03B: trees count multiple:", result)
