import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    board = {}
    MAX_Y = len(data.splitlines())
    MAX_X = len(data.splitlines()[0])
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            board[y,x] = int(c)
    sol_board = defaultdict(lambda :10000)
    sol_board[MAX_Y-1, MAX_X-1] = board[MAX_Y-1, MAX_X - 1]
    for y in reversed(range(MAX_Y)):
        for x in reversed(range(MAX_X)):
            if (y == MAX_Y - 1) and (x == MAX_X - 1):
                continue
            sol_board[y,x] = min(sol_board[y+1,x], sol_board[y,x+1]) + board[y,x]
    return sol_board[0,0] - board[0,0]


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
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


def example():
    assert sol(INPUT) == 40


if __name__ == '__main__':
    exit(main())
