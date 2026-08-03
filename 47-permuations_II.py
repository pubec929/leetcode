"""https://leetcode.com/problems/permutations-ii/description/"""
from itertools import permutations


class Solution:
    def permuteUnique(self, nums: list[int]):
        return list(set(permutations(nums, len(nums))))

if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 2]
    from rich import print
    print(sol.permuteUnique(nums))