import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    p1, p2 = data.splitlines()
    p1 = int(p1[-1])
    p2 = int(p2[-1])
    options = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    c_p = {(p1, p2, 0, 0): 1}
    count_p1 = 0
    count_p2 = 0
    while c_p:
        new_cp = defaultdict(int)
        for (pos1, pos2, score1, score2), count in c_p.items():
            for o, o_count in options.items():
                p = pos1 + o
                if p > 10:
                    p -= 10
                new_score = score1+p
                if new_score >= 21:
                    count_p1 += o_count*count
                else:
                    new_cp[(p, pos2, new_score, score2)] += o_count*count

        c_p = new_cp

        new_cp = defaultdict(int)
        for (pos1, pos2, score1, score2), count in c_p.items():
            for o, o_count in options.items():
                p2 = pos2 + o
                if p2 > 10:
                    p2 -= 10
                new_score = score2+p2
                if new_score >= 21:
                    count_p2 += o_count*count
                else:
                    new_cp[(pos1, p2, score1, new_score)] += o_count*count
        c_p = new_cp
    print(f"{count_p1=}")
    print(f"{count_p2=}")
    return max(count_p1, count_p2)


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
Player 1 starting position: 4
Player 2 starting position: 8
"""


def example():
    assert sol(INPUT) == 444356092776315

if __name__ == '__main__':
    exit(main())
