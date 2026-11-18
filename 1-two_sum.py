"""https://leetcode.com/problems/two-sum/"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, n in enumerate(nums):
            if (m := target - n) in seen:
                return [seen[m], i]
            seen[n] = i
        return [-1, -1]
