# nlantau, 2021-11-03

def comp(b,a):
    if len(a)<1 or len(b)<1:
        return False

    b = sorted([i*i for i in b])
    a = sorted(a)
    for i,j in zip(a,b):
        if i != j:
            return False
    return True

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp(a,b))


