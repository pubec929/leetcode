"""https://leetcode.com/problems/permutations/description/"""
from rich import print

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def _perm(nums: list[int]) -> list[list[int]]:
            if len(nums) == 1:
                return [nums]

            permutations = []
            for i in range(len(nums)):
                newNums = nums[:]
                n = newNums.pop(i)
                permutations.extend([n, *p] for p in _perm(newNums))
            return permutations

        return _perm(nums)

if __name__ == "__main__":
    nums = [0, 1]
    sol = Solution()
    
    print(sol.permute(nums))

        
        