"""https://leetcode.com/problems/binary-tree-preorder-traversal/description/"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

"""
recursive 
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
"""

class Solution: 
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        stack = deque([root])
        vals = []
        while stack:
            node = stack.pop()
            vals.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return vals
root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)

root.right = a
a.left = b

print(Solution().preorderTraversal(root))