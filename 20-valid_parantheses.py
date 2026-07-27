from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        charMap = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        queue = deque()
        for char in s:
            if char in charMap:
                queue.append(charMap[char])
            else:
                if len(queue) < 1 or char != queue[-1]:
                    return False
                queue.pop()

        if len(queue) != 0:
            return False
        return True

if __name__ == "__main__":
    sol = Solution()

    test_cases = ["()", "()[]{}", "(]", "([])", "([)]", "[", "){"]
    for case in test_cases:
        print(sol.isValid(case))