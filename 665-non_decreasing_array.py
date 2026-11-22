"""https://leetcode.com/problems/non-decreasing-array/description/"""

from itertools import pairwise

class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        modified = False
        floor = float("-Inf")

        for a, b in pairwise(nums):
            if b < a or b < floor:
                if modified:
                    return False
                modified = True
                floor = b if b >= floor else a
            else:
                floor = a
        return True
