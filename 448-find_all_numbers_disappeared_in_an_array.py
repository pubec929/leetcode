"""https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/"""

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums.sort()
        idx = 0
        expected = list(range(1, len(nums) + 1))
        missing = []
        r = 0
        for idx in range(0, len(nums)):
            n = nums[idx] 
            if idx >= 1 and n == nums[idx - 1]:
                continue
            if  expected[r] != n:
                missing.extend(expected[r:n - 1])
                r = n
            else:
                r += 1
        return missing + expected[r:]

sol = Solution()
nums = [1, 1, 1, 1]
print(sol.findDisappearedNumbers(nums))
