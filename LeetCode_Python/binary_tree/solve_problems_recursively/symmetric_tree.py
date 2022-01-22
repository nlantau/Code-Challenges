# nlantau, 2021-12-30

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative level order traversal
        """
        from collections import deque

        queue = deque([root])

        while queue:
            curr_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    curr_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    curr_level.append(None)
            for i in range(len(curr_level) // 2):
                if curr_level[i] != curr_level[len(curr_level) - 1 - i]:
                    return False
        return True


        
    def levelTrav(self, root):
        from collections import deque

        if not root: return []

        queue = deque([root])
        visited = []

        while queue:
            curr_lev = []

            for _ in range(len(queue)):
                node = queue.popleft()
                curr_lev.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            visited.append(curr_lev)
        return visited

    def isSym2(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        return self.compareNodes(root.left, root.right)
    
    def compareNodes(self, n1, n2) -> bool:
        if n1 is None and n2 is None: return True
        if n1 is None or n2 is None: return False
        if n1.val != n2.val: return False
        return self.compareNodes(n1.left, n2.right) and self.compareNodes(n1.right, n2.left)




if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    b1 = TreeNode(2)

    c = TreeNode(3)
    d = TreeNode(4)

    c1 = TreeNode(3)
    e = TreeNode(4)

    a.left = b
    a.right = b1
    b.left = c
    b.right = d
    b1.left = e
    b1.right = c1

    print(Solution().levelTrav(a))
    print(Solution().isSymmetric(a))
    print(Solution().isSym2(a))

    a = TreeNode(1)
    b = TreeNode(2)
    b1 = TreeNode(2)

    c = TreeNode(3)

    c1 = TreeNode(3)

    a.left = b
    a.right = b1
    b.right = c
    b1.right = c1
    print(Solution().levelTrav(a))
    print(Solution().isSymmetric(a))
    print(Solution().isSym2(a))