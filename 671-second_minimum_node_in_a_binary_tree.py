"""https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/"""

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        def _find_second(root: TreeNode, lowest: int) -> float:

            min_left = float("inf")
            if root.left:
                if root.left.val != lowest:
                    min_left = root.left.val
                else:
                    min_left = _find_second(root.left, lowest)

            min_right = float("inf")
            if root.right:
                if root.right.val != lowest:
                    min_right = root.right.val
                else:
                    min_right = _find_second(root.right, lowest)


            return min(min_left, min_right)
        if not root:
            return -1
        second = _find_second(root, root.val)
        return -1 if second == float("inf") else int(second)