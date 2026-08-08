"""https://leetcode.com/problems/array-partition/description/"""

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[0:len(nums):2])

sol = Solution()
nums = [6, 2, 6, 5, 1, 2]
print(sol.arrayPairSum(nums))