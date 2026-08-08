"""https://leetcode.com/problems/teemo-attacking/description/"""

class Solution: 
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        totalTime = 0
        lastTime = -1
        for second in timeSeries:
            if lastTime == -1:
                lastTime = second
            else:
                overlap = second - (duration + lastTime - 1)
                if overlap == 0:
                    totalTime += duration - 1
                elif overlap < 0:
                    totalTime += second - lastTime
                else: 
                    totalTime += duration
                lastTime = second
        if lastTime:
            totalTime += duration
        return totalTime

sol = Solution()
print(sol.findPoisonedDuration([0, 1], 1))