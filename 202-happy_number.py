"""https://leetcode.com/problems/happy-number/description/?envType=problem-list-v2&envId=two-pointers"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            num = 0
            for digit in str(n):
                num += int(digit) ** 2
            seen.add(n)
            n = num
            if n == 1:
                return True
        return False