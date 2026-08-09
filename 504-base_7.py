"""https://leetcode.com/problems/base-7/description/"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        sign = "-" if num < 0 else ""
        num = abs(num)
        n = ["0"] * 10
        exp = 10
        while num > 0:
            while 7**exp > num:
                exp -= 1
            quant = num // (7 **exp)
            n[-exp-1] = str(quant)
            num -= quant * (7 ** exp)
        n = "".join(n).lstrip("0")
        return sign + n

print(Solution().convertToBase7(7))
