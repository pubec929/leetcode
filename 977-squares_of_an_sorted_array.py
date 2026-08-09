"""https://leetcode.com/problems/squares-of-a-sorted-array/description/"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squares = [None] * len(nums)
        l, r = 0, len(nums) - 1
        idx = 0
        while l <= r:
            a, b = nums[l] ** 2, nums[r] ** 2
            if a > b:
                squares[-idx-1] = a
                l += 1
            else:
                squares[-idx - 1] = b
                r -= 1
            idx += 1
        return squares


print(Solution().sortedSquares([-2, 1, 2]))
        
