# nlantau, 2020-12-15
import copy
import os

# STARTING_NUMBERS = [2, 0, 6, 12, 1, 3]
STARTING_NUMBERS = [0, 3, 6]


def memory_builder():
    mem_list = copy.deepcopy(STARTING_NUMBERS)

    for i in range(len(mem_list) - 1, 8, 1):
        num = 0
        prev_index = i + 1
        index = 0
        spoken = mem_list[i]
        print("prev, spoken", prev_index, spoken)
        if spoken in mem_list[:-1]:
            for k in range(len(mem_list[:-1])):
                if mem_list[k] == spoken:
                    index = k + 1
                    print("index: ",index)
            num = prev_index - index
            mem_list.append(num)
        else:
            mem_list.append(0)
        print(mem_list)
    print(mem_list[len(mem_list) - 1])


def main():
    os.system("clear")
    print(f"{' BEGIN ':-^40}\n")
    memory_builder()


if __name__ == "__main__":
    main()
