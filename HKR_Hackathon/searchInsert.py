# nlantau, 2022-01-14

from typing import *

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            for i,v in enumerate(nums):
                if v == target: return i
        else:
            l, r = 0, len(nums)

            while l < r:
                if target < nums[l]: return l 
                l += 1
            return l


"""
Notes:
64/64
52 ms, 15.1 MB
"""

if __name__ == "__main__":
    n = [1,3,5,6]
    t = 5
    print(Solution().searchInsert(n, t)) # 2

    n = [1,3,5,6]
    t = 2
    print(Solution().searchInsert(n, t)) # 1

    n = [1,3,5,6]
    t = 7
    print(Solution().searchInsert(n, t)) # 4

    n = [1,3,5,6]
    t = 0
    print(Solution().searchInsert(n, t)) # 0

    n = [1]
    t = 0
    print(Solution().searchInsert(n, t)) # 0
