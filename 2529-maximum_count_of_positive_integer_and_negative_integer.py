"""https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/"""

def search(nums: list[int], condition):
    low, high = 0, len(nums)
    while low < high:
        mid = (low + high) // 2
        if condition(nums[mid]):
            high = mid
        else:
            low = mid + 1
    return low

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        neg_count = search(nums, lambda n: n >= 0)
        first_positive = search(nums, lambda n: n > 0)

        return max(neg_count, len(nums) - first_positive)
        