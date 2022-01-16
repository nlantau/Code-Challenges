# nlantau, 2022-01-16

class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)

"""
Notes:
97/97
119 ms, 14.6 MB
"""

if __name__ == "__main__":
    n = '32'
    print(Solution().minPartitions(n)) # 3

    n = '82734'
    print(Solution().minPartitions(n)) # 8
