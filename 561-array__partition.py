"""https://leetcode.com/problems/array-partition/description/"""

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])
