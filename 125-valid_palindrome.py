class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()

        filteredS = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                filteredS += char
        s.isalnum
        for i in range(len(filteredS) // 2):
            if filteredS[i] != filteredS[-i-1]:
                return False
        return True
