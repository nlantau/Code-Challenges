# nlantau, 2021-12-28
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        from copy import deepcopy
        t = deepcopy(s)
        for i,e in enumerate(s):
            s[i] = t[~i]
        return s


assert Solution().reverseString(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]
assert Solution().reverseString(["h","e","l","l","o"]) == ["o","l","l","e","h"]

"""
Notes:
I assumed that s = s[::-1] wouldn't work so I went for
a deepcopy and a bitwise NOT (complement)
228 ms, 18.5 MB, 16.52% faster
"""

