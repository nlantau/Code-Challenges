# nlantau, 2020-11-06
"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n.
If that value has more than one digit, continue reducing in
this way until a single-digit number is produced.
The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""


def digital_root(n):
    if sum([int(d) for d in str(n)]) > 9:
        return digital_root(sum([int(d) for d in str(n)]))
    return sum([int(d) for d in str(n)])


def digital_root38(n):
    if sum(list_ := [int(d) for d in str(n)]) > 9:
        return digital_root(sum(list_))
    return sum(list_)


print(f'{" 3.6 ":-^10}')

print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))

print(f'{" 3.8 ":-^10}')

print(digital_root38(16))
print(digital_root38(942))
print(digital_root38(132189))
print(digital_root38(493193))
