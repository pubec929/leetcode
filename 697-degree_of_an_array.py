"""https://leetcode.com/problems/degree-of-an-array/"""
from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        c = Counter()
        first = {}
        last = {}

        for i, n in enumerate(nums):
            c[n] += 1
            if n not in first:
                first[n] = i
            
            last[n] = max(getattr(last, str(n), 0), i)

        c = sorted(c.items(), reverse=True, key=lambda i: i[1])
        degrees = c[0][1]
        length = None
        for n, count in c:
            if count < degrees:
                break

            l, r = first[n], last[n]
            if length is None:
                length = r - l + 1
            else:
                length = min(length, r - l + 1)
        return length

nums = [1, 2, 2, 3, 1]
print(Solution().findShortestSubArray(nums))