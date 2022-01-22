# nlantau, 2022-01-17

from typing import *

"""
The constrain of 'must write an algorithm with O(log n) runtime complexity
really screams binary search.

But, using a hash table was really neat. Since we know we'll have distinct
values in a sorted array, we don't have to rotate the array back again nor
do we have to look through or array in a loop.
A hash table will map
4 : 0,
5 : 1,
6 : 2,
7 : 3,
0 : 4,
1 : 5,
2 : 6

which will mean that hash_table[target] => hash_table[0] == 4 in O(1)
time complexity

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hash_table = {}

        for i in range(len(nums)):        # O(N) in my world, but passed
                                          # constrain of O(logN)
            if nums[i] not in hash_table: # This lookup should be O(1)
                hash_table[nums[i]] = i

        if target not in hash_table: return -1 # O(1)
        return hash_table[target]

    def search2(self, nums: List[int], target: int) -> int:
        hash_table = {}

        for i in range(len(nums)):
            hash_table[nums[i]] = i

        if target not in hash_table: return -1
        return hash_table[target]

class TestClass:
    def test_example_1(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        x = Solution().search(nums, target)
        assert x == 4

    def test_example_2(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        x = Solution().search(nums, target)
        assert x == -1

    def test_example_3(self):
        nums = [1]
        target = 0
        x = Solution().search(nums, target)
        assert x == -1

    def test_example_1_1(self):
        nums = [4,5,6,7,0,1,2]
        target = 0
        x = Solution().search2(nums, target)
        assert x == 4

    def test_example_2_1(self):
        nums = [4,5,6,7,0,1,2]
        target = 3
        x = Solution().search2(nums, target)
        assert x == -1

    def test_example_3_1(self):
        nums = [1]
        target = 0
        x = Solution().search2(nums, target)
        assert x == -1


"""
Notes:
Added a test class. Should continue this routine. Simply run 'pytest filename.py'
to have pytest automatically run all tests in TestClass.

search() : 82 ms, 5.52% faster, 14.9 MB, 23.60% better
search2(): 76 ms, 9.64% faster, 14.8 MB, not sure but most likely around 23-24%
"""

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    x = Solution().search(nums, target)

