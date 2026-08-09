"""https://leetcode.com/problems/majority-element/description/"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = 0
        count = 0
        for n in nums:
            if not count:
                candidate = n

            if n == candidate:
                count += 1
            else:
                count -= 1
        return candidate
