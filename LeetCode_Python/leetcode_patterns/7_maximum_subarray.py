# nlantau, 2022-01-29

from typing import *

"""
A subarray is a contiguous part of an array

Kadane's Algo
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Notes: 664 ms, 97.63% faster, 28.7 MB, 59.51% better
        """
        max_res = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num

            if max_res < curr_sum:
                max_res = curr_sum
        return max_res

    def maxSubArray2(self, nums: List[int]) -> int:
        """
        Notes: 986 ms, 36.86% faster, 27.9 MB, 95.38% better
        """
        max_res = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_res = max(max_res, curr_sum)
        return max_res


class TestClass:
    def test_example_1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        res = Solution().maxSubArray(nums)
        assert res == 6

    def test_example_2(self):
        nums = [1]
        res = Solution().maxSubArray(nums)
        assert res == 1

    def test_example_3(self):
        nums = [5,4,-1,7,8]
        res = Solution().maxSubArray(nums)
        assert res == 23


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = Solution().maxSubArray(nums)

