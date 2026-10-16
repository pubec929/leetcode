"""https://leetcode.com/problems/can-place-flowers/description/"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        idx = 0
        while idx < len(flowerbed) and n != 0:
            if not flowerbed[idx] and no_adjecent_flowers(idx, flowerbed):
                n -= 1
                idx += 1
            idx += 1
        return n == 0

def no_adjecent_flowers(idx: int, flowerbed: list[int]) -> bool:
    return not flowerbed[max(0, idx - 1)] and not flowerbed[min(len(flowerbed) - 1, idx + 1)]
