"""https://leetcode.com/problems/jewels-and-stones/description/"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        total = 0
        for stone in stones:
            if stone in jewels:
                total += 1
        return total 