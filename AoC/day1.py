# nlantau, 2020-12-01
# Day 1 of AoC

path = r"/Users/nlantau/Docs/GitHub/DT256CHT20/AoC/1.txt"

with open(path, "r") as reader:
    numbs = [int(x.strip("\n")) for x in reader.readlines()]

for num in numbs:
    for el in numbs:
        if num + el == 2020:
            print(f"num:{num} el:{el}")
            print(f"{num}*{el}={num*el}")

# Part 2
for o in numbs:
    for u in numbs:
        for j in numbs:
            if o + u + j == 2020:
                print(f"{o} {u} {j}")
                print(o * u * j)

