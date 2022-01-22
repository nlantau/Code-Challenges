import os
import re

day = "14.txt"
day = os.path.join(os.path.dirname(__file__), day)


def read_file(day):
    with open(day, "r") as fin:
        data = " ".join([line.strip() for line in fin.readlines()]).split("mask")
        data = [line.replace("=", "").replace(" ", "") for line in data]
        data = [line.split("mem") for line in data]
    return data


def mask_bin_string(mask, val):
    new_val = ""
    for bit, binval in zip(mask, val):
        if bit == "X":
            new_val = new_val + binval
        elif bit == "0":
            new_val = new_val + bit
        elif bit == "1":
            new_val = new_val + bit
    return new_val


def convert_val_to_bin_string(val):
    # This is a keeper (store binary as string of 1's and 0's)
    val = f"{val:b}"
    # This is a keeper (fill up string length with '0' to 36 bit total)
    val = "0" * (36 - len(val)) + val
    return val


def count_mem_slots(data):
    with open(day, "r") as fin:
        cp = re.compile(r"mem\[\d+\]")
        data = [line.strip() for line in fin.readlines() if "mem" in line]
        dd = set()
        for line in data:
            if g := re.match(cp, line):
                dd.add(g.group(0))

        print("Totalz mem[]: %d" % len(data))  # 442
        print("Unique mem[]: %d" % len(dd))  # 385 = Not only unique addresses
    return data


def get_er_dune(data):
    bin_strings = list()
    memval = re.compile(r"\[(\d+)\](\d+)")
    mask_v = re.compile(r"[X10]{36}")
    memory = [0 for x in range(10000000)]
    for el in data:
        mask = ""
        new_el = list()
        for seq in el:
            if k := re.match(mask_v, seq):
                mask = k.group(0)
            if g := re.match(memval, seq):
                # print(g.group(2))  # Bingo
                x = convert_val_to_bin_string(int(g.group(2)))  # Bingo
                new_x = int(mask_bin_string(mask, x), 2)  # value
                # print(f"g.group(1): {g.group(1)}")  # memory address
                seq = "".join("[" + g.group(1) + "]" + str(new_x))  # Bingo
                new_el.append(seq)
                memory[int(g.group(1))] = new_x  # Part 1 winner
        el.clear()
        el.append(mask)
        el.append(new_el)
    memory = clear_memory(memory)  # Part 1 winner
    return data


def clear_memory(memory):
    new_mem = list()
    for val in memory:
        if val > 0:
            new_mem.append(val)
    print("new_mem: ", sum(new_mem))


def main():
    pass


if __name__ == "__main__":
    os.system("clear")
    print(f"{' StartZ ':.^30}")
    print(count_mem_slots(day))
    data = read_file(day)
    # print(data)
    data = get_er_dune(data)
    # print(data)
    # print(*data, sep="\n")
