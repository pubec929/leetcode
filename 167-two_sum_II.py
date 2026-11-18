"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        r = 1
        for l in range(0, len(numbers)):
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                while s < target:
                    if r + 1 >= len(numbers):
                        break
                    r += 1
                    s = numbers[l] + numbers[r]
                    if s == target:
                        return [l + 1, r + 1]
            else:
                while r >= 0 and r > l and s > target:
                    r -= 1
                    s = numbers[l] + numbers[r]
                    if s == target:
                        return [l + 1, r + 1]

        return [-1, -1]
        
numbers = [1,2,3,4,4,9,56,90]
target = 8
print(Solution().twoSum(numbers, target))