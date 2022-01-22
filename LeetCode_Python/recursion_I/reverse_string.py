# nlantau, 2021-12-30

from typing import *

class Solution:
    def reverseString2(self, s: List[str]) -> None:
        """
        Recursive
        Do not return anything, modify s in-place instead.
        While this works, s is not modified in-place...
        """
        if len(s) == 0 or len(s) == 1:
            return s
        return [s[-1]] + self.reverseString(s[:-1])


    def reverseString(self, s: List[str]) -> None:
        """
        Iterative
        Do not return anything, modify s in-place instead.
        Two-pointer approach... ?
        """
        start = 0
        end = len(s) - 1

        while start < end:
            # swap start with end
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


"""
Notes:
Wanted to do it recursively, but ended up with iterative.
375 ms (super-slow), 18.8 MB, 10.24% better memory usage...
"""



if __name__ == "__main__":
    s = ['h','e','l','l','o']
    Solution().reverseString(s)
    print(s)

