import argparse
from collections import defaultdict
from copy import deepcopy
from typing import List, Tuple


def print_board(board):
    print("================")
    for r in range(10):
        for c in range(10):
            print(board[r,c], end="")
        print()


def sol(data: str) -> int:
    count = 0

    RR = [-1, -1, -1, 0, 0, 1, 1, 1]
    CC = [-1,  0,  1, -1, 1, -1, 0, 1]
    board = defaultdict(int)
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line.strip()):
            board[x,y] = int(c)

    R = 10
    C = 10
    for _ in range(100):
        new_board = defaultdict(int)
        for key, val in board.items():
            new_board[key] = val+1
        board = deepcopy(new_board)
        flag = True
        visited = set()
        while flag:
            for (c, r), val in board.items():
                if val > 9 and (c, r) not in visited:
                    visited.add((c, r))
                    count += 1
                    for i in range(len(RR)):
                        new_c = c + CC[i]
                        new_r = r + RR[i]
                        if 0 <= new_c <= 9 and 0 <= new_r <= 9:
                            board[new_c, new_r] += 1
                    break
            else:
                flag = False
        new_board = defaultdict(int)
        for key, val in board.items():
            if val > 9:
                new_board[key] = 0
            else:
                new_board[key] = val
        board = deepcopy(new_board)
        print_board(board)
    return count


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
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


def example():
    assert sol(INPUT) == 1656


if __name__ == '__main__':
    exit(main())
