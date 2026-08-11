"""https://leetcode.com/problems/binary-tree-preorder-traversal/description/"""
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

root = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)

root.right = a
a.left = b

print(Solution().preorderTraversal(root))