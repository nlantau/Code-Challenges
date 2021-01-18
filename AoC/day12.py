import os
import re
import collections
import operator

day = os.path.join(os.path.dirname(__file__), r"12dummy.txt")
Turn = collections.namedtuple("Turn", "Deg")
Instruction = collections.namedtuple("Instruction", "Command Value")
# E & N = positive
# W & S = negative
Position = collections.namedtuple("Position", "EW NS Facing")


# ins_pat = re.compile(r"\w\d+")
fin = open(day, "r")
instructions = list()
Pos = [0, 0, "E"]
WayPoint = [10, 1, "E"]
print(Pos)

DIRECTION = ["E", "S", "W", "N"]

ins = fin.read().splitlines()
for i in ins:
    instructions.append(Instruction(i[0], i[1:]))

for i in instructions:
    print("P :", Pos)
    print("WP:", WayPoint)
    # N S E W
    if i.Command == "N":
        # Pos[1] += int(i.Value)
        WayPoint[1] += int(i.Value)
    elif i.Command == "S":
        # Pos[1] -= int(i.Value)
        WayPoint[1] -= int(i.Value)
    elif i.Command == "E":
        # Pos[0] += int(i.Value)
        WayPoint[0] += int(i.Value)
    elif i.Command == "W":
        # Pos[0] -= int(i.Value)
        WayPoint[0] -= int(i.Value)
    # F R L
    elif i.Command == "F":  # Forward
        if WayPoint[2] == "E" and WayPoint[1] >= 0:  # East and North
            Pos[0] += int(i.Value) * WayPoint[0]
            Pos[1] += int(i.Value) * WayPoint[1]
        elif WayPoint[2] == "E" and WayPoint[1] < 0:  # East and South
            Pos[0] += int(i.Value) * WayPoint[0]
            Pos[1] -= int(i.Value) * WayPoint[1]
        if WayPoint[2] == "W" and WayPoint[1] >= 0:  # West and North
            Pos[0] -= int(i.Value) * WayPoint[0]
            Pos[1] += int(i.Value) * WayPoint[1]
        elif WayPoint[2] == "W" and WayPoint[1] < 0:  # West and South
            Pos[0] -= int(i.Value) * WayPoint[0]
            Pos[1] -= int(i.Value) * WayPoint[1]
        if WayPoint[2] == "N" and WayPoint[0] >= 0:  # North and East
            Pos[1] += int(i.Value) * WayPoint[1]
            Pos[0] += int(i.Value) * WayPoint[0]
        elif WayPoint[2] == "N" and WayPoint[0] < 0:  # North and West
            Pos[1] += int(i.Value) * WayPoint[1]
            Pos[0] -= int(i.Value) * WayPoint[0]
        if WayPoint[2] == "S" and WayPoint[0] >= 0:  # South and East
            Pos[1] -= int(i.Value) * WayPoint[1]
            Pos[0] += int(i.Value) * WayPoint[0]
        elif WayPoint[2] == "S" and WayPoint[0] < 0:  # South and
            Pos[1] -= int(i.Value) * WayPoint[1]
            Pos[0] -= int(i.Value) * WayPoint[0]

    elif i.Command == "R":  # Turn right
        if i.Value == "90":
            if WayPoint[2] == "E":
                WayPoint[2] = "S"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "W":
                WayPoint[2] = "N"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "N":
                WayPoint[2] = "E"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "S":
                WayPoint[2] = "W"
                Pos[2] = WayPoint[2]
        elif i.Value == "180":
            if WayPoint[2] == "E":
                WayPoint[2] = "W"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "W":
                WayPoint[2] = "E"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "N":
                WayPoint[2] = "S"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "S":
                WayPoint[2] = "N"
                Pos[2] = WayPoint[2]
        elif i.Value == "270":
            if WayPoint[2] == "E":
                WayPoint[2] = "N"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "W":
                WayPoint[2] = "S"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "N":
                WayPoint[2] = "W"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "S":
                WayPoint[2] = "E"
                Pos[2] = WayPoint[2]

    elif i.Command == "L":  # Turn left
        if i.Value == "90":
            if WayPoint[2] == "E":
                WayPoint[2] = "N"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "W":
                WayPoint[2] = "S"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "N":
                WayPoint[2] = "W"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "S":
                WayPoint[2] = "E"
                Pos[2] = WayPoint[2]
        elif i.Value == "180":
            if WayPoint[2] == "E":
                WayPoint[2] = "W"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "W":
                WayPoint[2] = "E"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "N":
                WayPoint[2] = "S"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "S":
                WayPoint[2] = "N"
                Pos[2] = WayPoint[2]
        elif i.Value == "270":
            if WayPoint[2] == "E":
                WayPoint[2] = "S"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "W":
                WayPoint[2] = "N"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "N":
                WayPoint[2] = "E"
                Pos[2] = WayPoint[2]
            elif WayPoint[2] == "S":
                WayPoint[2] = "W"
                Pos[2] = WayPoint[2]

print(Pos)
res = abs(Pos[0]) + abs(Pos[1])
print(WayPoint)
print(res)
"""

        if i.Value == "90":
            if Pos[2] == "E":
                Pos[2] = "S"
            elif Pos[2] == "W":
                Pos[2] = "N"
            elif Pos[2] == "N":
                Pos[2] = "E"
            elif Pos[2] == "S":
                Pos[2] = "W"
        elif i.Value == "180":
            if Pos[2] == "E":
                Pos[2] = "W"
            elif Pos[2] == "W":
                Pos[2] = "E"
            elif Pos[2] == "N":
                Pos[2] = "S"
            elif Pos[2] == "S":
                Pos[2] = "N"
        elif i.Value == "270":
            if Pos[2] == "E":
                Pos[2] = "N"
            elif Pos[2] == "W":
                Pos[2] = "S"
            elif Pos[2] == "N":
                Pos[2] = "W"
            elif Pos[2] == "S":
                Pos[2] = "E"
        if i.Value == "90":
            if Pos[2] == "E":
                Pos[2] = "N"
            elif Pos[2] == "W":
                Pos[2] = "S"
            elif Pos[2] == "N":
                Pos[2] = "W"
            elif Pos[2] == "S":
                Pos[2] = "E"
        elif i.Value == "180":
            if Pos[2] == "E":
                Pos[2] = "W"
            elif Pos[2] == "W":
                Pos[2] = "E"
            elif Pos[2] == "N":
                Pos[2] = "S"
            elif Pos[2] == "S":
                Pos[2] = "N"
        elif i.Value == "270":
            if Pos[2] == "E":
                Pos[2] = "S"
            elif Pos[2] == "W":
                Pos[2] = "N"
            elif Pos[2] == "N":
                Pos[2] = "E"
            elif Pos[2] == "S":
                Pos[2] = "W"
"""