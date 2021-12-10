import argparse
from collections import defaultdict
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    # 1 4 7 8
    # 2 4 3 7
    count = 0
    board = defaultdict(lambda:10)
    max_y = len(data.splitlines())
    max_x = len(data.splitlines()[0])
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            board[x,y] = int(c)
    for y in range(max_y):
        for x in range(max_x):
            if (
                    board[x, y] < board[x - 1, y] and
                    board[x, y] < board[x + 1, y] and
                    board[x, y] < board[x, y + 1] and
                    board[x, y] < board[x, y - 1]):
                count+=board[x,y]+1
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
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def example():
    assert sol(INPUT) == 15


if __name__ == '__main__':
    exit(main())
