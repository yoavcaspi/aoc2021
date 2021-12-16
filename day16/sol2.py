import argparse
import math
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    val = int(data, 16)
    bin_val = bin(val)[2:]
    if "0" <= data[0] < "8":
        bin_val = "0" + bin_val
    i = 0
    version_number = 0
    while i < len(bin_val):
        i, val, version_number = sub_packet(bin_val, i, version_number)
        if len(bin_val) - i <= 8:
            break
    return val


def sub_packet(bin_val, i, version_number):
    version = int(bin_val[i:i + 3], 2)
    version_number += version
    i += 3
    type_id = int(bin_val[i:i + 3], 2)
    i += 3
    if type_id == 4:
        ret_val, i = get_literal(bin_val, i)
        return i, ret_val, version_number
    else:
        vals = []
        if bin_val[i] == "0":
            i += 1
            length = int(bin_val[i:i + 15], 2)
            i += 15
            new_i, val, version_number = sub_packet(bin_val, i, version_number)
            vals.append(val)
            while new_i - i < length:
                new_i, val, version_number = sub_packet(bin_val, new_i, version_number)
                vals.append(val)
            assert new_i - i == length
            i = new_i
        else:
            i += 1
            num_packets = int(bin_val[i:i + 11],2)
            i += 11
            for _ in range(num_packets):
                i, val, version_number = sub_packet(bin_val, i, version_number)
                vals.append(val)
        ret_val = 0
        if type_id == 0:
            ret_val = sum(vals)
        elif type_id == 1:
            ret_val = math.prod(vals)
        elif type_id == 2:
            ret_val = min(vals)
        elif type_id == 3:
            ret_val = max(vals)
        elif type_id == 5:
            ret_val = 1 if vals[0] > vals[1] else 0
        elif type_id == 6:
            ret_val = 1 if vals[0] < vals[1] else 0
        elif type_id == 7:
            ret_val = 1 if vals[0] == vals[1] else 0

        return i, ret_val, version_number


def get_literal(bin_val, i):
    flag = True
    number = ""
    while flag and i < len(bin_val):
        if bin_val[i] == "0":
            flag = False
        i += 1
        number += bin_val[i:i + 4]
        i += 4
    if number == "":
        number = 0
    else:
        number = int(number, 2)
    return number, i


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


INPUT_C = "880086C3E88112"
INPUT_D = "CE00C43D881120"


def example():
    # assert sol(INPUT_0) == 16
    assert sol(INPUT_C) == 7
    assert sol(INPUT_D) == 9


if __name__ == '__main__':
    exit(main())
