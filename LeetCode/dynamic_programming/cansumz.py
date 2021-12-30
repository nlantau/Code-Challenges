# nlantau, 2021-12-30
"""
Write a function howSum(targetSum, numbers) that takes in a
targetSum and an array of numbers as arguments

The function should return an array containing any combination
of elements that add up to exactly the targetSum. If there is no
combination that adds up to the targetSum, then return null

If there are multiple combinations possible, you may return any
single one
"""

def howSumRecursive(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        remainder = targetSum - num
        remainder_result = howSum(remainder, numbers)
        if remainder_result != None:
            return [*remainder_result, num]
    return None


def howSum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        remainder = targetSum - num
        remainder_result = howSum(remainder, numbers, memo)
        if remainder_result != None:
            memo[targetSum] = [*remainder_result, num]
            return memo[targetSum]
    memo[targetSum] = None
    return None

print(howSumRecursive(7, [5,3,4,7]))
print(howSumRecursive(7, [5,4,1]))
print(howSumRecursive(300, [5,3,4,7]))

print(howSum(7, [5,3,4,7]))
print(howSum(7, [5,4,1]))
print(howSum(300, [5,3,4,7]))

"""
Write a function canSum(targetSum, numbers) that takes in a
tagetSum and an array of numbers as argument.

The function should return a boolean indicating whether or not it
is possible to generate the targetSum using numbers from the array

Constraints:
You may use an element of the array as many times as needed.
You may assume that all input numbers are non-nogative.
"""

def canSum(targetSum, numbers, memo={}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True
    if targetSum < 0: return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False

print(canSum(7, [5,3,4,7]))
print(canSum(300, [5,3,4,7]))