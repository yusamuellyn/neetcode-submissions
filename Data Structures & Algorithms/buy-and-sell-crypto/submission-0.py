class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for sell in prices:
            if sell - minBuy > maxProfit: 
                maxProfit = sell - minBuy
            
            if sell < minBuy: 
                minBuy = sell

        return maxProfit
