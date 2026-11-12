"""https://leetcode.com/problems/baseball-game/"""

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        for op in operations:
            match op:
                case "C": record.pop()
                case "D": record.append(record[-1] * 2)
                case "+": record.append(record[-1] + record[-2])
                case _: record.append(int(op))

        return sum(record)