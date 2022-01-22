# nlantau, 2022-01-16

from typing import *
import heapq

"""
You are given an array of k linked-lists lists, each linked-list
is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and
return it
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Excellent case for usage of minheap!
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Dummy node as first node. Actual list starts at ph.next
        head = ListNode(0)
        ph = head
        res = []

        # Push node values to heap
        for node in lists:
            while node != None:
                heapq.heappush(res, node.val)
                node = node.next

        # Create merged linked-list
        while res:
            head.next = ListNode(heapq.heappop(res))
            head = head.next

        return ph.next

    def print_list(self, lists: Optional[ListNode]):
        while lists:
            print(lists.val, end=',')
            lists = lists.next
"""
Notes:
151 ms, 38.90% faster, 18.4 MB, 26.44% better
"""

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(5)

    a.next = b
    b.next = c

    c = ListNode(1)
    d = ListNode(3)
    e = ListNode(4)

    c.next = d
    d.next = e

    f = ListNode(2)
    g = ListNode(6)

    f.next = g

    x = [a,c,f]

    b = Solution().mergeKLists(x)
    print(type(b))
    print(b.val)
    print(b.next.val)

    print('>> Print merged and sorted linked-list')
    Solution().print_list(b)

