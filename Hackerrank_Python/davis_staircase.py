# nlantau, 2021-01-18

# 1, 2 or 3 steps at a time

def sp(n):
    m = int(1e10+7)
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2
    else:
        x = sp(n-1)+sp(n-2)+sp(n-3)
        return x % m

def stepPerms(n):
    m = int(1e10+7)
    res = [0] * (n + 2)
    res[0] = 1
    res[1] = 1
    res[2] = 2

    for i in range(3, n + 1):
        res[i] = res[i-1] + res[i-2] + res[i-3]

    return res[n] % m

n = 7

print(sp(n))
print(stepPerms(n))


