import argparse
from collections import defaultdict
from typing import List


def check_rows(boards, not_winners):
    last_remove = -1
    for board_id, board in boards.items():
        for i in range(5):
            for j in range(5):
                if board[(i, j)][1] == 0:
                    break
            else:
                if board_id in not_winners:
                    not_winners.remove(board_id)
                    last_remove = board_id

    return False, last_remove


def check_colunns(boards, not_winners):
    last_remove = -1
    for board_id, board in boards.items():
        for i in range(5):
            vals = True
            for j in range(5):
                if board[(j, i)][1] == 0:
                    break
            else:
                if board_id in not_winners:
                    not_winners.remove(board_id)
                    last_remove = board_id
    return False, last_remove


def check_for_winner(boards, not_winners):
    is_winner, board_id = check_rows(boards, not_winners)
    is_winner, board_id2 = check_colunns(boards, not_winners)
    if board_id2 == -1:
        return True, board_id
    else:
        return True, board_id2


def sol(data: List[str]) -> int:
    bingo_order = [int(val) for val in data.split("\n")[0].split(",")]

    boards = defaultdict(dict)
    boards_not_won = set()
    for i, board in enumerate(data.split("\n\n")[1:]):
        for row, line in enumerate(board.split("\n")):
            for column, val in enumerate(line.split()):
                boards[i][(row, column)] = (int(val), 0)
        boards_not_won.add(i)
    for current in bingo_order:
        for board in boards.values():
            for key, val in board.items():
                if current == val[0]:
                    board[key] = (val[0], 1)

        is_winner, board_id = check_for_winner(boards, boards_not_won)
        if len(boards_not_won) == 0:
            count = 0
            for val in boards[board_id].values():
                if val[1] == 0:
                    count += val[0]

            return (current * count)


def get_input(filename: str) -> str:
    with open(filename) as f:
        lines = f.read()
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
