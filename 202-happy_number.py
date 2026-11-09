"""https://leetcode.com/problems/happy-number/description/?envType=problem-list-v2&envId=two-pointers"""

from functools import reduce

def step(n: int) -> int:
    total = 0
    while n:
        n, d = divmod(n, 10)
        total += d * d
    return total

"""
class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            slow = step(slow)
            fast = step(step(fast))
            if slow == fast:
                return slow == 1
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = step(n)
        return n == 1
print(Solution().isHappy(200))
