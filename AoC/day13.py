import os
from collections import *

day = "13.txt"
day = os.path.join(os.path.dirname(__file__), day)
"""
bus_7 = 7
bus_13 = 13
time_stamp = 939
bus_7_closest = (time_stamp // bus_7) * bus_7
bus_13_closest = (time_stamp // bus_13) * bus_13
print(bus_7_closest)
print(bus_13_closest)
"""


def read_file_p1(day):
    fin = open(day, "r")
    data = fin.read().split()
    time_stamp = int(data[0])
    bus_list = data[1].split(",")
    return bus_list, time_stamp


def part_one(bus_list, time_stamp):
    bus_list = [int(i) for i in bus_list if i.isdigit()]
    print(f"Time Stamp: {time_stamp}")
    print(f"Bus List  : {bus_list}")

    def get_closest_departure(time_stamp, bus_list):
        smallest = 10000000
        bus_nr = 0
        for bus in bus_list:
            closest = bus + (time_stamp // bus) * bus
            if closest < smallest:
                smallest = closest
                bus_nr = bus
        return smallest, bus_nr

    def busID_mul_wait(time_stamp, next_departure, ID):
        wait = next_departure - time_stamp
        return wait * ID

    next_dep, bus = get_closest_departure(time_stamp, bus_list)
    mul_res = busID_mul_wait(time_stamp, next_dep, bus)
    print(mul_res)


def main_1():
    bus_list, time_stamp = read_file_p1(day)
    part_one(bus_list, time_stamp)


def read_file_p2(day):
    fin = open(day, "r")
    data = fin.read().split()
    time_stamp = int(data[0])
    bus_list = data[1].split(",")
    bus_dict = dict()
    counter = -1
    counter = [counter := counter + 1 for _ in range(len(bus_list))]
    for i, _ in enumerate(bus_list):
        if bus_list[i].isdigit():
            bus_list[i] = int(bus_list[i])
        else:
            bus_list[i] = chr(i + 65)
        bus_dict[counter[i]] = bus_list[i]
    bus_dict.clear()
    for bus_num in bus_list:
        bus_dict[bus_num] = [1]

    # print(bus_dict)
    # print(f"Time Stamp: {time_stamp}")
    # print(f"Bus List  : {bus_list}")
    return bus_dict


def remove_empty_buslines(bd):
    new_bd = dict()
    for k, v in bd.items():
        if k != 0:
            new_bd[k] = v
    return new_bd


def add_depature_list(bd):
    new_bd = dict()


def solve(bd, day) -> int:
    x = 1
    with open(day + r"12", "w") as w:
        for busnr, dep in bd.items():
            if y := isinstance(busnr, int):
                w.write(f"{busnr},")
        w.write("\n")
        while x < 10000:
            for (busnr, dep) in bd.items():
                if y := isinstance(busnr, int):
                    if x % busnr == 0:
                        dep.clear()
                        dep.append(x)
                        # w.write(str(*dep) + ",")
            x += 1
            # w.write("-,")
            # w.write("\n")

    return bd


if __name__ == "__main__":
    # main_1()
    bd = read_file_p2(day)
    # bd = remove_empty_buslines(bd)
    print(bd)
    res = solve(bd, day)
    print(res)