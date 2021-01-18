# nlantau, 2020-12-05

import re
import sys
import os

path = r"/Users/nlantau/Docs/GitHub/DT256CHT20/AoC/5.txt"


def main():
    fin = open(path, "r")
    lines = [line.strip() for line in fin.readlines() if line.strip()]
    max_ID = 0
    all_id = []
    for line in lines:
        num, col = [int(x) for x in range(0, 128)], [int(x) for x in range(8)]
        row, seat, ID = 0, 0, 0
        for pivot in line:
            if pivot == "F":
                num = num[: len(num) // 2]
            elif pivot == "B":
                num = num[len(num) // 2 :]
            if len(num) == 1:
                row = num[0]
                if pivot == "L":
                    col = col[: len(col) // 2]
                elif pivot == "R":
                    col = col[len(col) // 2 :]
                if len(col) == 1:
                    seat = col[0]
                    ID = row * 8 + seat
                    all_id.append(ID)
                    if ID > max_ID:
                        max_ID = ID
    print(max_ID)
    all_id = sorted(all_id)
    for i, e in enumerate(all_id):
        if e - 1 not in all_id:
            print(e - 1)


if __name__ == "__main__":
    main()