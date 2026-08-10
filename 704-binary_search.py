"""https://leetcode.com/problems/binary-search/description/"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)
        while r - l > 1:
            mid = l + (r - l) // 2
            n = nums[mid]
            if target < n:
                r = mid
            elif target > n:
                l = mid
            else:
                return mid
        if l >= 0:
            return l if nums[l] == target else -1
        return -1
        
        

print(Solution().search([13, 17], 13))