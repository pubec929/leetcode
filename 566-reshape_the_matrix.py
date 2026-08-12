"""https://leetcode.com/problems/reshape-the-matrix/"""

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat

        newMatrix = [[0] * c for _ in range(r)]
        pos = 0
        for row in mat:
            for val in row:
                newMatrix[pos // c][pos % c] = val
                pos += 1
        
        return newMatrix

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(Solution().matrixReshape(matrix, 2, 6))