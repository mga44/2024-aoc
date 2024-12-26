import utils
import re
from functools import reduce

bots = utils.read_lines("resources\\2024-12-14.txt")

max_x = 11  # 1,2,3,4,5 | 7,8,9,10,11 -->
max_y = 7  # 1,2,3 | 5,6,7

"""
  1 2 3 4 5 6 7 8 9 10 11
1           |
2           |
3           |
4 ------------------------
5           |
6           |
7           |
"""


def to_bot(line: str) -> dict:
    # p=0,4 v=3,-3
    p = re.findall(r"p=(\d+,\d+)", line)[0]
    v = re.findall(r"v=(.*)", line)[0]
    p = tuple(int(i) for i in p.split(","))
    v = tuple(int(i) for i in v.split(","))

    print(f"Creating bot: {p}, {v}")
    return {"p": p, "v": v}


def get_by_quadrants(bots_list):
    # 0 (v) 1
    # (h)
    # 2     3
    vert_divider = (max_x+1) / 2
    horiz_divider = (max_y+1) / 2
    qs = [0, 0, 0, 0]
    qs_2 = [[], [], [], []]
    for b in bots_list:
        x = b["p"][0]
        y = b["p"][1]
        if x == vert_divider or y == horiz_divider:
            continue

        if x < vert_divider and y < horiz_divider:
            qs[0] += 1
            qs_2[0].append(b["p"])
        elif x < vert_divider and y > horiz_divider:
            qs[1] += 1
            qs_2[1].append(b["p"])
        elif x > vert_divider and y < horiz_divider:
            qs[2] += 1
            qs_2[2].append(b["p"])
        elif x > vert_divider and y > horiz_divider:
            qs[3] += 1
            qs_2[3].append(b["p"])
        else:
            print(f'Not counting bot on {b["p"]}')

    print(f"Bots grouped in below quadrants: {qs_2}")
    return qs


bots = list(map(lambda line: to_bot(line), bots))


"""
p2 = p + v

if p2 < 0: max - (p2+1)
if p2 > max: p3 - max
"""


def move_in_direction(pos: int, vel: int, max_val: int) -> int:
    new_pos = (pos + vel) % max_val

    return new_pos


for sec in range(100):
    for bot in bots:
        p = bot["p"]
        v = bot["v"]
        bot["p"] = (
            move_in_direction(p[0], v[0], max_x),
            move_in_direction(p[1], v[1], max_y),
        )
        print(f'New bot position: {bot["p"]}')

print(list(str(b["p"]) for b in bots))
quadrants = get_by_quadrants(bots)
print(f"Quadrants sum: {quadrants}")
security_fact = reduce(lambda a, b: a * b, quadrants)

print(f"Security Factor is {security_fact}")
