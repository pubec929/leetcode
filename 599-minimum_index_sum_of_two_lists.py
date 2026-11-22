"""https://leetcode.com/problems/minimum-index-sum-of-two-lists/"""

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        seen = {name: idx for idx, name in enumerate(list1)}
        seen_twice = {}
        for idx, name in enumerate(list2):
            if name in seen:
                seen_twice[name] = seen[name] + idx

        lowest = float("Inf")
        output = []
        for name, idx in seen_twice.items():
            if idx < lowest:
                output = [name]
                lowest = idx
            elif idx == lowest:
                output.append(name)
        return output

