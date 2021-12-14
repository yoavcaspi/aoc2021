import argparse
from collections import defaultdict
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    count = 0
    board = defaultdict(lambda: ".")
    dots, folds = data.split("\n\n",2)
    max_x = 0
    max_y = 0
    for dot in dots.split("\n"):
        x, y = [int(val) for val in dot.split(",")]
        if x > max_x:
            max_x=x
        if y > max_y:
            max_y=y
        board[x,y] = "#"
    print(max_x, max_y)

    for fold in folds.split("\n"):
        val_s = fold.split(" ")[-1]
        if val_s == "":
            break
        axis, val = val_s.split("=")
        val = int(val)
        if axis == "y":
            for i,y in enumerate(range(val + 1, max_y+1),start=1):
                for x in range(max_x+1):
                    if board[x,y] == "#":
                        board[x,val - i] = "#"
                        board[x,y] = "."
        else:
            for i, x in enumerate(reversed(range(val)),start=1):
                for y in range(max_y+1):
                    if board[x,y] == "#":
                        board[val + i,y] = "#"
                        board[x,y] = "."

        break
    # for y in range(max_y + 1):
    #     for x in range(max_x + 1):
    #         print(board[x,y],end="")
    #     print()
    count = 0
    for val in board.values():
        if val == "#":
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
    example()
    print(sol(data))
    return 0


INPUT = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


def example():
    assert sol(INPUT) == 17


if __name__ == '__main__':
    exit(main())
