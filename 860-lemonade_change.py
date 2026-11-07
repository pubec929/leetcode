"""https://leetcode.com/problems/lemonade-change/description/?envType=problem-list-v2&envId=greedy"""

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        change = {
            5: 0,
            10: 0,
            20: 0
        }
        change_list = [5, 10, 20]
        for bill in bills:
            change[bill] += 1
            if not (diff := bill - 5):
                continue
            idx = len(change_list) - 1
            while diff > 0 and idx >= 0:
                n = change_list[idx]
                if n <= diff and change[n] >= 1:
                    diff -= n
                    change[n] -= 1
                else:
                    idx -= 1
            if diff != 0:
                return False
        return True

def main():
    bills = [5, 5, 10, 10, 20]
    print(Solution().lemonadeChange(bills))

main()

