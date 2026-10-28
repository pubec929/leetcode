"""https://leetcode.com/problems/shortest-distance-to-a-character/description/"""

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        indices = [i for (i, char) in enumerate(s) if char == c]

        if len(indices) == 1:
            idx = indices[0]
            return [abs(idx - i) for i in range(len(s))]

        answer = [0] * len(s)
        r = 0, 1
        lower, upper = indices[r[0]:r[1] + 1]
        for i in range(len(s)):
            if i <= lower:
                answer[i] = lower - i
            elif i <= upper:
                answer[i] = min(abs(i - lower), abs(upper - i))
            else:
                if r[1] + 1 >= len(indices):
                    answer[i] = i - upper
                else:
                    r = r[0] + 1, r[1] + 1
                    lower, upper = indices[r[0]:r[1] + 1]
                    answer[i] = min(abs(i - lower), abs(upper - i))
        return answer

def case_1():
    s = "loveleetcode" 
    c = "e"
    answer = Solution().shortestToChar(s, c)
    print(answer)
    assert answer == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

def case_2():
    s = "aaab" 
    c = "b"
    answer = Solution().shortestToChar(s, c)
    assert answer == [3, 2, 1, 0]

def case_3():
    s = "aaba"
    c = "b"
    print(Solution().shortestToChar(s, c))
def main():
    case_1()
    case_2()
    case_3()
    print("tests ran")

main()
                