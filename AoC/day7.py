# nlantau, 2020-12-07

import os, sys, re, math

day = "7.txt"
path = os.path.abspath(os.curdir) + r"/AoC/" + str(day)
fin = open(path, "r")

lines = [
    line.strip().replace(",", "").replace(".", "")
    for line in fin.readlines()
    if line.strip()
]
# lines = fin.read().split("\n\n")


def main():
    li = lines
    ba = "shiny gold"
    sg = [l.replace("bags", "").replace("bag", "") for l in li]
    sg = [l for l in sg if "no other" not in l]
    la = []
    sd = dict()
    for li in sg:
        w = re.match("(\w+)\s(\w+)\s", li)
        sd[w.group(0).strip(" ")] = 0

    print(*sg, sep="\n")
    print(f"Line count: {len(sg)}")
    print(la)
    print(sd)


if __name__ == "__main__":
    main()