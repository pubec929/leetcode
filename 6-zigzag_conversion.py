"""https://leetcode.com/problems/zigzag-conversion/description/"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        curr = 0
        countUp = True
        for char in s:
            rows[curr].append(char)
            curr = min(curr + 1, numRows - 1) if countUp else max(curr - 1, 0)
            if curr <= 0 or curr >= numRows - 1:
                countUp = not countUp

        zigzag = ""
        for row in rows:
            zigzag += "".join(row)

        return zigzag

print(Solution().convert("AB", 1))