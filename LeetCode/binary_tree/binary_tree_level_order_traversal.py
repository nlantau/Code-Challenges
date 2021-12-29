# nlantau, 2021-12-29

from typing import *

"""
Level order traversal of a tree is the same as 
breadth first traversal
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def preOrder(self, root: Optional[TreeNode]) -> List[int]:
        visited = list()

        if root:
            visited.append(root.val)
            visited += self.preOrder(root.left)
            visited += self.preOrder(root.right)
        return visited


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Using deque from collections because it's faster with inserts
        and pops from the beginning of a list than a normal list
        """
        from collections import deque

        if not root: return []

        queue = deque([root])
        result = []

        while queue:
            current_level = list()
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            result.append(current_level)
        return result

"""
Notes:
55 ms, 14.3 MB, 7.95% faster :(
99.48% better memory usage :D
"""


if __name__ == "__main__":
    a = TreeNode(3)
    b = TreeNode(9)
    c = TreeNode(20)
    d = TreeNode(15)
    e = TreeNode(7)

    a.left = b
    a.right = c
    c.left = d
    c.right = e

    print(Solution().preOrder(a))
    print(Solution().levelOrder(a))
