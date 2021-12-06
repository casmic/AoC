#!/usr/bin/python3
def example(value1, value2):
    return value1 + value2

def init_fishes(fishes):
    fishes_list = [int(x) for x in fishes.strip().split(',')]
    return_fishes = [0 for x in range(9)]

    for fish in fishes_list:
        return_fishes[fish] += 1

    return return_fishes

def grow_fishes(fishes, days):
    if(days == 0):
        return fishes
    
    fishes_to_add = fishes[0]

    for x in range(1, len(fishes)):
        fishes[x-1] = fishes[x]
        fishes[x] = 0

    fishes[6] += fishes_to_add
    fishes[8] += fishes_to_add

    return(grow_fishes(fishes, days -1))

if __name__ == "__main__":
    with open('input_06.txt') as f: 
        fishes_str = f.readline()

    fishes = init_fishes(fishes_str)
    fishes = grow_fishes(fishes, 80)

    print("06A - lanternfishes number:", sum(fishes))

    fishes = init_fishes(fishes_str)
    fishes = grow_fishes(fishes, 256)
    print("06B - lanternfishes number:", sum(fishes))
