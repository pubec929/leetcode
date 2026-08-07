"""https://leetcode.com/problems/integer-to-roman/description/"""

class Solution:
    def intToRoman(self, num: int):
        table = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        roman = ""
        idx = len(table) - 1

        keys = list(table.keys())
        literals = list(table.values())
            
        while num >= 1:
            while (val := keys[idx]) > num:
                idx -= 1
            
            quant = num // val
            roman += literals[idx] * quant
            num -= quant * val

        return roman


sol = Solution()
print(sol.intToRoman(1001))