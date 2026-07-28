"""https://leetcode.com/problems/binary-tree-inorder-traversal/"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def _traverse(node: TreeNode):
            nums = []
            if node.left:
                nums.extend(_traverse(node.left))

            nums.append(node.val)
            if node.right:
                nums.extend(_traverse(node.right))

            return nums

        return _traverse(root) if root else []


if __name__ == "__main__":
    tree = TreeNode(1, right = TreeNode(2, left= TreeNode(3)))
    sol = Solution()
    print(sol.inorderTraversal(tree))