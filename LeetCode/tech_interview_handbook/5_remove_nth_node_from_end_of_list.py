# nlantau, 2022-01-08

"""
As I've completed this quite recently, I'm going to try a different approach.

Last time I created a function that returned the length of the linked list. This
time I'll try something else... Not sure yet what..


Found one two-pointer solution that was pretty cool
"""

from typing import *

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2 = head, head

        while n > 0:
            p1 = p1.next
            n -= 1

        while p1 != None and p1.next != None:
            p2 = p2.next
            p1 = p1.next

        if p1 != None:
            p2.next = p2.next.next
        else:
            head = head.next

        return head

    def printList(self, head: Optional[ListNode]):
        while head:
            print(head.val, end=",")
            head = head.next

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = None

    Solution().printList(Solution().removeNthFromEnd(a, 2))

