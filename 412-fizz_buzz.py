"""https://leetcode.com/problems/fizz-buzz/submissions/2094311021/"""

class Solution:
    def fizzBuzz(self, n: int) -> list[int]:
        outcome = []
        for i in range(1, n + 1):
            item = ""
            if i % 3 == 0:
                item += "Fizz"
            if i % 5 == 0:
                item += "Buzz"
            outcome.append(item or str(i))
        return outcome
