# nlantau, 2021-12-29

"""
Pre-order traversal
1. Visit the root node first
2. Traverse the left subtree
3. Traverse the right subtree

In-order traversal
1. Traverse the left subtree
2. Visit the root node
3. Traverse the right tree
"""

from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = list()

        if root:
            visited.append(root.val)
            visited = visited + self.preorderTraversal(root.left)
            visited = visited + self.preorderTraversal(root.right)
        return visited

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = list()

        if root:
            visited = self.inorderTraversal(root.left)
            visited.append(root.val)
            visited = visited + self.inorderTraversal(root.right)
        return visited

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = list()

        if root:
            visited = self.postorderTraversal(root.left)
            visited = visited + self.postorderTraversal(root.right)
            visited.append(root.val)
        return visited
"""
Notes:
Pre-order:
69/69 test cases passed. Nice.
32 ms, 14.2 MB, 59.73% faster

In-order:
24 ms, 14.3 MB, 95.59% faster

Post-order:
32 ms, 14.3 MB, 60.89% faster

Follow up: Do it iteratively!


"""

if __name__ == "__main__":
    root = TreeNode(1)
    c1 = TreeNode(2)
    c2 = TreeNode(3)
    root.right = c1
    c1.left = c2

    print(Solution().preorderTraversal(root))
    print(Solution().inorderTraversal(root))
    print(Solution().postorderTraversal(root))
