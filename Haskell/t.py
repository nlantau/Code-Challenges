
def trouble(x, t):
    temp = 0
    res = list()
    for i in range(0, len(x) - 1):
        if x[i] + x[i + 1] == t:
            temp = x[i + 1]
        if x[i] != temp:
            res.append(x[i])
    return res

print(trouble([1,3,5,6,7,4,3], 7))
print(trouble([4, 1, 1, 1, 4], 2))
            # Fuck off...