import fileinput
from collections import deque
from copy import deepcopy
import re


n, a = fileinput.input()
dig = re.compile(r'\d')
sa = re.findall(dig, n)[0]
d = re.findall(dig, n)[1]
d = int(d)
a = re.findall(dig, a)
a = [int(i) for i in a]

# collections, deque
def rotLeft(a,d):
    from collections import deque
    a = deque(a)
    a.rotate(-d)
    return list(a)

# Modulus
def rotLeft_mod(a,d):
    #a = [a[(i+d)%len(a)] for i,x in enumerate(a)]
    b = list()
    for i,x in enumerate(a):
        b.append(a[(i+d)%len(a)])
    return b

print(rotLeft(deepcopy(a),d))
print(rotLeft_mod(deepcopy(a),d))
