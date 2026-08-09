"""https://leetcode.com/problems/contains-duplicate/description/"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
