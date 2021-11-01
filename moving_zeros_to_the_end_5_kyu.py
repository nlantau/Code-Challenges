#!/usr/bin/python
# nlantau, 2021-11-01

move_zeros=lambda x:[*filter(lambda r:r>0, x)]+[0 for _ in range(len(x)-len([*filter(lambda r:r>0, x)]))]


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
