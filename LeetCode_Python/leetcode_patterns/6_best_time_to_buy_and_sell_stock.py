# nlantau, 2022-01-29

from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Notes: 1172 ms, 49.83% faster, 25.1 MB, 82.63% better
        """
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            res = prices[r] - prices[l]
            max_profit = max(max_profit, res)

            if prices[l] > prices[r]:
                l = r
            r += 1
        return max_profit


class TestClass:
    def test_example_1(self):
        prices = [7,1,5,3,6,4]
        result = Solution().maxProfit(prices)
        assert result == 5

    def test_example_2(self):
        prices = [7,6,4,3,1]
        result = Solution().maxProfit(prices)
        assert result == 0


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    result = Solution().maxProfit(prices)
    print(result)
