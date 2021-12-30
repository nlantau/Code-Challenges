# nlantau, 2021-12-30
"""
Write a function canSum(targetSum, numbers) that takes in a
tagetSum and an array of numbers as argument.

The function should return a boolean indicating whether or not it
is possible to generate the targetSum using numbers from the array

Constraints:
You may use an element of the array as many times as needed.
You may assume that all input numbers are non-nogative.
"""

def canSum(targetSum, numbers):
    if targetSum == 0: return True
    if targetSum < 0: return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers):
            return True
    return False

print(canSum(7, [5,3,4,7]))