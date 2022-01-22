# nlantau, 2020-12-12

import os
import collections
import timeit
import cProfile

day = os.path.join(os.path.dirname(__file__), r"12.txt")
Instruction = collections.namedtuple("Instruction", "Command Value")


def read_file(day, Instruction):
    with open(day, "r") as fin:
        instructions = list()
        ins = fin.read().splitlines()
        for i in ins:
            instructions.append(Instruction(i[0], i[1:]))
        return instructions


def move_ship(s, w, value):
    value = int(value)
    wx, wy = w[0], w[1]
    sx, sy = s[0], s[1]
    sx += value * wx
    sy += value * wy
    s = [sx, sy]
    return s


def rotate_WP(w, direction, deg):
    if direction == "L":
        if deg == "90":
            w = rotate_90_CCW(w)
        elif deg == "180":
            w = rotate_90_CCW(w)
            w = rotate_90_CCW(w)
        elif deg == "270":
            w = rotate_90_CCW(w)
            w = rotate_90_CCW(w)
            w = rotate_90_CCW(w)
    elif direction == "R":
        if deg == "90":
            w = rotate_90_CW(w)
        elif deg == "180":
            w = rotate_90_CW(w)
            w = rotate_90_CW(w)
        elif deg == "270":
            w = rotate_90_CW(w)
            w = rotate_90_CW(w)
            w = rotate_90_CW(w)
    return w


def rotate_90_CW(w: list):
    w[0], w[1] = w[1], w[0] * -1
    return w


def rotate_90_CCW(w: list):
    w = rotate_90_CW(w)
    w = rotate_90_CW(w)
    w = rotate_90_CW(w)
    return w


def run(s, wp, instructions):
    for i in instructions:
        if i.Command == "F":
            s = move_ship(s, wp, i.Value)
        elif i.Command == "L":
            wp = rotate_WP(wp, i.Command, i.Value)
        elif i.Command == "R":
            wp = rotate_WP(wp, i.Command, i.Value)
        elif i.Command == "N":
            wp[1] = wp[1] + int(i.Value)
        elif i.Command == "E":
            wp[0] = wp[0] + int(i.Value)
        elif i.Command == "S":
            wp[1] = wp[1] - int(i.Value)
        elif i.Command == "W":
            wp[0] = wp[0] - int(i.Value)
    return s


def manhattan_distance(s):
    return abs(s[0]) + abs(s[1])


def main():
    ship = [0, 0]
    waypoint = [10, 1]
    instructions = read_file(day, Instruction)
    ship = run(ship, waypoint, instructions)
    print(f"The manhattan distance is : {manhattan_distance(ship)}")
    print(f"Final location of ship    : {ship}")
    print(f"Final location of waypoint: {waypoint}")


if __name__ == "__main__":
    print(f"Completed in {timeit.timeit(main, number=1):.5f} seconds")
    cProfile.run("main()")