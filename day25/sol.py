import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from itertools import product
from typing import List, Tuple, NamedTuple, Any, Dict


def move_right(board, Y, X):
    new_board = {}
    flag = False
    for x in range(0, X):
        for y in range(0, Y):
            new_x = (x + 1) % X
            if board[y, x] == ">" and board[y, new_x] == ".":
                flag = True
                new_board[y,x] = "."
                new_board[y,new_x] = ">"
            elif (y,x) not in new_board:
                new_board[y, x] = board[y, x]

    return flag, new_board


def move_down(board, Y, X):
    new_board = {}
    flag = False
    for y in range(0, Y):
        for x in range(0, X):
            new_y = (y + 1) % Y
            if board[y, x] == "v" and board[new_y, x] == ".":
                flag = True
                new_board[y,x] = "."
                new_board[new_y,x] = "v"
            elif (y, x) not in new_board:
                new_board[y, x] = board[y, x]
    return flag, new_board


def sol(data: str) -> int:
    board = {}
    Y = len(data.splitlines())
    X = len(data.splitlines()[0])
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            board[y,x] = c
    flag = True
    i = 0
    while flag:
        print(i)
        # for y in range(Y):
        #     for x in range(X):
        #         print(board[y,x],end="")
        #     print()
        # print("\n\n")
        flag1, new_board = move_right(board, Y, X)
        board = deepcopy(new_board)
        flag2, new_board = move_down(board, Y, X)
        flag = flag1 | flag2
        board = deepcopy(new_board)
        i += 1
    print(i)
    return i



def get_input(filename: str) -> str:
    with open(filename) as f:
        lines = f.read()
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='input.txt')
    args = parser.parse_args()
    data = get_input(args.filename)
    example()
    print(sol(data))
    return 0


INPUT = """\
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""


def example():
    assert sol(INPUT) == 58


if __name__ == '__main__':
    exit(main())
