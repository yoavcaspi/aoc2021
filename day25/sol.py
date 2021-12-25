import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from itertools import product
from typing import List, Tuple, NamedTuple, Any, Dict


def move_right(first, second, X):
    cucumbers = first | second
    new_east = set()
    flag = False
    for y, x in first:
        new_x = (x + 1) % X
        if (y, new_x) not in cucumbers:
            flag = True
            new_east.add((y, new_x))
        else:
            new_east.add((y, x))
    return flag, new_east


def move_down(first, second, Y):
    cucumbers = first | second
    new_south = set()
    flag = False
    for y, x in second:
        new_y = (y + 1) % Y
        if (new_y, x) not in cucumbers:
            flag = True
            new_south.add((new_y, x))
        else:
            new_south.add((y, x))
    return flag, new_south


def sol(data: str) -> int:
    Y = len(data.splitlines())
    X = len(data.splitlines()[0])
    east = set()
    south = set()
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == ">":
                east.add((y, x))
            elif c == "v":
                south.add((y, x))
    flag = True
    i = 0
    while flag:
        flag1, new_east = move_right(east, south, X)
        east = deepcopy(new_east)
        flag2, new_south = move_down(east, south, Y)
        flag = flag1 | flag2
        south = deepcopy(new_south)
        i += 1
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
