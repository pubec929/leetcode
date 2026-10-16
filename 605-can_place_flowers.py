"""https://leetcode.com/problems/can-place-flowers/description/"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        plots = valid_plots(flowerbed)
        while len(plots) != 0 and n != 0:
            plots = place_flower(plots)
            n -= 1
        return n == 0

def place_flower(valid_plots: list[int]) -> list[int]:
    planted_plot = valid_plots.pop(0)
    if len(valid_plots) >= 1 and valid_plots[0] - planted_plot == 1:
        valid_plots.pop(0)
    return valid_plots

def no_adjecent_flowers(idx: int, flowerbed: list[int]) -> bool:
    return not flowerbed[max(0, idx - 1)] and not flowerbed[min(len(flowerbed) - 1, idx + 1)]

def valid_plots(flowerbed: list[int]) -> list[int]:
    plots = []
    for (idx, plot) in enumerate(flowerbed):
        if not plot and no_adjecent_flowers(idx, flowerbed):
            plots.append(idx)
    return plots


def main():
    flowerbed = [1, 0, 0, 0, 1]
    print(Solution().canPlaceFlowers(flowerbed, 1))

main()
    