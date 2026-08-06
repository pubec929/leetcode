"""https://leetcode.com/problems/smallest-divisible-digit-product-i/description/?envType=daily-question&envId=2026-08-06"""

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def _digitProduct(n: int):
            if n < 10:
                return n
            return (n // 10) * (n % 10)

        def isDivisible(a, b):
            return a % b == 0

        for i in range(10):
            product = _digitProduct(n + i)
            if isDivisible(product, t):
                return n + i

        return -1