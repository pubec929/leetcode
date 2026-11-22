"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for l in range(0, len(numbers) - 1):
            s = numbers[l] + numbers[l + 1]
            if s == target:
                return [l + 1, l + 2]
            if s > target:
                break
        else:
            return [-1, -1]
        r = l + 1
        while l >= 0 and s > target:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            l -= 1
        return [-1, -1]
        
numbers = [-5,-3,0,2,4,6,8]
target = 5
print(Solution().twoSum(numbers, target))