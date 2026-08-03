"""https://leetcode.com/problems/permutations/description/"""
from itertools import permutations, product

class Solution:
    def permute(self, nums: list[int]):
        return list(permutations(nums, len(nums)))