"""https://leetcode.com/problems/squares-of-a-sorted-array/description/"""

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        l = 0
        # set r 
        r = 0
        while r <= len(nums) - 1 and nums[r] < 0:
            r += 1
        l = r -1

        squares = []
        while l >= 0 or r <= len(nums) - 1:
            if l < 0:
                squares.append(nums[r] ** 2)
                r += 1
            elif r > len(nums) - 1:
                squares.append(nums[l] ** 2)
                l -= 1
            else:
                a, b = nums[l] ** 2, nums[r] ** 2
                if a < b:
                    squares.append(a)
                    l -= 1
                else:
                    squares.append(b)
                    r += 1
        return squares


print(Solution().sortedSquares([-2, 1, 2]))
        
