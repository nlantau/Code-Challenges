import math

path = r"/Users/nlantau/Docs/GitHub/DT256CHT20/AoC/2018/1.txt"


def main():
    fine = open(path, "r")
    b = fine.read().split("\n")
    c = 0
    d = 0
    c = sum([c + int(x[1:]) for x in b if x[0] == "+"])
    d = sum([d + int(x[1:]) for x in b if x[0] == "-"])

    # d = sum([c + int(x[1:]) for x in b if x[0] == "-"])
    print(c)
    print(d)
    print(abs(c - d))


if __name__ == "__main__":
    main()