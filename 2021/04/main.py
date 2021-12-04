from board import *

def example(value1, value2):
    return value1 + value2

def get_winner_score(boards, draws):

    return_value = []
    found_sum = 0
    found_drawn_value = 0

    for drawn_value in draws:
        for board in boards:
            if(board._board_won == False):
                found_sum = board.Draw(drawn_value)
                if found_sum > 0:
                    found_drawn_value = drawn_value
                    return_value.append(found_sum * drawn_value)

    return return_value

def read_input_data(filename):

    return_draws=[]
    return_boards = []
    result=[]
    board_index=0
    with open(filename) as f:
        return_draws = f.readline().strip('\n').split(',')
        return_draws = [int(x) for x in return_draws]

        for line in f.readlines():
            line = line.strip('\n')
            if line=="":
                return_boards.append(Board(board_index))
                board_index += 1
            else:
                values = line.split()
                values = [int(x) for x in values]
                return_boards[len(return_boards)-1].AddRow(values)

    return return_draws, return_boards

if __name__ == "__main__":

    draws, boards = read_input_data("input_04.txt")

    results=get_winner_score(boards, draws)
    resultA=results[0]
    resultB=results[len(results)-1]

    print(f'Day 04A: {resultA}')
    print(f'Day 04B: {resultB}')
    pass
