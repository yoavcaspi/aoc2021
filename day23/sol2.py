import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple, NamedTuple, Any, Dict


class AmphiState(NamedTuple):
    state: str
    x: int
    y: int

energy = {"A": 1,
          "B": 10,
          "C": 100,
          "D": 1000}
final_pos = {"A": 3, "B": 5, "C": 7, "D": 9}

cache = {}
class State(NamedTuple):
    amphi: Dict[str, AmphiState]
    board: Any
    energy: int

    def sol(self, min_res, stack):
        if not self.is_valid_state():
            return -1
        # print(f"        {min_res} {self.energy}")
        fp = tuple((sorted([(key[0],val) for key,val in self.amphi.items()])))
        if fp not in cache:
            cache[fp] = self.energy
        else:
            if cache[fp] <= self.energy:
                return -1
            else:
                cache[fp] = self.energy
        if self.energy + self.min_left() >= min_res:
            return -1
        for key in ["A0", "A1", "A2", "A3",
                    "B0", "B1", "B2", "B3",
                    "C0", "C1", "C2", "C3",
                    "D0", "D1", "D2", "D3",
                    ]:
            val = self.amphi[key]
            if val.state == "final":
                continue
            elif val.state == "moved":
                flag, y, x = self.col_free(key[0])
                if flag and self.free_to_move(val.x, x):
                    new_board = deepcopy(self.board)
                    new_amphi = deepcopy(self.amphi)
                    new_board[y,x] = key[0]
                    new_board[val.y, val.x] = "."
                    new_amphi[key] = AmphiState("final", x, y)
                    new_energy = self.energy + (y - 1 + abs(val.x - final_pos[key[0]])) * energy[key[0]]
                    # print(f"{key} -> final")
                    res = State(new_amphi, new_board, new_energy).sol(min_res, f"{stack}-{key}{y}{x}")
                    if res > 0:
                        min_res = min(min_res, res)
            elif val.state == "init":
                if self.board[val.y -1, val.x] != ".":
                    continue
                for x in range(val.x, 12):
                    if self.board[1, x] != ".":
                        break
                    new_board = deepcopy(self.board)
                    new_amphi = deepcopy(self.amphi)
                    new_board[1, x] = key[0]
                    new_board[val.y, val.x] = "."
                    new_amphi[key] = AmphiState("moved", x, 1)
                    new_energy = self.energy + (val.y - 1 + abs(val.x - x)) * energy[key[0]]
                    # print(f"{key} -> moved to {x}")
                    res = State(new_amphi, new_board, new_energy).sol(min_res, stack+key+"1"+str(x))
                    if res > 0:
                        min_res = min(min_res, res)
                for x in reversed(range(1, val.x)):
                    if self.board[1, x] != ".":
                        break
                    new_board = deepcopy(self.board)
                    new_amphi = deepcopy(self.amphi)
                    new_board[1, x] = key[0]
                    new_board[val.y, val.x] = "."
                    new_amphi[key] = AmphiState("moved", x, 1)
                    # print(f"{key} -> moved to {x}")
                    new_energy = self.energy + (val.y - 1 + abs(val.x - x)) * energy[key[0]]
                    res = State(new_amphi, new_board, new_energy).sol(min_res, stack+key+"1"+str(x))
                    if res > 0:
                        min_res = min(min_res, res)
        if all([val.state == "final" for val in self.amphi.values()]):
            print(f"Final score: {self.energy}, {min_res=}")
            return self.energy
        else:
            if min_res == 10000000:
                return -1
            return min_res

    def sol1(self, min_res, stack):
        if not self.is_valid_state():
            return -1
        # print(f"        {min_res} {self.energy}")
        if self.energy + self.min_left() >= min_res:
            return -1
        for key in ["A0", "A1", "A2", "A3",
                    "B0", "B1", "B2", "B3",
                    "C0", "C1", "C2", "C3",
                    "D0", "D1", "D2", "D3"
                    ]:
            val = self.amphi[key]
            if val.state == "final":
                continue
            elif val.state == "moved":
                flag, y, x = self.col_free(key[0])
                if flag and self.free_to_move(val.x, x):
                    new_board = deepcopy(self.board)
                    new_amphi = deepcopy(self.amphi)
                    new_board[y,x] = key[0]
                    new_board[val.y, val.x] = "."
                    new_amphi[key] = AmphiState("final", x, y)
                    new_energy = self.energy + (y - 1 + abs(val.x - final_pos[key[0]])) * energy[key[0]]
                    # print(f"{key} -> final")
                    res = State(new_amphi, new_board, new_energy).sol(min_res, stack+key+y+x)
                    if res > 0:
                        min_res = min(min_res, res)
            elif val.state == "init":
                if self.board[val.y -1, val.x] != ".":
                    continue
                for x in range(val.x, 12):
                    if self.board[1, x] != ".":
                        break
                    new_board = deepcopy(self.board)
                    new_amphi = deepcopy(self.amphi)
                    new_board[1, x] = key[0]
                    new_board[val.y, val.x] = "."
                    new_amphi[key] = AmphiState("moved", x, 1)
                    new_energy = self.energy + (val.y - 1 + abs(val.x - x)) * energy[key[0]]
                    print(f"{key} -> moved to {x}")
                    res = State(new_amphi, new_board, new_energy).sol(min_res, stack+key+"1"+str(x))
                    if res > 0:
                        min_res = min(min_res, res)
                for x in reversed(range(1, val.x)):
                    if self.board[1, x] != ".":
                        break
                    new_board = deepcopy(self.board)
                    new_amphi = deepcopy(self.amphi)
                    new_board[1, x] = key[0]
                    new_board[val.y, val.x] = "."
                    new_amphi[key] = AmphiState("moved", x, 1)
                    print(f"{key} -> moved to {x}")
                    new_energy = self.energy + (val.y - 1 + abs(val.x - x)) * energy[key[0]]
                    res = State(new_amphi, new_board, new_energy).sol(min_res, stack+key+"1"+str(x))
                    if res > 0:
                        min_res = min(min_res, res)
        if all([val.state == "final" for val in self.amphi.values()]):
            print(f"Final score: {self.energy}, {min_res=}")
            return self.energy
        else:
            if min_res == 10000000:
                return -1
            return min_res

    def free_to_move(self, x1, x2):
        for x in range(min(x1, x2) + 1, max(x1,x2)):
            if self.board[1, x] != ".":
                return False
        return True

    def is_valid_state(self):
        return (
                self.board[1,3] == "." and
                self.board[1,5] == "." and
                self.board[1,7] == "." and
                self.board[1,9] == "."
        )

    def col_free(self, key):
        if key == "A":
            return self.a_free()
        elif key == "B":
            return self.b_free()
        elif key == "C":
            return self.c_free()
        elif key == "D":
            return self.d_free()

    def a_free(self):
        room = "".join([self.board[i, 3] for i in range(2,6)])
        if room in [
            "....",
            "...A",
            "..AA",
            ".AAA",
        ]:
            return True, room.rfind(".") + 2, 3
        else:
            return False, -1, -1

    def b_free(self):
        room = "".join([self.board[i, 5] for i in range(2,6)])
        if room in [
            "....",
            "...B",
            "..BB",
            ".BBB",
        ]:
            return True, room.rfind(".") + 2, 5
        else:
            return False, -1, -1

    def c_free(self):
        room = "".join([self.board[i, 7] for i in range(2,6)])
        if room in [
            "....",
            "...C",
            "..CC",
            ".CCC"
        ]:
            return True, room.rfind(".") + 2, 7
        else:
            return False, -1, -1

    def d_free(self):
        room = "".join([self.board[i, 9] for i in range(2,6)])
        if room in [
            "....",
            "...D",
            "..DD",
            ".DDD",
        ]:
            return True, room.rfind(".") + 2, 9
        else:
            return False, -1, -1

    def min_left(self):
        res = 0

        for key, val in self.amphi.items():
            if val.state == "final":
                continue
            if val.state == "moved":
                res += (abs(val.x - final_pos[key[0]]) + 1) * energy[key[0]]
            if val.state == "init":
                steps = min(4, (abs(val.x - final_pos[key[0]]) + val.y))
                res += steps * energy[key[0]]
        return res


def sol(data: str) -> int:
    board = {}
    num_a = 0
    num_b = 0
    num_c = 0
    num_d = 0
    amphi = {}
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            board[y, x] = c
            if c == "A":
                amphi[f"A{num_a}"] = AmphiState("init", x, y)
                num_a +=1
            if c == "B":
                amphi[f"B{num_b}"] = AmphiState("init", x, y)
                num_b +=1
            if c == "C":
                amphi[f"C{num_c}"] = AmphiState("init", x, y)
                num_c +=1
            if c == "D":
                amphi[f"D{num_d}"] = AmphiState("init", x, y)
                num_d +=1
    final_pos = {"A": 3, "B": 5, "C": 7, "D": 9}
    for key, val in amphi.items():
        if val.y == 5 and final_pos[key[0]] == val.x:
            amphi[key] = AmphiState("final", val.x, val.y)
    state = State(amphi, board, 0)
    val = state.sol1(10000000, "")
    print(val)
    return val


def get_input(filename: str) -> str:
    with open(filename) as f:
        lines = f.read()
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='input2.txt')
    args = parser.parse_args()
    data = get_input(args.filename)
    # example()
    print(sol(data))
    return 0


INPUT = """\
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########
"""


def example():
    assert sol(INPUT) == 44169


if __name__ == '__main__':
    exit(main())
