"""https://leetcode.com/problems/assign-cookies/description/"""

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        c = 0
        g = sorted(g)
        s = sorted(s)
        for i, child in enumerate(g):
            while True:
                if c >= len(s):
                    return i
                if child <= s[c]:
                    break
                c += 1
            c += 1
        return len(g)

print(Solution().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
            
