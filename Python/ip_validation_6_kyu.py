#!/usr/bin/python3
# nlantau, 2021-08-17

v1 = "1.2.3.4"
v2 = "123.45.67.89"

i1 = "1.2.3"
i2 = "1.2.3.4.5"
i3 = "123.456.78.90"
i4 = "123.045.067.089"

import re

def is_valid_IP(s):
    n = re.compile(r'\d+\.\d+\.\d+\.\d+')
    if not n.fullmatch(s):
        return False
    s = s.split(".")
    for n in s:
        if n[0] == '0' and len(n) > 1:
            return False
        try:
            x = int(n)
            if x > 255:
                return False
        except:
            return False
    print(f's: {s} len: {len(s)}')
    return True



print("> Valid")
print(is_valid_IP(v1))
print(is_valid_IP(v2))
print("> Invalid")
print(is_valid_IP(i1))
print(is_valid_IP(i2))
print(is_valid_IP(i3))
print(is_valid_IP(i4))
