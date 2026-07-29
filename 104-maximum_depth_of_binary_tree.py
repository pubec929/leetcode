"""https://leetcode.com/problems/maximum-depth-of-binary-tree/"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _depth(node: TreeNode):
            l, r = 0, 0
            if node.left:
                l = _depth(node.left)
            if node.right:
                r = _depth(node.right)

            return 1 + max(l, r)

        return _depth(root) if root else 0 
        