"""https://leetcode.com/problems/pascals-triangle-ii/"""

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for numRow in range(1, rowIndex + 1):
            newRow = [0] * (numRow + 1)
            for i, num in enumerate(row):
                newRow[i] += num
                newRow[i + 1] += num
            row = newRow
        return row
