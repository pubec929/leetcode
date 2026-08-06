"""https://leetcode.com/problems/pascals-triangle/description/"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        rows = [[1]]
        for numRow in range(1, numRows):
            newRow = [0] * (numRow + 1)
            for i, num in enumerate(rows[numRow - 1]):
                newRow[i] += num
                newRow[i + 1] += num
            rows.append(newRow)
        return rows