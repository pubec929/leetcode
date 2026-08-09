"""https://leetcode.com/problems/contains-duplicate/description/"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

print(Solution().containsDuplicate([1, 2, 3, 4]))