import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple, NamedTuple, Set


class Cube(NamedTuple):
    x0:int
    x1:int
    y0:int
    y1:int
    z0:int
    z1:int

    def volume(self):
        return (self.x1 - self.x0) * (self.y1 - self.y0) * (self.z1 - self.z0)

    def intersects(self, other):
        return (
            self.x1 > other.x0 and
            self.x0 < other.x1 and
            self.y1 > other.y0 and
            self.y0 < other.y1 and
            self.z1 > other.z0 and
            self.z0 < other.z1
        )

    def contains(self, other):
        return (self.x0 <= other.x0 and
                self.x1 >= other.x1 and
                self.y0 <= other.y0 and
                self.y1 >= other.y1 and
                self.z0 <= other.z0 and
                self.z1 >= other.z1
                )

    def split_cubes(self, other):
        xs = sorted([self.x0, self.x1, other.x0, other.x1])
        ys = sorted([self.y0, self.y1, other.y0, other.y1])
        zs = sorted([self.z0, self.z1, other.z0, other.z1])

        own_cube = []
        for x0, x1 in zip(xs, xs[1:]):
            for y0, y1 in zip(ys, ys[1:]):
                for z0, z1 in zip(zs, zs[1:]):
                    c = Cube(x0, x1, y0, y1, z0, z1)
                    if self.contains(c) and not other.intersects(c):
                        own_cube.append(c)
        return own_cube


def sol(data: str) -> int:
    on_set: Set[Cube] = set()
    for line in data.splitlines():
        s, c = line.split(" ")
        X,Y,Z = c.split(",")
        x_min, x_max = [int(val) for val in X[2:].split("..")]
        y_min, y_max = [int(val) for val in Y[2:].split("..")]
        z_min, z_max = [int(val) for val in Z[2:].split("..")]
        cube = Cube(x_min, x_max + 1, y_min, y_max + 1, z_min, z_max + 1)
        for c in set(on_set):
            if c.intersects(cube):
                on_set.remove(c)
                for cube2 in c.split_cubes(cube):
                    if cube2.volume() != 0:
                        on_set.add(cube2)
        if s == "on":
            on_set.add(cube)
    return sum([cube.volume() for cube in on_set])


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
"""

INPUT2 = """\
on x=0..2,y=0..2,z=0..2
on x=1..1,y=1..1,z=1..1
"""

def example():
    assert sol(INPUT2) == 27
    assert sol(INPUT) == 590784


if __name__ == '__main__':
    exit(main())
