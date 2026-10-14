"""https://leetcode.com/problems/maximum-repeating-substring/description"""

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 1
        concat = word
        while concat in sequence:
            k += 1
            concat += word
        return k - 1
