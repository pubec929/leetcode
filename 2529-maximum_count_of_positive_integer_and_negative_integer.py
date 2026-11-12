"""https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/"""

class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0 if nums[0] == 0 else 1

        def _search(l, r):
            if l == r:
                return None
            mid = (l + r) // 2
            a, b = nums[mid], nums[mid + 1]
            if a < 0 and b >= 0 or a <= 0 and b > 0:
                return mid, mid + 1
            elif a == 0 and b == 0:
                return _search(l, mid) or _search(mid + 1, r)
            elif a < 0 and b < 0:
                return _search(mid + 1, r)
            elif a > 0 and b > 0:
                return _search(l, mid)

        s = _search(0, len(nums) - 1)
        print(s)
        if s is None:
            return len(nums) if nums[0] != 0 else 0
        else:
            l, r = s

        while nums[l] == 0:
            if l == 0:
                return len(nums) - r
            l -= 1
        while nums[r] == 0:
            if r == len(nums) - 1:
                return l + 1
            r += 1
        return max(l + 1, len(nums) - r)

def case_1():
    nums = [-2, -1, -1, 1, 2, 3]
    assert Solution().maximumCount(nums) == 3

def case_2():
    nums = [-3, -2, -1, 0, 0, 1, 2]
    print(Solution().maximumCount(nums))
    assert Solution().maximumCount(nums) == 3

def case_3():
    nums = [5, 20, 66, 1314]
    assert Solution().maximumCount(nums) == 4

def case_4():
    nums = [0, 0]
    assert Solution().maximumCount(nums) == 0

def case_5():
    nums = [-2, -1, -1, 0, 0, 0]
    print(Solution().maximumCount(nums))

def main():
    #case_1()
    #case_2()
    #case_3()
    #case_4()
    case_5()

if __name__ == "__main__":
    main()
