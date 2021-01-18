# nlantau, 2020-12-07

import os, sys, re, math

day = "8.txt"
path = os.path.join(os.path.dirname(__file__), day)

fin = open(path, "r")
data = fin.readlines()

code = list()
for line in data:
    op, arg = line.split()
    code.append([["nop", "jmp", "acc"].index(op), int(arg)])
print(code)

NOP, JMP, ACC = range(3)
visited = set()
ip = 0
acc = 0
while ip not in visited and ip < len(code):
    visited.add(ip)
    op, arg = code[ip]
    print(op, arg)

    if op == 1:
        ip += arg
    elif op == 2:
        acc += arg
        ip += 1
    else:
        ip += 1
print(ip >= len(code), acc)
