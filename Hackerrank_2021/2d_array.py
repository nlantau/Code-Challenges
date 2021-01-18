# nlantau, 2021-01-18

# Works for 7/9 test cases. The failing cases are locked, so I don't understand what's
# not working. I'm pretty proud about this solution otherwise. 

sample = [
        [1, 1, 1, 0, 0, 0], #0
        [0, 1, 0, 0, 0, 0], #1
        [1, 1, 1, 0, 0, 0], #2
        [0, 0, 2, 4, 4, 0], #3
        [0, 0, 0, 2, 0, 0], #4
        [0, 0, 1, 2, 4, 0], #5
        ]

# Largest hourglass sum = 19
def hourglassSum(a):
    R = len(a)
    lr = R -3
    C = len(a[0])
    lc = C - 2

    t = 0
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
            if s > t:
                t = s
            s = 0
    return t

print(hourglassSum(sample))
