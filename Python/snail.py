#!/usr/bin/python
# nlantau, 2021-11-01

import numpy as np

def snail(m):
    f=[]
    if len(m) < 1:
        return [[]]
    m = np.array(m)
    f.extend(m[0])

    while True:
        if len(m[0]) < 1:
            break
        m = np.rot90(np.delete(m, 0, 0))
        f.extend(m[0])
    return f






a = [
        [1,2,3],
        [8,9,4],
        [7,6,5]
        ]

print(snail(a))


