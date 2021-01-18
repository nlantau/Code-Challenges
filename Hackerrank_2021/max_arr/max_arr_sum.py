"""
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. 
Calculate the sum of that subset. It is possible that the maximum sum is , the case when all elements are negative.

For example, given an array  we have the following possible subsets. 
These exclude the empty subset and single element subsets which are also valid.

arr = [-2, 1, 3, -3, 5]

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8
Our maximum subset sum is . Note that any individual element is a subset as well.

As another example, . In this case, it is best to choose no element: return .

Constraints:
1 <= n <= 10**5
-10**4 <= arr[i] <= 10**4

"""
import fileinput
import re

dig = re.compile(r'-?\d+')
L = [i.strip() for i in list(fileinput.input())]
L = re.findall(dig, *L)
L = [int(i) for i in L]
print(L)


def maxSubsetSum(a):
    if len(a) == 1:
        return a[0]
    l = [None] * len(a)
    l[0] = a[0]
    l[1] = max(a[0], a[1])
    for i in range(2, len(a)):
        l[i] = max(l[i-1], l[i-2] + a[i])
        l[i] = max(l[i], a[i])
    return l[len(a)-1]




print(maxSubsetSum(L))

