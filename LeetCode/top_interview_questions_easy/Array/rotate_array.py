# nlantau, 2021-12-27
from typing import List
from copy import deepcopy

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        tmp = deepcopy(nums)
        for i in range(len(nums)):
            nums[i] = tmp[(i - k) % len(tmp)]
        print(nums)

    def rotate2(self, nums: List[int], k: int) -> None:
        nums = [nums[(i - k) % len(nums)] for i,_ in enumerate(nums)]
        print(nums)



Solution().rotate([1,2,3,4,5,6,7], 3)
Solution().rotate([-1,-100,3,99], 2)

Solution().rotate2([1,2,3,4,5,6,7], 3)
Solution().rotate2([-1,-100,3,99], 2)

"""
Notes:
rotate(): 264 ms, 25.6 MB, 29.21% faster

rotate2(): not accepted... but it works?
"""
