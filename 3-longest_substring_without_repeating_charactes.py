"""https://leetcode.com/problems/longest-substring-without-repeating-characters/description/"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxLength = 0
        l, r = 0, 0
        for char in s:
            if (pos := s.find(char, l, r)) != -1:
                maxLength = max(r - l, maxLength)
                l = pos + 1
            r += 1
        return max(r - l, maxLength)
            
sol = Solution()
s = "cdcda"
print(sol.lengthOfLongestSubstring(s))