import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple


class Pair:
    def __init__(self, left = None, right = None):
        self.val = None
        self.parent = None
        self.left = left
        self.right = right
        self._i = 0

    @classmethod
    def from_line(cls, line):
        self = cls()
        if line[self._i + 1] == "[":
            self._i += 1
            self.left = Pair.from_line(line[self._i:])
            self.left.parent = self
            self._i += self.left._i + 1
        else:
            assert line[self._i + 1].isdigit()
            assert line[self._i + 2] == ","
            self.left = int(line[self._i + 1])
            self._i += 2

        if line[self._i + 1] == "[":
            self._i += 1
            self.right = Pair.from_line(line[self._i:])
            self.right.parent = self
            self._i += self.right._i + 1

        else:
            assert line[self._i + 1].isdigit()
            assert line[self._i + 2] == "]"
            self.right = int(line[self._i + 1])
            self._i += 2
        return self

    def __add__(self, other):
        assert isinstance(other, Pair)
        new = Pair(self, other)
        new.left.parent = new
        new.right.parent = new
        new.reduce()
        return new

    def reduce(self):
        flag = True
        while flag:
            flag, _ = self.explode_in_order(0, False)
            if flag:
                continue
            flag = self.split_in_order(0, False)

    def magnitude(self):
        left = self.left if isinstance(self.left, int) else self.left.magnitude()
        right = self.right if isinstance(self.right, int) else self.right.magnitude()
        return 3*left + 2*right

    def explode_in_order(self, height, flag):
        if flag:
            return True, False
        if height == 4:
            assert isinstance(self.left, int)
            assert isinstance(self.right, int)
            self.increase_left(self.left)
            self.increase_right(self.right)
            return True, True
        if isinstance(self.left, Pair):
            flag, first = self.left.explode_in_order(height + 1, flag)
            if flag:
                if first:
                    self.left = 0
                return True, False
        if isinstance(self.right, Pair):
            flag, first = self.right.explode_in_order(height + 1, flag)
            if flag and first:
                self.right = 0
            return flag, False
        return flag, False

    def increase_left(self, val: int):
        p = self
        while p.parent:
            new_p = p.parent
            if new_p.left != p:
                p = new_p.left
                if isinstance(new_p.left, int):
                    new_p.left += val
                    return
                break
            else:
                p = new_p
        else:
            return
        while isinstance(p.right, Pair):
            p = p.right
        p.right += val

    def increase_right(self, val):
        p = self
        while p.parent:
            new_p = p.parent
            if new_p.right != p:
                if isinstance(new_p.right, int):
                    new_p.right += val
                    return
                p = new_p.right
                break
            else:
                p = new_p
        else:
            return
        while isinstance(p.left, Pair):
            p = p.left
        p.left += val

    def split_in_order(self, height, flag):
        if flag:
            return True
        if isinstance(self.left, Pair):
            flag = self.left.split_in_order(height + 1, flag)
            if flag:
                return True
        else:
            if self.left >= 10:
                self.left = Pair(self.left // 2, self.left // 2 + self.left % 2)
                self.left.parent = self
                return True

        if isinstance(self.right, Pair):
            flag = self.right.split_in_order(height + 1, flag)
        else:
            if self.right >= 10:
                self.right = Pair(self.right // 2, self.right // 2 + self.right % 2)
                self.right.parent = self
                return True

        return flag


def sol(data: str) -> int:
    for i, line in enumerate(data.splitlines()):
        if i == 0:
            root = Pair.from_line(line)
            continue
        second = Pair.from_line(line)
        root = root + second
    return root.magnitude()


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


INPUT_A = """\
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""

INPUT_B = """\
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
"""


def example():
    p1 = Pair.from_line("[[[[3,0],[5,3]],[4,4]],[5,5]]")
    assert p1.magnitude() == 791
    assert sol(INPUT_A) == 4140


if __name__ == '__main__':
    exit(main())
