"""https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/"""

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        idx, dist = -1, float("inf")
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                d = abs(x - a) + abs(y - b)
                if d < dist:
                    idx, dist = i, d
        return idx
