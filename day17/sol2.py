import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    count = 0
    data = data.split(":",2)[-1][1:]
    x,y = data.split(", ")

    x_min, x_max = x[2:].split("..")
    x_min = int(x_min)
    x_max = int(x_max)

    y_min, y_max = y[2:].split("..")
    y_min = int(y_min)
    y_max = int(y_max)

    results = set()
    for Y in range(y_min, -y_min):
        y = 0
        t = 0
        flag = False
        Y2 = Y
        T = []
        while y > y_max:
            t += 1
            y += Y2
            Y2 -= 1
            if y_max >= y >= y_min:
                flag = True
                while y >= y_min:
                    T.append(t)
                    t += 1
                    y += Y2
                    Y2 -= 1
                break
            if y < y_min:
                break
        if not flag:
            continue
        # The probe's x position increases by its x velocity.
        # The probe's y position increases by its y velocity.
        # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
        # Due to gravity, the probe's y velocity decreases by 1.
        for X in range(x_max+1):
            for t in T:
                x = 0
                X2 = X
                for s in range(t):
                    x += X2
                    if X2 > 0:
                        X2 -= 1
                if x_min <= x <= x_max:
                    results.add((X,Y))
    return len(results)








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
    assert sol(INPUT_A) == 112


if __name__ == '__main__':
    exit(main())
