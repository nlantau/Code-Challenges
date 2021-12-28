# nlantau, 2021-12-28

from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.list_length(head)
        # what if list length is 0?

        # |1|2|3|4|5|
        # |----5----| = List length
        # |----2----| = nth node from end of the list
        # 5-2 = 3 <- index to remove
        index_to_remove = length - n
        if index_to_remove == 0: return head.next # I missed 'head.next' here for instance

        curr = head
        prev = None

        while index_to_remove > 0:
            prev = curr
            curr = curr.next
            index_to_remove -= 1

        prev.next = curr.next # This algorithm is so clean and clever
        curr.next = None
        return head



    def list_length(self, head: Optional[ListNode]) -> int:
        length = 0

        current = head
        if current == None: return 0
        if current.next == None: return 1

        nnext = head.next

        while current.next != None:
            length += 1
            current = nnext
            nnext = current.next

            # tail
            if current.next == None:
                length += 1
        return length

"""
Notes:
Ah, this was a frustrating one. Shouldn't have taken so long, but I messed up a few
details along the way and started to complicate everything. Had to get some hints online
to confirm some of my thoughts after a while. Got blinded! Should've been an easy task...

36 ms, 14.3MB, 49.52% faster
"""

"""
Test cases and code
"""
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

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
print("\n>> head = [1,2,3,4,5], n = 1")
print_linkedlist(a)
Solution().removeNthFromEnd(a, 2)
print(">>> Expected: [1,2,3,5] and got:")
print_linkedlist(a)

print("\n>> head = [1], n = 1")
a = ListNode(1)
print_linkedlist(a)
Solution().removeNthFromEnd(a, 1)
print(">>> Expected: [] and got: ")
print_linkedlist(a)

print("\n>> head = [1,2], n = 1")
a = ListNode(1)
b = ListNode(2)
a.next = b
print_linkedlist(a)
Solution().removeNthFromEnd(a, 1)
print(">>> Expected: [1] and got: ")
print_linkedlist(a)






#assert Solution().list_length(a) == 6
assert Solution().list_length(ListNode(99)) == 1
assert Solution().list_length(None) == 0


