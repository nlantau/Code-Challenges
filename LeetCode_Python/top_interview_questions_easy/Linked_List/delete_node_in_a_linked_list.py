# nlantau, 2021-12-28

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Essentially what we're doing is that we're removing
        # the next node. But first we copy next.val to current.val
        # and then we copy next.next to current.next.
        node.val = node.next.val
        node.next = node.next.next


"""
Notes:
36 ms, 14.7 MB, 85.09% faster
"""


"""
Test cases and code
"""
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

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


print_linkedlist(a)
print("deleting d = 4")
Solution().deleteNode(d)
print("result: ")
print_linkedlist(a)

