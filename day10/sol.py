import argparse
from collections import defaultdict
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    # 1 4 7 8
    # 2 4 3 7
    count = 0

    op = {"(", "[", "<", "{"}
    cl = {")", "]", ">", "}"}
    brackets = {
        ")": "(",
        "]": "[",
        ">": "<",
        "}": "{"
    }
    score = {")": 3,
             "]": 57,
             "}": 1197,
             ">": 25137}
    for y, line in enumerate(data.splitlines()):
        stack = []
        for c in line:
            if c in op:
                stack.append(c)
            else:
                if brackets[c] == stack[-1]:
                    stack.pop(-1)
                else:
                    count+= score[c]
                    break
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
    example()
    print(sol(data))
    return 0


INPUT = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


def example():
    assert sol(INPUT) == 26397


if __name__ == '__main__':
    exit(main())
