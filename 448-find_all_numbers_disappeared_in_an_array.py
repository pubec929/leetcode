"""https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/"""

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        setNums = set(nums)
        missing = [n for n in range(1, len(nums) + 1) if n not in setNums]
        return missing
        
            

sol = Solution()
nums = [4,3,2,7,8,2,3,1]
print(sol.findDisappearedNumbers(nums))
