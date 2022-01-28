# nlantau, 2022-01-28

from typing import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}

        for num in nums:
            if num in hash_map:
                hash_map[num] = False
            else:
                hash_map[num] = True
        for k,v in hash_map.items():
            if v:
                return k
"""
Notes:
167 ms, 49.65%, 16.6 MB, 86.24% better
"""


class TestClass:
    def test_example_1(self):
        nums = [2,2,1]
        res = Solution().singleNumber(nums)
        assert res == 1

    def test_example_2(self):
        nums = [4,1,2,1,2]
        res = Solution().singleNumber(nums)
        assert res == 4

    def test_example_3(self):
        nums = [1]
        res = Solution().singleNumber(nums)
        assert res == 1


if __name__ == "__name__":
    nums = [2,2,1]
    res = Solution().singleNumber(nums)
