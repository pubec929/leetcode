"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - buy_price)
            buy_price = min(buy_price, price)
        return max_profit
