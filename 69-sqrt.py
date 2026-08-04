"""https://leetcode.com/problems/sqrtx/description/"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        start, end = 1, x
        while end - start > 1:
            mid = start + (end - start) // 2

            square = mid * mid
            if square > x:
                end = mid
            elif square < x:
                start = mid
            else:
                return mid
        return start
