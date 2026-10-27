"""https://leetcode.com/problems/rotate-string/"""
from collections import deque

def shift(text: deque) -> deque:
    text.append(text.popleft())
    return text

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        text = deque(s)
        goal_deque = deque(goal)
        for _ in range(len(s)):
            text = shift(text)
            if text == goal_deque:
                return True
        return False

def main():
    print(Solution().rotateString("abcde", "cdeab"))
    print(Solution().rotateString("abcde", "abced"))

    print(Solution().rotateString("uqbjvaxu", "xuuqbjva"))
main()