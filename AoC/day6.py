# nlantau, 2020-12-06

import os

day = "6.txt"
path = os.path.abspath(os.curdir) + r"/AoC/" + str(day)


def part1():
    fin = open(path, "r")
    lines = fin.read().split("\n\n")
    for i, group in enumerate(lines):
        lines[i] = "".join(set("".join(group.split())))
    lines = "".join(line for line in lines)
    print(len(lines))


def part2():
    fin = open(path, "r")
    lines = fin.read().split("\n\n")
    for i, el in enumerate(lines):
        lines[i] = el.split()
    valid = 0
    for i, group in enumerate(lines):
        for k, v in dict((x, "".join(group).count(x)) for x in set("".join(group))).items():
            if v == len(group):
                valid += 1
    print(valid)


if __name__ == "__main__":
    part1()
    part2()