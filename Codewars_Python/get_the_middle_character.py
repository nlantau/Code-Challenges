# nlantau, 2020-11-08


def get_middle(s):
    return s[len(s) // 2 -1:len(s) // 2 +1] if len(s) % 2 == 0 else s[len(s) // 2: len(s) // 2 +1]


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
print(get_middle("of"))
