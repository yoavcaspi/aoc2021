import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from itertools import product
from typing import List, Tuple, NamedTuple, Any, Dict


def sol(data: str) -> int:
    min_val = 163857431

    # for j, v in enumerate(product('123456789', repeat=4)):
    #     v = "".join(v)
    #     for val2 in "12345":
    #         v2 = v+val2+str(int(val2)+4)
    #         for val3 in "1234567":
    val = "22811513911391"
    x1 = "23456789"
    val = "21611513911181"
    i = 0
    reg = {"w": 0,
           "x": 0,
           "y": 0,
           "z": 0,
           }
    for inst in data.splitlines():
        opcode, *values = inst.split(" ")
        if opcode == "inp":
            if i == len(val):
                break
            reg[values[0]] = int(val[i])
            i+=1
        else:
            a, b = values
            if b in ["w", "x", "y", "z"]:
                b = reg[b]
            else:
                b = int(b)
            if opcode == "add":
                reg[a] += b
            elif opcode == "mul":
                reg[a] *= b
            elif opcode == "div":
                reg[a] = reg[a] // b
            elif opcode == "mod":
                reg[a] = reg[a] % b
            else:
                reg[a] = int(reg[a] == b)
    # if reg['z'] <= min_val:
    #     min_val = reg['z']
    print(f"{''.join(val)}, {reg}")
    return 0

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
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
"""


def example():
    sol(INPUT)


if __name__ == '__main__':
    exit(main())
