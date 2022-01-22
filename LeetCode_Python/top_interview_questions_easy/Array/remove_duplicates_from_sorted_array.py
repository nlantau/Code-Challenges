# nlantau, 2021-12-27
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        current_length = len(nums) - 1

        while i < current_length:
            while nums[i] == nums[i+1]:
                del(nums[i])
                current_length -= 1
                if i + 1 > current_length:
                    break
            i += 1
        return len(nums)

    def removeDuplicates2(self, nums: List[int]) -> int:
        """ Does not work on leetcode. Perhaps
        the creation of a new list messes with me
        """
        nums = list(set(nums))
        print(nums)
        return len(nums)

print(Solution().removeDuplicates([1,2,3,3,4]))
print(Solution().removeDuplicates([1,1,1,2,3,3,3,4]))
print(Solution().removeDuplicates([1,1,2]))
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(Solution().removeDuplicates([1,1]))


print(Solution().removeDuplicates2([1,2,3,3,4]))
print(Solution().removeDuplicates2([1,1,1,2,3,3,3,4]))
print(Solution().removeDuplicates2([1,1,2]))
print(Solution().removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))
print(Solution().removeDuplicates2([1,1]))
"""
Notes:
[1,1] was a sneaky bastard. Fixed it by adding
'if i + 1 > current_length' in nested loop.
Was thinking about using list(set()), but wanted to try using loops only

Submission Detail:
362/362 test cases passed
Runtime: 148 ms
Memory Usage: 15.7 MB
Faster than 21.92% of all Python3 submissions



"""
