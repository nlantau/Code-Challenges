# nlantau, 2022-01-07

"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                zum = a + nums[l] + nums[r]

                if zum > 0: r -= 1
                elif zum < 0: l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

"""
Notes:
764 ms, 85.64% faster, 17.4 MB, 74.18% better

Time Complexity
Sorting:   O(NlogN)
Iteration: O(N^2)
Total:     O(N^2)

Space Complexity
Sorting algo might take some additional spcae

"""


if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(Solution().threeSum(nums))
