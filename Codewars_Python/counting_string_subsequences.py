# nlantau, 2020-11-06

"""
Test.it("Basic tests")
Test.assert_equals(count_subsequences("happy birthday", "appyh appy birth day"), 1)
Test.assert_equals(count_subsequences("happy birthday", "hhaappyy bbiirrtthhddaayy"), 2048)
Test.assert_equals(count_subsequences("happy birthday", "happy holidays"), 0)
"""


def count_subsequences(a: str, b: str):
    m = len(b)
    n = len(a)

    list_ = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(n + 1):
        list_[0][i] = 0

    for i in range(m + 1):
        list_[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if b[i - 1] == a[j - 1]:
                list_[i][j] = list_[i - 1][j - 1] + list_[i - 1][j]

            else:
                list_[i][j] = list_[i - 1][j]

    return list_[m][n]


# 1
one = "happy birthday"
# 2048
two = "hhaappyy bbiirrtthhddaayy"
three = "happy holidays"

print(count_subsequences(one, three))
print(count_subsequences(one, one))
print(count_subsequences(one, two))
