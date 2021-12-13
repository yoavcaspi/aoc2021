import argparse
from collections import defaultdict
from copy import deepcopy
from typing import List, Tuple


def num_path(visited, start, twice, caves):
    count = 0
    if start == "end":
        return 1
    for cave in caves[start]:
        if cave in visited:
            if cave == "start":
                continue
            if not twice:
                count += num_path(visited, cave, {cave}, caves)
            continue
        elif cave == "end":
            count += 1
        elif cave.islower():
            count += num_path(visited | {cave}, cave, twice, caves)
        else:
            count += num_path(visited, cave, twice, caves)
    return count


def sol(data: str) -> int:
    caves = defaultdict(set)
    for line in data.splitlines():
        a, b = line.split("-")
        caves[a].add(b)
        caves[b].add(a)
    print(caves)
    val = num_path({"start"}, "start", set(), caves)
    print(val)
    return val


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
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

INPUT2 = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""


def example():
    assert sol(INPUT2) == 36
    assert sol(INPUT) == 3509


if __name__ == '__main__':
    exit(main())
