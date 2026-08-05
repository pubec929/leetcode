"""https://leetcode.com/problems/longest-substring-without-repeating-characters/description/"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxLength = 0
        l, r = 0, 0
        last_seen: dict[str, int] = {}
        for i, char in enumerate(s):
            if char in last_seen and (pos := last_seen[char]) >= l:
                maxLength = max(r - l, maxLength)
                l = pos + 1
            last_seen[char] = i
            r += 1
        return max(r - l, maxLength)
            