"""https://leetcode.com/problems/stone-removal-game/description/"""

class Solution:
    def canAliceWin(self, n: int) -> bool:
        subtract = 10
        aliceTurn = True
        while True:
            n -= subtract
            if n < 0:
                return not aliceTurn
            subtract -= 1
            aliceTurn = not aliceTurn

print(Solution().canAliceWin(1))
