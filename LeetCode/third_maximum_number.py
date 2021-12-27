# nlantau, 2021-12-25
"""
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Success!
Runtime: 28ms, faster than 98.91% of Python submissions
"""

class Solution(object):
    def thirdMax(self, nums):
        from functools import reduce

        n = list(set(nums))
        if len(n) < 3:
            return reduce(max, n)
        return sorted(list(set(n)))[-3]

if __name__ == "__main__":
    sol = Solution()
    assert 1 == sol.thirdMax([3,2,1])
    assert 2 == sol.thirdMax([1,2])
    assert 1 == sol.thirdMax([2,2,3,1])
