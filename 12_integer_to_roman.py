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
        idx = 0
        def addRoman(num: int, roman):
            prev = list(table.items())[idx]
            for curr in list(table.items())[1:]:
                val, _ = curr
                if val > num:
                    break
                prev = curr

            val, literal = prev
            quant = num // val
            roman += quant * literal
            num -= quant * val
            return num, roman
            
        while num >= 1:
            num, roman = addRoman(num, roman)
        return roman


sol = Solution()
print(sol.intToRoman(999))