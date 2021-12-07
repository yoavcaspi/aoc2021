import argparse
from collections import defaultdict
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    count = 0

    fishes = [int(val) for val in data.split(",")]
    for q in range(80):
        for i,val in enumerate(fishes):
            if val > 0:
                fishes[i] -= 1
            else:
                fishes[i] = 6
                fishes.append(9)

    return len(fishes)



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


INPUT = """3,4,3,1,2
"""


def example():
    assert sol(INPUT) == 5934


if __name__ == '__main__':
    exit(main())
