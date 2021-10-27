# nlantau, 2021-10-27

"""
Write a function that takes a positive integer and returns the next smaller
positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017

Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros

    some tests will include very large numbers.
    test data only employs positive integers.
"""
from itertools import permutations

def next_smaller2(n):
    l = len(str(n))
    if l < 2:
        return -1
    g = list()
    for a in list(permutations(str(n), l)):
        t = ''
        for i in a:
            t += i
        g.append(int(t))

    x = sorted(g)
    ii = 0
    for i,j in enumerate(x):
        if j == n:
            ii = i
            break
    q = x[i-1]
    if len(str(q)) != len(str(n)) or q > n:
        return -1
    return q


def next_smaller(n):
    """
    907 -> 790

    123456978 -> 123456897
    1<2<3<4<5<6<9>7<8
                 ^
                 |
    => 978 -> find combination < 978


    253412537463
    2<5>3<4>1<2<5>3<7>4<6>3
       ^   ^     ^   ^   ^
       |   |     |   |   |


    """
    a = str(n)

    # 12345 can't be arranged differently
    ordered = True
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            ordered = False
            break
    if ordered:
        return -1


# assert next_smaller(1027) == -1
print(next_smaller(21))
print(next_smaller(531))
print(next_smaller(2071))

assert next_smaller(9) == -1
print(next_smaller(9))
print(next_smaller(135))
print(next_smaller(1027))
