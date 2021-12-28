# nlantau, 2021-12-28

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current != None:
            nnext = current.next
            current.next = prev
            prev = current
            current = nnext
        head = prev
        return head


def print_linkedlist(node):
    current_node = node
    next_node = current_node.next

    while current_node.next != None:
        print(f"current: {current_node.val}")
        current_node = next_node
        next_node = current_node.next

        # print tail
        if next_node == None:
            print(f"current: {current_node.val}")


"""
Notes:
36 ms, 15.7 MB, 67.45% faster
"""


if __name__ == "__main__":
    print("\n>> head = [1,2,3,4,5]")
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    print_linkedlist(a)
    print('>> Reversing the linked list...')
    n = Solution().reverseList(a)
    print_linkedlist(n)
    
