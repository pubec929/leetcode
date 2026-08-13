"""https://leetcode.com/problems/distribute-candies/"""

class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        maxCandies = len(candyType) // 2
        return min(len(set(candyType)), maxCandies)
