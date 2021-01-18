"""
All seats except edges:
[i-1][j-1]  [i-1][j]  [i-1][j+1]
[i][j-1]    >[i][j]<    [i][j+1]
[i+1][j-1]  [i+1][j]  [i+1][j+1]

Left edge, top:         Right edge, top:
[i][0]<  [i][1]      [i][-2]    >[i][-1]
[i+1][0] [i+1][1]    [i+1][-2] [i+1][-1]

Left edge, bottom       Right edge, bottom
[i-1][0] [i-1][1]       [i-1][-2] [i-1][-1]
[i][0]<  [i][1]         [i][-2]    >[i][-1]

• Above is a pain in the butt to implement.
-> Add one row above and below
-> Add one col to the left and right
=> No indexoutofbounds

Prior:
L.LL.LL.LL = 10 elements
LLLLLLL.LL
L.L.L..L..

After:
........... = 12 elements
.L.LL.LL.LL.
.LLLLLLL.LL.
.L.L.L..L...
............

"""
import os
from collections import namedtuple

day = "11dummy.txt"


class Seats:
    def __init__(self, path, max=0):
        self.path = os.path.join(os.path.dirname(__file__), path)
        self.data = []
        with open(self.path, "r") as d:
            self.data = list(d.read().split())
        self.max = len(self.data)

    def add_borders(self):
        data = self.data
        dots = "".join(["." for _ in range(len(self.data) + 2)])
        d = []
        for row in data:
            d.append("." + row + ".")
        data = [dots] + d + [dots]
        self.data = data

    def update_data(self, new_list):
        # print(">>>>>>>> Prior:")
        # print(*self.get_seats(), sep="\n")
        self.data = new_list
        self.add_borders()
        # print(">>>>>>>> After:")
        # print(*self.get_seats(), sep="\n")

    def __iter__(self):
        for i in range(len(self.data)):
            yield self.data[i]

    def __len__(self, x_or_y="y"):
        if x_or_y == "y":  # count rows
            c = 0
            for row in self.data:
                c += 1
            return c
        return False

    def get_seats(self):
        return self.data

    def get_seats_no_border(self):
        data = self.data
        d = []
        for row in data:
            d.append(row[1 : len(row) - 1])
        d = d[1 : len(d) - 1]
        return d


s = Seats(day)
s.add_borders()
# print(*s.get_seats(), sep="\n")
"""
If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.

If a seat is occupied (#) and four or more seats adjacent to it are also occupied, 
the seat becomes empty.

Otherwise, the seat's state does not change.

"""


def check_neighbors(s: list, i: int, j: int, row_len, col_len):
    TL = s[i - 1][j - 1] != "#"
    TM = s[i - 1][j] != "#"
    TR = s[i - 1][j + 1] != "#"
    LS = s[i][j - 1] != "#"
    RS = s[i][j + 1] != "#"
    BL = s[i + 1][j - 1] != "#"
    BM = s[i + 1][j] != "#"
    BR = s[i + 1][j + 1] != "#"
    NL = [TL, TM, TR, LS, RS, BL, BM, BR]

    if i == 0:
        TL, TM, TR = True, True, True
    elif i + 1 == row_len:
        BL, BM, BR = False, False, False
    if j == 0:
        LS, TL, BL = True, True, True
    elif j + 1 == col_len:
        TR, RS, BR = False, False, False

    return sum(NL)


def check_adjecent(s):
    x = s
    s = s.get_seats()
    mod = list()
    for i, row in enumerate(s):
        if i == 0:
            continue
        if i == len(s) - 1:
            continue
        for j, seat in enumerate(range(1, len(row) - 1)):
            if row[seat] == "L":
                if check_neighbors(s, i, j, len(row), len(s)) == 8:
                    mod.append("#")
                else:
                    mod.append("L")
            elif row[seat] == "#":
                if check_neighbors(s, i, j, len(row), len(s)) < 4:
                    mod.append("L")
                else:
                    mod.append("#")
            else:
                mod.append(row[seat])
        mod.append("\n")
    mod = "".join(mod).split()
    x.update_data(mod)
    return x


# print(*s.get_seats(), sep="\n")
os.system("clear")
print(f"\n{ 'START' :-^50}")
s = check_adjecent(s)
print(">---------------------------------<")
print(*s.get_seats(), sep="\n")

print(">---------------------------------<")
s = check_adjecent(s)
print(*s.get_seats(), sep="\n")
print(">---------------------------------<")
print(*s.get_seats_no_border(), sep="\n")