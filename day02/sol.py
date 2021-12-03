import argparse
from typing import List, Tuple


def sol(data: List[str]) -> int:
    data_int: List[Tuple[str, int]] = [(val.split(" ")[0], int(val.split(" ")[1])) for val in data]
    f = 0
    d = 0
    for direction, size in data_int:
        if direction == "forward":
            f += size
        elif direction == "down":
            d += size
        elif direction == "up":
            d -= size
        else:
            print(direction)
    return d*f


def sol2(data: List[str]) -> int:
    data_int: List[Tuple[str, int]] = [(val.split(" ")[0], int(val.split(" ")[1])) for val in data]
    aim = 0
    f = 0
    d = 0
    for direction, size in data_int:
        if direction == "forward":
            f += size
            d += aim*size
        elif direction == "down":
            aim += size
        elif direction == "up":
            aim -= size
        else:
            print(direction)
    return d*f


def get_input(filename: str) -> List[str]:
    with open(filename) as f:
        lines = f.readlines()
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='input.txt')
    args = parser.parse_args()
    data = get_input(args.filename)
    print(sol(data))
    print(sol2(data))
    return 0


if __name__ == '__main__':
    exit(main())
