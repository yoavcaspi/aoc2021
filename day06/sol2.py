import argparse
import time
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    count = 0
    fishes = [int(val) for val in data.split(",")]
    counter = Counter(fishes)
    for q in range(256):
        new_dict = defaultdict(int)
        for key, val in counter.items():
            if key > 0:
                new_dict[key-1] += val
            else:
                new_dict[8] = val
                new_dict[6] += val
        counter = deepcopy(new_dict)
    return sum(counter.values())



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

# 1 = 1401
# 2 = 1191
# 3 = 1154
# 4 = 1034
# 5 = 950,

def example():
    assert sol(INPUT) == 26_984_457_539


if __name__ == '__main__':
    exit(main())
