"""https://leetcode.com/problems/non-decreasing-array/description/"""

from itertools import pairwise

class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        if len(nums) <= 1:
            return True
        pairs = pairwise(nums)
        a, b = next(pairs)
        if a <= b:
            modified = False
        else:
            modified = True
        minimum = min(a, b)
        
        for a, b in pairs:
            if b < a or b < minimum:
                if modified:
                    return False
                modified = True
                if b >= minimum:
                    minimum = b
                else:
                    minimum = a
                
            else:
                minimum = a
        return True
    

#nums = [4, 1, 2]
#nums = [3, 4, 2, 3]
nums = [1, 4, 1, 2]
#nums = [-1, 4, 2, 3]
#nums = [1,5,4,6,7,10,8,9]
#nums = [4, 2, 3]
print(Solution().checkPossibility(nums))