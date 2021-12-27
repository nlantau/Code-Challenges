# nlantau, 2021-12-28

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [x for x in nums1 if x in nums2]

nums1 = [1,2,2,1]
nums2 = [2,2]
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]

print(Solution().intersect(nums1, nums2))
print(Solution().intersect(nums3, nums4))

assert Solution().intersect(nums1, nums2) == [2,2]
assert Solution().intersect(nums3, nums4) == [4,9]


"""
Notes:
NOT COMPLETED
"""

