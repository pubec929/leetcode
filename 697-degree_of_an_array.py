"""https://leetcode.com/problems/degree-of-an-array/"""
from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        c = Counter(nums)
        first = {}
        last = {}
        
        for i, n in enumerate(nums):
            first.setdefault(n, i)
            last[n] = i

        degree = max(c.values())
        length = len(nums)
        for n, count in c.items():
            if count == degree:
                l, r = first[n], last[n]
                length = min(length, r - l + 1)
        return length
