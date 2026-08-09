"""https://leetcode.com/problems/majority-element/description/"""
from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = Counter()
        l = len(nums) // 2
        for n in nums:
            counter[n] += 1
            if counter[n] > l:
                return n
        return -1

print(Solution().majorityElement([3, 2, 3]))