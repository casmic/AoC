#!/usr/bin/python3

def aggregate_measurements(measurements):
    aggregated_measurements = []

    for index in range(len(measurements)):
        if(len(measurements[index:]) > 2):
            val=sum(measurements[index:index+3])
            aggregated_measurements.append(val)

    return aggregated_measurements

def count_increases(measurements):
    nr_increases = 0
    
    if(len(measurements)==0):
        return nr_increases

    previous=measurements[0]
    for measure in measurements:
        if(measure > previous):
            nr_increases += 1
        previous = measure
    
    return nr_increases

# https://docs.python.org/3/library/typing.html
#Measurements = list[str]


if __name__ == "__main__":
    with open('input_01.txt') as f: 
        measures = [int(x) for x in f.readlines()]
    
    print("01A: Number of Increases:",count_increases(measures))
    print("01B: Number of Aggregated Increases:",count_increases(aggregate_measurements(measures)))

    #do something
