# nlantau, 2022-01-26

from typing import *

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Brute force solution
        nums.sort() # O(NlogN)
        l, r = 0, len(nums)

        if nums[0] != 0: return 0

        while l < r: # O(N)
            if nums[l] + 1 not in nums:
                return nums[l] + 1
            l += 1

"""
Notes:
Brute force: Super-slow. 4058 ms, 5.01% faster, 15.5 MB, 51.77%

Failed a few times due to not checking nums[0] for 0 after sorting

"""


class TestClass:
    def test_example_1(self):
        nums = [3,0,1]
        res = Solution().missingNumber(nums)
        assert res == 2

    def test_example_2(self):
        nums = [0,1]
        res = Solution().missingNumber(nums)
        assert res == 2

    def test_example_3(self):
        nums = [9,6,4,2,3,5,7,0,1]
        res = Solution().missingNumber(nums)
        assert res == 8

    def test_example_4(self):
        nums = [1]
        res = Solution().missingNumber(nums)
        assert res == 0

    def test_example_5(self):
        nums = [1,2]
        res = Solution().missingNumber(nums)
        assert res == 0

if __name__ == "__main__":
    pass
