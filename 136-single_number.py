"""https://leetcode.com/problems/single-number/description/"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]

        return nums[-1]

if __name__ == "__main__":
    sol = Solution()

    nums = [4,1,2,1,2]
    print(sol.singleNumber(nums))