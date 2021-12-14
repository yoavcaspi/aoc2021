import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    count = 0
    rules = {}
    poly, ruless = data.split("\n\n",2)
    poly = poly.split("\n")[0]
    for rule in ruless.split("\n"):
        if rule == "":
            continue
        first, second = rule.split(" -> ")
        print(first, second)
        rules[first] = second
    for step in range(10):
        new_poly = []
        for i in range(len(poly) -1):
            pair = poly[i] + poly[i+1]
            start = 0 if len(new_poly) == 0 else len(new_poly) - 1
            if pair in rules:
                if start == 0:
                    new_poly.append(poly[i])
                new_poly.append(rules[pair])
                new_poly.append(poly[i+1])
            else:
                new_poly.append(poly[i])
        poly = "".join(new_poly)
        c = Counter(poly)
    print(c)
    return (c.most_common(1)[0][1] - c.most_common(len(c))[-1][1])




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
"NN -> NCN"
"NCN -> NBCC"
"NBCC"

def example():
    assert sol(INPUT) == 1588


if __name__ == '__main__':
    exit(main())
