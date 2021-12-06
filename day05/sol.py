import argparse
from collections import defaultdict
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    count = 0
    board = defaultdict(int)
    for line in data.splitlines():
        start, end = line.split(" -> ")
        x1, y1 = start.split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2, y2 = end.split(",")
        x2 = int(x2)
        y2 = int(y2)
        min_x = min(x1,x2)
        max_x = max(x1,x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        if x1 == x2 or y1 == y2:
            for x in range(min_x, max_x+1):
                for y in range(min_y, max_y+1):
                    board[x,y]+=1
    count = 0
    for val in board.values():
        if val >= 2:
            count+=1
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
    print(sol(data))
    return 0


INPUT = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def test_example():
    assert sol(INPUT) == 5


if __name__ == '__main__':
    exit(main())
