# nlantau, 2021-12-27
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(list(set(nums)))

"""
Notes:
440 ms, 26.3 MB, 21.71 % faster
"""
