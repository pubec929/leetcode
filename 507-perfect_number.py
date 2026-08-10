"""https://leetcode.com/problems/perfect-number/description/"""
import math 

def getDivisors(num: int):
    divisors = [1]
    sqrt = math.isqrt(num)
    for n in range(2, sqrt):
        if num % n == 0:
            divisors.append(n)
            divisors.append(num // n)
    if sqrt.is_integer():
        divisors.append(sqrt)
    return divisors

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        return sum(getDivisors(num)) == num

print(getDivisors(100))
print(Solution().checkPerfectNumber(28))