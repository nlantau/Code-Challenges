import fileinput
from copy import deepcopy


L = [list(l.strip()) for l in list(fileinput.input())]
R = len(L)
C = len(L[0])

print(L,C,R)

while True:
    newL = deepcopy(L)
    change = False

    for r in range(R):
        for c in range(C):
            nocc = 0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if not (dr==0 and dc==0):
                        rr = r+dr # neighbor row
                        cc = c+dc # neighbor col

                        while 0<=rr<R and 0<=cc<C and L[rr][cc]=='.':
                            rr = rr+dr
                            cc = cc+dc
                            print(rr, "rr")
                            print(cc, "cc")
                        if 0<=rr<R and 0<=cc<C and L[rr][cc]=="#":
                            nocc += 1

            if L[r][c]=='L':
                if nocc==0:
                    newL[r][c]='#'
                    change=True
            elif L[r][c] == '#' and nocc>=4:
                newL[r][c]='L'
                change=True
    if not change:
        break
    L = deepcopy(newL)


