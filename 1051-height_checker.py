"""https://leetcode.com/problems/height-checker/description/"""

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        output = 0
        for a, b in zip(heights, sorted(heights)):
            if a != b:
                output += 1
        return output