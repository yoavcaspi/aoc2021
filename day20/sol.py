import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple

# ##..#.#...##.####..#..###.#.#.#.#.####.#.##.....#####.##..#..#.#.##.......##.##.#.#...#....#.####..#.##.##....###..##.#####.##....##.#.#.#.#....####...##.#......#.#..##......##..#..###.#..####.###...##.#.##.#..##.##..#.#.#..###..##.####.#.#.#..#.##...#..##...##.#####..##.##..#...#..###.#.#...#..#..##...#.#..........#...#...#.#.#.#..#.###..##....####..#######.##.#.....#.#.###...##...###...#.##.##.##..#......#.###...#.#.#.#...##.#.#.##.#..###.#...##...##.......####.##..#.#....#.#####..#..#####.#.....#....#.#.
def sol(data: str) -> int:
    h, p = data.split("\n\n")
    grid = defaultdict(lambda: ".")
    R = len(p.splitlines())
    C = len(p.splitlines()[0])
    for r, line in enumerate(p.splitlines()):
        for c, v in enumerate(line):
            grid[r,c] = v

    MIN_R = 0
    MIN_C = 0
    MAX_R = R
    MAX_C = C
    for t in range(50):
        if t % 2 == 0:
            new_grid = defaultdict(lambda: "#")
        else:
            new_grid = defaultdict(lambda: ".")
        for r in range(MIN_R - 10, MAX_R + 10):
            for c in range(MIN_C - 10, MAX_C + 10):
                val = ""
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        val += "0" if grid[r+i,c+j] == "." else "1"
                new_grid[r, c] = h[int(val, 2)]
        MIN_R -= 3
        MIN_C -= 3
        MAX_R += 3
        MAX_C += 3
        grid = new_grid

        # for r in range(-20,120):
        #     for c in range(-20,120):
        #         print(grid[r, c], end="")
        #     print()
    count = 0
    for (r,c), v in grid.items():

            if v == "#":
                count+=1
    return count


def get_input(filename: str) -> str:
    with open(filename) as f:
        lines = f.read()
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='input.txt')
    args = parser.parse_args()
    data = get_input(args.filename)
    # example()
    print(sol(data))
    return 0


INPUT = """\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""


def example():
    assert sol(INPUT) == 35


if __name__ == '__main__':
    exit(main())
