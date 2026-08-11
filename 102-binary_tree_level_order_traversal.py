"""https://leetcode.com/problems/binary-tree-level-order-traversal/"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        vals = []
        queue = deque([root])
        while queue:
            newQueue = deque()
            currentVals = []
            while queue:
                node = queue.popleft()
                currentVals.append(node.val)
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            vals.append(currentVals)
            queue = newQueue
        return vals

root = TreeNode(3)
a = TreeNode(9)
b = TreeNode(20)
c = TreeNode(15)
d = TreeNode(7)

root.left = a
root.right = b
b.left = c
b.right = d

print(Solution().levelOrder(root))