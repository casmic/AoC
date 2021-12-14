#!/usr/bin/python3
from typing import Counter

def polymer_insert(polymer:str, rules:dict, steps):
    elems_count = {}
    result_elem_count = {}

    for rule in rules:
        elems_count[rules[rule]] = 0
        result_elem_count[rules[rule]] = 0

    for x in polymer:
        elems_count[x] += 1

    i = 0
    j = i+1
    pairs = {}
    new_pairs = {}
    while j < len(polymer):
        pair = polymer[i] + polymer[j]
        if(pair not in pairs):
            pairs[pair] = 0
        pairs[pair] += 1
        i += 1
        j += 1 

    for _ in range(steps):
        new_pairs = {}
        for pair, count in pairs.items():
            insert = rules[pair]

            if(pair[0]+insert not in new_pairs):
                new_pairs[pair[0]+insert] = 0
            new_pairs[pair[0]+insert] += count

            if(insert + pair[1] not in new_pairs):
                new_pairs[insert + pair[1]] = 0
            new_pairs[insert + pair[1]] += count

            elems_count[insert] += count
        
        pairs = new_pairs

    return elems_count

def subratct_more_common_less_common(elems:dict):
    min_elem = 10000000000000000000
    max_elem = 0

    for elem in elems:
        if(elems[elem] > max_elem):
            max_elem = elems[elem]
        if(elems[elem] < min_elem):
            min_elem = elems[elem]
    
    return max_elem - min_elem


def read_template_rules(filename):
    template = ""
    rules = {}

    with open(filename) as f:
        data = f.readlines()

    template = data[0].strip()

    for rule in data[2:]:
        pair = rule.strip()[:2]
        insertion = rule.strip()[-1]
        rules[pair] = insertion

    return template, rules

if __name__ == "__main__":
    
    filename = "input_14.txt"

    template, rules = read_template_rules(filename)
    elems_count = polymer_insert(template, rules, 10)
    result = subratct_more_common_less_common(elems_count)
    print("13A difference:", result)

    template, rules = read_template_rules(filename)
    elems_count = polymer_insert(template, rules, 40)
    result = subratct_more_common_less_common(elems_count)
    print("13B difference:", result)