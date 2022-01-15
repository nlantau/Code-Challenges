# nlantau, 2022-01-15

from typing import *
from collections import Counter
import heapq

class Solution:
    def isNStraightHand2(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        hs = {}
        for d in hand:
            hs[d] = 1 + hs.get(d, 0)

        min_heap = list(hs.keys())
        heapq.heapify(min_heap)

        while min_heap:
            min_val = min_heap[0]

            for i in range(min_val, min_val + groupSize):
                if i not in hs:
                    return False
                hs[i] -= 1
                if hs[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        hs = Counter(hand)
        min_heap = list(hs.keys())
        heapq.heapify(min_heap)

        while min_heap:
            min_val = min_heap[0]

            for i in range(min_val, min_val + groupSize):
                if i not in hs: return False
                hs[i] -= 1
                if hs[i] == 0:
                    if i != min_heap[0]: return False
                    heapq.heappop(min_heap)
        return True

"""
Notes:
74/74
268 ms, 15.9 MB

'Hand of Straights' Leetcode 846.
"""

if __name__ == "__main__":
    r = [1,2,3,6,2,3,4,7,8]
    b = 3
    print(Solution().isNStraightHand(r, b)) # True

    r = [1,2,3,6,2,3,4,7,3]
    b = 3
    print(Solution().isNStraightHand(r, b)) # False

    r = [1,2,3,4,5]
    b = 4
    print(Solution().isNStraightHand(r, b)) # False
