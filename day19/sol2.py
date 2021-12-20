import argparse
from collections import defaultdict, Counter
from copy import deepcopy
from typing import List, Tuple


def directions(x, y, z):
    return [(x, y, z),
            (x, -y, -z),
            (x, z, -y),
            (x, -z, y),

            (-x, z, y),
            (-x, -z, -y),
            (-x, y, -z),
            (-x, -y, z),

            (y, -x, z),
            (y, x, -z),
            (y, z, x),
            (y, -z, -x),

            (-y, x, z),
            (-y, -x, -z),
            (-y, z, -x),
            (-y, -z, x),

            (z, x, y),
            (z, -x, -y),
            (z, y, -x),
            (z, -y, x),

            (-z, -x, y),
            (-z, x, -y),
            (-z, y, x),
            (-z, -y, -x),
            ]


def sol(data: str) -> int:
    scanners = []
    for val in data.split("\n\n"):
        print(val.splitlines()[0])
        scanners.append([tuple([int(v) for v in va.split(",")]) for va in
                         val.splitlines()[1:]])
    print(scanners[0])
    scanner = scanners.pop(0)
    solved_beacons = set(scanner)
    scanner_pos = [(0, 0, 0)]
    while scanners:
        scanner = scanners.pop(0)
        flag = False
        for solved_beacon in deepcopy(solved_beacons):
            for i in range(24):
                s_direction = [directions(x, y, z)[i] for x, y, z in scanner]
                for val1 in s_direction:
                    diff_x = val1[0] - solved_beacon[0]
                    diff_y = val1[1] - solved_beacon[1]
                    diff_z = val1[2] - solved_beacon[2]
                    new_s = set(
                        [(v1[0] - diff_x, v1[1] - diff_y, v1[2] - diff_z) for v1
                         in s_direction])
                    if len(new_s.intersection(solved_beacons)) >= 12:
                        print(f"{diff_x},{diff_y},{diff_z} -> {len(new_s.intersection(solved_beacons))}")
                        scanner_pos.append((diff_x, diff_y, diff_z))
                        for beacon in new_s - solved_beacons:
                            solved_beacons.add(beacon)
                        flag = True
                        break
                else:
                    continue
                if flag:
                    break
            if flag:
                break
        if not flag:
            scanners.append(scanner)
    max_val = 0
    for x1, y1, z1 in scanner_pos:
        for x2, y2, z2 in scanner_pos:
            d = (abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))
            max_val = max(d, max_val)
    print(max_val)
    return max_val


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
--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
"""


def example():
    assert {(5, 6, -4), (-5, 4, -6), (4, 6, 5), (-4, -6, 5),
            (-6, -4, -5)} < set(directions(5, 6, -4))
    assert sol(INPUT) == 3621


if __name__ == '__main__':
    exit(main())
