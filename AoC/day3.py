# nlantau, 2020-12-03
import math
from aocd import data, submit


path = r"/Users/nlantau/Docs/GitHub/DT256CHT20/AoC/3.txt"

m = []

with open(path, "r") as r:
    for line in r.readlines():
        m.append(line.strip("\n"))

w = len(m[0])
sl = []


def s(n, r):
    x = 0
    trees = 0
    for row, line in enumerate(m):
        if row == 0:
            continue
        if r == 1:
            x += n
        elif r == 2 and row % 2 != 0:
            x += n
        if line[x % w] == "#":
            if r == 1:
                trees += 1
            elif r == 2 and row % 2 == 0:
                trees += 1
    sl.append(trees)


s(1, 1)
s(3, 1)  # part 1
s(5, 1)
s(7, 1)
s(1, 2)
print(sl)
print(math.prod(sl))
submit(math.prod(sl), part="b")