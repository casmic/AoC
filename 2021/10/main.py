#!/usr/bin/python3
from delimiter import Delimiter

def example(value1, value2):
    return value1 + value2

def process_input_line(line):
    chunk_list = []
    corruption_score = 0
    for charachter in line:
        delimiter = Delimiter(charachter)

        if(delimiter.is_opening_char()):
            chunk_list.append(delimiter)
        else:
            if(charachter == chunk_list[-1]._expected):
                del chunk_list[-1]
            else:
                corruption_score = delimiter._corruption_score
                chunk_list = []
                break
    
    return chunk_list, corruption_score

def calc_completion_score(chunks, score):
    if(len(chunks)==0):
        return score
    score = (score*5) + chunks[-1]._completion_score
    return(calc_completion_score(chunks[:-1], score))

def calc_middle_completion_score(chunks):
    completion_scores= []
    result = 0
    for chunk in chunks:
        completion_scores.append(calc_completion_score(chunk, 0))

    scores_count = len(completion_scores)
    if(scores_count>0):
        completion_scores.sort()
        result = completion_scores[scores_count // 2]

    return result

def process_input_data(input_data):
    total_corruption = 0
    chunk_list = []
    for line in input_data:
        chunks, corruption = process_input_line(line.strip())
        total_corruption += corruption
        if(len(chunks) > 0):
            chunk_list.append(chunks)

    return chunk_list, total_corruption
    
if __name__ == "__main__":
    with open("input_10.txt") as f:
        input_data = f.readlines()

    chunks, corruption = process_input_data(input_data)
    print("10A - total corruption:", corruption)

    middle_completion_score = calc_middle_completion_score(chunks)
    print("10B - middle completion score:", middle_completion_score)

    pass
