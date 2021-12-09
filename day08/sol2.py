import argparse
from collections import defaultdict


def sol(data: str) -> int:
    # 1 4 7 8
    # 2 4 3 7
    count = 0
    vals = [val.split(" | ") for val in data.splitlines()]
    sums = []
    for val_ in vals:
        final_res = {}
        res = defaultdict(set)
        hist = defaultdict(int)
        for i in val_[0].split():
            for c1 in i:
                hist[c1] += 1
            res[len(i)].add(tuple(sorted(i)))
        for o in val_[1].split():
            res[len(o)].add(tuple(sorted(o)))
        one = res[2].pop()
        final_res["".join(one)] = 1
        seven = res[3].pop()
        final_res["".join(seven)] = 7
        eight = res[7].pop()
        final_res["".join(eight)] = 8
        four = res[4].pop()
        final_res["".join(four)] = 4
        for key, val in hist.items():
            if val == 4:
                e = key
            elif val == 9:
                f = key
            elif val == 6:
                b = key
        c = (set(one) - set(f)).pop()
        a = (set(seven) - set(one)).pop()

        hist5 = defaultdict(int)
        for val in res[5]:
            for c1 in val:
                hist5[c1] +=1
        horiz = set()
        for key, v in hist5.items():
            if v == 3:
                horiz.add(key)
                if key in set(four):
                    d = key
        g = (horiz - set(four) - set(seven)).pop()
        final_res["".join(sorted([a,b,c,e,f,g]))] = 0
        final_res["".join(sorted([a,c,d,e,g]))] = 2
        final_res["".join(sorted([a,c,d,f,g]))] = 3
        final_res["".join(sorted([a,b,d,f,g]))] = 5
        final_res["".join(sorted([a,b,d,e,f,g]))] = 6
        final_res["".join(sorted([a,b,c,d,f,g]))] = 9
        sum_num = 0
        for o in val_[1].split():
            sum_num*=10
            sum_num += final_res["".join(sorted(o))]
        count += sum_num

    # a = 8, b = 6, c = 8, d = 7, e = 4, f = 9, g = 7
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
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


def example():
    assert sol(INPUT) == 61229


if __name__ == '__main__':
    exit(main())
