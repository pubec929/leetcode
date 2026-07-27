class Solution:
    def romanToInt(self, s: str):
        hashmap = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        num = 0
        i = 0
        while i < len(s):
            double = s[i:i+2]
            if i < len(s) - 1 and double in hashmap:
                num += hashmap[double]
                i += 2
            else:
                num += hashmap[s[i]]
                i += 1
        return num

if __name__ == "__main__":
    roman = "MCMXCIV"
    sol = Solution()
    print(sol.romanToInt(roman))
