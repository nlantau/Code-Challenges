# nlantau, 2021-01-17


INT_MIN=-32422


def cut_log(p,n):
    r = [0 for _ in range(n+1)]
    r[0] = 0
    for j in range(1,n+1):
        q = INT_MIN
        for i in range(1,j+1):
            q = max(q, p[i] + r[j-i])
        r[j] = q
    return r[n]


# Clever solutions
def cl(p,n):
    l = [0]
    for _ in range(n):
        l.append(max(pi+li for pi, li in zip(p[1:], l[::-1])))
    return l[n]


p = [  0,   1,   5,   8,   9,  10,  17,  17,  20,  24, # 0X's
      30,  32,  35,  39,  43,  43,  45,  49,  50,  54, # 1X's
      57,  60,  65,  68,  70,  74,  80,  81,  84,  85, # 2X's
      87,  91,  95,  99, 101, 104, 107, 112, 115, 116, # 3X's
     119] # 40th element



print(cut_log(p, 8), "should equal 22")
print(cl(p, 8), "should equal 22")
print(cut_log(p, 10), "should equal 30")
print(cl(p, 10), "should equal 30")
print(cut_log(p, 22), "should equal 65")
print(cl(p, 22), "should equal 65")
print(cut_log(p, 35), "should equal 105")
print(cl(p, 35), "should equal 105")
