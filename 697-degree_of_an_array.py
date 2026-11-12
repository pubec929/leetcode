"""https://leetcode.com/problems/degree-of-an-array/"""
from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        c = Counter()
        for n in nums:
            c[n] += 1
        c = sorted(c.items(), reverse=True, key=lambda item: item[1])
        
        length = None
        degrees = c[0][1]
        for n, count in c:
            if degrees != count:
                break
                
            l = 0
            while l <= len(nums) - 1:
                if n == nums[l]:
                    break
                l += 1

            r = len(nums) - 1
            while r >= 0:
                if n == nums[r]:
                    break
                r -= 1
            
            if length is None:
                length = r - l + 1
            else:
                length = min(r - l + 1, length)
                
        return length

nums = [1]
print(Solution().findShortestSubArray(nums))