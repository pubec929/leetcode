"""https://leetcode.com/problems/daily-temperatures/description/"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        output = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                output[j] = i - j
            stack.append(i)
        return output