# nlantau, 2020-12-04

import re

path = r"/Users/nlantau/Docs/GitHub/DT256CHT20/AoC/4.txt"
path2 = r"/Users/nlantau/Docs/GitHub/DT256CHT20/AoC/op.json"

batch = []
batch2 = []
pp_pattern = re.compile("(\w+):(\S+)")
pid_pattern = re.compile(r"[0-9]{9}")
v_list = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
cid = "cid"
ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def database():
    with open(path, "r") as r:
        te = r.read().split("\n\n")
        for q, i in enumerate(te):
            s = i.replace("\n", " ")
            batch.append({k: v for (k, v) in re.findall(pp_pattern, s)})


def check_validity(b: dict) -> bool:
    counter = 0
    counter = [counter + 1 for (k, v) in b.items() if k in v_list]
    return sum(counter) >= 7


def loop_check(b: list) -> int:
    valid = 0
    valid = [valid + 1 for di in b if check_validity(di)]
    return sum(valid)


def check_byr(d: dict) -> bool:
    return int(d["byr"]) >= 1920 and int(d["byr"]) <= 2002


def check_iyr(d: dict) -> bool:
    return int(d["iyr"]) >= 2010 and int(d["iyr"]) <= 2020


def check_eyr(d: dict) -> bool:
    return int(d["eyr"]) >= 2020 and int(d["eyr"]) <= 2030


def check_hgt(d: dict) -> bool:
    if "in" in d["hgt"]:
        return int(d["hgt"].strip("in")) >= 59 and int(d["hgt"].strip("in")) <= 76
    elif "cm" in d["hgt"]:
        return int(d["hgt"].strip("cm")) >= 150 and int(d["hgt"].strip("cm")) <= 193
    else:
        return False


def check_hcl(d: dict) -> bool:
    x = 0
    if d["hcl"][0] == "#":
        return 6 == sum(
            [
                int(x) + 1
                for i in d["hcl"][1:]
                if ord(i) >= 48 and ord(i) <= 57 or ord(i) >= 97 and ord(i) <= 102
            ]
        )


def check_ecl(d: dict) -> bool:
    return d["ecl"] in ecl_list


def check_pid(d: dict) -> bool:
    return re.fullmatch(pid_pattern, d["pid"]) != None


def loop_check_part2(b: list) -> int:
    valid = 0
    for d in b:
        if check_validity(d):
            if check_byr(d):
                if check_iyr(d):
                    if check_hcl(d):
                        if check_eyr(d):
                            if check_hgt(d):
                                if check_ecl(d):
                                    if check_pid(d):
                                        valid += 1
    return valid


if __name__ == "__main__":
    database()
    print(loop_check(batch))
    # print(*batch, sep="\n")
    print(f"Part A: {loop_check(batch)}")
    print(f"Part B: {loop_check_part2(batch)}")
    print(check_pid(te1))

    import json

    with open(path2, "w") as w:
        json.dump(batch, w)