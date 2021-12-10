#!/usr/bin/python3
from typing import List


def example(value1, value2):
    return value1 + value2

def get_first_two_numbers(numbers:List, sum_value):
    result = [0,0]

    for number in numbers:
        result[0] = number
        if (sum_value - number in numbers):
            result[1] = sum_value - number 
            break

    return result

def get_first_three_numbers(numbers:List, sum_value):
    result = [0,0,0]

    for number in numbers:
        result[0] = number
        two_numbers =[0,0]
        two_numbers = get_first_two_numbers(numbers, sum_value - number)
        if(two_numbers[1]!=0):
            result[1] = two_numbers[0]
            result[2] = two_numbers[1]
            break

    return result

def multiply_list(numbers):
    result = 1

    for number in numbers:
        result *= number

    return result
    
if __name__ == "__main__":

    numbers=[]
    with open("01.in") as f:
        for line in f.readlines():
            numbers.append(int(line.strip()))

    result = get_first_two_numbers(numbers, 2020)
    print("01A result two numbers:", multiply_list(result))

    result = get_first_three_numbers(numbers, 2020)
    print("01B result three numbers:", multiply_list(result))
    pass
