"""https://leetcode.com/problems/maximum-subarray/"""
from itertools import islice

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = current = nums[0]
        for n in islice(nums, 1, None):
            current = max(current + n, n)
            max_sum = max(max_sum, current)
        return max_sum
