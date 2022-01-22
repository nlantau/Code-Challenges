# nlantau, 2022-01-14

from typing import *
class Solution:
    def findDuplicates2(self, nums: List[int]) -> List[int]:
        return list(set(x for x in nums if nums.count(x) > 1))

    def findDuplicates3(self, nums: List[int]) -> List[int]:
        b = set(nums)
        for v in b:
            nums.remove(v)
        return nums

    def findDuplicates(self, nums: List[int]) -> List[int]:
        b = set()
        u = set()
        for v in nums:
            if v in b:
                u.add(v)
            else:
                b.add(v)

        return list(u)

"""
Notes:
28/28
468 ms, 23.9 MB
Failed 3 times due to Time Limit Exceeded...
"""


if __name__ == "__main__":
    n = [4,3,2,7,8,2,3,1]
    print(Solution().findDuplicates(n)) # [2,3]

    n = [1,1,2]
    print(Solution().findDuplicates(n)) # [1]

    n = [1]
    print(Solution().findDuplicates(n)) # []
