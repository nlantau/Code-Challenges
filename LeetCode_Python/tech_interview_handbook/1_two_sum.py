# nlantau, 2022-01-04

"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
input:  [2,7,11,15], 9
output: [0,1], because nums[0] + nums[1] = 9

Example 2:
input:  [3,2,4], 6
output: [1,2]
"""


from typing import *

class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        Not completed
        """
        if target == 0: return []
        if target < 0: return None

        nums_without_num = []

        for num in nums:
            remainder = target - num

            for n in nums:
                if n != num:
                    nums_without_num.append(n)

            res = self.twoSum(nums_without_num, remainder)
            if res:
                return res

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Completed
        """
        for i in range(len(nums)):
            for j in range(len(nums)-1, i-1, -1):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]

    def stolen_twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Stolen. Really cool
        """
        hash_table = {}
        print(f'target: {target}')
        for i in range(len(nums)):
            if nums[i] in hash_table:
                print("Returning...")
                print(f'hash_table: {hash_table}')
                print(f'hash_table[nums[i]]: {hash_table[nums[i]]}')
                print(f'nums[i]: {nums[i]}')
                print(f'i: {i}')
                return [hash_table[nums[i]], i]
            else:
                hash_table[target - nums[i]] = i
                print("Appending...")
                print(f'hash_table: {hash_table}')
                #print(f'hash_table[nums[i]]: {hash_table[nums[i]]}')
                print(f'nums[i]: {nums[i]}')
                print(f'i: {i}')


"""
Notes:
Iterative solution: 4856 ms, 11.56% faster, 14.8 MB, 92,13% better

Super slow solution. Should definately look at other submissions and
learn their strategies.

TODO:
Really need to study stolen_twoSum(). Do some drawings with test cases to learn.
Clever solution. Made drawing to understand it better

"""


if __name__ == "__main__":
    print("hello")
    print(Solution().twoSum([2,7,11,15], 9))
    print(Solution().twoSum([3,2,4], 6))
    print(Solution().twoSum([3,3], 6))
    print("<----------->")
    print(Solution().stolen_twoSum([2,7,11,15], 9))
    print("<----------->")
    print(Solution().stolen_twoSum([3,2,4], 6))
    print("<----------->")
    print(Solution().stolen_twoSum([3,3], 6))
    print("<----------->")
