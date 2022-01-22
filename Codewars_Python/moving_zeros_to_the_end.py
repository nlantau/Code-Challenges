# nlantau, 2020-11-07
"""
Write an algorithm that takes an array and moves
all of the zeros to the end, preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) #
returns[False,1,1,2,1,3,"a",0,0]
Test.describe("Basic tests")
"""


def move_zeros(array):
    new_array = [i for i in array if str(i) != str(0)]
    diff = len(array) - len(new_array)
    for i in range(diff):
        new_array.append(0)
    for i in new_array:
        if str(i) == str(0.0):
            new_array.remove(0.0)
            new_array.append(0)
    return new_array


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros([0, 1, None, 2, False, 1, 0]))
print(move_zeros(["a", "b"]))
print(move_zeros(["a"]))
print(move_zeros([0, 0]))
print(move_zeros([0]))
print(move_zeros([False]))
print(move_zeros([]))
