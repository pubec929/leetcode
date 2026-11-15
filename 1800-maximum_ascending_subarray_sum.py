"""https://leetcode.com/problems/maximum-ascending-subarray-sum/description/"""

class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        current = nums[0]
        max_sum = current
        for r in range(1, len(nums)):
            if nums[r] > nums[r - 1]:
                current += nums[r]
            else:
                current = nums[r]
            max_sum = max(max_sum, current)
        return max_sum
