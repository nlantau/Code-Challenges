# nlantau, 2020-12-02

import regex as re

path = r"/Users/nlantau/Docs/GitHub/DT256CHT20/AoC/2.txt"

first_num = 0
second_num = 0
tot = 0
tot2 = 0

with open(path, "r") as r:
    lines = r.readlines()
    for line in lines:
        first_num, second_num = re.findall(r"\d+", line)
        match_letter = re.findall(r"\w:", line)
        ml = match_letter[0].strip(":")
        psw = line.split(" ")[2]
        counter = 0
        for ch in psw:
            if ml is ch:
                counter += 1
        if counter in range(int(first_num), int(second_num) + 1):
            tot += 1
        # part 2
        try:
            if ml == psw[int(first_num) - 1] and ml != psw[int(second_num) - 1]:
                tot2 += 1
            elif ml != psw[int(first_num) - 1] and ml == psw[int(second_num) - 1]:
                tot2 += 1
        except IndexError:
            continue


print(tot)
print(tot2)
