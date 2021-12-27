# nlantau, 2021-12-27
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = list()
        for i in range(0, len(prices) - 1):
            diff.append(prices[i+1] - prices[i])
        return sum([*filter(lambda x:x>0, diff)])

    def maxProfit2(self, prices: List[int]) -> int:
        return sum([*filter(lambda x:x>0, [prices[i+1] - prices[i] for i in range (len(prices) - 1)])])



print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1]))

print(Solution().maxProfit2([7,1,5,3,6,4]))
print(Solution().maxProfit2([1,2,3,4,5]))
print(Solution().maxProfit2([7,6,4,3,1]))

"""
Notes:
Worked on first attempt. Minor clean up afterwards.

maxProfit2() is even nicer (more unreadable =) )
200/200 test cases passed
Runtime: 64 ms, beats 45.23% of Python3 submissions
Memory Usage: 15.2 MB
"""
