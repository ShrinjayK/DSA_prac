from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        most = 0
        buy, sell = 0, 1
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                most = max(most, profit)
            if prices[sell] < prices[buy]:
                buy = sell
            sell += 1
        return most