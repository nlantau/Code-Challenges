def gimme(i):
    a, b, c = i
    print(a)
    print(b)
    print(c)
    if c > b > a:
        return b
    if b > a > c:
        return b
    if a > c > b:
        return c


print(gimme([3, 2, 1]))
