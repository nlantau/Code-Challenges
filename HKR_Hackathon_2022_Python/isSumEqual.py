# nlantau, 2022-01-14

from typing import *

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        fw = int("".join([str(f-97) for f in [*map(ord, firstWord)]]))
        sw = int("".join([str(f-97) for f in [*map(ord, secondWord)]]))
        tw = int("".join([str(f-97) for f in [*map(ord, targetWord)]]))
        return fw + sw == tw


"""
Notes:
100/100
50 ms, 14.4 MB
"""


if __name__ == "__main__":
    first   = "acb"
    second  = "cba"
    target  = "cdb"
    print(Solution().isSumEqual(first, second, target)) # True

    first   = "aaa"
    second  = "a"
    target  = "aab"
    print(Solution().isSumEqual(first, second, target)) # False

    first   = "aaa"
    second  = "a"
    target  = "aaaa"
    print(Solution().isSumEqual(first, second, target)) # True
