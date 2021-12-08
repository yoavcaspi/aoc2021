import argparse
from collections import defaultdict
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    count = 0
    crabs = [int(val) for val in data.split(",")]
    sums = []
    avg = sum(crabs) / len(crabs)
    costs = {}
    cost = 0
    for i in range(10000):
        cost+=i
        costs[i] = cost
    for i in range(10000):
        new_sum = 0
        for crab in crabs:

            new_sum += costs[abs(i - crab)]
        sums.append(new_sum)
    return min(sums)


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


INPUT = """16,1,2,0,4,2,7,1,2,14
"""


def example():
    assert sol(INPUT) == 168


if __name__ == '__main__':
    exit(main())
