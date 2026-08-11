"""https://leetcode.com/problems/binary-tree-postorder-traversal/description/"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
"""
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        vals = deque()
        stack = deque([root])
        while stack:
            node = stack.pop()
            vals.appendleft(node.val)

            if node.left:
                stack.append(node.left)

            if node.right: 
                stack.append(node.right)

        return list(vals)
        

root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)

root.right = a
a.left = b

print(Solution().postorderTraversal(root))