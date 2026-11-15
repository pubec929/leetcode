"""https://leetcode.com/problems/second-largest-digit-in-a-string/description/"""

class Solution:
    def secondHighest(self, s: str) -> int:
        unique_digits = sorted({int(n) for n in s if n.isdigit()})
        return unique_digits[-2] if len(unique_digits) > 1 else -1