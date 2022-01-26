# nlantau, 2022-01-26

from typing import *

class Solution:
    def containsDuplicate2(self, nums: List[int]) -> bool:
        #return len(nums) != len(list(set(nums)))
        return len(nums) != len(set(nums))

    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for val in nums:
            if val in hash_table:
                return True
            hash_table[val] = 1
        return False

"""
Notes:
Hash table ran at 838 ms, 25.7 MB
Set ran at 701 ms, 25.9 MB
Set and list ran at 440 ms, 26.3 MB
"""
        

class TestClass:
    def test_example_1(self):
        nums = [1,2,3,1]
        res = Solution().containsDuplicate(nums)
        assert res == True

    def test_example_2(self):
        nums = [1,2,3,4]
        res = Solution().containsDuplicate(nums)
        assert res == False

    def test_example_3(self):
        nums = [1,1,1,3,3,4,3,2,4,2]
        res = Solution().containsDuplicate(nums)
        assert res == True

if __name__ == "__main__":
    pass

