#!/usr/bin/python3
# nlantau, 2021-08-17



def to_alternating_case(s):
    x = ''
    for c in s:
        if 64 < ord(c) < 91:
            x += c.lower()
        elif 96 < ord(c) < 123:
            x += c.upper()
        elif c.isspace():
            x += ' '
        else:
            x += c
    return x





a = "HELLO WORLD"
b = "hello WORLD"
c = "123"
d = "a1B2c3"

print(to_alternating_case(a))
print(to_alternating_case(b))
print(to_alternating_case(c))
print(to_alternating_case(d))
