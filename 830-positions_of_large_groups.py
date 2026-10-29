"""https://leetcode.com/problems/positions-of-large-groups/"""

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        l, r = 0, 1
        groups = []
        s += " "
        while r < len(s):
            if s[l] != s[r]:
                if r - l >= 3:
                    groups.append([l, r-1])
                l = r
            r += 1
        return groups

            