import argparse
from copy import deepcopy
from typing import List, Tuple


def sol(data: List[str]) -> int:
    count = 0
    most_common = ""
    least_common = ""
    for i in range(len(data[0].strip())):
        hist = {"0": 0, "1": 0}
        for line in data:
            hist[line[i]] += 1
        if hist["0"] > hist["1"]:
            most_common += "0"
            least_common += "1"
        else:
            most_common += "1"
            least_common += "0"
    print(int(most_common, 2))
    print(int(least_common, 2))
    return int(most_common, 2) * int(least_common, 2)


def sol2(data: List[str]) -> int:
    i = 0
    hist = {"0": [], "1": []}
    for line in data:
        hist[line[i]].append(line)
    if len(hist["0"]) > len(hist["1"]):
        most_common = deepcopy(hist["0"])
        least_common = deepcopy(hist["1"])
    else:
        most_common = deepcopy(hist["1"])
        least_common = deepcopy(hist["0"])

    while len(most_common) != 1:
        i += 1
        hist = {"0": [], "1": []}
        for line in most_common:
            hist[line[i]].append(line)
        if len(hist["0"]) > len(hist["1"]):
            most_common = deepcopy(hist["0"])
        else:
            most_common = deepcopy(hist["1"])
    i=0
    while len(least_common) != 1:
        i += 1
        hist = {"0": [], "1": []}
        for line in least_common:
            hist[line[i]].append(line)
        if len(hist["0"]) > len(hist["1"]):
            least_common = deepcopy(hist["1"])
        else:
            least_common = deepcopy(hist["0"])
    print(int(least_common[0], 2))
    print(int(most_common[0], 2))
    return int(most_common[0], 2) * int(least_common[0], 2)


def get_input(filename: str) -> List[str]:
    with open(filename) as f:
        lines = f.readlines()
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='input.txt')
    args = parser.parse_args()
    data = get_input(args.filename)
    print(sol(data))
    print(sol2(data))
    return 0

INPUT = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def test_example():
    assert sol2(INPUT.splitlines()) == 230

if __name__ == '__main__':
    exit(main())
