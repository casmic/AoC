#!/usr/bin/python3
from typing import List
#from unittest import result

def example(value1, value2):
    return value1 + value2

def count_obvious_result_patterns(cyphers):

    obvious_patterns_count = 0

    if(cyphers is not None):
        for results in cyphers:
            for result in results:
                result_len = len(result)
                if (result_len == 2 or result_len==3 or result_len==4 or result_len==7):
                    obvious_patterns_count += 1

    return obvious_patterns_count

def process_input_dataA(data):
    data_inputs = []
    data_results = []
    for line in data:
        line_list = line.strip().split()
        inputs = line_list[:line_list.index('|')]
        outputs = line_list[line_list.index('|')+1:]
        data_inputs.append(inputs)
        data_results.append(outputs)
    return data_inputs, data_results

def _sort_signal(signal):
    signal_list = [signal[x] for x in range(len(signal))]
    signal_list.sort()
    sorted_signal= "".join(signal_list)

    return sorted_signal

def _signal_to_set(signal):
    return_set = set()

    for x in signal:
        return_set.add(x)

    return return_set

def get_result_number(input:List, output:List):
    number = ""
    signals_dict = {}
    signals_dict['len'] = {}
    signals_dict['number'] = {}
    remaining_signals = []

    for i in [2,3,4,5,6,7]:
        signals_dict['len'][i] = []

    for signal in input:
        #sorted_signal = _sort_signal(signal)
        #signals_dict['len'][sig_len].append(sorted_signal)
        sig_set=_signal_to_set(signal)
        sig_len = len(sig_set)

        signals_dict['len'][sig_len].append(sig_set)
        if(sig_len == 2):
            signals_dict['number']["1"]=sig_set
        elif(sig_len == 3):
            signals_dict['number']["7"]=sig_set
        elif(sig_len == 4):
            signals_dict['number']["4"]=sig_set
        elif(sig_len == 7):
            signals_dict['number']["8"]=sig_set
        else:
            remaining_signals.append(sig_set)

    for i in ["2","3","5","6","9","0"]:
        signals_dict['number'][i] = None

    keep_going = True
    while(len(remaining_signals)>0):
        for sig_set in remaining_signals:
            sig_len = len(sig_set)
            if(sig_len == 5):
                if(signals_dict['number']["7"].issubset(sig_set)):
                    signals_dict['number']["3"] = sig_set
                    remaining_signals.remove(sig_set)
                elif(signals_dict['number']["9"] is not None):
                    if(sig_set.issubset(signals_dict['number']["9"])):
                        signals_dict['number']["5"] = sig_set
                        remaining_signals.remove(sig_set)
                    else:
                        signals_dict['number']["2"] = sig_set
                        remaining_signals.remove(sig_set)
            elif(sig_len == 6):
                if(signals_dict['number']["3"] is not None):
                    if(sig_set == signals_dict['number']["3"].union(signals_dict['number']["4"])):
                        signals_dict['number']["9"] = sig_set
                        remaining_signals.remove(sig_set)
                    elif(signals_dict['number']["1"].issubset(sig_set)):
                        signals_dict['number']["0"] = sig_set
                        remaining_signals.remove(sig_set)
                    else:
                        signals_dict['number']["6"] = sig_set
                        remaining_signals.remove(sig_set)

    for signal in output:
        sig_set = _signal_to_set(signal)
        for key in signals_dict['number']:
            if(signals_dict['number'][key] == sig_set):
                number += str(key)
                break
    
    return number

def get_results_number_sum(input, outputs):

    result_sum =0 
    for i in range(len(input)):
        result_sum += get_result_number(input[i], outputs[i])

    return result_sum
if __name__ == "__main__":
    with open("input_08.txt") as f:
        data = f.readlines()
        signals_inputs, signals_results = process_input_dataA(data)
        obvious_results_count = count_obvious_result_patterns(signals_results)

        print('08A - obvious results count:', obvious_results_count)
        result = 0
        for i in range(len(signals_inputs)):
            number = get_result_number(signals_inputs[i], signals_results[i])
            result += int(number)

        print('08B - sum of all outputs:', result)
    pass
