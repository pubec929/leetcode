"""https://leetcode.com/problems/find-the-difference/description/"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) <= 1:
            return t

        s, t = sorted(s), sorted(t)

        for l, r in zip(s, t):
            if l != r:
                return r
        return t[-1]


print(Solution().findTheDifference("abcd", "abcde"))