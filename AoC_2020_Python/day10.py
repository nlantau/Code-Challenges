import os
import collections as c
import heapq
import itertools as it
from functools import lru_cache

data = "10dummy.txt"
data = os.path.join(os.path.dirname(__file__), data)

fin = open(data, "r")
d = list(map(int, fin.readlines()))
d = sorted(d)

diff_one = 0
diff_three = 0
d = [0] + d + [d[-1] + 3]
for i in range(len(d) - 1):
    if abs(d[i] - d[i + 1]) == 1:
        diff_one += 1
    if abs(d[i] - d[i + 1]) == 3:
        diff_three += 1


@lru_cache
def arrangements(i):
    if i >= len(d):
        return 1

    x = d[i]
    result = arrangements(i + 1)

    if i + 2 < len(d) and d[i + 2] - x <= 3:
        result += arrangements(i + 2)

        if i + 3 < len(d) and d[i + 3] - x <= 3:
            result += arrangements(i + 3)

    return result


print(diff_one * diff_three)
print(arrangements(0))


print(diff_one * diff_three)