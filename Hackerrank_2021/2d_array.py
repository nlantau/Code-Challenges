# nlantau, 2021-01-18

import fileinput

L = [i.split() for i in list(fileinput.input())]
L = [[int(i) for i in L[x]] for x in range(6)]

# Largest hourglass sum = 19
def hourglassSum(a):
    R = len(a)
    lr = R -3
    C = len(a[0])
    lc = C - 2

    t = list()
    s = 0
    for r in range(R):
        for c in range(C):
            if 0<=r<=lr and 1<=c<=lc:
                for dr in [0,1,2]:
                    for dc in [-1,0,1]:
                        rr = r + dr
                        cc = c + dc
                        if rr == r:
                            s += a[rr][cc]
                        if rr == r + 1 and cc == c:
                            s += a[rr][cc]
                        if rr == r + 2:
                            s += a[rr][cc]
                t.append(s)
                s = 0

    return max(t)

print(hourglassSum(L))
