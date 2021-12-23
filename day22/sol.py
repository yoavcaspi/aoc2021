import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple

def sol(data: str) -> int:
    board = defaultdict(int)
    for line in data.splitlines():
        s, c = line.split(" ")
        print(s)
        X,Y,Z = c.split(",")
        x_min, x_max = [int(val) for val in X[2:].split("..")]
        y_min, y_max = [int(val) for val in Y[2:].split("..")]
        z_min, z_max = [int(val) for val in Z[2:].split("..")]
        print(x_min, x_max)
        if x_min < -50 and x_max < -50:
            continue
        elif x_min > 50 and x_max > 50:
            continue

        if y_min < -50 and y_max < -50:
            continue
        elif y_min > 50 and y_max > 50:
            continue

        if z_min < -50 and z_max < -50:
            continue
        elif z_min > 50 and z_max > 50:
            continue


        val = 0
        if s == "on":
            val = 1
        for x in range(x_min, x_max+1):
            for y in range(y_min, y_max+1):
                for z in range(z_min, z_max+1):
                    board[x,y,z] = val
    return sum(board.values())


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
on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682
"""


def example():
    assert sol(INPUT) == 590784


if __name__ == '__main__':
    exit(main())
