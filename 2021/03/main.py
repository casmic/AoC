#!/usr/bin/python3
# def sum(value1, value2):
#    return value1 + value2


def consumption_of_the_submarine(diagnostic_report):
    gamma = calculate_gamma_rate(diagnostic_report)
    epsilon = calculate_epsilon_rate(diagnostic_report)

    return gamma * epsilon

def calculate_life_support_rating(diagnostic_report):
    oxygen=oxygen_rating(diagnostic_report)
    co2=co2_scrubbing(diagnostic_report)

    return oxygen * co2

def oxygen_rating(diagnostic_report):
    result= _filter_diagnostic_report(diagnostic_report,[0],True)
    return int(result,2)

def co2_scrubbing(diagnostic_report):
    result= _filter_diagnostic_report(diagnostic_report,[0],False)
    return int(result,2)

def _filter_diagnostic_report(diagnostic_report, bit_position, is_higher):
    if(len(diagnostic_report)==1):
        return diagnostic_report[0]
    
    counter=_calculate_counter(diagnostic_report,bit_position)

    if(is_higher):
        if(counter[0]>=0):
            choosen_bit="1"
        else:
            choosen_bit="0"
    else:
        if(counter[0]<0):
            choosen_bit="1"
        else:
            choosen_bit="0"

    filtered_report = []
    for binary_number in diagnostic_report:
        if(binary_number[bit_position[0]]==choosen_bit):
            filtered_report.append(binary_number)

    return _filter_diagnostic_report(filtered_report, [bit_position[0]+1], is_higher)

def _calculate_counter(diagnostic_report, bit_range):
    counter = [0 for b in bit_range]
    for binary_number in diagnostic_report:
        counter_position = 0
        for position in bit_range:
            if binary_number[position] == "1":
                counter[counter_position] += 1
            else:
                counter[counter_position] -= 1
            counter_position += 1
    return counter


def calculate_gamma_rate(diagnostic_report):
    counter = _calculate_counter(diagnostic_report,range(len(diagnostic_report[0])))

    binary_result = "".join(["1" if bit >= 0 else "0" for bit in counter])
    return int(binary_result, 2)

def calculate_epsilon_rate(diagnostic_report):
    counter = _calculate_counter(diagnostic_report,range(len(diagnostic_report[0])))

    binary_result = "".join(["1" if bit < 0 else "0" for bit in counter])
    return int(binary_result, 2)

def read_input_data(filename):
    result=[]
    with open(filename) as f:
        result = f.read().split()

    return result

if __name__ == "__main__":
    diagnostic_report=read_input_data("input_03.txt")
    print(consumption_of_the_submarine(diagnostic_report))
    print(calculate_life_support_rating(diagnostic_report))
