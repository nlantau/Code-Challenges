# nlantau, 2022-01-26

from typing import *

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Brute force solution
        l, r = 0, len(nums)
        res = []
        unique = set(nums)

        while l < r:
            if l+1 not in unique:
                res.append(l+1)
            l += 1
        return res

"""
Notes:
Brute force: 312 ms, 99.55% faster, 24 MB, 39.59% better
"""


class TestClass:
    def test_exampel_1(self):
        nums = [4,3,2,7,8,2,3,1]
        res = Solution().findDisappearedNumbers(nums)
        assert res == [5,6]

    def test_exampel_2(self):
        nums = [1,1]
        res = Solution().findDisappearedNumbers(nums)
        assert res == [2]


if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    res = Solution().findDisappearedNumbers(nums)
