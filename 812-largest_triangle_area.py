"""https://leetcode.com/problems/largest-triangle-area/"""
from itertools import combinations

def area(p1, p2, p3):
  x1, y1 = p1[0], p1[1]
  x2, y2 = p2[0], p2[1]
  x3, y3 = p3[0], p3[1]
  return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0

class Solution:
    def largestTriangleArea(self, points: list[list[int]]):
        combos = combinations(points, 3)
        max_area = 0
        for p in combos:
            max_area = max(max_area, area(*p))
        return max_area
