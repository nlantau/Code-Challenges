# nlantau, 2022-01-31

from typing import *


class Solution:
    def countBits2(self, n: int) -> List[int]:
        # Brute force solution
        res = []

        for i in range(n + 1):
            num = bin(i)
            temp = 0

            for d in num:
                if d == '1':
                    temp += 1
                    
            res.append(temp)
        return res

    def countBits3(self, n: int) -> List[int]:
        arr = [0]

        for i in range(1, n + 1):
            arr.append(arr[i // 2] + i % 2)
        return arr

    def countBits(self, n: int) -> List[int]:
        arr = [0] * (n + 1)

        for i in range(1, n + 1):
            arr[i] = arr[i >> 1] + i % 2
        return arr
"""
Notes:
Brute force solution: 202 ms, 19.99%, 20.9 MB, 70.62%, O(N^2)
O(N) solution       : 134 ms, 40.29%, 20.8 MB, 91.50% 


"""

class TestClass:
    def test_example_1(self):
        n = 2
        res = Solution().countBits(n)
        assert res == [0,1,1]

    def test_example_2(self):
        n = 5
        res = Solution().countBits(n)
        assert res == [0,1,1,2,1,2]


if __name__ == "__main__":
    pass
