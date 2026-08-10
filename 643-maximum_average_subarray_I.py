"""https://leetcode.com/problems/maximum-average-subarray-i/description/"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l, r = 0, k - 1
        maxSum = sum(nums[l:r + 1])
        window = maxSum
        while r < len(nums) - 1:
            window -= nums[l]
            r += 1
            l += 1
            window += nums[r]
            maxSum = max(window, maxSum) 
        return maxSum / k
