# nlantau, 2022-01-01

"""
Attempt at algo from scratch

Steps:
1. BFT / Level order traversal using queue
2. 
"""
from typing import *
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            curr_lvl = []

            for _ in range(len(queue)):
                curr_node = queue.popleft()

                if curr_node:
                    curr_lvl.append(curr_node.val)
                #if curr_node.left:
                    queue.append(curr_node.left)
                #if curr_node.right:
                    queue.append(curr_node.right)
                if not curr_node:
                    curr_lvl.append(None)

            for i in range(len(curr_lvl) // 2):
                if curr_lvl[i] != curr_lvl[len(curr_lvl) - 1 - i]:
                    return False
        return True
"""
Notes:
197/197, 37 ms (21.71% faster), 14.4 MB
Well, I fell into some pit falls: I forgot 'for _ in range(len(queue))' which
lead to only visiting half the tree (I think...).

Essentially:
1. If node -> append to current level, append its children (even if they're None)
   This works since 'if curr_node' conditions None
2. We cannot forget to add a None to our current level if we are missing a node,
   hence 'if not curr_node: curr_lvl.append(None)'
"""

        
if __name__ == "__main__":
    a = TreeNode(1)
    al = TreeNode(2)
    ar = TreeNode(2)
    al_l = TreeNode(3)
    al_r = TreeNode(4)
    ar_l = TreeNode(4)
    ar_r = TreeNode(3)

    a.left = al
    a.right = ar
    al.left = al_l
    al.right = al_r
    ar.left = ar_l
    ar.right = ar_r


    print(Solution().isSymmetric(a)) # True

    b = TreeNode(1)
    bl = TreeNode(2)
    br = TreeNode(2)
    bl_r = TreeNode(3)
    br_r = TreeNode(3)

    b.left = bl
    b.right = br
    bl.right = bl_r
    br.right = br_r

    print(Solution().isSymmetric(b)) # False

    c = TreeNode(1)
    cl = TreeNode(2)
    cr = TreeNode(3)

    c.left = cl
    c.right = cr

    print(Solution().isSymmetric(c)) # False
