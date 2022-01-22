# nlantau, 2022-01-03

"""
You are climbing a staircase. It take n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?

Solution:
input: n = 2
output: 2
1. 1 step + 1 step
2. 2 step
Total: 2 distinct ways

input: n = 3
output: 3
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 step + 1 step
Total: 3 distinct ways

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        first, sec = 1, 1
        for i in range(n-1):
            first, sec = first + sec, first
        return first

    def climbStairs2(self, n: int, memo={}) -> int:
        if n in memo: return memo[n]
        if n <= 2: return 1
        memo[n] = self.climbStairs2(n-1, memo) + self.climbStairs2(n-2, memo)
        return memo[n]

"""
Notes:
67 ms, super-slow, 14.2 MB, 72.59% better
"""

if __name__ == "__main__":
    print(Solution().climbStairs(3))
    print(Solution().climbStairs2(3))
    print(Solution().climbStairs(45))
    print(Solution().climbStairs2(45))
    print(Solution().climbStairs2(46))
        
