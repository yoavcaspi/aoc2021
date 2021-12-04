import argparse
from collections import defaultdict
from copy import deepcopy
from typing import List, Tuple


def check_rows(boards):
    for board_id, board in boards.items():
        for i in range(5):
            vals = True
            for j in range(5):
                if board[(i, j)][1] == 0:
                    break
            else:
                return True, board_id
    return False, -1


def check_colunns(boards):
    for board_id, board in boards.items():
        for i in range(5):
            vals = True
            for j in range(5):
                if board[(j, i)][1] == 0:
                    break
            else:
                return True, board_id
    return False, -1


def check_for_winner(boards):
    is_winner, board_id = check_rows(boards)
    if is_winner:
        return True, board_id
    return check_colunns(boards)


def sol(data: str) -> int:
    count = 0
    bingo_order = [int(val) for val in data.split("\n")[0].split(",")]

    boards = defaultdict(dict)
    for i, board in enumerate(data.split("\n\n")[1:]):
        for row, line in enumerate(board.split("\n")):
            for column, val in enumerate(line.split()):
                boards[i][(row, column)] = (int(val), 0)

    for current in bingo_order:
        for board in boards.values():
            for key, val in board.items():
                if current == val[0]:
                    board[key] = (val[0], 1)

        is_winner, board_id = check_for_winner(boards)
        if is_winner:
            count = 0
            for val in boards[board_id].values():
                if val[1] == 0:
                    count += val[0]
            return current*count


def get_input(filename: str) -> str:
    with open(filename) as f:
        lines = f.read()
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='input.txt')
    args = parser.parse_args()
    data = get_input(args.filename)
    print(sol(data))
    return 0

# INPUT = """
# """
#
#
# def test_example():
#     assert sol2(INPUT.splitlines()) == 230


if __name__ == '__main__':
    exit(main())
