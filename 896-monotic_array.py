"""https://leetcode.com/problems/monotonic-array/description/"""

from itertools import pairwise

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return all(a <= b for a, b in pairwise(nums)) or all(a >= b for a, b in pairwise(nums))