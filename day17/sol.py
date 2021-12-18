import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    # target area: x=175..227, y=-134..-79
    data = data.split(":", 2)[-1][1:]
    x,y = data.split(", ")

    y_min, y_max = y[2:].split("..")
    y_min = int(y_min)
    y_max = int(y_max)
    results = []
    for Y in range(-y_min):
        x,y = 0, 0
        t = 0
        Y2 = Y
        while y > y_max:
            t += 1
            y += Y2
            Y2 -= 1
            if y_max >= y >= y_min:
                results.append(Y)
                break
            if y < y_min:
                break
    return sum(range(results[-1]+1))


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


INPUT_A = """\
target area: x=20..30, y=-10..-5
"""


def example():
    assert sol(INPUT_A) == 45


if __name__ == '__main__':
    exit(main())
