"""https://leetcode.com/problems/last-stone-weight/description/"""

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = sorted(stones)
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if y != x:
                stones = binary_insert(stones, y - x)
        return stones[0] if len(stones) == 1 else 0

def binary_insert(sorted_array, val):
    upper, lower = len(sorted_array), 0
    while (upper - lower) > 0:
        mid = lower + ((upper - lower) // 2)
        if sorted_array[mid] > val:
            upper = mid
        elif sorted_array[mid] < val:
            lower = mid + 1
        else:
            sorted_array.insert(mid, val)
            return sorted_array
    sorted_array.insert(upper, val)
    return sorted_array
