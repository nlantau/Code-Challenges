# nlantau, 2022-01-29

from typing import *

class Solution:
    def climbStairs2(self, n: int, memo={}) -> int:
        """
        Notes: 74 ms, 5.71% faster, 14 MB, 97.43% better
        """
        if n in memo:
            return memo[n]
        if n < 2: return 1
        if n == 2:
            return 2
        memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        return memo[n]

    def climbStairs(self, n: int) -> int:
        """
        Notes: 28 ms, 87.27% faster, 13.8 MB, 99.72% faster
        """
        first, second = 1, 1
        for i in range(n-1):
            first, second = first + second, first
        return first
        


class TestClass:
    def test_example_1(self):
        n = 2
        res = Solution().climbStairs(n)
        assert res == 2

    def test_example_2(self):
        n = 3
        res = Solution().climbStairs(n)
        assert res == 3

if __name__ == "__main__":
    n = 2
    res = Solution().climbStairs(n)
    print(res)

