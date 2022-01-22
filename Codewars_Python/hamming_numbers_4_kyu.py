# nlantau, 2021-10-28
l = list()
for i in range(5):
    for j in range(5):
        for k in range(5):
            l.append(2**i * 3**j * 5**k)

print(sorted(l))
