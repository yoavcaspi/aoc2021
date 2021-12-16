import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple


def sol(data: str) -> int:
    val = int(data, 16)
    bin_val = bin(val)[2:]
    if "0"<= data[0] < "8":
        bin_val = "0" + bin_val
    print(bin_val)
    i = 0
    version_number = 0
    while i < len(bin_val):
        i, val, version_number, _ = sub_packet(bin_val, i, version_number, len(bin_val))
    print(f"{version_number}")
    return version_number


def sub_packet(bin_val, i, version_number, max_i):
    if max_i - i <= 8:
        return max_i, 0, version_number, max_i
    version = int(bin_val[i:i + 3], 2)
    version_number += version
    i += 3
    type_id = int(bin_val[i:i + 3], 2)
    i += 3
    print(f"{type_id=}")
    if type_id == 4:
        print(f"Literal={version=}==================")
        val, i = get_literal(bin_val, i, max_i)
    else:
        print(f"Operator={version=}=================")
        if bin_val[i] == "0":
            i += 1
            length = int(bin_val[i:i + 15], 2)
            i += 15
            print(f"{length=}")
            new_i, val, version_number, _ = sub_packet(bin_val, i, version_number, i + length)
            while new_i - i < length:
                new_i, val, version_number, _ = sub_packet(bin_val, new_i, version_number, i + length)
            assert new_i - i == length
            i = new_i
        else:
            i += 1
            num_packets = int(bin_val[i:i + 11],2)
            print(f"{num_packets=}")
            i += 11

            for _ in range(num_packets):
                i, val, version_number, _ = sub_packet(bin_val, i,version_number, max_i)
    return i, val, version_number, max_i


def get_literal(bin_val, i, max_i):
    flag = True
    number = ""
    while flag and i < len(bin_val):
        if bin_val[i] == "0":
            flag = False
        i += 1
        number += bin_val[i:i + 4]
        i += 4
    # while i < max_i and bin_val[i] == "0":
    #     i += 1
    if number == "":
        number = 0
    else:
        number = int(number, 2)
    print(f"{number=}")
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


INPUT_A = """\
8A004A801A8002F478
"""
INPUT_0 = "D2FE28"
INPUT_B = "620080001611562C8802118E34"
INPUT_C = "C0015000016115A2E0802F182340"
INPUT_D = "A0016C880162017C3686B18A3D4780"


def example():
    # assert sol(INPUT_0) == 16
    print("A")
    # assert sol(INPUT_A) == 16
    print("B")
    assert sol(INPUT_B) == 12
    print("C")
    assert sol(INPUT_C) == 23
    print("D")
    assert sol(INPUT_D) == 31


if __name__ == '__main__':
    exit(main())
