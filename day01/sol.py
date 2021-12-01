import argparse
from typing import List


def sol(data: List[str]) -> int:
    data_int: List[int] = [int(val) for val in data]
    count = 0
    for a, b in zip(data_int, data_int[3:]):
        if a < b:
            count += 1
    return count


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
    return 0


if __name__ == '__main__':
    exit(main())
