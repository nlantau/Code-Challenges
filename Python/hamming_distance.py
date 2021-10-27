# nlantau, 2021-10-28

def hamminga(a, b):
    x = 0
    for c,d in zip(a,b):
        if c != d:
            x += 1
    return x


hamming2 = lambda a,b: sum([1 for c,d in zip(a,b) if c != d])

# hamming = lambda a,b: abs(sum([*map(ord, a)]) - sum([*map(ord, b)]))

# hamming = lambda a,b: len([*filter(lambda a: a[0] != a[1], zip(a,b))])

hamming=lambda a,b:sum(filter(bool,map(lambda x,y:x!=y,a,b)))

# hamming = lambda a,b: [*zip(a,b)]

print(hamming("Hello World","Hello World"))
print(hamming("I like turtles","I like turkeys"))
