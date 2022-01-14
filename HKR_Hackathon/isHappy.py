# nlantau, 2022-01-14

class Solution:
    def isHappy(self, n: int) -> bool:
        y = 0
        # brute force solution + taking a chance with 100
        while y < 100:
            n = sum([int(x)**2 for x in str(n)])
            y += 1
            if n == 1: return True
        return False

"""
Notes:
402/402
108 ms, 14.4 MB
"""

if __name__ == "__main__":
    n = 19
    print(Solution().isHappy(n)) # True

    n = 2
    print(Solution().isHappy(n)) # False
