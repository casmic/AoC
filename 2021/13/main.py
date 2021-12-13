#!/usr/bin/python3
from typing import List, Tuple

def print_paper(paper):

    for line in paper:
        string = ""
        for val in line:
            string += str(val)
        print(string)

def fold_paper_x(paper, coord):
    min_x = int(coord)
    max_x = len(paper[0])
    max_y = len(paper)

    folded_paper = []
    for line in paper:
        folded_paper.append(line[:min_x])

    folded_x = min_x
    for x in range(min_x + 1, max_x):
        folded_x -= 1
        for y in range(max_y):
            if(paper[y][x] == '#'):
                folded_paper[y][folded_x] = paper[y][x]

    return folded_paper

def fold_paper_y(paper, coord):

    max_x = len(paper[0])
    min_y = coord
    max_y = len(paper)

    folded_paper = paper[:min_y][:max_x]

    folded_y = min_y
    for y in range(min_y +1, max_y):
        folded_y -= 1
        for x in range(len(paper[y])):
            if(paper[y][x] == '#'):
                folded_paper[folded_y][x] = paper[y][x]

    return folded_paper

def fold_paper(paper:List, fold:Tuple):
    
    if(fold[0] == 'x'):
        folded_paper = fold_paper_x(paper,int(fold[1]))
    else:
        folded_paper = fold_paper_y(paper,int(fold[1]))

    return folded_paper
    
def count_visible_dots(paper:List, folds:List, folds_number:int):
    dots_count = 0
    if folds == [] or paper == [] or folds_number > len(folds):
        return 0

    folded_paper = paper
    for i in range(folds_number):
        fold = folds[i]
        folded_paper = fold_paper(folded_paper, fold)
        print("Step:", i)
        print_paper(folded_paper)

    for line in folded_paper:
        for x in line:
            if(x == 1):
                dots_count += 1
    return dots_count 

def add_dot(paper, coords):
    dot_x = coords[0]
    dot_y = coords[1]

    y_len = len(paper)
    x_len = 1
    if(y_len > 0):
        x_len = len(paper[0])

    for y in range(len(paper), dot_y + 1):
        paper.append(['.']*x_len)
     
    x_len = len(paper[0])
    if(dot_x >= x_len):
        for y in range(len(paper)):
            paper[y].extend(['.'] * (dot_x - x_len + 1))

    paper[dot_y][dot_x] = '#'
    return paper 

def fill_paper_folds(filename):
    paper = []
    folds = []

    with open(filename) as f:
        data = f.readlines()

    we_are_dotting = True
    for line in data:
        line_stripped = line.strip()
        if(line_stripped) == "":
            we_are_dotting = False

        if(we_are_dotting):
            coords = [int(x) for x in line_stripped.split(',')]
            paper = add_dot(paper, coords)
        else:
            if(line_stripped != ""):
                folds.append(line_stripped[11:].split('='))

    return paper, folds 

if __name__ == "__main__":

    filename = 'input_13.txt'
    paper, folds = fill_paper_folds(filename)
    result = count_visible_dots(paper, folds, 1)
    print("13A dots number:", result)

    paper, folds = fill_paper_folds(filename)
    result = count_visible_dots(paper, folds, 12)
    print("13A dots number:", result)

