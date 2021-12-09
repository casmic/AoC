#!/usr/bin/python3
def example(value1, value2):
    return value1 + value2

def init_crabs(crabs):

    return_crabs=[]
    for scrab in crabs.split(','):
        crab=int(scrab)
        if(crab > len(return_crabs)-1):
            for _ in range(len(return_crabs), crab+1):
                return_crabs.append(0)
        return_crabs[crab] += 1

    return return_crabs

def calc_fuel_spent(crabs, position, cost_per_further_step = 0):
    
    fuel_spent=0
    for i in range(len(crabs)):
        steps_to_do = abs(i - position)
        steps_consumption = 0
        if(cost_per_further_step==0):
            steps_consumption = abs(i - position)
        else:
            for j in range(steps_to_do):
                steps_consumption += j+cost_per_further_step

        fuel_spent += crabs[i] * steps_consumption

    return fuel_spent

def calc_cheaper_position(crabs, cost_per_further_step = 0):
    
    min_consumption_pos = -1
    min_consumption = -1
    for i in range(len(crabs)):
        consumption = calc_fuel_spent(crabs, i, cost_per_further_step)
        if(consumption < min_consumption or min_consumption == -1):
            min_consumption = consumption
            min_consumption_pos = i

    return min_consumption_pos, min_consumption

if __name__ == "__main__":    
    with open('input_07.txt') as f: 
        crabs_str = f.readline()
        crabs = init_crabs(crabs_str)

        pos, consumption = calc_cheaper_position(crabs)
        print(f'07A minimum consumption: {consumption} - Position:{pos}')
        pos, consumption = calc_cheaper_position(crabs, 1)
        print(f'07B minimum consumption: {consumption} - Position:{pos}')