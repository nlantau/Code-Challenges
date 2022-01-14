# nlantau, 2022-01-14

from typing import *


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = int("".join([str(d) for d in digits]))
        x += 1
        return [int(d) for d in str(x)]


"""
Notes:
111/111 tests passed
28 ms, 14.2 MB
"""

if __name__ == "__main__":
    s = [1,2,3] # [1,2,4]
    print(Solution().plusOne(s))

    s = [0] # [0]
    print(Solution().plusOne(s))
        
    s = [1,2,9] # [1,3,0]
    print(Solution().plusOne(s))

    s = [9,9] # [1,0,0]
    print(Solution().plusOne(s))
