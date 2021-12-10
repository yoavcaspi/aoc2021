import argparse
from collections import defaultdict
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    board = defaultdict(lambda:9)
    max_y = len(data.splitlines())
    max_x = len(data.splitlines()[0])
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            board[x,y] = int(c)
    basins_sizes = []
    basins = []
    for y in range(max_y):
        for x in range(max_x):
            if (
                    board[x, y] < board[x - 1, y] and
                    board[x, y] < board[x + 1, y] and
                    board[x, y] < board[x, y + 1] and
                    board[x, y] < board[x, y - 1]):
                basins.append((x,y))
    for basin in basins:
        q = [basin]
        count = 0
        visited = set()
        while q:
            count += 1
            x,y = q.pop()
            visited.add((x,y))
            if board[x - 1, y] != 9 and board[x,y] < board[x - 1, y]:
                if (x-1,y) not in (visited | set(q)):
                    q.append((x-1, y))
            if board[x + 1, y] != 9 and board[x,y] < board[x + 1, y]:
                if (x+1,y) not in (visited | set(q)):
                    q.append((x+1, y))
            if board[x, y - 1] != 9 and board[x,y] < board[x, y - 1]:
                if (x,y -1) not in (visited | set(q)):
                    q.append((x, y - 1))
            if board[x, y + 1] != 9 and board[x,y] < board[x, y + 1]:
                if (x,y + 1) not in (visited | set(q)):
                    q.append((x, y + 1))
        basins_sizes.append(count)
    basins_sizes.sort()
    return basins_sizes[-3] * basins_sizes[-2] * basins_sizes[-1]


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
    assert sol(INPUT) == 1134


if __name__ == '__main__':
    exit(main())
