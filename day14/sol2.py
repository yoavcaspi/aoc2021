import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    poly, ruless = data.split("\n\n",2)
    poly = poly.split("\n")[0]
    rules = {}
    for rule in ruless.split("\n"):
        if rule == "":
            continue
        first, second = rule.split(" -> ")
        rules[first] = second
    pairs = defaultdict(int)
    for i in range(len(poly) - 1):
        pair = poly[i] + poly[i + 1]
        pairs[pair] += 1

    for step in range(40):
        new_pairs = defaultdict(int)
        for pair, count in pairs.items():
            f, s = pair[0], pair[1]
            res = rules[pair]
            f_pair = f + res
            s_pair = res + s
            new_pairs[f_pair] += count
            new_pairs[s_pair] += count
        pairs = deepcopy(new_pairs)
        res = defaultdict(int)
        for pair, count in pairs.items():
            f, s = pair[0], pair[1]
            res[f] += count
        res[poly[-1]] += 1
    c = Counter(res)
    result = (max(c.values()) - min(c.values()))
    return result


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
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


def example():
    assert sol(INPUT) == 2_188_189_693_529


if __name__ == '__main__':
    exit(main())
