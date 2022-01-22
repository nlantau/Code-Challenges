# nlantau, 2022-01-01

"""
Given the root of a binary tree and an integer targetSum,
return true if the tree has a >> root-to-leaf << path such that
adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        elif not root.left and not root.right:
            return root.val == targetSum
        else:
            return self.hasPathSum(root.left, targetSum - root.val) or \
            self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = [root]
        seq = []
        tmp = []

        while stack:
            curr = stack.pop()
            print(curr.val)
            
            tmp.append(curr.val)

            for child in [curr.left, curr.right]:
                if child:
                    stack.append(child)
                elif not child:
                    seq.append(tmp)
                    tmp = []
        return seq



"""
Notes:
117/117, 50 ms (18.26% faster), 15.2 MB (42.85% better)

Tried a few own variants, but somehome input [], 0 resulted in True
but should've been False...

"""

if __name__ == "__main__":
    a = TreeNode(5)
    al = TreeNode(4)
    al_l = TreeNode(11)
    al_l_l = TreeNode(7)
    al_l_r = TreeNode(2)

    ar = TreeNode(8)
    ar_l = TreeNode(13)
    ar_r = TreeNode(4)
    ar_r_r = TreeNode(1)

    a.left = al
    al.left = al_l
    al_l.left = al_l_l
    al_l.right = al_l_r

    a.right = ar
    ar.left = ar_l
    ar.right = ar_r
    ar_r.right = ar_r_r

    print(Solution().hasPathSum(a, 22))
    print(Solution().hasPathSum2(a, 22))

    z = TreeNode(None)
    print(Solution().hasPathSum(z, 0))
