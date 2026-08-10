"""https://leetcode.com/problems/binary-search/description/"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            n = nums[mid]
            if target < n:
                r = mid - 1
            elif target > n:
                l = mid + 1
            else:
                return mid
        return -1
        
        

print(Solution().search([13, 17], 13))