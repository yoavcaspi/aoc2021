import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple

# ##..#.#...##.####..#..###.#.#.#.#.####.#.##.....#####.##..#..#.#.##.......##.##.#.#...#....#.####..#.##.##....###..##.#####.##....##.#.#.#.#....####...##.#......#.#..##......##..#..###.#..####.###...##.#.##.#..##.##..#.#.#..###..##.####.#.#.#..#.##...#..##...##.#####..##.##..#...#..###.#.#...#..#..##...#.#..........#...#...#.#.#.#..#.###..##....####..#######.##.#.....#.#.###...##...###...#.##.##.##..#......#.###...#.#.#.#...##.#.#.##.#..###.#...##...##.......####.##..#.#....#.#####..#..#####.#.....#....#.#.
def sol(data: str) -> int:
    p1, p2 = data.splitlines()
    p1 = int(p1[-1])
    p2 = int(p2[-1])
    s1,s2 = 0,0
    print(p1)
    print(p2)
    t=0
    dice = list(range(1,101))
    j = 0
    while s1 < 1000 and s2 < 1000:
        t+=3
        res = dice[j]
        j += 1
        j %= 100
        res += dice[j]
        j += 1
        j %= 100
        res += dice[j]
        j += 1
        j %= 100
        p1 += res
        while p1 > 10:
            p1 -= 10
        s1 += p1
        print(f"{t=}, {s1=}")
        if s1 >= 1000:
            break
        t+=3
        res = dice[j]
        j += 1
        j %= 100
        res += dice[j]
        j += 1
        j %= 100
        res += dice[j]
        j += 1
        j %= 100
        p2 += res
        while p2 > 10:
            p2 -= 10
        s2 += p2
        print(f"{s2=}")

    return t*min(s1, s2)


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
    assert sol(INPUT) == 739785


if __name__ == '__main__':
    exit(main())
