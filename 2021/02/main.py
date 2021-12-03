#!/usr/bin/python3
def sum(value1, value2):
    return value1 + value2


# https://docs.python.org/3/library/typing.html
#Measurements = list[str]

def process_command(command):
    result = [0,0]
    if(command is None):
        return result
    
    if(len(command) != 2):
        return result

    print(command)

    direction=command[0]
    value=int(command[1])

    if direction=='forward':
        result=[value,0]
    elif direction=='up':
        result=[0,-1*value]
    elif direction=='down':
        result=[0,value]

    return result


def process_inputB(filename):
    final_route=[0,0,0]
    route_change=[0,0,0]
    result=0
    with open(filename) as f:
        line = f.readline()
        while (line is not None and line != ''):
            command = line.split()
            route_change=process_command(command)
            final_route[0]+=route_change[0]
            final_route[2] += route_change[1]
            if(route_change[0]!=0):
                final_route[1]+=(route_change[0]*final_route[2])
            print(final_route)
            line=f.readline()
    result=final_route[0]*final_route[1]
    return result            

def process_inputA(filename):
    final_route=[0,0]
    route_change=[0,0]
    result=0
    with open(filename) as f:
        line = f.readline()
        while (line is not None and line != ''):
            command = line.split()
            route_change=process_command(command)
            final_route[0] += route_change[0]
            final_route[1] += route_change[1]
            line=f.readline()
    
    result=final_route[0]*final_route[1]
    return result

if __name__ == "__main__":

    resultA= process_inputA('input_02.txt')
    resultB= process_inputB('input_02.txt')

    print("02A: final result:",resultA)
    print("02B: final result:",resultB)